import numpy as np
import torch
import os
import h5py
from torch.utils.data import TensorDataset, DataLoader
import random
import IPython
from PIL import Image
import ManiBox
# from ManiBox.utils import get_norm_stats


e = IPython.embed
import cv2
from ManiBox.dataloader.EpisodicDataset import EpisodicDataset
from ManiBox.dataloader.HistoryEpisodicDataset import HistoryEpisodicDataset
from ManiBox.dataloader.BBoxHistoryEpisodicDataset import BBoxHistoryEpisodicDataset


def get_norm_stats(dataset_dir, num_episodes, episode_begin, episode_end):
    data = torch.load(os.path.join(dataset_dir, "integration.pkl"), map_location='cpu')
    # normalize all data["qpos_data"][:, episode_begin:episode_end] 
    qpos_mean = data["qpos_data"][:num_episodes, episode_begin:episode_end].mean(dim=[0, 1], keepdim=True)
    qpos_std = data["qpos_data"][:num_episodes, episode_begin:episode_end].std(dim=[0, 1], keepdim=True)
    qpos_std = torch.clip(qpos_std, 1e-2, np.inf)  # clipping
    
    action_mean = data["action_data"][:num_episodes, episode_begin:episode_end].mean(dim=[0, 1], keepdim=True)
    action_std = data["action_data"][:num_episodes, episode_begin:episode_end].std(dim=[0, 1], keepdim=True)
    action_std = torch.clip(action_std, 1e-2, np.inf)  # clipping
    
    data["qpos_data"] = (data["qpos_data"] - qpos_mean) / qpos_std
    data["action_data"] = (data["action_data"] - action_mean) / action_std
    
    norm_stats = {
        "action_mean": action_mean.numpy().squeeze(), "action_std": action_std.numpy().squeeze(),
        "qpos_mean": qpos_mean.numpy().squeeze(), "qpos_std": qpos_std.numpy().squeeze()
    }
    return norm_stats


def load_data(dataset_dir, num_episodes, arm_delay_time, max_pos_lookahead, use_dataset_action, 
              use_depth_image, use_robot_base, camera_names, batch_size_train, batch_size_val, episode_begin=0, episode_end=-1,
              context_len=1, prefetch_factor=2, dataset_type=HistoryEpisodicDataset):
    print(f'\nData from: {dataset_dir}\n')
    # obtain train test split
    train_ratio = 0.9  #  default 0.8
    shuffled_indices = np.random.permutation(num_episodes)  # 

    # TODO: debug for just 1 dataset, we use it for both training and testing
    train_indices = shuffled_indices[:int(train_ratio * num_episodes)]
    # print(f"train_indices {train_indices}")
    val_indices = shuffled_indices[int(train_ratio * num_episodes):]
    # val_indices = shuffled_indices[:int(train_ratio * num_episodes)]

    norm_stats = None
    # obtain normalization stats for qpos and action  
    norm_stats = get_norm_stats(dataset_dir, num_episodes, episode_begin, episode_end)

    # construct dataset and dataloader 
    # if context_len == 1:
    #     train_dataset = EpisodicDataset(train_indices, dataset_dir, camera_names, norm_stats, arm_delay_time,
    #                                     max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
    #                                     episode_begin, episode_end)

    #     val_dataset = EpisodicDataset(val_indices, dataset_dir, camera_names, norm_stats, arm_delay_time, 
    #                                 max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
    #                                 episode_begin, episode_end)
    # else:
    # train_dataset = HistoryEpisodicDataset(train_indices, dataset_dir, camera_names, norm_stats, arm_delay_time,
    #                                 max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
    #                                 episode_begin, episode_end)

    # val_dataset = HistoryEpisodicDataset(val_indices, dataset_dir, camera_names, norm_stats, arm_delay_time, 
    #                             max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
    #                             episode_begin, episode_end)
    
    if dataset_type is BBoxHistoryEpisodicDataset:
        if not os.path.exists(os.path.join(dataset_dir, f"integration.pkl")):
            from yolo_process_data import ProcessDataFromHDF5
            process_data = ProcessDataFromHDF5(shuffled_indices, dataset_dir, camera_names, norm_stats, arm_delay_time,
                                    max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
                                    episode_begin, episode_end)
            process_data.process_data() # TODO
    
    train_dataset = dataset_type(train_indices, dataset_dir, camera_names, norm_stats, arm_delay_time,
                                    max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
                                    episode_begin, episode_end, random_mask_ratio=0.3)

    val_dataset = dataset_type(val_indices, dataset_dir, camera_names, norm_stats, arm_delay_time, 
                                max_pos_lookahead, use_dataset_action, use_depth_image, use_robot_base,
                                episode_begin, episode_end, random_mask_ratio=0)
    
    # import pdb
    # pdb.set_trace()

    train_dataloader = DataLoader(train_dataset, batch_size=batch_size_train, shuffle=True, pin_memory=True,
                                  num_workers=8, prefetch_factor=prefetch_factor)

    val_dataloader = DataLoader(val_dataset, batch_size=batch_size_val, shuffle=True, pin_memory=True, num_workers=8,
                                prefetch_factor=prefetch_factor)

    return train_dataloader, val_dataloader, norm_stats, train_dataset.is_sim
