# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Script to play a checkpoint if an RL agent from RSL-RL."""

"""Launch Isaac Sim Simulator first."""

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

def main():
    """Play with RSL-RL agent."""
    # parse configuration
    env_cfg = parse_env_cfg(
        args_cli.task, use_gpu=not args_cli.cpu, num_envs=args_cli.num_envs, use_fabric=not args_cli.disable_fabric
    )
    agent_cfg: RslRlOnPolicyRunnerCfg = cli_args.parse_rsl_rl_cfg(args_cli.task, args_cli)
    
    # Async collect data and process it by yolo
    # if args_cli.task == "Isaac-Lift-Cube-MobileAloha-Play-v0":
    #     from VFCNet.yolo_process_data import AsyncYoloProcessDataFromHDF5
    #     num_envs = args_cli.num_envs
    #     processor = AsyncYoloProcessDataFromHDF5(num_envs, CollectEpsBuf.dataset_path)
    #     process_thread = threading.Thread(target=processor.run)
    #     process_thread.daemon = True  # 确保主线程退出时这个线程也退出
    #     process_thread.start()


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
    
    # reset environment
    obs, obs_dict = env.get_observations()
    # init: done_episodes are all env.num_envs
    step_counters = torch.zeros(env.num_envs, dtype=torch.int, device=env.unwrapped.device)

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
            obs, reward, done, info = env.step(actions)
            # print the action with 3 decimal points
            # print(f"action: {actions}\n")
            # if done:
            #     print("Episode done.\n-------------------------------------------------")
            # print(f"qpos: {torch.round(obs[:, 3:11] * 1000) / 1000}")
            # # print each dim of obs[:, 3:11] with 3 decimal points
            # print("qpos: ", end="")
            # ee_w = env.unwrapped.scene["ee_frame"].data.target_pos_w[..., 0, :]
            # cube_pos_w = env.unwrapped.scene["object"].data.root_pos_w 
            # # platform_height = env.unwrapped.scene['platform'].data.root_pos_w[:, 2].unsqueeze(1) + height_offset
            # # print("platform_height", platform_height, initial_object_height - 0.035)
            # distance = torch.norm(cube_pos_w - ee_w, dim=1).unsqueeze(1)            
            
            # term_cfg = env.env.reward_manager.get_term_cfg('reaching_object')
            # reaching_rew = term_cfg.func(env.env, **term_cfg.params)
            # import  omni.isaac.lab_tasks.manager_based.manipulation.lift.mdp as mdp
            # from omni.isaac.lab.managers import SceneEntityCfg
            # quat_rew = mdp.object_quat_similar(env.env, 0.1, SceneEntityCfg("object"), SceneEntityCfg("ee_frame")).item()
            # print("step ", step_counters.item(), "rew", reward.item(), "reaching", reaching_rew.item(), "quat", quat_rew)
            # success: rew > 1, reaching > 0.5, quat > 1.7
            # import pdb; pdb.set_trace()
            # object_quat_similar()
            # env.env.reward_manager.get_term_cfg
            
            # position_diff = torch.abs(ee_w - cube_pos_w)
            # # print(position_diff)
            # xy_dis = position_diff[..., :2].max(dim=1)
            # z_dis = position_diff[..., 2]
            # print("step", step_counters.item(), "distance", distance.item(), "xy_dis", xy_dis.values.item(), "z_dis", z_dis.item())
            
            # in the first 3 step, we use all zero action rather than policy action
            # done_episodes are those env in which done == 1
            # update step counters and reset those that have done episodes
            step_counters += 1
            # env.env
            step_counters = torch.where(done.bool(), 0, step_counters)


    # close the simulator
    env.close()


if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()
