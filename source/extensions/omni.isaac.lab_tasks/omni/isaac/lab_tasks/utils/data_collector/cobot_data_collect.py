import time
import h5py
import argparse
import os
import torch
import numpy as np
from omni.isaac.lab_tasks.manager_based.manipulation.lift import ObjectHisPosBuf, CollectEpsBuf
from VFCNet.yolo_process_data import YoloCollectData, plot_xyxyn_boxes_to_image
import dm_env
from omni.isaac.lab_tasks.utils.data_collector.compress_data import compress_single_hdf5
import cv2

# project_to_rotation and save_data is for image-based data
# v4 is for bbox-based data

def project_to_rotation(offset):
    """
    The gripper is controlled parallel in simulator, but with gear in real machine,
    apply projection function to transfer the action
    
    Input: horizontal offset of gripper (num_envs, 1)
    Output: rotate angle radians
    """
    # define the hyper-params 
    # TODO: need adjustment
    # Radius = 2.00
    # radius = 3.2
    # theta = 2.5
    
    # arc = (offset - torch.tensor(Radius) * torch.sin(torch.tensor(theta))) / (2 * torch.tensor(radius))
    # angle_of_rotation = torch.clamp(torch.asin(arc), -1, 1)
    
    # return angle_of_rotation.unsqueeze(0)
    # expected offset: [0, 0.042]
    
    # if offset is float
    if isinstance(offset, float): 
        qpos = 107.43576967 * offset - 0.14160313
        # clip the qpos to [-0.183, 4.5]
        qpos = np.clip(qpos, -0.183, 4.3)
        return qpos
    elif isinstance(offset, torch.Tensor):
        qpos = 107.43576967 * offset - 0.14160313
        # clip the qpos to [-0.183, 4.5]
        qpos = torch.clamp(qpos, -0.183, 4.3)
        return qpos


def transfer_sim_image_to_standard_img_tensor(img):
    """
    Args:
        img (torch.Tensor): (num_envs, 480, 640, 4), RGB, 0~255(torch.uint8)
        num_envs dim is not necessary

    Returns:
        torch.Tensor: (num_envs, 3, 480, 640), RGB, 0~1(torch.float32)
    """
    assert isinstance(img, torch.Tensor)
    if len(img.shape) == 4:
        return img[:, :, :, :3].permute(0, 3, 1, 2).float() / 255.0
    elif len(img.shape) == 3:
        return img[:, :, :3].permute(2, 0, 1).float() / 255.0


from VFCNet.yolo_process_data import YoloProcessDataByTimeStep

def push_tensor_obs_action_to_buf(obs_tensor, cam_high, cam_left_wrist, cam_right_wrist, reward, env_id, info:dict=None, bboxes=None):
    """Convert obs tensor from single env to the unified data form. And save it.
    all the args are **torch.tensor()**
    
    obs_tensor must be from obs_dict["student"], so that qpos is placed at the beginning of the obs
    """
    # print("-----------------------------------------cam_high", cam_high.shape)
    # cam_high torch.Size([480, 640, 4])
    # cam_high = cam_high.unsqueeze(0)
    # cam_left_wrist = cam_left_wrist.unsqueeze(0)
    # cam_right_wrist = cam_right_wrist.unsqueeze(0)
    
    # qpos
    # TODO: Attention! check the index of qpos every time you change the observation space
    qpos = obs_tensor[0:6].cpu().numpy()  # left arm
    left_gripper_qpos = obs_tensor[6:8].cpu()

    left_gripper_qpos_mean = project_to_rotation(torch.mean(left_gripper_qpos).item())
    processed_gripper_qpos = np.array([left_gripper_qpos_mean])
    # concat left gripper
    qpos = np.concatenate([qpos, processed_gripper_qpos], axis=-1)    # concat left gripper
    # concat right arm and right gripper
    qpos = np.concatenate([qpos, np.zeros([7])], axis=-1)
    
    # qvel
    qvel = obs_tensor[11:17].cpu().numpy()  # left arm
    left_gripper_qvel = np.zeros([1])
    # concat left gripper
    qvel = np.concatenate([qvel, left_gripper_qvel], axis=-1)
    # concat right arm and right gripper: we currently do not use the right arm
    qvel = np.concatenate([qvel, np.zeros([7])], axis=-1)
    
    # In fact, the action here is of no use. The action will be set to the next qpos anyway.
    left_arm_actions = obs_tensor[-8:].cpu().numpy() 
    
    # clip first six dimension and concatenate with projected gripper actions
    # action = obs_tensor[50:56].cpu().numpy() 
    
    # gripper_actions = obs_tensor[57].cpu() # the last two dimensions are set to be the same
    # processed_gripper_actions = project_to_rotation(gripper_actions).numpy()
    
    # concatenate the two piece of actions
    # left_arm_actions = np.concatenate([action, processed_gripper_actions], axis=-1)
    
    # concat right action: 0
    action = np.concatenate([left_arm_actions, np.zeros([7])], axis=-1)
    dtype = np.float32
    
    if CollectEpsBuf.use_yolo_sync_process:  # it is the part of push_tensor_obs_action_to_buf_v4()
        # push_tensor_obs_action_to_buf_v4(obs_tensor, cam_high, cam_left_wrist, cam_right_wrist, reward, env_id, info)
        if bboxes is None:
            # YoloCollectData.envs_process[env_id].process(cam_high[:, :, :3], cam_left_wrist[:, :, :3], cam_right_wrist[:, :, :3])
            image_data = YoloCollectData.envs_process[0].process(
                transfer_sim_image_to_standard_img_tensor(cam_high), 
                transfer_sim_image_to_standard_img_tensor(cam_left_wrist), 
                transfer_sim_image_to_standard_img_tensor(cam_right_wrist)
            ) 
            # image_data: (1, 12 * len(objects_names))
        else:
            image_data = bboxes[env_id:env_id+1]  # (1, 12 * len(objects_names))
        obs = {
            'images': {
                # 'cam_high': 
                #     # cv2.imencode('.jpg', cam_high[:, :, :3].cpu().numpy())[1].tobytes(),
                #     cam_high[:, :, :3],
                # 'cam_left_wrist': 
                #     # cv2.imencode('.jpg', cam_left_wrist[:, :, :3].cpu().numpy())[1].tobytes(),
                #     cam_left_wrist[:, :, :3],
                # 'cam_right_wrist': 
                #     # cv2.imencode('.jpg', cam_right_wrist[:, :, :3].cpu().numpy())[1].tobytes(),
                #     cam_right_wrist[:, :, :3],
            },
            'images_depth': None,
            'qpos': qpos.astype(dtype),
            'qvel': qvel.astype(dtype),
            'effort': np.zeros([14], dtype=dtype),  # TODO
            'base_vel': np.zeros([2], dtype=dtype),  # TODO
            'image_data': image_data,
        }
    else:
        obs = {
            'images': {
                'cam_high': 
                    cv2.imencode('.jpg', cam_high[:, :, :3].cpu().numpy())[1].tobytes() if CollectEpsBuf.is_compress \
                        else cam_high[:, :, :3].cpu().numpy(),
                'cam_left_wrist': 
                    cv2.imencode('.jpg', cam_left_wrist[:, :, :3].cpu().numpy())[1].tobytes() if CollectEpsBuf.is_compress \
                        else cam_left_wrist[:, :, :3].cpu().numpy(),
                    # cam_left_wrist[:, :, :3].cpu().numpy(),
                'cam_right_wrist': 
                    cv2.imencode('.jpg', cam_right_wrist[:, :, :3].cpu().numpy())[1].tobytes() if CollectEpsBuf.is_compress \
                        else cam_right_wrist[:, :, :3].cpu().numpy(),
                    # cam_right_wrist[:, :, :3].cpu().numpy(),
            },
            'images_depth': None,
            'qpos': qpos.astype(dtype),
            'qvel': qvel.astype(dtype),
            'effort': np.zeros([14], dtype=dtype),  # TODO
            'base_vel': np.zeros([2], dtype=dtype),  # TODO
        }
    
    step_type = dm_env.StepType.MID if len(CollectEpsBuf.timesteps[env_id]) > 0 else dm_env.StepType.FIRST
    
    CollectEpsBuf.timesteps[env_id].append(obs)
    CollectEpsBuf.actions[env_id].append(action.astype(dtype))  # the action is not correct, will be replaced as next qpos in `randomization.py`
    
    CollectEpsBuf.rewards[env_id].append(reward.item())  
    # dont append reward which is tensor and will cause same-reward-problem
    CollectEpsBuf.infos[env_id].append(info)
    # TODO: if CollectEpsBuf.trajectory_num < len(CollectEpsBuf.timesteps) and env_id==0, then save the image with bbox
    if CollectEpsBuf.use_yolo_sync_process and bboxes is not None:
        # step = len(CollectEpsBuf.rewards[env_id]) - 1
        # if step < 90 and step > 30 and (obs['qpos'][6] > 4.0 or obs['qpos'][6] < 2.0):
        #     print("qpos is abnormally small/big")
        #     breakpoint()
        #     plot_xyxyn_boxes_to_image(
        #         transfer_sim_image_to_standard_img_tensor(cam_high), 
        #         bboxes[env_id:env_id+1, :4], 
        #         f"cam_high_{len(CollectEpsBuf.rewards[env_id])-1}",
        #         CollectEpsBuf.images_path
        #     )
            
        #     plot_xyxyn_boxes_to_image(
        #         transfer_sim_image_to_standard_img_tensor(cam_left_wrist), 
        #         bboxes[env_id:env_id+1, 4:8], 
        #         f"cam_left_wrist_{len(CollectEpsBuf.rewards[env_id])-1}",
        #         CollectEpsBuf.images_path
        #     )
            
        #     plot_xyxyn_boxes_to_image(
        #         transfer_sim_image_to_standard_img_tensor(cam_right_wrist), 
        #         bboxes[env_id:env_id+1, 8:12], 
        #         f"cam_right_wrist_{len(CollectEpsBuf.rewards[env_id])-1}",
        #         CollectEpsBuf.images_path
        #     )
        #     breakpoint()
        if CollectEpsBuf.trajectory_num < len(CollectEpsBuf.timesteps) and env_id == 0:
            # import pdb; pdb.set_trace()
            plot_xyxyn_boxes_to_image(
                transfer_sim_image_to_standard_img_tensor(cam_high), 
                bboxes[env_id:env_id+1, :4], 
                f"cam_high_{len(CollectEpsBuf.rewards[env_id])-1}",
                CollectEpsBuf.images_path
            )
            
            plot_xyxyn_boxes_to_image(
                transfer_sim_image_to_standard_img_tensor(cam_left_wrist), 
                bboxes[env_id:env_id+1, 4:8], 
                f"cam_left_wrist_{len(CollectEpsBuf.rewards[env_id])-1}",
                CollectEpsBuf.images_path
            )
            
            plot_xyxyn_boxes_to_image(
                transfer_sim_image_to_standard_img_tensor(cam_right_wrist), 
                bboxes[env_id:env_id+1, 8:12], 
                f"cam_right_wrist_{len(CollectEpsBuf.rewards[env_id])-1}",
                CollectEpsBuf.images_path
            )
            # TODO: refer to BBoxHistoryEpisodicDataset, add kalman filter
# plot_xyxyn_boxes_to_image(transfer_sim_image_to_standard_img_tensor(cam_high), bboxes[env_id, :4], f"cam_high_{len(CollectEpsBuf.rewards[env_id])-1}","./data/images/")
# YoloCollectData.envs_process[env_id].process(transfer_sim_image_to_standard_img_tensor(cam_high), transfer_sim_image_to_standard_img_tensor(cam_left_wrist), transfer_sim_image_to_standard_img_tensor(cam_right_wrist)) 
# YoloCollectData.envs_process[env_id].detect_bounding_boxes(transfer_sim_image_to_standard_img_tensor(cam_high))


def save_data(args, timesteps, actions, rewards, infos, dataset_path, flat_reward):
    if CollectEpsBuf.use_yolo_sync_process:
        save_data_v4(args, timesteps, actions, rewards, infos, dataset_path, flat_reward)
        return
    # breakpoint()
        
    # drop the first step of each episode
    # TODO: maybe should drop ~10 steps
    # timesteps = timesteps[1:]
    # actions = actions[1:]
    CollectEpsBuf.trajectory_num += 1
    print(f"\nsaving the trajectory No.{CollectEpsBuf.trajectory_num} to {dataset_path}: \
        len: {len(timesteps)}, reward: {flat_reward:.3f}\n\n")
    t0 = time.time()
    # current path: os.getcwd() is xxx/GES-low-level-Orbit
    # dataset_path is like xxx/data/mobile_aloha/episode_0
    # if not os.path.exists(dataset_path):
    #     os.makedirs(dataset_path, exist_ok=True)
    
    data_dict = {
        # 一个是奖励里面的qpos，qvel， effort ,一个是实际发的action
        '/observations/qpos': [],
        '/observations/qvel': [],
        '/observations/effort': [],
        '/action': [],
        '/reward': [],
        '/base_action': [],
        # '/base_action_t265': [],
    }
    # 相机字典  观察的图像
    for cam_name in args.camera_names:
        data_dict[f'/observations/images/{cam_name}'] = []
        if args.use_depth_image:
            data_dict[f'/observations/images_depth/{cam_name}'] = []
    # 下面这个循环其实是没有必要的，不过save_data这个函数总耗时为0.0s，所以懒得改了
    while actions:
        # 循环弹出一个队列
        action = actions.pop(0)   # 动作  当前动作
        reward = rewards.pop(0)   # 动作  当前动作
        ts = timesteps.pop(0)     # 奖励  前一帧

        # 往字典里面添值
        # Timestep返回的qpos，qvel,effort
        data_dict['/observations/qpos'].append(ts['qpos'])
        data_dict['/observations/qvel'].append(ts['qvel'])
        data_dict['/observations/effort'].append(ts['effort'])

        # 实际发的action
        data_dict['/action'].append(action)
        data_dict['/base_action'].append(ts['base_vel'])
        data_dict['/reward'].append(reward)

        # 相机数据
        for cam_name in args.camera_names:
            data_dict[f'/observations/images/{cam_name}'].append(ts['images'][cam_name])
            if args.use_depth_image:
                data_dict[f'/observations/images_depth/{cam_name}'].append(ts['images_depth'][cam_name])
    
    base_action_t265 = None
    # for root, dirs, files in os.walk(dataset_dir):
        # for filename in fnmatch.filter(files, '*.hdf5'):
    action = data_dict['/action'][:]
    reward = data_dict['/reward'][:]
    base_action = data_dict['/base_action'][:]
    if 'base_action_t265' in data_dict:
        base_action_t265 = data_dict['/base_action_t265'][:]
    else:
        base_action_t265 = None
    qpos = data_dict['/observations/qpos'][:]
    qvel = data_dict['/observations/qvel'][:]
    effort = data_dict['/observations/effort'][:]
    cam_high = data_dict['/observations/images/cam_high'][:]
    cam_left_wrist = data_dict['/observations/images/cam_left_wrist'][:]
    cam_right_wrist = data_dict['/observations/images/cam_right_wrist'][:]
    # cam_high = [cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() \
    #     for img in data_dict['/observations/images/cam_high'][:]]
    # cam_left_wrist = [cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() \
    #     for img in data_dict['/observations/images/cam_left_wrist'][:]]
    # cam_right_wrist = [cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() \
    #     for img in data_dict['/observations/images/cam_right_wrist'][:]]
    if args.use_depth_image:
        try:
            cam_high_depth = data_dict['/observations/images_depth/cam_high'][:]
            cam_left_wrist_depth = data_dict['/observations/images_depth/cam_left_wrist'][:]
            cam_right_wrist_depth = data_dict['/observations/images_depth/cam_right_wrist'][:]
        except KeyError:
            cam_high_depth = None
            cam_left_wrist_depth = None
            cam_right_wrist_depth = None
            print("No depth images found in the dataset")
    else:
        cam_high_depth = None
        cam_left_wrist_depth = None
        cam_right_wrist_depth = None
        print("Depth images not saved")
    
    filename = dataset_path.split('/')[-1] + ".hdf5"
    dataset_path = '/'.join(dataset_path.split('/')[:-1])
    # if new file already exists, delete the old one
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path, exist_ok=True)
    new_file_path = os.path.join(dataset_path, filename)
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    
    
    with h5py.File(new_file_path, 'a') as f_new:
        f_new.attrs['sim'] = False
        f_new.attrs['compress'] = CollectEpsBuf.is_compress
        
        f_new.create_dataset('action', data=action)
        f_new.create_dataset('reward', data=reward)
        f_new.create_dataset('base_action', data=base_action)
        if base_action_t265 is not None:
            f_new.create_dataset('base_action_t265', data=base_action_t265)
        f_new.create_dataset('observations/qpos', data=qpos)
        f_new.create_dataset('observations/qvel', data=qvel)
        f_new.create_dataset('observations/effort', data=effort)
        f_new.create_dataset('observations/images/cam_high', data=np.bytes_(cam_high))
        f_new.create_dataset('observations/images/cam_left_wrist', data=np.bytes_(cam_left_wrist))
        f_new.create_dataset('observations/images/cam_right_wrist', data=np.bytes_(cam_right_wrist))
        if cam_high_depth is not None:
            f_new.create_dataset('observations/images_depth/cam_high', data=np.bytes_(cam_high_depth))
            f_new.create_dataset('observations/images_depth/cam_left_wrist', data=np.bytes_(cam_left_wrist_depth))
            f_new.create_dataset('observations/images_depth/cam_right_wrist', data=np.bytes_(cam_right_wrist_depth))
        
    from datetime import datetime
    time_now = datetime.now()
    timestamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")
    print(f"Processed {filename} Saving: {time.time() - t0:.1f} secs, in {timestamp}")


def save_data_v4(args, timesteps, actions, rewards, infos, dataset_path, flat_reward):
    # drop the first step of each episode
    # TODO: maybe should drop ~10 steps
    # timesteps = timesteps[1:]
    # actions = actions[1:]
    dataset_dir = "/".join(dataset_path.split('/')[:-1])
    CollectEpsBuf.trajectory_num += 1
    print(f"\nsaving the trajectory No.{CollectEpsBuf.trajectory_num} to {dataset_dir}/integration: \
        len: {len(timesteps)}, reward: {flat_reward:.3f}")
    t0 = time.time()
    # current path: os.getcwd() is xxx/GES-low-level-Orbit
    # dataset_path is like xxx/data/mobile_aloha/episode_0
    # if not os.path.exists(dataset_path):
    #     os.makedirs(dataset_path, exist_ok=True)
    
    data_dict = {
        # 一个是奖励里面的qpos，qvel， effort ,一个是实际发的action
        '/observations/qpos': [],
        '/observations/qvel': [],
        '/observations/effort': [],
        '/action': [],
        '/reward': [],
        '/base_action': [],
        '/image_data': [],
    }
    # # 相机字典  观察的图像
    # for cam_name in args.camera_names:
    #     data_dict[f'/observations/images/{cam_name}'] = []
    #     if args.use_depth_image:
    #         data_dict[f'/observations/images_depth/{cam_name}'] = []
    # 下面这个循环其实是没有必要的，不过save_data这个函数总耗时为0.0s，所以懒得改了
    while actions:
        # 循环弹出一个队列
        action = actions.pop(0)   # 动作  当前动作
        reward = rewards.pop(0)   # 动作  当前动作
        ts = timesteps.pop(0)     # 奖励  前一帧

        # 往字典里面添值
        # Timestep返回的qpos，qvel,effort
        data_dict['/observations/qpos'].append(ts['qpos'])
        data_dict['/observations/qvel'].append(ts['qvel'])
        data_dict['/observations/effort'].append(ts['effort'])

        # 实际发的action
        data_dict['/action'].append(action)
        data_dict['/reward'].append(reward)
        data_dict['/base_action'].append(ts['base_vel'])
        # 相机数据
        data_dict['/image_data'].append(ts['image_data'])
    
    base_action_t265 = None
    # for root, dirs, files in os.walk(dataset_dir):
        # for filename in fnmatch.filter(files, '*.hdf5'):
    action = data_dict['/action'][:]
    reward = data_dict['/reward'][:]
    base_action = data_dict['/base_action'][:]
    if 'base_action_t265' in data_dict:
        base_action_t265 = data_dict['/base_action_t265'][:]
    else:
        base_action_t265 = None
    qpos = data_dict['/observations/qpos'][:]
    qvel = data_dict['/observations/qvel'][:]
    effort = data_dict['/observations/effort'][:]
    image_data = data_dict['/image_data'][:]
    image_data = torch.cat(image_data, dim=0)  # (120, 24)
    
    if args.use_depth_image:
        try:
            cam_high_depth = data_dict['/observations/images_depth/cam_high'][:]
            cam_left_wrist_depth = data_dict['/observations/images_depth/cam_left_wrist'][:]
            cam_right_wrist_depth = data_dict['/observations/images_depth/cam_right_wrist'][:]
        except KeyError:
            cam_high_depth = None
            cam_left_wrist_depth = None
            cam_right_wrist_depth = None
            print("No depth images found in the dataset")
    else:
        cam_high_depth = None
        cam_left_wrist_depth = None
        cam_right_wrist_depth = None
        print("Depth images not saved")
    
    YoloCollectData.save_data(image_data, qpos, action, reward, dataset_dir)
        
    from datetime import datetime
    time_now = datetime.now()
    timestamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")
    print(f"Yolo-Processed {dataset_dir}/integration [{CollectEpsBuf.trajectory_num - 1}] cost: {time.time() - t0:.1f} secs in {timestamp}")
