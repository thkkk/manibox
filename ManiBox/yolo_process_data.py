

import os
import random
import cv2
import h5py
import contextlib

import numpy as np
import torch
from torch.utils.data import Dataset
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont

os.environ['YOLO_VERBOSE'] = str(False)  # disable the output of yolo predict
from ultralytics import YOLO

class ProcessDataFromHDF5:

    def __init__(self, episode_ids, dataset_dir, camera_names, norm_stats, arm_delay_time, max_pos_lookahead,
                 use_dataset_action, use_depth_image, use_robot_base, episode_begin, episode_end):
        self.episode_ids = episode_ids  # 1000
        self.num_episodes = len(episode_ids)
        self.episode_len = episode_end - episode_begin
        
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
        
        self.detection_model = YOLO("yolov8l-world.pt")
        self.detection_model.set_classes(["apple", "table"])
        
        # self.process_item(0)  # initialize self.is_sim

    def __len__(self):
        return len(self.episode_ids)
    
    def shuffle(self):
        np.random.shuffle(self.episode_ids)
    
    def process_data(self):
        data = {
            "image_data": torch.zeros(self.num_episodes, self.episode_len, 24),  # Tensor, shape: (num_episodes, episode_len, 24)
            "image_depth_data": None,
            "qpos_data": torch.zeros(self.num_episodes, self.episode_len, 14),  # Tensor, shape: (num_episodes, episode_len, 14)
            "next_action_data": None,
            "next_action_is_pad": None,
            "action_data": torch.zeros(self.num_episodes, self.episode_len, 14),   # Tensor, shape: (num_episodes, episode_len, 14)
            "action_is_pad": None,
        }
        for episode_id in tqdm(self.episode_ids):
            self.process_item(data, episode_id)
        # save the data to (dataset_dir, "integration.pkl")
        torch.save(data, os.path.join(self.dataset_dir, f"integration.pkl"))
        print(f"Successfully saved the {self.num_episodes} processed data to ", os.path.join(self.dataset_dir, f"integration.pkl"))
    
    def process_item(self, data, index):
        episode_id = self.episode_ids[index]
        dataset_path = os.path.join(self.dataset_dir, f'episode_{episode_id}.hdf5')

        with h5py.File(dataset_path, 'r') as root:
            is_sim = root.attrs['sim']
            is_compress = root.attrs['compress']
            original_action_shape = root['/action'][self.episode_begin:self.episode_end].shape
            max_action_len = original_action_shape[0]
            if self.use_robot_base:
                original_action_shape = (original_action_shape[0], original_action_shape[1] + 2)

            start_ts = max_action_len
            history_start = 0
            next_action_size = random.randint(0, self.max_pos_lookahead)
            if self.use_dataset_action:
                actions = root['/action'][self.episode_begin:self.episode_end]
            else:
                actions = root['/observations/qpos'][self.episode_begin:self.episode_end][1:]
                actions = np.append(actions, actions[-1][np.newaxis, :], axis=0)
            end_next_action_index = min(start_ts + next_action_size, max_action_len - 1)
            
            qpos = root['/observations/qpos'][self.episode_begin:self.episode_end][history_start: start_ts + 1]
            if self.use_robot_base:
                qpos = np.concatenate((qpos, root['/base_action'][self.episode_begin:self.episode_end][start_ts]), axis=0)
            all_cam_images = []
            all_cam_images_depth = []
            all_cam_bbox_history_apple = []
            all_cam_bbox_history_table = []
            
            for cam_name in self.camera_names:
                all_cam_images.append([])
                all_cam_bbox_history_apple.append([])
                all_cam_bbox_history_table.append([])
                kalman_filter_apple = KalmanFilter()
                kalman_filter_table = KalmanFilter()
                if is_compress:
                    decoded_image = root[f'/observations/images/{cam_name}'][self.episode_begin:self.episode_end][history_start: start_ts + 1]
                    for i in range(decoded_image.shape[0]):
                        image = cv2.imdecode(np.frombuffer(decoded_image[i], np.uint8), 1)
                        bbox_apple, bbox_table = self.detect_bounding_boxes(image)
                        all_cam_bbox_history_apple[-1].append(kalman_filter_apple.fill_missing_bbox_with_kalman(bbox_apple))
                        all_cam_bbox_history_table[-1].append(kalman_filter_table.fill_missing_bbox_with_kalman(bbox_table))
                        # all_cam_images[-1].append(image)
                else:  # ERROR here
                    image = root[f'/observations/images/{cam_name}'][self.episode_begin:self.episode_end][start_ts]
                    bbox_apple, bbox_table = self.detect_bounding_boxes(image)
                    all_cam_bbox_history_apple[-1].append(kalman_filter_apple.fill_missing_bbox_with_kalman(bbox_apple))
                    all_cam_bbox_history_table[-1].append(kalman_filter_table.fill_missing_bbox_with_kalman(bbox_table))
                    # all_cam_images[-1].append(image)

                if self.use_depth_image:
                    all_cam_images_depth.append([])
                    all_cam_images_depth[-1].append(root[f'/observations/images_depth/{cam_name}'][self.episode_begin:self.episode_end][start_ts])

                # all_cam_bbox_history_apple[-1] = self.fill_missing_bboxes_with_kalman(all_cam_bbox_history_apple[-1])
                # all_cam_bbox_history_table[-1] = self.fill_missing_bboxes_with_kalman(all_cam_bbox_history_table[-1])

            action = actions[history_start: start_ts + 1] 
            next_action = actions[start_ts: start_ts]
            if self.use_robot_base:
                action = np.concatenate((action, root['/base_action'][self.episode_begin:self.episode_end][index:]), axis=1)
                next_action = np.concatenate((next_action, root['/base_action'][self.episode_begin:self.episode_end][start_ts:index]), axis=1)

        self.is_sim = is_sim
        padded_next_action = np.zeros((self.max_pos_lookahead, original_action_shape[1]), dtype=np.float32)
        next_action_is_pad = np.zeros(self.max_pos_lookahead)
        # all_cam_images = np.stack(all_cam_images, axis=0)
        # image_data = torch.from_numpy(all_cam_images)
        # image_data = torch.einsum('n k h w c -> k n c h w', image_data)
        # image_data = image_data / 255.0

        image_depth_data = np.zeros(1, dtype=np.float32)
        if self.use_depth_image:
            all_cam_images_depth = np.stack(all_cam_images_depth, axis=0)
            image_depth_data = torch.from_numpy(all_cam_images_depth)
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

        # image_data.shape: (episode_len, cam_num=3, RGB=3, 480, 640)
        
        all_cam_bbox_history_apple = torch.tensor(all_cam_bbox_history_apple).float()  # (3, episode_len, 4)
        all_cam_bbox_history_table = torch.tensor(all_cam_bbox_history_table).float()
        # make the episode_len dim to be the first dim
        all_cam_bbox_history_apple = all_cam_bbox_history_apple.permute(1, 0, 2)  # (episode_len, 3, 4)
        all_cam_bbox_history_table = all_cam_bbox_history_table.permute(1, 0, 2)
        image_data = torch.cat((all_cam_bbox_history_apple, all_cam_bbox_history_table), dim=-1)  # (episode_len, 3, 8)
        # flatten the image in each timestep
        image_data = image_data.view(image_data.shape[0], -1)  # (episode_len, 24)
        
        # import pdb; pdb.set_trace()
        # qpos.shape: (episode_len, state_dim=14)
        # action_data.shape: (episode_len, action_dim=14)
        data["image_data"][index] = image_data
        data["qpos_data"][index] = qpos_data
        data["action_data"][index] = action_data
        # return image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad

    def detect_bounding_boxes(self, image):
        # with contextlib.redirect_stdout(None):
        with torch.no_grad():
            results = self.detection_model.predict(image)

        bbox_apple, bbox_table = None, None
        for box in results[0].boxes:
            if results[0].names[box.cls.item()] == "apple":
                bbox_apple = box.xyxyn.squeeze().cpu().numpy().tolist()
            elif results[0].names[box.cls.item()] == "table":
                bbox_table = box.xyxyn.squeeze().cpu().numpy().tolist()
        return bbox_apple, bbox_table


class YoloProcessDataByTimeStep:
    # objects_names = ["apple", "table"]  # always put the goal object in the first position
    objects_names = ["apple"]  # always put the goal object in the first position
    def __init__(self, detection_model=None, objects_names=None):
        if detection_model == None:
            self.detection_model = YOLO("yolov8l-world.pt")
        else:
            self.detection_model = detection_model
        
        # self.detection_model.eval()  # amazing?
        if objects_names:
            if isinstance(objects_names, str):
                objects_names = [objects_names]
            self.objects_names = objects_names
            print("grasping target:", self.objects_names)
        self.cameras_names = ["cam_high", "cam_left_wrist", "cam_right_wrist"]
        self.object_to_idx = {obj: idx for idx, obj in enumerate(self.objects_names)}  
        # don't modify self.objects_names if there are multi-object
        self.detection_model.set_classes(self.objects_names)
        self.using_kalman_filter = False
    
    def modify_objects_names(self, objects_names):
        if isinstance(objects_names, str):
            objects_names = [objects_names]
        self.objects_names = objects_names
        self.object_to_idx = {obj: idx for idx, obj in enumerate(self.objects_names)}
        self.detection_model.set_classes(self.objects_names)
    
    def reset_new_episode(self):
        if self.using_kalman_filter:
            self.kalman_filter_objects = [[KalmanFilter() for _ in range(len(self.objects_names))] for _ in range(len(self.cameras_names))]
        # shape: (3 cameras, object_num=2)
    
    def detect_bounding_boxes(self, image):
    
        if isinstance(image, np.ndarray):
            return self.parallel_detect_bounding_boxes([image])
        elif isinstance(image, torch.Tensor):
            if len(image.shape) == 3:
                image = image.unsqueeze(0)
            return self.parallel_detect_bounding_boxes(image)

    def process(self, cam_high, cam_left_wrist, cam_right_wrist):
        if isinstance(cam_high, np.ndarray):
            return self.parallel_process_traj([cam_high], [cam_left_wrist], [cam_right_wrist])
        elif isinstance(cam_high, torch.Tensor):
            return self.parallel_process_traj(cam_high.unsqueeze(0), cam_left_wrist.unsqueeze(0), cam_right_wrist.unsqueeze(0))

    def parallel_detect_bounding_boxes(self, images):
        batch_size = len(images)
        if isinstance(images[0], np.ndarray):
            assert len(images[0].shape) == 3
            assert images[0].shape[-1] == 3
            for i in range(len(images)):
                images[i] = cv2.cvtColor(images[i], cv2.COLOR_RGB2BGR)
        if isinstance(images, torch.Tensor):
            assert images.shape[1] == 3
            assert len(images.shape) == 4
            
        with torch.no_grad():
            results = self.detection_model.predict(images, batch=batch_size)
        
        batched_bbox_list = []
        for i in range(batch_size):
            bbox_list = [KalmanFilter.NO_BBOX for _ in range(len(self.objects_names))]
            for box in results[i].boxes:
                bbox = box.xyxyn.squeeze().cpu().numpy().tolist()
                name = results[i].names[round(box.cls.item())]  # could be 0.0?
                if name in self.object_to_idx:
                    bbox_list[self.object_to_idx[name]] = bbox
            batched_bbox_list.append(bbox_list)
        return batched_bbox_list  # shape: (batch_size, objects_num, 4)
    
    def parallel_process_traj(self, cams_high, cams_left_wrist, cams_right_wrist):
        batch_size = 96  # to avoid memory overflow
        epi_len = len(cams_high)  # = epi_len
        cam_num = len(self.cameras_names)
        objects_num = len(self.objects_names)
        # shape: (epi_len, cam_num, objects_num, xyxyn)
        batched_cam_bbox_objects_list = [[[] for _ in range(cam_num)] for _ in range(epi_len)]
        
        if isinstance(cams_high, list):
            cams = cams_high + cams_left_wrist + cams_right_wrist  # shape: (3 * epi_len, 480, 640, 3)
        elif isinstance(cams_high, torch.Tensor):
            # cat the 3 cameras
            cams = torch.cat((cams_high, cams_left_wrist, cams_right_wrist), dim=0)  # shape: (3 * epi_len, 3, 480, 640)
        elif isinstance(cams_high, np.ndarray):
            cams = np.concatenate((cams_high, cams_left_wrist, cams_right_wrist), axis=0)
        # if cams[0].shape[0] == 3:
        #     for i in range(len(cams)):  # for torch.Tensor
        #         cams[i] = cams[i].permute(1, 2, 0).float()
        
        # batched_bbox_list = self.parallel_detect_bounding_boxes(cams)  # (3 * epi_len, objects_num, 4)
        
        # Process images in batches to avoid memory overflow
        batched_bbox_list = []
        for start_idx in range(0, len(cams), batch_size):
            batch_images = cams[start_idx:start_idx + batch_size]
            batch_bbox_list = self.parallel_detect_bounding_boxes(batch_images)
            batched_bbox_list.extend(batch_bbox_list)
        # batched_bbox_list: (3 * epi_len, objects_num, 4)
        
        if self.using_kalman_filter:
            for i in range(epi_len):
                for j in range(cam_num):
                    batched_cam_bbox_objects_list[i][j] = batched_bbox_list[j * epi_len + i]
            # batched_cam_bbox_objects_list: (epi_len, cam_num, objects_num, 4)
            # apply kalman filter along the episode length
            for j in range(cam_num):
                for k in range(len(self.objects_names)):
                    kalman_filter = KalmanFilter()
                    for i in range(epi_len):
                        batched_cam_bbox_objects_list[i][j][k] = kalman_filter.fill_missing_bbox_with_kalman(batched_cam_bbox_objects_list[i][j][k])
                
            batched_cam_bbox_objects_list = torch.tensor(batched_cam_bbox_objects_list).float()  # (epi_len, cam_num, objects_num, 4)
        else:
            batched_cam_bbox_objects_list = torch.tensor(batched_bbox_list).float()  # (3 * epi_len, objects_num, 4)
            # NOTE that the bbox in the list is: [cam_high_0, cam_high_1, ..., cam_left_wrist_0, cam_left_wrist_1, ..., cam_right_wrist_0, cam_right_wrist_1, ...]
            batched_cam_bbox_objects_list = batched_cam_bbox_objects_list.reshape(cam_num, epi_len, objects_num, -1)  # (cam_num, epi_len, objects_num, 4)
            batched_cam_bbox_objects_list = batched_cam_bbox_objects_list.permute(1, 0, 2, 3)  # (epi_len, cam_num, objects_num, 4)

        batched_cam_bbox_objects_list = batched_cam_bbox_objects_list.reshape(epi_len, -1)  # (epi_len, cam_num * objects_num * 4)        
        return batched_cam_bbox_objects_list

class KalmanFilter:
    """return the filtered bbox list with Kalman Filter in each frame
    TODO: check
    """
    NO_BBOX = [0, 0, 0, 0]
    def __init__(self):
        self.prev_bbox = KalmanFilter.NO_BBOX
        self.kalman = self.create_kalman_filter()
    
    def create_kalman_filter(self):
        kalman = cv2.KalmanFilter(4, 2)
        kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
        kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
        kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03
        return kalman

    def fill_missing_bbox_with_kalman(self, bbox):
        # without for-loop here
        filled_bbox = KalmanFilter.NO_BBOX
        if bbox is KalmanFilter.NO_BBOX:
            if self.prev_bbox is not KalmanFilter.NO_BBOX:
                prediction = self.kalman.predict()
                bbox = [prediction[0][0], prediction[1][0], prediction[0][0] + self.prev_bbox[2], prediction[1][0] + self.prev_bbox[3]]
                filled_bbox = bbox
            else:
                filled_bbox = [0, 0, 0, 0]
        else:
            self.kalman.correct(np.array([[np.float32(bbox[0])], [np.float32(bbox[1])]], np.float32))
            filled_bbox = bbox
            self.prev_bbox = bbox
        return filled_bbox

import numpy as np
import cv2

import os
os.environ['YOLO_VERBOSE'] = str(False)  # disable the output of yolo predict
from ultralytics import YOLO
import h5py
import time


class AsyncYoloProcessDataFromHDF5:
    def __init__(self, num_envs, dataset_dir) -> None:
        self.dataset_dir = dataset_dir
        YoloCollectData.init(num_envs)  # no use, only [0] is used
        self.episode_begin = 0
        self.episode_end = 90
        self.use_dataset_action = True
        self.use_robot_base = False
    
    def process_item(self, episode_id):
        env_id = 0
        dataset_path = os.path.join(self.dataset_dir, f'episode_{episode_id}.hdf5')

        with h5py.File(dataset_path, 'r') as data_file:
            is_sim = data_file.attrs['sim']
            is_compress = data_file.attrs['compress']
            original_action_shape = data_file['/action'][self.episode_begin:self.episode_end].shape
            max_action_len = original_action_shape[0]

            start_ts = max_action_len
            if self.use_dataset_action:
                actions = data_file['/action'][self.episode_begin:self.episode_end]  # (90, 14)
            else:
                actions = data_file['/observations/qpos'][self.episode_begin:self.episode_end][1:]
                actions = np.append(actions, actions[-1][np.newaxis, :], axis=0)
            
            qpos = data_file['/observations/qpos'][self.episode_begin:self.episode_end]  # (90, 14)
            if self.use_robot_base:
                qpos = np.concatenate((qpos, data_file['/base_action'][self.episode_begin:self.episode_end][start_ts]), axis=0)
            
            YoloCollectData.envs_process[env_id].reset_new_episode()
            
            # image_data = []
            # for i in range(self.episode_begin, self.episode_end):
            #     cams = []
            #     for cam_name in YoloCollectData.cameras_names:
            #         if is_compress:
            #             raw_image = data_file[f'/observations/images/{cam_name}'][i]
            #             image = cv2.imdecode(np.frombuffer(raw_image, np.uint8), 1)
            #         else:
            #             image = data_file[f'/observations/images/{cam_name}'][i]    
            #         image = torch.tensor(image).float().to('cuda')
            #         cams.append(image)
            #     image_data.append(YoloCollectData.envs_process[env_id].process(cams[0], cams[1], cams[2]))  # (1, 12)
            
            image_data = []
            cams = {
                "cam_high": [],
                "cam_left_wrist": [],
                "cam_right_wrist": []
            }
            for i in range(self.episode_begin, self.episode_end):
                for cam_name in YoloCollectData.cameras_names:
                    if is_compress:
                        raw_image = data_file[f'/observations/images/{cam_name}'][i]
                        image = cv2.imdecode(np.frombuffer(raw_image, np.uint8), 1)
                    else:
                        image = data_file[f'/observations/images/{cam_name}'][i]    
                    cams[cam_name].append(image)  # np.array, shape: (480, 640, 3)
            image_data = YoloCollectData.envs_process[env_id].parallel_process_traj(
                cams["cam_high"], cams["cam_left_wrist"], cams["cam_right_wrist"])  # (90, 12)
            
            # image_data = torch.cat(image_data, dim=0)  # (90, 12)
            YoloCollectData.save_data(image_data, qpos, actions, self.dataset_dir)
        print(f"AsyncYoloProcessDataFromHDF5 has processed {episode_id}th episode to integration.pkl")
    
    def run(self, episode_id=0):
        # make sure CollectEpsBuf.use_yolo_sync_process == False
        while True:
            file_path = os.path.join(self.dataset_dir, f'episode_{episode_id}.hdf5')
            if os.path.exists(file_path):
                self.process_item(episode_id)
                if not ((2 <= episode_id < 19)):
                    os.remove(file_path)
                episode_id += 1
            else:
                time.sleep(0.1)  


class YoloCollectData:
    # num_episodes = 30000
    detection_model = YOLO("yolov8l-world.pt") # YOLO("yolov8m-world.pt")
    cameras_names = ["cam_high", "cam_left_wrist", "cam_right_wrist"]
    objects_names = ["apple"]  # , "table"
    episode_length = 90
    store_device = "cpu"
    data = {
        "image_data": torch.zeros((0, episode_length, 12 * len(objects_names)), device=store_device),  # Tensor, shape: (0, episode_len, 24)
        "image_depth_data": None,
        "qpos_data": torch.zeros((0, episode_length, 14), device=store_device),  # Tensor, shape: (0, episode_len, 14)
        "next_action_data": None,
        "next_action_is_pad": None,
        "action_data": torch.zeros((0, episode_length, 14), device=store_device),  # Tensor, shape: (0, episode_len, 14)
        "action_is_pad": None,
        "reward": torch.zeros((0, episode_length), device=store_device),
    }
    # TODO: save only one model
    @staticmethod
    def init(num_envs) -> None:
        YoloProcessDataByTimeStep.objects_names = YoloCollectData.objects_names  # modify the class to be detected
        YoloCollectData.object_to_idx = {obj: idx for idx, obj in enumerate(YoloCollectData.objects_names)}
        YoloCollectData.detection_model.set_classes(YoloCollectData.objects_names)
        print(f"YoloProcessDataByTimeStep.objects_names: {YoloProcessDataByTimeStep.objects_names}")
        YoloCollectData.envs_process = [YoloProcessDataByTimeStep(YoloCollectData.detection_model) for _ in range(num_envs)]
        YoloCollectData.num_envs = num_envs
    
    @staticmethod
    def save_data(image_data, qpos, action, reward, dataset_dir):
        if isinstance(image_data, list) or isinstance(qpos, list):
            image_data = torch.from_numpy(np.array(image_data)).float().unsqueeze(0).to(YoloCollectData.store_device)
            qpos = torch.from_numpy(np.array(qpos)).float().unsqueeze(0).to(YoloCollectData.store_device)
            action = torch.from_numpy(np.array(action)).float().unsqueeze(0).to(YoloCollectData.store_device)
            reward = torch.from_numpy(np.array(reward)).float().unsqueeze(0).to(YoloCollectData.store_device)
        else:
            image_data = torch.tensor(image_data).float().unsqueeze(0).to(YoloCollectData.store_device)  # Add batch dimension
            qpos = torch.tensor(qpos).float().unsqueeze(0).to(YoloCollectData.store_device)
            action = torch.tensor(action).float().unsqueeze(0).to(YoloCollectData.store_device)
            reward = torch.tensor(reward).float().unsqueeze(0).to(YoloCollectData.store_device)
        print(f"image_data, qpos, action, reward:", image_data.shape, qpos.shape, action.shape, reward.shape)
        # torch.Size([1, 90, 12]) torch.Size([1, 90, 14]) torch.Size([1, 90, 14])
        
        YoloCollectData.data["image_data"] = torch.cat([YoloCollectData.data["image_data"], image_data], dim=0)
        YoloCollectData.data["qpos_data"] = torch.cat([YoloCollectData.data["qpos_data"], qpos], dim=0)
        YoloCollectData.data["action_data"] = torch.cat([YoloCollectData.data["action_data"], action], dim=0)
        YoloCollectData.data["reward"] = torch.cat([YoloCollectData.data["reward"], reward], dim=0)
        
        # save the data to (dataset_dir, "integration.pkl")
        num_episodes = YoloCollectData.data["image_data"].shape[0]
        if num_episodes % 10 == 0:  # I checked it, it is correct because CollectEpsBuf.trajectory_num will be added by 1 first
            torch.save(YoloCollectData.data, os.path.join(dataset_dir, f"integration.pkl"))
            print(f"Save {num_episodes}th data to {os.path.join(dataset_dir, f'integration.pkl')}")
    
    
def plot_xyxyn_boxes_to_image(image, bboxes, cam_id=0, path="./"):
    '''
    image: np.array (H, W, 3), RGB, 0~255 
        or torch.tensor (3, H, W), RGB, 0~1
    bboxes: torch.Tensor, bounding box, each bounding box is [[x1, y1, x2, y2]] (x, y ∈ [0, 1]), shape: (num_boxes, 4)
    '''
    assert len(image.shape) == 3

    if isinstance(image, torch.Tensor) and image.shape[0] == 3:  # Check if the image is (3, W, H) and convert to (W, H, 3)
        image = image.permute(1, 2, 0)
        image = image.cpu().numpy()
        image = (image * 255).astype(np.uint8)
    
    if len(bboxes.shape) == 1 and bboxes.shape[0] == 4:
        bboxes = bboxes.unsqueeze(0)
    
    # image: (H, W, 3)
    H, W, _ = image.shape
    image_Image = Image.fromarray(np.uint8(image), 'RGB')
    draw = ImageDraw.Draw(image_Image, 'RGB')
    
    for bbox in bboxes:
        bbox = bbox * torch.tensor([W, H, W, H], dtype=torch.float32, device=bboxes.device)
        draw.rectangle(bbox.tolist(), outline="red", width=5)
    
    # image_Image.show()
    
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    image_Image.save(os.path.join(path, f'{cam_id}_first_image.jpg'), 'JPEG')
    # print(f"Save the image to {cam_id}_first_image.jpg")