import numpy as np
import torch
import os
import h5py
from torch.utils.data import TensorDataset, DataLoader
import random
import IPython
from PIL import Image
import ManiBox
from ManiBox.utils import get_norm_stats_old

import cv2

class EpisodicDataset(torch.utils.data.Dataset):

    def __init__(self, episode_ids, dataset_dir, camera_names, norm_stats, arm_delay_time, max_pos_lookahead,
                 use_dataset_action, use_depth_image, use_robot_base, episode_begin, episode_end):
        super(EpisodicDataset).__init__()
        self.episode_ids = episode_ids  # 1000
        self.dataset_dir = dataset_dir
        self.camera_names = camera_names
        self.norm_stats = norm_stats
        self.is_sim = None
        self.max_pos_lookahead = max_pos_lookahead
        self.use_dataset_action = use_dataset_action
        self.use_depth_image = use_depth_image
        self.arm_delay_time = arm_delay_time
        self.use_robot_base = use_robot_base
        
        self.episode_begin = episode_begin
        self.episode_end = episode_end
        
        self.__getitem__(0)  # initialize self.is_sim

    def __len__(self):
        return len(self.episode_ids)

    def shuffle(self):
        np.random.shuffle(self.episode_ids)
        
    def __getitem__(self, index):
        # print('episode_ids', self.episode_ids)
        episode_id = self.episode_ids[index]
        # print(f"episode_id {episode_id}")
        dataset_path = os.path.join(self.dataset_dir, f'episode_{episode_id}.hdf5')
        # print('load path:', dataset_path)

        with h5py.File(dataset_path, 'r') as root:
            # import pdb
            # pdb.set_trace()
            # keys in root: ['action', 'base_action', 'observations']
            # root['action']: 500 * 14
            # root['observations']: 'effort', 'images', 'images_depth', 'qpos', 'qvel'
            # keys in root.attrs: sim, compress
            
            # if self.episode_begin is not None:
            #     root['action'] = root['action'][self.episode_begin:self.episode_end]
            #     root['base_action'] = root['base_action'][self.episode_begin:self.episode_end]
            #     root['observations/effort'] = root['observations/effort'][self.episode_begin:self.episode_end]
            #     root['observations/qpos'] = root['observations/qpos'][self.episode_begin:self.episode_end]
            #     root['observations/qvel'] = root['observations/qvel'][self.episode_begin:self.episode_end]
            #     root['observations/images/cam_high'] = root['observations/images/cam_high'][self.episode_begin:self.episode_end]
            #     root['observations/images/cam_left_wrist'] = root['observations/images/cam_left_wrist'][self.episode_begin:self.episode_end]
            #     root['observations/images/cam_right_wrist'] = root['observations/images/cam_right_wrist'][self.episode_begin:self.episode_end]
            #     root['observations/images_depth/cam_high'] = root['observations/images_depth/cam_high'][self.episode_begin:self.episode_end]
            #     root['observations/images_depth/cam_left_wrist'] = root['observations/images_depth/cam_left_wrist'][self.episode_begin:self.episode_end]
            #     root['observations/images_depth/cam_right_wrist'] = root['observations/images_depth/cam_right_wrist'][self.episode_begin:self.episode_end]
            
            
            is_sim = root.attrs['sim']
            is_compress = root.attrs['compress']
            original_action_shape = root['/action'][self.episode_begin:self.episode_end].shape
            max_action_len = original_action_shape[0]  # max_episode
            if self.use_robot_base:
                original_action_shape = (original_action_shape[0], original_action_shape[1] + 2)

            # max_action_len may be self.episode_end 
            start_ts = np.random.choice(max_action_len)  
            next_action_size = random.randint(0, self.max_pos_lookahead)
            if self.use_dataset_action:
                actions = root['/action'][self.episode_begin:self.episode_end]
            else:
                actions = root['/observations/qpos'][self.episode_begin:self.episode_end][1:]
                actions = np.append(actions, actions[-1][np.newaxis, :], axis=0)
            end_next_action_index = min(start_ts + next_action_size, max_action_len - 1)
            qpos = root['/observations/qpos'][self.episode_begin:self.episode_end][start_ts]
            if self.use_robot_base:
                qpos = np.concatenate((qpos, root['/base_action'][self.episode_begin:self.episode_end][start_ts]), axis=0)
            image_dict = dict()
            image_depth_dict = dict()
            for cam_name in self.camera_names:
                if is_compress:
                    
                    decoded_image = root[f'/observations/images/{cam_name}'][self.episode_begin:self.episode_end][start_ts]
                    # image_dict[cam_name] = cv2.imdecode(decoded_image, 1)
                    image_dict[cam_name] = cv2.cvtColor(cv2.imdecode(np.frombuffer(decoded_image, np.uint8), 1), cv2.COLOR_BGR2RGB) 
                    # Image.fromarray(image_dict[cam_name], 'RGB').save(f'{cam_name}_first_image.jpg', 'JPEG')
                    # cv2.imwrite(f'~/Videos/ACT_reconstruction_image.jpg', image_dict[cam_name])
                    # print("save image!")
                    # exit(0)
                    # print(image_dict[cam_name].shape)
                    # exit(-1)
                else:
                    image_dict[cam_name] = root[f'/observations/images/{cam_name}'][self.episode_begin:self.episode_end][start_ts]

                if self.use_depth_image:
                    image_depth_dict[cam_name] = root[f'/observations/images_depth/{cam_name}'][self.episode_begin:self.episode_end][start_ts]

            start_action = end_next_action_index
            # action = actions[start_action:]
            # next_action = actions[start_ts:start_action]
            # action_len = max_action_len - start_action
            # next_action_len = start_action - start_ts
            index = max(0, start_action - self.arm_delay_time)
            # print("qpos:", qpos[7:-2])
            action = actions[index:]  # hack, to make timesteps more aligned
            # print("action:", action[:30, 7:-2])
            next_action = actions[start_ts:index]  # could be empty if start_ts == index
            if self.use_robot_base:
                action = np.concatenate((action, root['/base_action'][self.episode_begin:self.episode_end][index:]), axis=1)
                next_action = np.concatenate((next_action, root['/base_action'][self.episode_begin:self.episode_end][start_ts:index]), axis=1)
            action_len = max_action_len - index  # hack, to make timesteps more aligned
            next_action_len = index - start_ts
            # if is_sim:
            #     action = actions[start_action:]
            #     next_action = actions[start_ts:start_action]
            #     action_len = max_action_len - start_action
            #     next_action_len = start_action - start_ts
            # else:
            #     index = max(0, start_action - 1)
            #     action = actions[index:]  # hack, to make timesteps more aligned
            #     next_action = actions[start_ts:index]
            #     action_len = max_action_len - index  # hack, to make timesteps more aligned
            #     next_action_len = index - start_ts

        self.is_sim = is_sim

        padded_action = np.zeros(original_action_shape, dtype=np.float32)
        padded_action[:action_len] = action
        action_is_pad = np.zeros(max_action_len)
        action_is_pad[action_len:] = 1
        padded_next_action = np.zeros((self.max_pos_lookahead, original_action_shape[1]), dtype=np.float32)

        next_action_is_pad = np.zeros(self.max_pos_lookahead)
        if next_action_len <= 0:
            next_action_is_pad[:] = 1
        else:
            padded_next_action[:next_action_len] = next_action
            next_action_is_pad[next_action_len:] = 1

        all_cam_images = []
        for cam_name in self.camera_names:
            all_cam_images.append(image_dict[cam_name])
        all_cam_images = np.stack(all_cam_images, axis=0)
        # construct observations
        image_data = torch.from_numpy(all_cam_images)
        image_data = torch.einsum('k h w c -> k c h w', image_data)
        # image_data: (cam_num, RGB3, 480, 640)
        image_data = image_data / 255.0

        image_depth_data = np.zeros(1, dtype=np.float32)
        if self.use_depth_image:
            all_cam_images_depth = []
            for cam_name in self.camera_names:
                all_cam_images_depth.append(image_depth_dict[cam_name])
            all_cam_images_depth = np.stack(all_cam_images_depth, axis=0)
            # construct observations
            image_depth_data = torch.from_numpy(all_cam_images_depth)
            # image_depth_data = torch.einsum('k h w c -> k c h w', image_depth_data)
            image_depth_data = image_depth_data / 255.0

        qpos_data = torch.from_numpy(qpos).float()
        qpos_data = (qpos_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]
        next_action_data = torch.from_numpy(padded_next_action).float()
        next_action_is_pad = torch.from_numpy(next_action_is_pad).bool()
        action_data = torch.from_numpy(padded_action).float()
        action_is_pad = torch.from_numpy(action_is_pad).bool()
        if self.use_dataset_action:
            next_action_data = (next_action_data - self.norm_stats["action_mean"]) / self.norm_stats["action_std"]
            action_data = (action_data - self.norm_stats["action_mean"]) / self.norm_stats["action_std"]
        else:
            next_action_data = (next_action_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]
            action_data = (action_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]

        # torch.set_printoptions(precision=10, sci_mode=False)
        # torch.set_printoptions(threshold=float('inf'))
        # print("qpos_data:", qpos_data[7:])
        # print("action_data:", action_data[:, 7:])
        
        # import pdb; pdb.set_trace()
        # image_data.shape: (3, 3, 480, 640)
        # qpos_data.shape: (14)
        # action_data.shape: (~87, 14)
        return image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad

