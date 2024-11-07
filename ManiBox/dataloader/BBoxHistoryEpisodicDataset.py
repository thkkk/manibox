import numpy as np
import torch
import torch.nn as nn
import os
import h5py
from torch.utils.data import TensorDataset, DataLoader
import random
import IPython
from PIL import Image
import ManiBox

import cv2


import os
import random
import numpy as np
import torch
import cv2
import h5py
import glob
import contextlib
from torch.utils.data import Dataset

os.environ['YOLO_VERBOSE'] = str(False)  # disable the output of yolo predict
from ultralytics import YOLO

from ManiBox.dataloader.EpisodicDataset import EpisodicDataset
from ManiBox.yolo_process_data import YoloProcessDataByTimeStep, KalmanFilter

class BBoxHistoryEpisodicDataset(Dataset):

    def __init__(self, episode_ids, dataset_dir, camera_names, norm_stats, arm_delay_time, max_pos_lookahead,
                 use_dataset_action, use_depth_image, use_robot_base, episode_begin, episode_end, random_mask_ratio=0):
        # norm_stats above is useless
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
        self.random_mask_ratio = random_mask_ratio
        
        # load data dict from os.path.join(self.dataset_dir, f"integration.pkl")
        self.data = torch.load(os.path.join(self.dataset_dir, "integration.pkl"), map_location='cpu')
        # the data form: see process_data() in yolo_process_data.py
        print("Load data from", os.path.join(self.dataset_dir, "integration.pkl"), "Shape: ", self.data["image_data"].shape)
        image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad = self.__getitem__(0)
        print(f"image_data.shape, qpos_data.shape, action_data.shape: ", image_data.shape, qpos_data.shape, action_data.shape)

    def __len__(self):
        return len(self.episode_ids)
    
    def shuffle(self):
        np.random.shuffle(self.episode_ids)
     
    def get_bbox_idx(self, cam_idx, obj_idx):
        # bbox idx: [self.get_bbox_idx(cam_idx, obj_idx): self.get_bbox_idx(cam_idx, obj_idx)+4]
        return cam_idx * self.object_num * 4 + obj_idx * 4 
     
    def __getitem__(self, index):
        # NOTE: qpos and action here are not been normalized!!
        episode_id = self.episode_ids[index]
        
        # self.data["image_data"]:  Tensor, 
        image_data = self.data["image_data"][episode_id][self.episode_begin:self.episode_end]  # shape: (episode_end-episode_begin, 24)
        
        # for test, copy the image_data 
        # test_image = image_data.clone()
        # test_image = test_image.reshape(image_data.shape[0], 3, 2, 4)[0:10, 0, :, :]  # 3 cameras, apple and table, bbox xyxyn
        # print("test_image: ", test_image)
        
        epi_len = image_data.shape[0]
        
        if len(YoloProcessDataByTimeStep.objects_names) == 1 and image_data.shape[1] == 24:  # ["apple", \del"table"\del]
            # throw the bbox of table
            image_data = image_data.reshape(epi_len, 3, 2, 4)  # (epi_len, cam_num=3, object_num=2, 4)
            image_data = image_data[:, :, 0, :]
            image_data = image_data.reshape(epi_len, 12)   # shape: (epi_len, 12=3*4)
        # else image_data only contains apple, and its dim = 12
        
        image_depth_data = torch.zeros(1, dtype=torch.float32)  # just for batch iteration
        qpos_data = self.data["qpos_data"][episode_id][self.episode_begin:self.episode_end] 
        next_action_data, next_action_is_pad, action_is_pad = torch.zeros(1, dtype=torch.float32), torch.zeros(1, dtype=torch.float32), torch.zeros(1, dtype=torch.float32)
        action_data = self.data["action_data"][episode_id][self.episode_begin:self.episode_end]
        
        cam_num = len(self.camera_names)
        bbox_size = 4
        object_num = round(image_data.shape[1] / bbox_size / cam_num)
        self.cam_num = cam_num
        self.object_num = object_num
        
        # test: set cam_right to 0
        # image_data[:, 8:12] = 0.0
        
        # randomly mask one of the bbox to (0,0,0,0) in the image_data (5% probability in each timestep?)
        # randomly choose 5% timesteps to mask one of the bbox to (0,0,0,0)
        if self.random_mask_ratio != 0:
            mask_ratio = self.random_mask_ratio * np.random.rand()
            # mask_timesteps = np.random.choice(epi_len, int(epi_len*mask_ratio), replace=False)
            # mask_cam_idx = np.random.choice(cam_num, int(cam_num*epi_len))
            # mask_obj_idx = np.random.choice(object_num, int(epi_len*mask_ratio))
            # for i, mask_timestep in enumerate(mask_timesteps):
            #     bbox_idx = self.get_bbox_idx(mask_cam_idx[i], mask_obj_idx[i])
            #     image_data[mask_timestep, bbox_idx:bbox_idx+4] = torch.tensor([0, 0, 0, 0], dtype=torch.float32)
            # breakpoint()
            total_len = cam_num * epi_len
            cam_idx = np.full(total_len, -1)
            random_indices = np.random.choice(total_len, int(mask_ratio*total_len), replace=False)
            random_values = np.random.randint(0, 1, size = int(mask_ratio*total_len))
            cam_idx[random_indices] = random_values
            for i, mask_cam in enumerate(cam_idx):
                if mask_cam != -1:
                    bbox_idx = self.get_bbox_idx(i%cam_num, 0)
                    traj_idx = int(i / cam_num)
                    if traj_idx == 0 and bbox_idx == 0:
                        continue  # the first cam_high must be valid
                    image_data[traj_idx, bbox_idx:bbox_idx+4] = torch.tensor([0, 0, 0, 0], dtype=torch.float32)        
        
        # cam_ids = torch.tensor([0, 1, 2])

        # # cam ID one-hot encoding
        # # shape: (num_cams, cam_id_dim) => (3, 3)
        # cam_one_hot = nn.functional.one_hot(cam_ids, num_classes=cam_num).float()
        # # cam_one_hot[0] is like [1, 0, 0]
        # # image_data: (episode_len, 12)
        # # for each trajectory i, image_data[i] <- concat(image_data[i, 0:4], cam_one_hot[0], image_data[i, 4:8], 
        # # cam_one_hot[1], image_data[i, 8:12], cam_one_hot[2])
        # image_data = torch.cat([image_data[:, 0:4], cam_one_hot[0].repeat(epi_len, 1), image_data[:, 4:8],
        #                         cam_one_hot[1].repeat(epi_len, 1), image_data[:, 8:12], cam_one_hot[2].repeat(epi_len, 1)], dim=1)
        # # image_data: (episode_len, 12+3+3+3=21)
                    
        # apply kalman filter for smooth bbox
        # kalman_filter_objects = [[KalmanFilter() for _ in range(object_num)] for _ in range(cam_num)]
        
        # for i in range(cam_num):
        #     for j in range(object_num):
        #         # image_data.shape: (episode_len, 12)
        #         for k in range(epi_len):
        #             # image_data[k, i*bbox_size*object_num+j*bbox_size: i*bbox_size*object_num+(j+1)*bbox_size] is the bbox of object j in camera i
        #             bbox = image_data[k, i*bbox_size*object_num+j*bbox_size: i*bbox_size*object_num+(j+1)*bbox_size]
        #             image_data[k, i*bbox_size*object_num+j*bbox_size: i*bbox_size*object_num+(j+1)*bbox_size] = kalman_filter_objects[i][j].fill_missing_bbox_with_kalman(bbox)
        
        # normalize:
        # qpos_data = (qpos_data - self.norm_stats["qpos_mean"]) / self.norm_stats["qpos_std"]
        # action_data = (action_data - self.norm_stats["action_mean"]) / self.norm_stats["action_std"]
        
        # import pdb; pdb.set_trace()
        # qpos.shape: (episode_len, state_dim=14)
        # action_data.shape: (episode_len, action_dim=14)
        return image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad
