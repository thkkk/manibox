# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Script to play a checkpoint if an RL agent from RSL-RL."""

"""Launch Isaac Sim Simulator first."""

import os
import argparse
from omni.isaac.lab.app import AppLauncher

# local imports
import cli_args

# add argparse arguments
parser = argparse.ArgumentParser(description="Train an RL agent with RSL-RL.")
parser.add_argument("--cpu", action="store_true", default=False, help="Use CPU pipeline.")
parser.add_argument(
    "--disable_fabric", action="store_true", default=False, help="Disable fabric and use USD I/O operations."
)
parser.add_argument("--num_envs", type=int, default=None, help="Number of environments to simulate.")
parser.add_argument("--task", type=str, default=None, help="Name of the task.")
parser.add_argument("--seed", type=int, default=None, help="Seed used for the environment")
# append RSL-RL cli arguments
cli_args.add_rsl_rl_args(parser)
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""

import gymnasium as gym
import os
import torch

from rsl_rl.runners import OnPolicyRunner

import omni.isaac.lab_tasks  # noqa: F401
from omni.isaac.lab_tasks.utils import get_checkpoint_path, parse_env_cfg
from omni.isaac.lab_tasks.utils.wrappers.rsl_rl import (
    RslRlOnPolicyRunnerCfg,
    RslRlVecEnvWrapper,
    export_policy_as_jit,
    export_policy_as_onnx,
)
from omni.isaac.lab_tasks.manager_based.manipulation.lift import CollectEpsBuf
import threading

from VFCNet.yolo_process_data import YoloCollectData
from omni.isaac.lab.envs import ManagerBasedRLEnv
from omni.isaac.lab_tasks.utils.data_collector.cobot_data_collect import project_to_rotation, push_tensor_obs_action_to_buf, \
    transfer_sim_image_to_standard_img_tensor, save_data
from omni.isaac.lab.assets import RigidObject
from omni.isaac.lab_tasks.manager_based.manipulation.lift import object_pos, apple_to_tablecloth_height_diff
from omni.isaac.lab.sensors.frame_transformer.frame_transformer import FrameTransformer

def get_image_and_save_step(env: ManagerBasedRLEnv, obs_student: torch.Tensor, cams_dict: dict, reward_tensor):
    """
    Termination is checked at every step, so the image is obtained and the state and action are put into the buffer.
    s a -> s', we put `s'` and `a` into the buffer.
    
        obs_student shape: (num_envs, student_num_obs), qpos is at the beginning
        cams_dict: keys: cam_high, cam_left_wrist, cam_right_wrist
            cam_*: torch.Tensor, torch.Size([num_envs, 480, 640, 4]), RGB, 0~255(torch.uint8)
    """
    if not hasattr(env.cfg, 'collect_dataset') or not env.cfg.collect_dataset:
        return torch.zeros(env.num_envs, device=env.device, dtype=torch.bool)
    
    # env.observation_manager.compute()["policy"]:
    # contact_force: (24,), joint_obs: (8,), joint_vel: (8,), object_position: (3,)
    # target_object_position: (7,), actions: （8，）
    # student: joint_obs: (8,), joint_vel: (8,), actions: （8，）
    # obs_student: torch.Tensor = env.observation_manager.compute()["student"]  # (num_envs, student_num_obs)
    # obs_dict: dict = env.observation_manager.compute()
    # import pdb; pdb.set_trace()
    # print("obs_tensor.shape: ", obs_tensor.shape)
    # print("obs_dict", obs_dict)
    
    # print("obs_tensor.shape: ", obs_tensor.shape)  # torch.Size([num_envs, 57])
    num_envs = obs_student.shape[0]
    # object: RigidObject = env.scene["object"]
    # print('object_pos_z', object.data.root_pos_w[:, 2].cpu())
    
    cam_high: torch.Tensor = cams_dict["cam_high"]
    cam_left_wrist: torch.Tensor = cams_dict["cam_left_wrist"]
    cam_right_wrist: torch.Tensor = cams_dict["cam_right_wrist"]
    # cam_high: torch.Tensor, torch.Size([num_envs, 480, 640, 4]), RGB, 0~255(torch.uint8)
    # import pdb; pdb.set_trace()
    object: RigidObject = env.scene["object"]
    
    # first parallel process the images to get the bounding boxes to speed up
    if CollectEpsBuf.use_yolo_sync_process:
        bboxes = YoloCollectData.envs_process[0].parallel_process_traj(
            transfer_sim_image_to_standard_img_tensor(cam_high), 
            transfer_sim_image_to_standard_img_tensor(cam_left_wrist), 
            transfer_sim_image_to_standard_img_tensor(cam_right_wrist)
        )  # no need to initialize
        # bboxes: (epi_len, cam_num * objects_num * 4)
    else:
        bboxes = None
        
    platform: RigidObject = env.scene["platform"]
    init_object_z = platform.data.root_pos_w[:, 2] + apple_to_tablecloth_height_diff
    
    ee_frame: FrameTransformer = env.scene["ee_frame"]
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    
    object: RigidObject = env.scene["object"]
    # Target object position: (num_envs, 3)
    cube_pos_w = object.data.root_pos_w
    
    # distance between end-effector and object
    distance = torch.norm(cube_pos_w - ee_w, dim=1)  # (num_envs,)
    # print(f"distance is {distance}")
    for i in range(num_envs):
        # push_tensor_obs_action_to_buf(
        #     obs_tensor[i], cam_high[i], cam_left_wrist[i], cam_right_wrist[i], 
        #     reward_tensor[i], i,
        #     info={'object_pos_z': object.data.root_pos_w[i, 2].cpu().item()}
        # )
        push_tensor_obs_action_to_buf(
            obs_student[i], cam_high[i], cam_left_wrist[i], cam_right_wrist[i],
            reward_tensor[i], i,
            info={'object_pos_z': object.data.root_pos_w[i, 2].cpu().item(), 'distance': distance[i].cpu().item()}, bboxes=bboxes #TODO
        )
        # it will also save the images with bbox 


def reset_dummy_save_traj(env: ManagerBasedRLEnv, env_ids: torch.Tensor):
    """Save the terminated trajectory using save_data()
    env: ...
    env_ids: It is a tensor of list, containing the indices of the environments to reset. If the tensor is empty, all 
    environments are to be reset.
    collect_dataset: a bool variable about whether we collect data
    """
    
    # print("***************************************hassattr", hasattr(env.cfg, 'collect_dataset'))
    # if hasattr(env.cfg, 'collect_dataset'):
    #     print("***************************************env.cfg.collect_dataset", env.cfg.collect_dataset)
    
    if not hasattr(env.cfg, 'collect_dataset') or not env.cfg.collect_dataset:
        return
    
    num_envs = env.num_envs
    
    if len(CollectEpsBuf.timesteps) == 0:  # initialization at first
        CollectEpsBuf.timesteps = [[] for _ in range(env.num_envs)]
        CollectEpsBuf.actions = [[] for _ in range(env.num_envs)]
        CollectEpsBuf.rewards = [[] for _ in range(env.num_envs)]
        CollectEpsBuf.infos = [[] for _ in range(env.num_envs)]
            
    # store the trajectories which are terminated
    # args.use_depth_image, args.camera_names
    args = argparse.Namespace(use_depth_image=False, camera_names=["cam_high", "cam_left_wrist", "cam_right_wrist"])

    
    # Use termination signal to determine if the data is failed (this variable means the episode is terminated unexpectedly)
    termination_signal: torch.Tensor = env.termination_manager.compute_unexpected_terminal()
    
    platform: RigidObject = env.scene["platform"]
    init_object_z = platform.data.root_pos_w[:, 2] + apple_to_tablecloth_height_diff
    
    ee_frame: FrameTransformer = env.scene["ee_frame"]
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    
    object: RigidObject = env.scene["object"]
    # Target object position: (num_envs, 3)
    cube_pos_w = object.data.root_pos_w
    
    # distance between end-effector and object
    distance = torch.norm(cube_pos_w - ee_w, dim=1)  # (num_envs,)
    # print("distance", distance)
    
    for i in env_ids:
        i = i.cpu().item()
        epi_len = len(CollectEpsBuf.actions[i])
        assert len(CollectEpsBuf.timesteps[i]) == epi_len
        max_epi_len = round(env.cfg.episode_length_s / env.cfg.sim.dt / env.cfg.decimation)  #  and max_epi_len == epi_len
        
        if len(CollectEpsBuf.timesteps[i]) and (not termination_signal[i]) and max_epi_len == epi_len:
            # check if return is larger than minimal to garantee successful grasping
            # 只有mean_return > minimal_return才会被记录
            flat_reward = sum(CollectEpsBuf.rewards[i])
            # TODO: many successful grasps aren't recorded due to "min_return < flat_reward and flat_reward < max_return"
            
            is_lifted = CollectEpsBuf.infos[i][-1]['object_pos_z'] > (init_object_z[i] + 0.02) 
            # if the table is too high?  --for tablecloth pos_z < 0.52, this problem will not happen
            if CollectEpsBuf.infos[i][-2]["distance"] > 0.12:
                print(f"distance is too large: {CollectEpsBuf.infos[i][-2]['distance']:.3f}")
                continue
            
            if flat_reward > 10:  # means successful grasping, i dont know why distance[i] < 0.12 does not work (distance is not updated)
                # here we want to save the trajectory
                # by calling def save_data(args, timesteps, actions, dataset_path)
                
                # assert len(CollectEpsBuf.timesteps[i]) > len(CollectEpsBuf.actions[i])
                # set action as the qpos of the state of next timestep (just use the next qpos as action!)
                for j in range(epi_len):
                    if j == epi_len - 1:  # in the last timestep, you can just use the last qpos as action
                        CollectEpsBuf.actions[i][j] = CollectEpsBuf.timesteps[i][j]['qpos']
                    else:
                        CollectEpsBuf.actions[i][j] = CollectEpsBuf.timesteps[i][j+1]['qpos']
                    
                if len(CollectEpsBuf.timesteps[i]) > len(CollectEpsBuf.actions[i]):
                    CollectEpsBuf.timesteps[i].pop()  # because we saved `s'` and `a` into the buffer.
            
                if not os.path.exists(CollectEpsBuf.dataset_path):
                    os.makedirs(CollectEpsBuf.dataset_path, exist_ok=True)
                    
                save_data(args, CollectEpsBuf.timesteps[i], CollectEpsBuf.actions[i], CollectEpsBuf.rewards[i], CollectEpsBuf.infos[i],
                        os.path.join(CollectEpsBuf.dataset_path, f"episode_{CollectEpsBuf.trajectory_num}"), flat_reward)
                if not CollectEpsBuf.use_yolo_sync_process and CollectEpsBuf.trajectory_num == CollectEpsBuf.data_limit:  # YoloCollectData.num_episodes
                    print(f"The number of trajectories has reached {CollectEpsBuf.data_limit}, the data collection is finished.")
                    exit(0)
                # if termination_signal:
                #     print(f"This trajectory is aborted due to unexpected termination")
            else:
                # print(f"object_pos_z: start {CollectEpsBuf.infos[i][3]['object_pos_z']:.3f}, \
# end {CollectEpsBuf.infos[i][-1]['object_pos_z']:.3f}. init_object_z[i]: {init_object_z[i]}")
                print(f"distance: {distance[i]:.3f}")
                print(f"This trajectory is aborted due to return is {flat_reward:.3f} or failure to grasp")
        else:
            print(f"This trajectory is aborted due to unexpected termination: \
{len(CollectEpsBuf.timesteps[i])} and (not {termination_signal[i]}) and {max_epi_len} == {epi_len}")
        
        # reset the buffer
        CollectEpsBuf.timesteps[i].clear()
        CollectEpsBuf.actions[i].clear()
        CollectEpsBuf.rewards[i].clear()
        CollectEpsBuf.infos[i].clear()
    


def main():
    """Play with RSL-RL agent."""
    # parse configuration
    env_cfg = parse_env_cfg(
        args_cli.task, use_gpu=not args_cli.cpu, num_envs=args_cli.num_envs, use_fabric=not args_cli.disable_fabric
    )
    agent_cfg: RslRlOnPolicyRunnerCfg = cli_args.parse_rsl_rl_cfg(args_cli.task, args_cli)
    

    # create isaac environment
    env = gym.make(args_cli.task, cfg=env_cfg)
    # wrap around environment for rsl-rl
    env = RslRlVecEnvWrapper(env)

    # specify directory for logging experiments
    log_root_path = os.path.join("logs", "rsl_rl", agent_cfg.experiment_name)
    log_root_path = os.path.abspath(log_root_path)
    print(f"[INFO] Loading experiment from directory: {log_root_path}")
    resume_path = get_checkpoint_path(log_root_path, agent_cfg.load_run, agent_cfg.load_checkpoint)
    print(f"[INFO]: Loading model checkpoint from: {resume_path}")

    # load previously trained model
    ppo_runner = OnPolicyRunner(env, agent_cfg.to_dict(), log_dir=None, device=agent_cfg.device)
    ppo_runner.load(resume_path)
    print(f"[INFO]: Loading model checkpoint from: {resume_path}")

    # obtain the trained policy for inference
    policy = ppo_runner.get_inference_policy(device=env.unwrapped.device)

    # export policy to onnx
    export_model_dir = os.path.join(os.path.dirname(resume_path), "exported")
    export_policy_as_jit(
        ppo_runner.alg.actor_critic, ppo_runner.obs_normalizer, path=export_model_dir, filename="policy.pt"
    )
    export_policy_as_onnx(ppo_runner.alg.actor_critic, path=export_model_dir, filename="policy.onnx")

    assert env.env.cfg.collect_dataset == True
    
    # reset environment
    obs, obs_dict = env.get_observations()
    # init: done_episodes are all env.num_envs
    step_counters = torch.zeros(env.num_envs, dtype=torch.int, device=env.unwrapped.device)
    
    CollectEpsBuf.timesteps = [[] for _ in range(env.num_envs)]
    CollectEpsBuf.actions = [[] for _ in range(env.num_envs)]
    CollectEpsBuf.rewards = [[] for _ in range(env.num_envs)]
    CollectEpsBuf.infos = [[] for _ in range(env.num_envs)]
    
    if CollectEpsBuf.use_yolo_sync_process:
        YoloCollectData.init(1)
    # if not os.path.exists(dataset_path):
    #     os.makedirs(dataset_path, exist_ok=True)

    print(f"init qpos: {torch.round(obs[:, 24:31] * 1000) / 1000}", obs_dict)
    # simulate environment
    while simulation_app.is_running():
        # run everything in inference mode
        with torch.inference_mode():
            # agent stepping
            zero_action = torch.zeros_like(torch.tensor(env.action_space.sample(), device=env.unwrapped.device))
            actions = torch.where(step_counters[:, None] < 3, zero_action, policy(obs))
            # actions = policy(obs)
            
            # env stepping
            cam_dict = {
                "cam_high": env.env.scene.sensors["cam_high"].data.output["rgb"],
                "cam_left_wrist": env.env.scene.sensors["cam_left_wrist"].data.output["rgb"],
                "cam_right_wrist": env.env.scene.sensors["cam_right_wrist"].data.output["rgb"]
            }
            # *** here we get the image and obs
            
            obs_next, reward, done, info = env.step(actions)
            # import pdb; pdb.set_trace()
            
            # *** here we save the image and obs
            get_image_and_save_step(env.env, obs_dict['observations']['student'], cam_dict, reward)
            # TODO: copy the last qpos
            
            # save the terminated trajectory, terminated_env are the env_id in which done == 1
            terminated_env = torch.nonzero(done).squeeze(1)
            # print("terminated_env", terminated_env)
            # import pdb; pdb.set_trace()
            if len(terminated_env) > 0:
                reset_dummy_save_traj(env.env, terminated_env)
            
            # in the first 3 step, we use all zero action rather than policy action
            # done_episodes are those env in which done == 1
            # update step counters and reset those that have done episodes
            step_counters += 1
            step_counters = torch.where(done.bool(), 0, step_counters)
            
            # obs = obs_next
            obs, obs_dict = env.get_observations()


    # close the simulator
    env.close()


if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()
