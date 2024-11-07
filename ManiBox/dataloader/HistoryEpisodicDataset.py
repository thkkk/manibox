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
from ManiBox.dataloader.EpisodicDataset import EpisodicDataset
# from ManiBox.utils.try_yolo import output_RGB_image

from matplotlib import pyplot as plt
def output_RGB_image(img):
    plt.imshow(img)
    plt.show()

class HistoryEpisodicDataset(torch.utils.data.Dataset):

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
            
            is_sim = root.attrs['sim']
            is_compress = root.attrs['compress']
            original_action_shape = root['/action'][self.episode_begin:self.episode_end].shape
            max_action_len = original_action_shape[0]  # max_episode
            if self.use_robot_base:
                original_action_shape = (original_action_shape[0], original_action_shape[1] + 2)

            # max_action_len may be self.episode_end 
            start_ts = max_action_len
            history_start = 0
            # input: states of timesteps [history_start, start_ts]
            # output: actions of timesteps [start_ts, start_ts + ?]
            next_action_size = random.randint(0, self.max_pos_lookahead)
            if self.use_dataset_action:
                actions = root['/action'][self.episode_begin:self.episode_end]
            else:
                actions = root['/observations/qpos'][self.episode_begin:self.episode_end][1:]
                actions = np.append(actions, actions[-1][np.newaxis, :], axis=0)
            end_next_action_index = min(start_ts + next_action_size, max_action_len - 1)
            
            # state: qpos and images
            # TODO: i have not modified the extra branch below
            qpos = root['/observations/qpos'][self.episode_begin:self.episode_end][history_start: start_ts + 1]
            if self.use_robot_base:
                qpos = np.concatenate((qpos, root['/base_action'][self.episode_begin:self.episode_end][start_ts]), axis=0)
            # image_dict = dict()
            all_cam_images = []  # (cam_num, context_len, 480, 640, RGB3)
            # image_depth_dict = dict()
            all_cam_images_depth = []
            for cam_name in self.camera_names:
                all_cam_images.append([])  # cam_num
                if is_compress:
                    decoded_image = root[f'/observations/images/{cam_name}'][self.episode_begin:self.episode_end][history_start: start_ts + 1]
                    for i in range(decoded_image.shape[0]):  # i: each timestep
                        image = cv2.imdecode(np.frombuffer(decoded_image[i], np.uint8), 1)
                        all_cam_images[-1].append(image)  # (480, 640, RGB3)
                        # image here is RGB, (480, 640, 3), 0~255
                    # image_dict[cam_name] = cv2.cvtColor(cv2.imdecode(np.frombuffer(decoded_image, np.uint8), 1), cv2.COLOR_BGR2RGB) 
                    
                    # test:
                    # image = cv2.imdecode(np.frombuffer(decoded_image[10], np.uint8), 1)
                    # print("image.shape", image.shape)
                    # print("image value", image[0, 0, :])
                    # output_RGB_image(image)
                    # exit(0)
                    # Image.fromarray(image, 'RGB').save(f'{cam_name}_first_image.jpg', 'JPEG')
                    # cv2.imwrite(f'~/Videos/ACT_reconstruction_image.jpg', image)
                    # print("save image!")
                    # exit(0)
                else:
                    all_cam_images[-1].append(root[f'/observations/images/{cam_name}'][self.episode_begin:self.episode_end][start_ts])

                if self.use_depth_image:
                    all_cam_images_depth.append([])
                    all_cam_images_depth[-1].append(root[f'/observations/images_depth/{cam_name}'][self.episode_begin:self.episode_end][start_ts])

            action = actions[history_start: start_ts + 1] 
            next_action = actions[start_ts: start_ts] # []
            if self.use_robot_base:
                action = np.concatenate((action, root['/base_action'][self.episode_begin:self.episode_end][index:]), axis=1)
                next_action = np.concatenate((next_action, root['/base_action'][self.episode_begin:self.episode_end][start_ts:index]), axis=1)

        self.is_sim = is_sim
        padded_next_action = np.zeros((self.max_pos_lookahead, original_action_shape[1]), dtype=np.float32)

        next_action_is_pad = np.zeros(self.max_pos_lookahead)

        # all_cam_images = []
        # for cam_name in self.camera_names:
        #     all_cam_images.append(image_dict[cam_name])
        all_cam_images = np.stack(all_cam_images, axis=0)
        # construct observations
        image_data = torch.from_numpy(all_cam_images)
        # image_data: (cam_num, context_len, 480, 640, RGB3)
        image_data = torch.einsum('n k h w c -> k n c h w', image_data)
        # image_data: (context_len, cam_num, RGB3, 480, 640)
        image_data = image_data / 255.0

        image_depth_data = np.zeros(1, dtype=np.float32)
        if self.use_depth_image:
            # all_cam_images_depth = []
            # for cam_name in self.camera_names:
            #     all_cam_images_depth.append(image_depth_dict[cam_name])
            all_cam_images_depth = np.stack(all_cam_images_depth, axis=0)
            # construct observations
            image_depth_data = torch.from_numpy(all_cam_images_depth)
            # image_depth_data = torch.einsum('k h w c -> k c h w', image_depth_data)
            image_depth_data = image_depth_data / 255.0

        qpos_data = torch.from_numpy(qpos).float()
        qpos_data = (qpos_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]
        
        next_action_data = torch.from_numpy(padded_next_action).float()
        next_action_is_pad = torch.from_numpy(next_action_is_pad).bool()
        
        action_data = torch.from_numpy(action).float()
        action_is_pad = torch.zeros([action_data.shape[0]]).bool()
        
        if self.use_dataset_action:
            next_action_data = (next_action_data - self.norm_stats["action_mean"]) / self.norm_stats["action_std"]
            action_data = (action_data - self.norm_stats["action_mean"]) / self.norm_stats["action_std"]
        else:
            next_action_data = (next_action_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]
            action_data = (action_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]

        # import pdb; pdb.set_trace()
        # image_data.shape: (episode_len, cam_num=3, RGB=3, 480, 640)
        # qpos.shape: (episode_len, state_dim=14)
        # action_data.shape: (episode_len, action_dim=14)
        return image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad
