#!/home/lin/software/miniconda3/envs/aloha/bin/python
# -- coding: UTF-8
"""
#!/usr/bin/python3
"""

import torch
import numpy as np
import os
import pickle
import json
import argparse
from einops import rearrange

# from utils import compute_dict_mean, set_seed, detach_dict # helper functions
# from policy import ACTPolicy, CNNMLPPolicy, DiffusionPolicy
import collections
from collections import deque

import rospy
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Image as Image_msg
from nav_msgs.msg import Odometry
from cv_bridge import CvBridge
import time
import threading
import math
import threading

from PIL import Image, ImageDraw, ImageFont
# from 

from VFCNet.yolo_process_data import YoloProcessDataByTimeStep, plot_xyxyn_boxes_to_image
from VFCNet.train import make_policy  # , set_model_config


import sys
sys.path.append("./")

task_config = {'camera_names': ['cam_high', 'cam_left_wrist', 'cam_right_wrist']}

inference_thread = None
inference_lock = threading.Lock()
inference_actions = None
inference_timestep = None

def set_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)

def interpolate_action(args, prev_action, cur_action):
    steps = np.concatenate((np.array(args.arm_steps_length), np.array(args.arm_steps_length)), axis=0)
    diff = np.abs(cur_action - prev_action)
    step = np.ceil(diff / steps).astype(int)
    step = np.max(step)
    if step <= 1:
        return cur_action[np.newaxis, :]
    new_actions = np.linspace(prev_action, cur_action, step + 1)
    return new_actions[1:]


# def actions_interpolation(args, pre_action, actions, stats):
#     steps = np.concatenate((np.array(args.arm_steps_length), np.array(args.arm_steps_length)), axis=0)
#     if args.use_dataset_action:
#         pre_process = lambda next_action: (next_action - stats["action_mean"]) / stats["action_std"]
#         post_process = lambda a: a * stats['action_std'] + stats['action_mean']
#     else:
#         pre_process = lambda s_qpos: (s_qpos - stats['qpos_mean']) / stats['qpos_std']
#         post_process = lambda a: a * stats['qpos_std'] + stats['qpos_mean']

#     # Original action sequence
#     action_seq = post_process(actions[0])
#     action_seq = np.concatenate((pre_action[np.newaxis, :], action_seq), axis=0)

#     # Interpolated action sequence
#     interp_action = []
#     # Interpolation
#     for i in range(1, action_seq.shape[0]):
#         # Difference between two adjacent actions
#         diff = np.abs(action_seq[i] - action_seq[i - 1])
#         # Number of steps to interpolate
#         step = np.ceil(diff / steps).astype(int)
#         # Interpolation by the maximum number of steps
#         step = np.max(step)
#         if step <= 1:
#             # No need to interpolate if the difference is smaller than the step size
#             interp_action.append(action_seq[i:i+1])
#         else:
#             new_actions = np.linspace(action_seq[i - 1], action_seq[i], step + 1)
#             interp_action.append(new_actions[1:])
    
#     # while len(result) < args.chunk_size+1:
#     #     result.append(result[-1])

#     result = np.concatenate(interp_action, axis=0)
#     result = result[:args.chunk_size]

#     result = pre_process(result)
#     result = result[np.newaxis, :]
#     return result


def get_model_config(args):
    # 设置随机种子，你可以确保在相同的初始条件下，每次运行代码时生成的随机数序列是相同的。
    set_seed(args.seed)

    # 如果是ACT策略
    # fixed parameters
    
    if args.load_config:
        # load the policy config from the old model as well
        config_file = os.path.join(args.ckpt_dir, 'config.json') # 'logs/rsl_rl/2024-06-07_22-16-34CNNRNN/config.json'
        with open(config_file, 'r') as f:
            config_json = f.read()
        policy_config = json.loads(config_json)['policy_config']
        print(f"The training config {args.ckpt_dir} has been synced for inference!")
    else:
        raise NotImplementedError
    
    config = {
        'ckpt_dir': args.ckpt_dir,
        'ckpt_name': args.ckpt_name,
        'ckpt_stats_name': args.ckpt_stats_name,
        'episode_len': args.max_publish_step,
        'state_dim': args.state_dim,
        'policy_class': args.policy_class,
        'policy_config': policy_config,
        'temporal_agg': args.temporal_agg,
        'camera_names': task_config['camera_names'],
    }
    return config

last_right_image = None
def get_image(observation, camera_names):
    global last_right_image
    curr_images = []
    for cam_name in camera_names:
        curr_image = rearrange(observation['images'][cam_name], 'h w c -> c h w')
        if cam_name == 'cam_right_wrist':
            # print(f"Image of Right is {curr_image}")
            # if last_right_image is not None:
            #     print(f"right image distance {np.linalg.norm(curr_image - last_right_image)}")
            last_right_image = curr_image
            
        curr_images.append(curr_image)
    curr_image = np.stack(curr_images, axis=0)
    curr_image = torch.from_numpy(curr_image / 255.0).float().cuda().unsqueeze(0)  # 
    return curr_image


def get_depth_image(observation, camera_names):
    curr_images = []
    for cam_name in camera_names:
        curr_images.append(observation['images_depth'][cam_name])
    curr_image = np.stack(curr_images, axis=0)
    curr_image = torch.from_numpy(curr_image / 255.0).float().cuda().unsqueeze(0)
    return curr_image


def inference_thread_fn(args, config, ros_operator, policy, next_actions, stats, t, pre_action, yolo_process_data=None):
    global inference_lock
    global inference_actions
    global inference_timestep
    
    if config['policy_class'] in ["RNN", "FCNet", "DiffusionState", "CEPPolicy"]:
        is_qpos_normalized = False
        yolo_preprocess = True
        yolo_process_data: YoloProcessDataByTimeStep
    else:
        is_qpos_normalized = True
        yolo_preprocess = False
    
    print_flag = True
    pre_pos_process = lambda s_qpos: (s_qpos - stats['qpos_mean']) / stats['qpos_std']
    pre_action_process = lambda next_action: (next_action - stats["action_mean"]) / stats["action_std"]
    rate = rospy.Rate(args.publish_rate)
    while True and not rospy.is_shutdown():
        # import pdb; pdb.set_trace()
        result = ros_operator.get_frame()
        if not result:
            if print_flag:
                print("syn fail")
                print_flag = False
            rate.sleep()
            continue
        print_flag = True
        (img_front, img_left, img_right, img_front_depth, img_left_depth, img_right_depth,
         puppet_arm_left, puppet_arm_right, robot_base) = result
        obs = collections.OrderedDict()
        image_dict = dict()

        image_dict[config['camera_names'][0]] = img_front
        image_dict[config['camera_names'][1]] = img_left
        image_dict[config['camera_names'][2]] = img_right


        obs['images'] = image_dict

        if args.use_depth_image:
            image_depth_dict = dict()
            image_depth_dict[config['camera_names'][0]] = img_front_depth
            image_depth_dict[config['camera_names'][1]] = img_left_depth
            image_depth_dict[config['camera_names'][2]] = img_right_depth
            obs['images_depth'] = image_depth_dict

        obs['qpos'] = np.concatenate(
            (np.array(puppet_arm_left.position), np.array(puppet_arm_right.position)), axis=0)
        obs['qvel'] = np.concatenate(
            (np.array(puppet_arm_left.velocity), np.array(puppet_arm_right.velocity)), axis=0)
        obs['effort'] = np.concatenate(
            (np.array(puppet_arm_left.effort), np.array(puppet_arm_right.effort)), axis=0)
        if args.use_robot_base:
            obs['base_vel'] = [robot_base.twist.twist.linear.x, robot_base.twist.twist.angular.z]
            obs['qpos'] = np.concatenate((obs['qpos'], obs['base_vel']), axis=0)
        else:
            obs['base_vel'] = [0.0, 0.0]
        # 取obs的位姿qpos
        if args.max_pos_lookahead != 0:
            padded_next_action = np.zeros((args.max_pos_lookahead, obs['qpos'].shape[0]), dtype=np.float32)
            next_action_is_pad = np.zeros(args.max_pos_lookahead)
            if next_actions is not None:
                padded_next_action[0:next_actions.shape[0]] = next_actions
                next_action_is_pad[next_actions.shape[0]:] = 1
        else:
            padded_next_action = None
            next_action_is_pad = None

        # qpos_numpy = np.array(obs['qpos'])

        # 归一化处理qpos 并转到cuda
        # TODO: you should consider whether to preprocess the qpos data
        if is_qpos_normalized:
            qpos = pre_pos_process(obs['qpos'])
        else:
            qpos = obs['qpos']

        qpos[7:] = 0
        # qpos = np.zeros(0)
        qpos = torch.from_numpy(qpos).float().cuda().unsqueeze(0)
        if args.max_pos_lookahead != 0:
            next_actions = padded_next_action  # pre_action_process(padded_next_action)
            next_actions = torch.from_numpy(next_actions).float().cuda().unsqueeze(0)
            next_action_is_pad = torch.from_numpy(next_action_is_pad).float().cuda().unsqueeze(0)
        else:
            next_actions = None
            next_action_is_pad = None
        # 当前图像curr_image获取图像
        # print(img_front.shape)
        curr_image = get_image(obs, config['camera_names'])
        curr_depth_image = None
        if args.use_depth_image:
            curr_depth_image = get_depth_image(obs, config['camera_names'])
        
        if yolo_preprocess:
            # print(f"curr_image shape {curr_image.shape}")
            # curr_image shape torch.Size([1, 3, 3, 480, 640])
            # cams = [curr_image[0][0], curr_image[0][1], curr_image[0][2]]
            cams = [torch.tensor(img_front), torch.tensor(img_left), torch.tensor(img_right)]
            # img_*: RGB, shape: (480, 640, 3), 0~255
            for i, cam in enumerate(cams):
                cams[i] = cams[i].permute(2, 0, 1) / 255.0
            # img_*: RGB, shape: (3, 480, 640), 0~1
            image_data = yolo_process_data.process(cams[0].cuda(), cams[1].cuda(), cams[2].cuda())
            
            bboxes = image_data.reshape(3, len(YoloProcessDataByTimeStep.objects_names), 4)  # (3 cameras, apple and table, xyxyn)
            
            # show the high, left, right images with bounding box:
            if t <= 40:
                for i in range(len(cams)):
                    plot_xyxyn_boxes_to_image(cams[i], bboxes[i], config['camera_names'][i] + "_" + str(t))
            #     W, H = image.shape[1:3]
            #     bbox = bboxes[i]
            #     bbox = bbox * torch.Tensor([W, H, W, H])
            #     draw = ImageDraw.Draw(image)
            #     draw.rectangle(bbox.tolist(), outline="red", width=5)
            #     image.show()
            
            print(f"bbox {image_data}")
            if t == 1 and image_data[0][0].sum() == 0.0:
                print("No object detected!!!!!!!!!!!!!!!!")
            image_data = image_data.cuda()
            qpos = qpos.cuda()
        
        time1 = time.time() 
        # TODO: policy inference, maybe you need to modify the code here
        if yolo_preprocess:
            all_actions = policy(image_data, curr_depth_image, qpos, next_actions, next_action_is_pad, None, None)
        else:
            all_actions = policy(curr_image, curr_depth_image, qpos, next_actions, next_action_is_pad)
        print("model_time: ", time.time() - time1)
        inference_lock.acquire()
        # print('--------------', all_actions.shape)  # -------------- torch.Size([1, 30, 14])
        inference_actions = all_actions.cpu().detach().numpy()
        print("left finger", inference_actions[0, 6])
        # if pre_action is None:
        #     pre_action = obs['qpos']
        # print("obs['qpos']:", obs['qpos'][7:])
        # if args.use_actions_interpolation:
        #     inference_actions = actions_interpolation(args, pre_action, inference_actions, stats)
        inference_timestep = t
        inference_lock.release()
        break


def detect_object(prompt, ros_operator, yolo_process_data: YoloProcessDataByTimeStep = None):
    # detect whether there is specified object in the camera
    if yolo_process_data is None:
        return True
    result = ros_operator.get_frame()
    (img_front, img_left, img_right, img_front_depth, img_left_depth, img_right_depth,
         puppet_arm_left, puppet_arm_right, robot_base) = result
    cams = [torch.tensor(img_front), torch.tensor(img_left), torch.tensor(img_right)]
    # img_*: RGB, shape: (480, 640, 3), 0~255
    for i, cam in enumerate(cams):
        cams[i] = cams[i].permute(2, 0, 1) / 255.0
    # img_*: RGB, shape: (3, 480, 640), 0~1
    image_data = yolo_process_data.process(cams[0].cuda(), cams[1].cuda(), cams[2].cuda()) 
    if image_data[0][0].sum() == 0.0:
        print(f"No {prompt} detected in cam_high!!!!!!!!!!!!!!!!")
        return False
    else:
        print(f"{prompt} detected in cam_high")
        return True


def model_inference(args, config, ros_operator, save_episode=True):
    global inference_lock
    global inference_actions
    global inference_timestep
    global inference_thread
    # Get the prediction from the inference thread
    def get_inference_result(inference_thread, inference_lock, inference_actions,
                            inference_timestep):
        if inference_thread is not None:
            inference_lock.acquire()
            action_chunk = inference_actions
            inference_actions = None
            action_t = inference_timestep
            inference_timestep = None
            inference_lock.release()
            return action_chunk.squeeze(0), action_t
        return None, None
    # Update the action to the action buffer
    def update_action_buffer(action_buffer, action_chunk, action_t):
        start_idx = action_t % chunk_size
        end_idx = (start_idx + chunk_size) % chunk_size
        action_buffer[start_idx:] = action_chunk[:chunk_size - start_idx]
        action_buffer[:end_idx] = action_chunk[chunk_size - start_idx:]
        return action_buffer
    

    # 1 创建模型数据  继承nn.Module
    # policy = make_policy(config['policy_class'], config['policy_config'])
    policy = make_policy(config['policy_class'], config['policy_config'], config['ckpt_dir']).to(device=args.device)
    # print("model structure\n", policy.model)
    
    # 2 加载模型权重 (in make_policy)
    # ckpt_path = os.path.join(config['ckpt_dir'], config['ckpt_name'])
    # state_dict = torch.load(ckpt_path)
    # new_state_dict = {}
    # for key, value in state_dict.items():
    #     if key in ["model.is_pad_head.weight", "model.is_pad_head.bias"]:
    #         continue
    #     if args.max_pos_lookahead == 0 and key in ["model.input_proj_next_action.weight", "model.input_proj_next_action.bias"]:
    #         continue
    #     new_state_dict[key] = value
    # loading_status = policy.deserialize(new_state_dict)
    # if not loading_status:
    #     print("ckpt path not exist")
    #     return False

    # 3 模型设置为cuda模式和验证模式
    policy = policy.cuda()
    policy.eval()  # or policy.model.eval()

    # 4 加载统计值
    stats_path = os.path.join(config['ckpt_dir'], config['ckpt_stats_name'])
    # 统计的数据  # 加载action_mean, action_std, qpos_mean, qpos_std 14维
    with open(stats_path, 'rb') as f:
        stats = pickle.load(f)

    # 数据预处理和后处理函数定义
    pre_process = lambda s_qpos: (s_qpos - stats['qpos_mean']) / stats['qpos_std']
    if args.use_dataset_action:
        post_process = lambda a: a * stats['action_std'] + stats['action_mean']
    else:
        post_process = lambda a: a * stats['qpos_std'] + stats['qpos_mean']

    max_publish_step = config['episode_len']
    chunk_size = config['policy_config']['chunk_size']

    # Initialize position of the puppet arm
    # left0 = [-0.00133514404296875, 0.00209808349609375, 0.01583099365234375, -0.032616615295410156, -0.00286102294921875, 0.00095367431640625, 3.557830810546875]
    # right0 = [-0.00133514404296875, 0.00438690185546875, 0.034523963928222656, -0.053597450256347656, -0.00476837158203125, -0.00209808349609375, 3.557830810546875]
    # left1 = [-0.00133514404296875, 0.00209808349609375, 0.01583099365234375, -0.032616615295410156, -0.00286102294921875, 0.00095367431640625, -0.3393220901489258]
    # right1 = [-0.00133514404296875, 0.00247955322265625, 0.01583099365234375, -0.032616615295410156, -0.00286102294921875, 0.00095367431640625, -0.3397035598754883]
    left1 = [0] * 6 + [-0.1350]
    # left1 = [-0.0050,  0.0520, -0.0080, -0.0000,  0.0000,  0.0000, -0.1350]
    right1 = [0] * 6 + [-0.1350]
    left0 = left1[:6] + [3.557830810546875]
    right0 = right1[:6] + [3.557830810546875]
    # left0 = [0] * 6 + [3.557830810546875]
    # left1 = [0] * 6 + [-0.3393220901489258]
    # right0 = [0] * 6 + [3.557830810546875]
    # right1 = [0] * 6 + [-0.3397035598754883]
    
    
    ros_operator.puppet_arm_publish_continuous(left0, right0)  # recover
    
    if config['policy_class'] in ["RNN", "FCNet", "DiffusionState", "CEPPolicy"]:
        is_qpos_normalized = False
        yolo_preprocess = True
    else:
        is_qpos_normalized = True
        yolo_preprocess = False
    
    if yolo_preprocess:
        yolo_process_data = YoloProcessDataByTimeStep()
        yolo_process_data.reset_new_episode()
        policy.reset_recur(1, "cuda:0")
    else:
        yolo_process_data = None
    # input("Press any key to continue")
    if yolo_preprocess:
        while True:
            try:
                prompt = input("Please input the object you wish to grab, the default is 'apple', then press enter to continue: ")
            except KeyboardInterrupt:
                print("Interrupted")
                exit(0)
            if prompt == "":
                prompt = "apple"
            print("your prompt:", prompt)
            yolo_process_data.modify_objects_names(prompt)
            if detect_object(prompt, ros_operator, yolo_process_data):
                break
    else:        
        input("Press any key to continue")
        
    ros_operator.puppet_arm_publish_continuous(left1, right1)
    
    # Initialize the previous action to be the initial robot state
    pre_action = np.zeros(config['state_dim'])
    pre_action[:14] = np.array(
        left1 + 
        right1
    )
    action = None
    
    
    
    # Inference loop
    with torch.inference_mode():
        while True and not rospy.is_shutdown():
            # The current time step
            t = 0
            # max_t = 0
            rate = rospy.Rate(args.publish_rate)
            # if config['temporal_agg']:
            #     all_time_actions = np.zeros([max_publish_step, max_publish_step + chunk_size, config['state_dim']])
            
            # Start the first thread and initialize the action buffer
            inference_thread = threading.Thread(target=inference_thread_fn,
                                                args=(args, config, ros_operator,
                                                    policy, None, stats, t, pre_action, yolo_process_data))
            inference_thread.start()
            action_buffer = np.zeros([chunk_size, config['state_dim']])
            
            while t < max_publish_step and not rospy.is_shutdown():
                start_time = time.time()
                # query policy
                # if config['policy_class'] == "ACT":
                    # if args.max_pos_lookahead != 0:
                    #     if t == 0:
                    #         pre_action = None
                    #         inference_thread = threading.Thread(target=inference_process,
                    #                                             args=(args, config, ros_operator,
                    #                                                   policy, None, stats, t, pre_action))
                    #         inference_thread.start()
                    #     if t >= max_t:
                    #         if inference_thread is not None:
                    #             inference_thread.join()
                    #             inference_lock.acquire()
                    #             if inference_actions is not None:
                    #                 inference_thread = None
                    #                 all_actions = inference_actions
                    #                 inference_actions = None
                    #                 max_t = t + args.pos_lookahead_step
                    #                 if config['temporal_agg']:
                    #                     all_time_actions[[t], t:t + chunk_size] = all_actions
                    #             inference_lock.release()
                    #             pre_action = post_process(all_actions[0][args.pos_lookahead_step-1])
                    #             inference_thread = threading.Thread(target=inference_process,
                    #                                                 args=(args, config, ros_operator,
                    #                                                       policy, all_actions[0][:args.pos_lookahead_step], stats, t, pre_action))
                    #             inference_thread.start()
                    #             print("inference:t=", t)
                    # else:
                        # if t >= max_t:

                # When coming to the middle or the end of the action chunk
                
                if config['policy_class'] in ["FCNet", "RNN", "DiffusionState", "CEPPolicy"]:
                    inference_thread.join()
                    action, action_t = get_inference_result(inference_thread, inference_lock, 
                                                inference_actions, inference_timestep)
                    # the action of model output shape: (1, 14)
                    # action: (14)
                    
                    # print(f"inference one-step action {action}")
                    raw_action = action
                    
                    # inference_thread = threading.Thread(target=inference_thread_fn,
                    #                                     args=(args, config, ros_operator,
                    #                                             policy, None, stats, t, pre_action, yolo_process_data))
                    # inference_thread.start()
                
                if config['policy_class'] == "ACTPolicy" and t % (chunk_size // 2) == 0:
                    # Wait for the previous inference thread to finish
                    inference_thread.join()
                    action_chunk, action_t = get_inference_result(inference_thread, inference_lock, 
                                                inference_actions, inference_timestep)
                    action_buffer = update_action_buffer(action_buffer, action_chunk, action_t)

                    # Start a new inference thread
                    inference_thread = threading.Thread(target=inference_thread_fn,
                                                        args=(args, config, ros_operator,
                                                                policy, None, stats, t, pre_action, yolo_process_data))
                    inference_thread.start()
                
                # inference_thread.join()
                # inference_lock.acquire()
                # if inference_actions is not None:
                #     inference_thread = None
                #     all_actions = inference_actions
                #     inference_actions = None
                    # max_t = t + args.pos_lookahead_step
                    # if config['temporal_agg']:
                    #     all_time_actions[[t], t:t + chunk_size] = all_actions
                # inference_lock.release()

                    # if config['temporal_agg']:
                    #     actions_for_curr_step = all_time_actions[:, t]
                    #     actions_populated = np.all(actions_for_curr_step != 0, axis=1)
                    #     actions_for_curr_step = actions_for_curr_step[actions_populated]
                    #     k = 0.01
                    #     exp_weights = np.exp(-k * np.arange(len(actions_for_curr_step)))
                    #     exp_weights = exp_weights / exp_weights.sum()
                    #     exp_weights = exp_weights[:, np.newaxis]
                    #     raw_action = (actions_for_curr_step * exp_weights).sum(axis=0, keepdims=True)
                    # else:
                    #     if args.pos_lookahead_step != 0:
                    #         raw_action = all_actions[:, t % args.pos_lookahead_step]
                    #     else:
                    #         raw_action = all_actions[:, t % chunk_size]
                # else:
                #     raise NotImplementedError

                    raw_action = action_buffer[t % chunk_size]
                if is_qpos_normalized:
                    action = post_process(raw_action)
                
                # ros_operator.puppet_arm_publish_continuous(action[:7], action[7:])
                # worse than the interpolation code below
                
                # Interpolate the original action sequence
                if args.use_actions_interpolation:
                    interp_actions = interpolate_action(args, pre_action, action)
                else:
                    interp_actions = action[np.newaxis, :]
                # Execute the interpolated actions one by one
                for act in interp_actions:
                    left_action = act[:7]  # 取7维度  shape:(7)
                    # left_action[0:6] = 0
                    # if t <=4 :
                    #     left_action[6] = 4.3
                    # print("----------------------left_action[6]", left_action[6])
                    # left_action[7] = 
                    right_action = act[7:14]
                    
                    ros_operator.puppet_arm_publish(left_action, right_action)  # puppet_arm_publish_continuous_thread
                
                    if args.use_robot_base:
                        vel_action = act[14:16]
                        ros_operator.robot_base_publish(vel_action)
                    rate.sleep()
                t += 1
                
                if config['policy_class'] in ["FCNet", "RNN", "DiffusionState", "CEPPolicy"]:
                    # inference_thread.join()
                    # action, action_t = get_inference_result(inference_thread, inference_lock, 
                    #                             inference_actions, inference_timestep)
                    # # the action of model output shape: (1, 14)
                    # # action: (14)
                    
                    # print(f"inference one-step action {action}")
                    # raw_action = action
                    
                    inference_thread = threading.Thread(target=inference_thread_fn,
                                                        args=(args, config, ros_operator,
                                                                policy, None, stats, t, pre_action, yolo_process_data))
                    inference_thread.start()
                end_time = time.time()
                
                print("Published Step", t)
                # print("time:", end_time - start_time)
                # print("left_action:", left_action)
                # print("right_action:", right_action)
                # rate.sleep()
                pre_action = action


class RosOperator:
    def __init__(self, args):
        self.robot_base_deque = None
        self.puppet_arm_right_deque = None
        self.puppet_arm_left_deque = None
        self.img_front_deque = None
        self.img_right_deque = None
        self.img_left_deque = None
        self.img_front_depth_deque = None
        self.img_right_depth_deque = None
        self.img_left_depth_deque = None
        self.bridge = None
        self.puppet_arm_left_publisher = None
        self.puppet_arm_right_publisher = None
        self.robot_base_publisher = None
        self.puppet_arm_publish_thread = None
        self.puppet_arm_publish_lock = None
        self.args = args
        self.init()
        self.init_ros()

    def init(self):
        self.bridge = CvBridge()
        self.img_left_deque = deque()
        self.img_right_deque = deque()
        self.img_front_deque = deque()
        self.img_left_depth_deque = deque()
        self.img_right_depth_deque = deque()
        self.img_front_depth_deque = deque()
        self.puppet_arm_left_deque = deque()
        self.puppet_arm_right_deque = deque()
        self.robot_base_deque = deque()
        self.puppet_arm_publish_lock = threading.Lock()
        self.puppet_arm_publish_lock.acquire()

    def puppet_arm_publish(self, left, right):
        joint_state_msg = JointState()
        joint_state_msg.header = Header()
        joint_state_msg.header.stamp = rospy.Time.now()  # 设置时间戳
        joint_state_msg.name = ['joint0', 'joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']  # 设置关节名称
        joint_state_msg.position = left
        self.puppet_arm_left_publisher.publish(joint_state_msg)
        joint_state_msg.position = right
        self.puppet_arm_right_publisher.publish(joint_state_msg)

    def robot_base_publish(self, vel):
        vel_msg = Twist()
        vel_msg.linear.x = vel[0]
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = vel[1]
        self.robot_base_publisher.publish(vel_msg)

    def puppet_arm_publish_continuous(self, left, right):
        rate = rospy.Rate(self.args.publish_rate)
        left_arm = None
        right_arm = None
        while True and not rospy.is_shutdown():
            if len(self.puppet_arm_left_deque) != 0:
                left_arm = list(self.puppet_arm_left_deque[-1].position)
            if len(self.puppet_arm_right_deque) != 0:
                right_arm = list(self.puppet_arm_right_deque[-1].position)
            if left_arm is None or right_arm is None:
                rate.sleep()
                continue
            else:
                break
        left_symbol = [1 if left[i] - left_arm[i] > 0 else -1 for i in range(len(left))]
        right_symbol = [1 if right[i] - right_arm[i] > 0 else -1 for i in range(len(right))]
        flag = True
        step = 0
        while flag and not rospy.is_shutdown():
            if self.puppet_arm_publish_lock.acquire(False):
                return
            left_diff = [abs(left[i] - left_arm[i]) for i in range(len(left))]
            right_diff = [abs(right[i] - right_arm[i]) for i in range(len(right))]
            flag = False
            for i in range(len(left)):
                if left_diff[i] < self.args.arm_steps_length[i]:
                    left_arm[i] = left[i]
                else:
                    left_arm[i] += left_symbol[i] * self.args.arm_steps_length[i]
                    flag = True
            for i in range(len(right)):
                if right_diff[i] < self.args.arm_steps_length[i]:
                    right_arm[i] = right[i]
                else:
                    right_arm[i] += right_symbol[i] * self.args.arm_steps_length[i]
                    flag = True
            joint_state_msg = JointState()
            joint_state_msg.header = Header()
            joint_state_msg.header.stamp = rospy.Time.now()  # 设置时间戳
            joint_state_msg.name = ['joint0', 'joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']  # 设置关节名称
            joint_state_msg.position = left_arm
            self.puppet_arm_left_publisher.publish(joint_state_msg)
            joint_state_msg.position = right_arm
            self.puppet_arm_right_publisher.publish(joint_state_msg)
            step += 1
            # print("puppet_arm_publish_continuous:", step)
            rate.sleep()

    def puppet_arm_publish_linear(self, left, right):
        num_step = 100
        rate = rospy.Rate(200)

        left_arm = None
        right_arm = None

        while True and not rospy.is_shutdown():
            if len(self.puppet_arm_left_deque) != 0:
                left_arm = list(self.puppet_arm_left_deque[-1].position)
            if len(self.puppet_arm_right_deque) != 0:
                right_arm = list(self.puppet_arm_right_deque[-1].position)
            if left_arm is None or right_arm is None:
                rate.sleep()
                continue
            else:
                break

        traj_left_list = np.linspace(left_arm, left, num_step)
        traj_right_list = np.linspace(right_arm, right, num_step)

        for i in range(len(traj_left_list)):
            traj_left = traj_left_list[i]
            traj_right = traj_right_list[i]
            traj_left[-1] = left[-1]
            traj_right[-1] = right[-1]
            joint_state_msg = JointState()
            joint_state_msg.header = Header()
            joint_state_msg.header.stamp = rospy.Time.now()  # 设置时间戳
            joint_state_msg.name = ['joint0', 'joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']  # 设置关节名称
            joint_state_msg.position = traj_left
            self.puppet_arm_left_publisher.publish(joint_state_msg)
            joint_state_msg.position = traj_right
            self.puppet_arm_right_publisher.publish(joint_state_msg)
            rate.sleep()

    def puppet_arm_publish_continuous_thread(self, left, right):
        if self.puppet_arm_publish_thread is not None:
            self.puppet_arm_publish_lock.release()
            self.puppet_arm_publish_thread.join()
            self.puppet_arm_publish_lock.acquire(False)
            self.puppet_arm_publish_thread = None
        self.puppet_arm_publish_thread = threading.Thread(target=self.puppet_arm_publish_continuous, args=(left, right))
        self.puppet_arm_publish_thread.start()

    def get_frame(self):
        if len(self.img_left_deque) == 0 or len(self.img_right_deque) == 0 or len(self.img_front_deque) == 0 or \
                (self.args.use_depth_image and (len(self.img_left_depth_deque) == 0 or len(self.img_right_depth_deque) == 0 or len(self.img_front_depth_deque) == 0)):
            return False
        if self.args.use_depth_image:
            frame_time = min([self.img_left_deque[-1].header.stamp.to_sec(), self.img_right_deque[-1].header.stamp.to_sec(), self.img_front_deque[-1].header.stamp.to_sec(),
                              self.img_left_depth_deque[-1].header.stamp.to_sec(), self.img_right_depth_deque[-1].header.stamp.to_sec(), self.img_front_depth_deque[-1].header.stamp.to_sec()])
        else:
            frame_time = min([self.img_left_deque[-1].header.stamp.to_sec(), self.img_right_deque[-1].header.stamp.to_sec(), self.img_front_deque[-1].header.stamp.to_sec()])

        if len(self.img_left_deque) == 0 or self.img_left_deque[-1].header.stamp.to_sec() < frame_time:
            return False
        if len(self.img_right_deque) == 0 or self.img_right_deque[-1].header.stamp.to_sec() < frame_time:
            return False
        if len(self.img_front_deque) == 0 or self.img_front_deque[-1].header.stamp.to_sec() < frame_time:
            return False
        if len(self.puppet_arm_left_deque) == 0 or self.puppet_arm_left_deque[-1].header.stamp.to_sec() < frame_time:
            return False
        if len(self.puppet_arm_right_deque) == 0 or self.puppet_arm_right_deque[-1].header.stamp.to_sec() < frame_time:
            return False
        if self.args.use_depth_image and (len(self.img_left_depth_deque) == 0 or self.img_left_depth_deque[-1].header.stamp.to_sec() < frame_time):
            return False
        if self.args.use_depth_image and (len(self.img_right_depth_deque) == 0 or self.img_right_depth_deque[-1].header.stamp.to_sec() < frame_time):
            return False
        if self.args.use_depth_image and (len(self.img_front_depth_deque) == 0 or self.img_front_depth_deque[-1].header.stamp.to_sec() < frame_time):
            return False
        if self.args.use_robot_base and (len(self.robot_base_deque) == 0 or self.robot_base_deque[-1].header.stamp.to_sec() < frame_time):
            return False

        while self.img_left_deque[0].header.stamp.to_sec() < frame_time:
            self.img_left_deque.popleft()
        img_left = self.bridge.imgmsg_to_cv2(self.img_left_deque.popleft(), 'passthrough')

        while self.img_right_deque[0].header.stamp.to_sec() < frame_time:
            self.img_right_deque.popleft()
        img_right = self.bridge.imgmsg_to_cv2(self.img_right_deque.popleft(), 'passthrough')

        while self.img_front_deque[0].header.stamp.to_sec() < frame_time:
            self.img_front_deque.popleft()
        img_front = self.bridge.imgmsg_to_cv2(self.img_front_deque.popleft(), 'passthrough')

        while self.puppet_arm_left_deque[0].header.stamp.to_sec() < frame_time:
            self.puppet_arm_left_deque.popleft()
        puppet_arm_left = self.puppet_arm_left_deque.popleft()

        while self.puppet_arm_right_deque[0].header.stamp.to_sec() < frame_time:
            self.puppet_arm_right_deque.popleft()
        puppet_arm_right = self.puppet_arm_right_deque.popleft()

        img_left_depth = None
        if self.args.use_depth_image:
            while self.img_left_depth_deque[0].header.stamp.to_sec() < frame_time:
                self.img_left_depth_deque.popleft()
            img_left_depth = self.bridge.imgmsg_to_cv2(self.img_left_depth_deque.popleft(), 'passthrough')

        img_right_depth = None
        if self.args.use_depth_image:
            while self.img_right_depth_deque[0].header.stamp.to_sec() < frame_time:
                self.img_right_depth_deque.popleft()
            img_right_depth = self.bridge.imgmsg_to_cv2(self.img_right_depth_deque.popleft(), 'passthrough')

        img_front_depth = None
        if self.args.use_depth_image:
            while self.img_front_depth_deque[0].header.stamp.to_sec() < frame_time:
                self.img_front_depth_deque.popleft()
            img_front_depth = self.bridge.imgmsg_to_cv2(self.img_front_depth_deque.popleft(), 'passthrough')

        robot_base = None
        if self.args.use_robot_base:
            while self.robot_base_deque[0].header.stamp.to_sec() < frame_time:
                self.robot_base_deque.popleft()
            robot_base = self.robot_base_deque.popleft()

        return (img_front, img_left, img_right, img_front_depth, img_left_depth, img_right_depth,
                puppet_arm_left, puppet_arm_right, robot_base)

    def img_left_callback(self, msg):
        if len(self.img_left_deque) >= 2000:
            self.img_left_deque.popleft()
        self.img_left_deque.append(msg)

    def img_right_callback(self, msg):
        if len(self.img_right_deque) >= 2000:
            self.img_right_deque.popleft()
        self.img_right_deque.append(msg)

    def img_front_callback(self, msg):
        if len(self.img_front_deque) >= 2000:
            self.img_front_deque.popleft()
        self.img_front_deque.append(msg)

    def img_left_depth_callback(self, msg):
        if len(self.img_left_depth_deque) >= 2000:
            self.img_left_depth_deque.popleft()
        self.img_left_depth_deque.append(msg)

    def img_right_depth_callback(self, msg):
        if len(self.img_right_depth_deque) >= 2000:
            self.img_right_depth_deque.popleft()
        self.img_right_depth_deque.append(msg)

    def img_front_depth_callback(self, msg):
        if len(self.img_front_depth_deque) >= 2000:
            self.img_front_depth_deque.popleft()
        self.img_front_depth_deque.append(msg)

    def puppet_arm_left_callback(self, msg):
        if len(self.puppet_arm_left_deque) >= 2000:
            self.puppet_arm_left_deque.popleft()
        self.puppet_arm_left_deque.append(msg)

    def puppet_arm_right_callback(self, msg):
        if len(self.puppet_arm_right_deque) >= 2000:
            self.puppet_arm_right_deque.popleft()
        self.puppet_arm_right_deque.append(msg)

    def robot_base_callback(self, msg):
        if len(self.robot_base_deque) >= 2000:
            self.robot_base_deque.popleft()
        self.robot_base_deque.append(msg)

    def init_ros(self):
        rospy.init_node('joint_state_publisher', anonymous=True)
        rospy.Subscriber(self.args.img_left_topic, Image_msg, self.img_left_callback, queue_size=1000, tcp_nodelay=True)
        rospy.Subscriber(self.args.img_right_topic, Image_msg, self.img_right_callback, queue_size=1000, tcp_nodelay=True)
        rospy.Subscriber(self.args.img_front_topic, Image_msg, self.img_front_callback, queue_size=1000, tcp_nodelay=True)
        if self.args.use_depth_image:
            rospy.Subscriber(self.args.img_left_depth_topic, Image_msg, self.img_left_depth_callback, queue_size=1000, tcp_nodelay=True)
            rospy.Subscriber(self.args.img_right_depth_topic, Image_msg, self.img_right_depth_callback, queue_size=1000, tcp_nodelay=True)
            rospy.Subscriber(self.args.img_front_depth_topic, Image_msg, self.img_front_depth_callback, queue_size=1000, tcp_nodelay=True)
        rospy.Subscriber(self.args.puppet_arm_left_topic, JointState, self.puppet_arm_left_callback, queue_size=1000, tcp_nodelay=True)
        rospy.Subscriber(self.args.puppet_arm_right_topic, JointState, self.puppet_arm_right_callback, queue_size=1000, tcp_nodelay=True)
        rospy.Subscriber(self.args.robot_base_topic, Odometry, self.robot_base_callback, queue_size=1000, tcp_nodelay=True)
        self.puppet_arm_left_publisher = rospy.Publisher(self.args.puppet_arm_left_cmd_topic, JointState, queue_size=10)
        self.puppet_arm_right_publisher = rospy.Publisher(self.args.puppet_arm_right_cmd_topic, JointState, queue_size=10)
        self.robot_base_publisher = rospy.Publisher(self.args.robot_base_cmd_topic, Twist, queue_size=10)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ckpt_dir', action='store', type=str, help='ckpt_dir', required=True)
    parser.add_argument('--task_name', action='store', type=str, help='task_name', default='aloha_mobile_dummy', required=False)
    parser.add_argument('--max_publish_step', action='store', type=int, help='max_publish_step', default=10000, required=False)
    parser.add_argument('--ckpt_name', action='store', type=str, help='ckpt_name', default='policy_best.ckpt', required=False)
    parser.add_argument('--ckpt_stats_name', action='store', type=str, help='ckpt_stats_name', default='dataset_stats.pkl', required=False)
    parser.add_argument('--policy_class', action='store', type=str, help='policy_class, capitalize', default='ACT', required=False)
    parser.add_argument('--batch_size', action='store', type=int, help='batch_size', default=8, required=False)
    parser.add_argument('--seed', action='store', type=int, help='seed', default=0, required=False)
    parser.add_argument('--num_epochs', action='store', type=int, help='num_epochs', default=2000, required=False)
    parser.add_argument('--lr', action='store', type=float, help='lr', default=1e-5, required=False)
    parser.add_argument('--weight_decay', type=float, help='weight_decay', default=1e-4, required=False)
    parser.add_argument('--dilation', action='store_true',
                        help="If true, we replace stride with dilation in the last convolutional block (DC5)", required=False)
    parser.add_argument('--position_embedding', default='sine', type=str, choices=('sine', 'learned'),
                        help="Type of positional embedding to use on top of the image features", required=False)
    parser.add_argument('--masks', action='store_true',
                        help="Train segmentation head if the flag is provided")
    parser.add_argument('--kl_weight', action='store', type=int, help='KL Weight', default=10, required=False)
    parser.add_argument('--hidden_dim', action='store', type=int, help='hidden_dim', default=512, required=False)
    parser.add_argument('--dim_feedforward', action='store', type=int, help='dim_feedforward', default=3200, required=False)
    parser.add_argument('--temporal_agg', action='store', type=bool, help='temporal_agg', default=False, required=False)

    parser.add_argument('--state_dim', action='store', type=int, help='state_dim', default=14, required=False)
    parser.add_argument('--lr_backbone', action='store', type=float, help='lr_backbone', default=1e-5, required=False)
    parser.add_argument('--backbone', action='store', type=str, help='backbone', default='resnet18', required=False)
    parser.add_argument('--loss_function', action='store', type=str, help='loss_function l1 l2 l1+l2', default='l1', required=False)
    parser.add_argument('--enc_layers', action='store', type=int, help='enc_layers', default=4, required=False)
    parser.add_argument('--dec_layers', action='store', type=int, help='dec_layers', default=7, required=False)
    parser.add_argument('--nheads', action='store', type=int, help='nheads', default=8, required=False)
    parser.add_argument('--dropout', default=0.1, type=float, help="Dropout applied in the transformer", required=False)
    parser.add_argument('--pre_norm', action='store_true', required=False)

    parser.add_argument('--img_front_topic', action='store', type=str, help='img_front_topic',
                        default='/camera_f/color/image_raw', required=False)
    parser.add_argument('--img_left_topic', action='store', type=str, help='img_left_topic',
                        default='/camera_l/color/image_raw', required=False)
    parser.add_argument('--img_right_topic', action='store', type=str, help='img_right_topic',
                        default='/camera_r/color/image_raw', required=False)
    
    parser.add_argument('--img_front_depth_topic', action='store', type=str, help='img_front_depth_topic',
                        default='/camera_f/depth/image_raw', required=False)
    parser.add_argument('--img_left_depth_topic', action='store', type=str, help='img_left_depth_topic',
                        default='/camera_l/depth/image_raw', required=False)
    parser.add_argument('--img_right_depth_topic', action='store', type=str, help='img_right_depth_topic',
                        default='/camera_r/depth/image_raw', required=False)
    
    parser.add_argument('--puppet_arm_left_cmd_topic', action='store', type=str, help='puppet_arm_left_cmd_topic',
                        default='/master/joint_left', required=False)
    parser.add_argument('--puppet_arm_right_cmd_topic', action='store', type=str, help='puppet_arm_right_cmd_topic',
                        default='/master/joint_right', required=False)
    parser.add_argument('--puppet_arm_left_topic', action='store', type=str, help='puppet_arm_left_topic',
                        default='/puppet/joint_left', required=False)
    parser.add_argument('--puppet_arm_right_topic', action='store', type=str, help='puppet_arm_right_topic',
                        default='/puppet/joint_right', required=False)
    
    parser.add_argument('--robot_base_topic', action='store', type=str, help='robot_base_topic',
                        default='/odom_raw', required=False)
    parser.add_argument('--robot_base_cmd_topic', action='store', type=str, help='robot_base_topic',
                        default='/cmd_vel', required=False)
    parser.add_argument('--use_robot_base', action='store', type=bool, help='use_robot_base',
                        default=False, required=False)
    parser.add_argument('--publish_rate', action='store', type=int, help='publish_rate',
                        default=30, required=False)
    parser.add_argument('--pos_lookahead_step', action='store', type=int, help='pos_lookahead_step',
                        default=0, required=False)
    parser.add_argument('--max_pos_lookahead', action='store', type=int, help='max_pos_lookahead',
                        default=0, required=False)
    parser.add_argument('--chunk_size', action='store', type=int, help='chunk_size',
                        default=30, required=False)
    parser.add_argument('--arm_steps_length', action='store', type=float, help='arm_steps_length',
                        default=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.2], required=False)
                        # default=[0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.1], required=False)

    parser.add_argument('--use_actions_interpolation', action='store', type=bool, help='use_actions_interpolation',
                        default=True, required=False)
    parser.add_argument('--use_dataset_action', action='store', type=bool, help='use_dataset_action',
                        default=True, required=False)
    parser.add_argument('--use_depth_image', action='store', type=bool, help='use_depth_image',
                        default=False, required=False)

    # for Diffusion
    parser.add_argument('--observation_horizon', action='store', type=int, help='observation_horizon', default=1, required=False)
    parser.add_argument('--action_horizon', action='store', type=int, help='action_horizon', default=8, required=False)
    parser.add_argument('--num_inference_timesteps', action='store', type=int, help='num_inference_timesteps', default=10, required=False)
    parser.add_argument('--ema_power', action='store', type=int, help='ema_power', default=0.75, required=False)
    
    parser.add_argument('--pretrain_timestamp', action='store', type=str, help='pretrain_timestamp, like 2024-03-27_16-52-32', default='', required=False)
    parser.add_argument('--load_config', action='store', type=int, help='load_config', default=1, required=False)
    parser.add_argument('--device', type=str, help='device', default='cuda:0')
    args = parser.parse_args()
    
    # args.arm_steps_length = [x * 2 for x in args.arm_steps_length]
    return args


def main():
    args = get_arguments()
    ros_operator = RosOperator(args)
    config = get_model_config(args)
    model_inference(args, config, ros_operator, save_episode=True)


if __name__ == '__main__':
    main()
