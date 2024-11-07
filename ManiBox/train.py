import os
import pickle
import argparse
from copy import deepcopy
from tqdm import tqdm
import json
# from einops import rearrange
from datetime import datetime

import IPython
# e = IPython.embe
import shutil
import sys
sys.path.append("./")

import torch.multiprocessing as mp
import torch
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader
from torch.cuda.amp import autocast, GradScaler
import numpy as np
from accelerate import Accelerator
import matplotlib.pyplot as plt

from ManiBox.utils import compute_dict_mean, set_seed, detach_dict
from ManiBox.dataloader.data_load import load_data
from ManiBox.dataloader.EpisodicDataset import EpisodicDataset
from ManiBox.dataloader.HistoryEpisodicDataset import HistoryEpisodicDataset
from ManiBox.dataloader.BBoxHistoryEpisodicDataset import BBoxHistoryEpisodicDataset


def get_arguments():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--dataset', action='store', type=str, help='dataset_dir', default='./dataset', required=True)
    # parser.add_argument('--ckpt_dir', action='store', type=str, help='ckpt_dir', required=True)
    parser.add_argument('--dataset', action='store', type=str, help='dataset_dir', default='./dataset')
    parser.add_argument('--ckpt_dir', action='store', type=str, help='ckpt_dir', default='./ckpt')
    parser.add_argument('--pretrain_timestamp', action='store', type=str, help='pretrain_timestamp, like 2024-03-27_16-52-32', default='', required=False)
    parser.add_argument('--task_name', action='store', type=str, help='task_name', default='', required=False)
    parser.add_argument('--num_episodes', action='store', type=int, help='num_episodes', default=2000, required=False)
    
    parser.add_argument('--ckpt_name', action='store', type=str, help='ckpt_name', default='policy_best.ckpt', required=False)
    parser.add_argument('--ckpt_stats_name', action='store', type=str, help='ckpt_stats_name', default='dataset_stats.pkl', required=False)
    parser.add_argument('--policy_class', action='store', type=str, help='policy_class, capitalize, CNNMLP, ACT, Diffusion', default='ACT', required=False)
    parser.add_argument('--batch_size', action='store', type=int, help='batch_size', default=32, required=False)
    parser.add_argument('--seed', action='store', type=int, help='seed', default=0, required=False)
    parser.add_argument('--num_epochs', action='store', type=int, help='num_epochs', default=50, required=False)

    parser.add_argument('--num_eval_step', action='store', type=int, help='num_eval_step', default=1, required=False)
    parser.add_argument('--num_train_step', action='store', type=int, help='num_train_step', default=5, required=False)

    parser.add_argument('--lr', action='store', type=float, help='lr', default=7e-5, required=False)
    parser.add_argument('--weight_decay', type=float, help='weight_decay', default=1e-4, required=False)
    parser.add_argument('--dilation', action='store_true',
                        help="If true, we replace stride with dilation in the last convolutional block (DC5)", required=False)
    parser.add_argument('--position_embedding', default='sine', type=str, choices=('sine', 'learned'),
                        help="Type of positional embedding to use on top of the image features", required=False)
    parser.add_argument('--masks', action='store_true',
                        help="Train segmentation head if the flag is provided")

    parser.add_argument('--state_dim', action='store', type=int, help='state_dim', default=14, required=False)
    parser.add_argument('--lr_backbone', action='store', type=float, help='lr_backbone', default=7e-5, required=False)
    parser.add_argument('--backbone', action='store', type=str, help='backbone', default='resnet18', required=False)
    parser.add_argument('--loss_function', action='store', type=str, help='loss_function l1 l2 l1+l2', default='l1', required=False)
    parser.add_argument('--enc_layers', action='store', type=int, help='enc_layers', default=4, required=False)
    parser.add_argument('--dec_layers', action='store', type=int, help='dec_layers', default=7, required=False)
    parser.add_argument('--nheads', action='store', type=int, help='nheads', default=8, required=False)
    parser.add_argument('--dropout', default=0.2, type=float, help="Dropout applied in the transformer", required=False)
    parser.add_argument('--pre_norm', action='store_true', required=False)
    parser.add_argument('--gradient_accumulation_steps', action='store', type=int, help='gradient_accumulation_steps', default=16, required=False)
    
    # which aug we use, default is None, now support aug, distort
    parser.add_argument('--aug', default=None, type=str)

    # for ACT
    parser.add_argument('--kl_weight', action='store', type=int, help='KL Weight', default=10, required=False)
    parser.add_argument('--chunk_size', action='store', type=int, help='chunk_size', default=32, required=False)
    parser.add_argument('--max_pos_lookahead', action='store', type=int, help='max_pos_lookahead', default=0, required=False)
    parser.add_argument('--hidden_dim', action='store', type=int, help='hidden_dim', default=512, required=False)
    parser.add_argument('--dim_feedforward', action='store', type=int, help='dim_feedforward', default=3200, required=False)
    parser.add_argument('--temporal_agg',  action='store', type=bool, help='temporal_agg', default=True, required=False)
    parser.add_argument('--warmup_ratio', default=0.1, type=float, help='warmup ratio for lr schedule')
    parser.add_argument('--scheduler', default='cos', type=str, help='schedule, support cos, none now')
    parser.add_argument('--use_accelerate', action='store', type=bool, help='whether use accelerate', default=False, required=False)
    parser.add_argument('--device', type=str, help='device', default='cuda:0')

    # for Diffusion
    parser.add_argument('--observation_horizon', action='store', type=int, help='observation_horizon', default=1, required=False)
    parser.add_argument('--action_horizon', action='store', type=int, help='action_horizon', default=8, required=False)
    parser.add_argument('--num_inference_timesteps', action='store', type=int, help='num_inference_timesteps', default=10, required=False)
    parser.add_argument('--ema_power', action='store', type=int, help='ema_power', default=0.75, required=False)

    # for CNNRNN, rnn_layers, rnn_hidden_dim
    parser.add_argument('--rnn_layers', action='store', type=int, help='rnn_layers', default=3, required=False)
    parser.add_argument('--rnn_hidden_dim', action='store', type=int, help='rnn_hidden_dim', default=512, required=False)
    parser.add_argument('--actor_hidden_dim', action='store', type=int, help='actor_hidden_dim', default=512, required=False)
    
    # for DiffusionState: max_time_steps, time_embed_dim
    parser.add_argument('--max_time_steps', action='store', type=int, help='max_time_steps', default=1000, required=False)
    parser.add_argument('--time_embed_dim', action='store', type=int, help='time_embed_dim', default=128, required=False)
    parser.add_argument('--num_samples_per_traj', action='store', type=int, help='num_samples_per_traj', default=10, required=False)
    parser.add_argument('--alpha', action='store', type=float, help='alpha', default=3.0, required=False)
    parser.add_argument('--fcnet_hidden_dim', action='store', type=int, help='fcnet_hidden_dim', default=512, required=False)
    parser.add_argument('--n_modes', action='store', type=int, help='n_modes', default=10, required=False)
    parser.add_argument('--n_layer', action='store', type=int, help='n_layer', default=4, required=False)
    parser.add_argument('--is_chunk_wise', action='store', type=bool, help='is_chunk_wise', default=False, required=False)
    parser.add_argument('--context_len', action='store', type=int, help='context_len', default=90, required=False)
    parser.add_argument('--ffn_hidden_size', action='store', type=int, help='ffn_hidden_size', default=1024, required=False)
    
    
    parser.add_argument('--use_robot_base', action='store', type=bool, help='use_robot_base', default=False, required=False)

    parser.add_argument('--arm_delay_time', action='store', type=int, help='arm_delay_time', default=0, required=False)

    parser.add_argument('--use_dataset_action', action='store', type=bool, help='use_dataset_action', default=True, required=False)
    parser.add_argument('--use_depth_image', action='store', type=bool, help='use_depth_image', default=False, required=False)

    args = parser.parse_args()
    return args


args = get_arguments()
    
# torch.backends.cudnn.enabled = False
os.environ["NCCL_P2P_DISABLE"] = "1"
os.environ["NCCL_IB_DISABLE"] = "1"

accelerator = Accelerator(gradient_accumulation_steps=args.gradient_accumulation_steps)
accelerator.wait_for_everyone()

time_now = datetime.now()
timestamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")

print(f"Timestamp: {timestamp}")


def plot_history(train_history, validation_history, num_epochs, ckpt_dir, seed):
    # save training curves
    for key in train_history[0]:
        plot_path = os.path.join(ckpt_dir, f'train_val_{key}_seed_{seed}.png')
        plt.figure()
        train_values = [summary[key].item() for summary in train_history]
        val_values = [summary[key].item() for summary in validation_history]
        plt.plot(np.linspace(0, num_epochs-1, len(train_history)), train_values, label='train')
        plt.plot(np.linspace(0, num_epochs-1, len(validation_history)), val_values, label='validation')
        # plt.ylim([-0.1, 1])
        plt.tight_layout()
        plt.legend()
        plt.title(key)
        plt.savefig(plot_path)
    print(f'Saved plots to {ckpt_dir}')
    

import torchvision.transforms as transforms

# Define distortion operations
def distort_image(image):
    # transform = transforms.Compose([
    transform = transforms.RandomChoice([
        # transforms.RandomCrop(size=(224, 224)),  # Random crop
        # transforms.RandomHorizontalFlip(),  # Random horizontal flip
        # transforms.RandomVerticalFlip(),  # Random vertical flip
        # transforms.RandomRotation(degrees=15),  # random rotation [-15, 15]
        # # transforms.RandomCrop(size=(450, 600), padding=(15, 20), padding_mode='edge'),
        # transforms.RandomResizedCrop(size=(480, 640)),
        transforms.ColorJitter(brightness=0.3, contrast=0.2, saturation=0.2, hue=0.2),  # Random adjustments to brightness, contrast, saturation, and hue
    ])
    return transform(image)


def make_policy(policy_class, policy_config, pretrain_ckpt_dir):
    if len(pretrain_ckpt_dir) != 0:
        pretrain_ckpt_dir = os.path.join(pretrain_ckpt_dir, "policy_best.ckpt")
    if policy_class == 'ACT':
        from ManiBox.policy.ACTPolicy import ACTPolicy
        policy = ACTPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            state_dict = torch.load(pretrain_ckpt_dir)
            new_state_dict = {}
            for key, value in state_dict.items():
                if key in ["model.is_pad_head.weight", "model.is_pad_head.bias"]:
                    continue
                if policy_config['num_next_action'] == 0 and key in ["model.input_proj_next_action.weight",
                                                                     "model.input_proj_next_action.bias"]:
                    continue
                new_state_dict[key] = value
            loading_status = policy.load_state_dict(new_state_dict)
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'CNNMLP':
        from ManiBox.policy.CNNMLPPolicy import CNNMLPPolicy
        policy = CNNMLPPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'HistoryCNNMLP':
        from ManiBox.policy.HistoryCNNMLPPolicy import HistoryCNNMLPPolicy
        policy = HistoryCNNMLPPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'CNNRNN':
        from ManiBox.policy.CNNRNNPolicy import CNNRNNPolicy
        policy = CNNRNNPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'FPNRNN':
        from ManiBox.policy.FPNRNNPolicy import FPNRNNPolicy
        policy = FPNRNNPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'RNN':
        from ManiBox.policy.RNNPolicy import RNNPolicy
        policy = RNNPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'DiffusionState':
        from ManiBox.policy.DiffusionStatePolicy import DiffusionStatePolicy
        policy = DiffusionStatePolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    elif policy_class == 'Diffusion':
        from ManiBox.policy.DiffusionPolicy import DiffusionPolicy
        policy = DiffusionPolicy(policy_config)
        if len(pretrain_ckpt_dir) != 0:
            loading_status = policy.load_state_dict(torch.load(pretrain_ckpt_dir))
            if not loading_status:
                print("ckpt path not exist")
    else:
        raise NotImplementedError
    return policy

def parse_dataloader(train_dataloader: torch.utils.data.DataLoader):
    print("---------------------  parse_dataloader ---------------------")
    # print train_dataloader[0]
    for data in train_dataloader:
        """
        data[0] images: batch_size * 3 * 3 * 480 * 640
        data[2] qpos state: batch_size * 14
        data[5] qpos actions: batch_size * 112 * 14
        """   
        print(len(data), data[0].shape)
        print(len(data), data[2].shape)
        print(len(data), data[5].shape)
        break
    print("---------------------  parse_dataloader ---------------------")
    exit(0)


# ------------------------------------------ ------------------------------------------ ------------------------------------------
# ------------------------------------------ below is for training ------------------------------------------
# ------------------------------------------ ------------------------------------------ ------------------------------------------

def set_model_config(args, camera_names, len_train_dataloader):
    
    # fixed parameters for policy
    if args.policy_class == 'ACT':
        policy_config = {
            'lr': args.lr,
            'lr_backbone': args.lr_backbone,
            'backbone': args.backbone,
            'masks': args.masks,
            'weight_decay': args.weight_decay,
            'dilation': args.dilation,
            'position_embedding': args.position_embedding,
            'loss_function': args.loss_function,
            'chunk_size': args.chunk_size,    
            'camera_names': camera_names,
            'num_next_action': args.max_pos_lookahead,
            'use_depth_image': args.use_depth_image,
            'use_robot_base': args.use_robot_base,
            'kl_weight': args.kl_weight,       
            'hidden_dim': args.hidden_dim,   
            'dim_feedforward': args.dim_feedforward,
            'enc_layers': args.enc_layers,
            'dec_layers': args.dec_layers,
            'nheads': args.nheads,
            'dropout': args.dropout,
            'pre_norm': args.pre_norm,
            'epochs': args.num_epochs,
            'train_loader_len': len_train_dataloader, # 6 \approx seq_len / batch_size = 100 / 16
            'warmup_ratio': args.warmup_ratio,
            'use_scheduler': args.scheduler,
            'use_accelerate': args.use_accelerate,
            'device': args.device,
            'state_dim': args.state_dim,
            'action_dim': args.action_dim,
            'policy_class': args.policy_class,
        }
    elif args.policy_class == 'CNNMLP' or args.policy_class == 'HistoryCNNMLP':
        policy_config = {
            'lr': args.lr,
            'lr_backbone': args.lr_backbone,
            'epochs': args.num_epochs,
            'train_loader_len': len_train_dataloader, # 6 \approx seq_len / batch_size = 100 / 16
            'warmup_ratio': args.warmup_ratio,
            'use_scheduler': args.scheduler,
            'backbone': args.backbone,
            'masks': args.masks,
            'weight_decay': args.weight_decay,
            'dilation': args.dilation,
            'position_embedding': args.position_embedding,
            'loss_function': args.loss_function,
            'chunk_size': 1,     
            'camera_names': camera_names,
            'num_next_action': args.max_pos_lookahead,
            'use_depth_image': args.use_depth_image,
            'use_robot_base': args.use_robot_base,
            'hidden_dim': args.hidden_dim,
            'device': args.device,
            'state_dim': args.state_dim,
            'action_dim': args.action_dim,
            'policy_class': args.policy_class,
        }
    elif args.policy_class == 'CNNRNN' or args.policy_class == 'FPNRNN'  or args.policy_class == 'RNN':
        policy_config = {
            'lr': args.lr,
            'lr_backbone': args.lr_backbone,
            'epochs': args.num_epochs,
            'train_loader_len': len_train_dataloader, # 6 \approx seq_len / batch_size = 100 / 16
            'warmup_ratio': args.warmup_ratio,
            'use_scheduler': args.scheduler,
            'backbone': args.backbone,
            'masks': args.masks,
            'weight_decay': args.weight_decay,
            'dilation': args.dilation,
            'position_embedding': args.position_embedding,
            'loss_function': args.loss_function,
            'chunk_size': 1,   
            'camera_names': camera_names,
            'num_next_action': args.max_pos_lookahead,
            'use_depth_image': args.use_depth_image,
            'use_robot_base': args.use_robot_base,
            'hidden_dim': args.hidden_dim,
            'device': args.device,
            'state_dim': args.state_dim,
            'action_dim': args.action_dim,
            'rnn_layers': args.rnn_layers,
            'rnn_hidden_dim': args.rnn_hidden_dim,
            'actor_hidden_dim': args.actor_hidden_dim,
            'policy_class': args.policy_class,
            "gradient_accumulation_steps": args.gradient_accumulation_steps,
        }
    elif args.policy_class in ['DiffusionState']:
        policy_config = {
            'lr': args.lr,
            'lr_backbone': args.lr_backbone,
            'epochs': args.num_epochs,
            'train_loader_len': len_train_dataloader, # 6 \approx seq_len / batch_size = 100 / 16
            'warmup_ratio': args.warmup_ratio,
            'use_scheduler': args.scheduler,
            'backbone': args.backbone,
            'masks': args.masks,
            'weight_decay': args.weight_decay,
            'dilation': args.dilation,
            'position_embedding': args.position_embedding,
            'loss_function': args.loss_function,
            'chunk_size': 1,    
            'camera_names': camera_names,
            'num_next_action': args.max_pos_lookahead,
            'use_depth_image': args.use_depth_image,
            'use_robot_base': args.use_robot_base,
            'hidden_dim': args.hidden_dim,
            'device': args.device,
            'state_dim': args.state_dim,
            'action_dim': args.action_dim,
            'observation_horizon': args.observation_horizon,
            'action_horizon': args.action_horizon,
            'num_inference_timesteps': args.num_inference_timesteps,
            'ema_power': args.ema_power,
            # for DiffusionState
            'alpha': args.alpha,
            'max_time_steps': args.max_time_steps,
            'time_embed_dim': args.time_embed_dim,
            "context_len": args.context_len,
            'num_samples_per_traj': args.num_samples_per_traj,
            'policy_class': args.policy_class,
            "gradient_accumulation_steps": args.gradient_accumulation_steps,
        }
    return policy_config
        
def train(args):
    set_seed(1)

    DATA_DIR = os.path.expanduser(args.dataset) 
    
    TASK_CONFIGS = {
        args.task_name: {
            # 'dataset_dir': DATA_DIR + args.task_name,
            'dataset_dir': DATA_DIR,
            'camera_names': ['cam_high', 'cam_left_wrist', 'cam_right_wrist'],
            'num_episodes': args.num_episodes,
        }
    }


    task_config = TASK_CONFIGS[args.task_name]
    cur_path = os.path.dirname(os.path.abspath(__file__))
    print(f"cur_path {cur_path}")
    print('num episodes', task_config['num_episodes'])
    
    dataset_dir = task_config['dataset_dir']
    num_episodes = task_config['num_episodes']
    camera_names = task_config['camera_names']
    
    # ----------------------------- Begin of load data -----------------------------
    prefetch_factor = 2 if not args.use_accelerate else 2
    # 2 for single-gpu machine, 8 for multi-gpu machine
    if args.policy_class in ["RNN", "DiffusionState"]:
        episode_begin = 0
        episode_end = 90
        dataset_type = BBoxHistoryEpisodicDataset  # it will be preprocessed in load_data()
        prefetch_factor = 8
    elif "History" in args.policy_class:
        episode_begin = 3
        episode_end = 72
        dataset_type = HistoryEpisodicDataset
    else:
        episode_begin = 3
        episode_end = 90
        dataset_type = EpisodicDataset
    train_dataloader, val_dataloader, stats, _ = load_data(dataset_dir, num_episodes, args.arm_delay_time,
                                                           args.max_pos_lookahead, args.use_dataset_action,
                                                           args.use_depth_image, args.use_robot_base, camera_names,
                                                           args.batch_size, args.batch_size,
                                                           episode_begin=episode_begin,  # to avoid apple disappearing
                                                           episode_end=episode_end, context_len=args.context_len, prefetch_factor=prefetch_factor, dataset_type=dataset_type)
    # parse_dataloader(train_dataloader)
    print('length of train dataloader', len(train_dataloader))
    # ----------------------------- End of load data -----------------------------
    
    args.state_dim = args.state_dim if not args.use_robot_base else args.state_dim + 2  # qpos=7
    args.action_dim = args.state_dim

    policy_config = set_model_config(args, camera_names, len(train_dataloader))
    
    original_ckpt_dir = args.ckpt_dir
    args.ckpt_dir = os.path.join(args.ckpt_dir, timestamp + args.policy_class)  # new timestamp 
    if not os.path.isdir(args.ckpt_dir):
        os.makedirs(args.ckpt_dir)
    
    if len(args.pretrain_timestamp) != 0:
        pretrain_ckpt_dir = os.path.join(original_ckpt_dir, args.pretrain_timestamp)
    else:
        pretrain_ckpt_dir = ''
    
    # if you load the old model, then it will cover the old policy config
    # if len(pretrain_timestamp) != 0:
    #     config_file = os.path.join(original_ckpt_dir, args.pretrain_timestamp, "config.json")
    #     with open(config_file, 'r') as f:
    #         config_json = f.read()
    #     config = json.loads(config_json)
    #     policy_config = config["policy_config"]
    #     args.policy_class = 
    #     print("")
    
    config = {
        'num_epochs': args.num_epochs,
        'num_episodes': args.num_episodes,
        'ckpt_stats_name': args.ckpt_stats_name,
        'use_dataset_action': args.use_dataset_action,
        'ckpt_dir': args.ckpt_dir,
        'policy_class': args.policy_class,
        'policy_config': policy_config,
        'seed': args.seed,
        'pretrain_timestamp': args.pretrain_timestamp,
        'pretrain_ckpt_dir': pretrain_ckpt_dir,
        'num_eval_step': args.num_eval_step,
        'num_train_step': args.num_train_step,
        'use_scheduler': args.scheduler,
        'use_accelerate': args.use_accelerate,
        'device': args.device,
        'aug': args.aug,
    }
    if len(args.pretrain_timestamp) != 0:
        # load the policy config from the old model as well
        config_file = os.path.join(args.ckpt_dir, 'config.json') #
        with open(config_file, 'r') as f:
            config_json = f.read()
        config['policy_config'] = json.loads(config_json)['policy_config']
        print("RESUME! policy config covered.")
    
    if not os.path.isdir(args.ckpt_dir):
        os.makedirs(args.ckpt_dir)
    # save dataset_stats
    stats_path = os.path.join(args.ckpt_dir, args.ckpt_stats_name)
    with open(stats_path, 'wb') as f:
        pickle.dump(stats, f)

    # save config
    config_json = json.dumps(config, indent=4)
    with open(os.path.join(args.ckpt_dir, "config.json"), 'w') as f:
        f.write(config_json)

    best_ckpt_info = train_process(train_dataloader, val_dataloader, config, stats)
    best_epoch, min_val_loss, best_state_dict = best_ckpt_info

    # copy the train.log in the current path
    source_path =  os.path.join(os.getcwd(), 'train.log')
    destination_path = os.path.join(args.ckpt_dir, "train.log")
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"train.log File copied to {destination_path}")
    else:
        print(f"Source file '{source_path}' does not exist.")
    
    # save best checkpoint (have been saved!)
    # ckpt_path = os.path.join(args.ckpt_dir, args.ckpt_name)
    # torch.save(best_state_dict, ckpt_path)
    print(f'Best ckpt, val loss {min_val_loss:.6f} @ epoch{best_epoch}')


def train_process(train_dataloader: DataLoader, val_dataloader: DataLoader, config, stats):
    if config['use_dataset_action']:
        post_process = lambda a: a * stats['action_std'] + stats['action_mean']
    else:
        post_process = lambda a: a * stats['qpos_std'] + stats['qpos_mean']

    num_epochs = config['num_epochs']
    ckpt_dir = config['ckpt_dir']
    seed = config['seed']
    policy_class = config['policy_class']
    policy_config = config['policy_config']
    pretrain_ckpt_dir = config['pretrain_ckpt_dir']
    num_eval_step = config['num_eval_step']
    num_train_step = config['num_train_step']
    set_seed(seed)

    policy = make_policy(policy_class, policy_config, pretrain_ckpt_dir)
    # policy = torch.load('/home/ycy17/Desktop/code/low-level-ACT/aloha-devel/act/ckpt_old4/policy_epoch_9740_seed_0.ckpt')
    optimizer = policy.optimizer
    
    scheduler = policy.scheduler

    
    if config['use_accelerate']:
        if config['use_scheduler'] == 'cos':
            policy, optimizer, scheduler, train_dataloader, val_dataloader = accelerator.prepare(policy, optimizer, scheduler, train_dataloader, val_dataloader)
        elif config['use_scheduler'] == 'none':
            policy, optimizer, train_dataloader, val_dataloader = accelerator.prepare(policy, optimizer, train_dataloader, val_dataloader)
        else:
            raise NotImplementedError
    else:
        policy = policy.to(device=config['device'])
    # scaler = GradScaler()

    train_history = []
    validation_history = []
    min_val_loss = np.inf
    best_ckpt_info = (0, np.inf, None)
    print_interval = 1
    eval_interval = 1
    save_interval = 20
    
    import time
    start_time = time.time()
    for epoch in tqdm(range(num_epochs)):
        # TODO: save file with timestamps, including png, ckpt, config, fewer tqdm info
        train_dataloader.dataset.shuffle()  # HistoryEpisodicDataset
        val_dataloader.dataset.shuffle()
        # ---------------------------- Training ----------------------------
        policy.train()
        iterator = (tqdm(enumerate(train_dataloader), mininterval=10, leave=False)
                    if epoch == 0 else
                    enumerate(train_dataloader))
        for batch_idx, data in iterator:
            """
            data[0] images: batch_size * context_len * 3 * 3 * 480 * 640
            data[2] qpos state: batch_size * context_len * 14
            data[5] qpos actions: batch_size * context_len * 14
            """   
            # print(len(data), data[0].shape)
            # print(len(data), data[2].shape)
            # print(len(data), data[5].shape)
            # exit(0)
            
            if not config['use_accelerate']:
                # stream = torch.cuda.Stream()
                # to_t1 = time.time()
                # data = [d.to(dtype=torch.float16) for d in data] 
                # with torch.cuda.stream(stream):
                data = [d.to(device=config['device'], non_blocking=True) for d in data]  # , non_blocking=True
                # it is too slow to copy data from cpu to cuda (0.8s per data for raw code)
                # data = [d.to(dtype=torch.float32) for d in data] 
                # print(f'to device time: {time.time() - to_t1} s')
                
            # import pdb
            # pdb.set_trace()
            if config['aug'] == 'distort':
                data[0] = distort_image(data[0])
            elif config['aug'] == None:
                # print('we do not aug')
                pass
            else:
                raise NotImplementedError
            
            # with autocast(dtype=torch.bfloat16):
            with accelerator.accumulate(policy):
                forward_dict, result = forward_pass(policy_config, data, policy)
                
                # print("result:", post_process(result.cpu().detach().numpy())[0, :, 7:])
                # backward
                loss = forward_dict['loss']
                if config['use_accelerate']:
                    accelerator.backward(loss)
                    # accelerator.backward(scaler.scale(loss))
                    # scaler.step(optimizer)
                    # scaler.update()
                else:
                    loss.backward()
                    # scaler.scale(loss).backward()
                    
                    # NOTE: dont delete these lines, for debugging
                    # print and compare grad (visual encoder vs. temporal model)
                    # visual_encoder_grad = []
                    # temporal_model_grad = []
                    # for name, param in policy.model.named_parameters():
                    #     if param.requires_grad and 'backbone' in name and param.grad != None:
                    #         print(f"visual encoder. Gradient for {name}: {param.grad.mean()}")
                    #         visual_encoder_grad.append(param.grad.mean().item())
                    #     elif param.requires_grad and 'backbone' not in name and param.grad != None:
                    #         print(f"temporal model. Gradient for {name}: {param.grad.mean()}")
                    #         temporal_model_grad.append(param.grad.mean().item())
                    # print(f"visual encoder grad: {np.mean(visual_encoder_grad)}")
                    # print(f"temporal model grad: {np.mean(temporal_model_grad)}")
                    # scaler.step(optimizer)
                    # scaler.update()
                torch.nn.utils.clip_grad_norm_(policy.parameters(), 1.0)

                optimizer.step()
                train_history.append(detach_dict(forward_dict))
                if scheduler != None:
                    scheduler.step()
                optimizer.zero_grad()
                
            
        epoch_summary = compute_dict_mean(train_history[(batch_idx+1)*epoch:(batch_idx+1)*(epoch+1)])
        epoch_train_loss = epoch_summary['loss']
        
        if epoch % print_interval == 0:
            print(f'\nEpoch {epoch}, lr:', optimizer.param_groups[0]['lr'])  # this lr means lr, not lr_backbone
            print(f'Train loss: {epoch_train_loss:.5f}')
            summary_string = ''
            for k, v in epoch_summary.items():
                summary_string += f'{k}: {v.item():.3f} '
            print(summary_string)
            plot_history(train_history, validation_history, epoch, ckpt_dir, seed)

        # if epoch % save_interval == 0:
        #     ckpt_path = os.path.join(ckpt_dir, f'policy_epoch_{epoch}_seed_{seed}.ckpt')
        #     if config['use_accelerate']:
        #         torch.save(policy, ckpt_path)
        #     else:
        #         torch.save(policy.state_dict(), ckpt_path)
        
        # ---------------------------- Validation ----------------------------
        # TODO: ACT
        if epoch % eval_interval == 0:
            with torch.inference_mode():
                policy.eval()
                epoch_dicts = []
                for batch_idx, data in enumerate(val_dataloader):
                    if not config['use_accelerate']:
                        data = [d.to(device=config['device']) for d in data]
                    forward_dict, result = forward_pass(policy_config, data, policy)
                    # print("result:", post_process(result.cpu().detach().numpy())[0, :, 7:])
                    epoch_dicts.append(forward_dict)
                    # if batch_idx >= num_eval_step:
                    #     break
                epoch_summary = compute_dict_mean(epoch_dicts)
                validation_history.append(epoch_summary)

                epoch_val_loss = epoch_summary['loss']
                
                accelerator.wait_for_everyone()
                if epoch_val_loss < min_val_loss:
                    min_val_loss = epoch_val_loss
                    best_path = os.path.join(ckpt_dir, f'policy_best.ckpt')
                    if config['use_accelerate']:
                        best_ckpt_info = (epoch, min_val_loss, deepcopy(policy))
                        if accelerator.is_main_process: 
                            unwrapped_model = accelerator.unwrap_model(policy)
                            torch.save(unwrapped_model.state_dict(), best_path)
                            # unwrap model, otherwise it will occur `Missing 'module.' key(s) in state_dict` error when loading model
                            # torch.save(policy.state_dict(), best_path)
                    else:
                        best_ckpt_info = (epoch, min_val_loss, deepcopy(policy.state_dict()))
                        torch.save(policy.state_dict(), best_path)
                    print(f'Best ckpt saved, val loss {min_val_loss:.6f} @ epoch{best_ckpt_info[0]}')
            accelerator.wait_for_everyone()  # # Ensure all processes sync up before continuing
            
            # print('time 2', time.time() - start_time)
            # print(f'Val loss:   {epoch_val_loss:.5f}')
            print(f'Val loss:   {epoch_val_loss:.5f}.   Best val loss: {min_val_loss:.5f} at epoch {best_ckpt_info[0]}')

            summary_string = ''
            for k, v in epoch_summary.items():
                summary_string += f'{k}: {v.item():.3f} '
            print(summary_string)

    # ckpt_path = os.path.join(ckpt_dir, f'policy_last.ckpt')
    # if config['use_accelerate']:
    #     if accelerator.is_main_process:
    #         unwrapped_model = accelerator.unwrap_model(policy)
    #         torch.save(unwrapped_model.state_dict(), ckpt_path)
    #         # torch.save(policy.state_dict(), ckpt_path)
    # else:
    #     torch.save(policy.state_dict(), ckpt_path)
    accelerator.wait_for_everyone()
    
    best_epoch, min_val_loss, best_state_dict = best_ckpt_info
    # ckpt_path = os.path.join(ckpt_dir, f'{min_val_loss:.4f}_policy_epoch_{best_epoch}_seed_{seed}.ckpt')
    # torch.save(best_state_dict, ckpt_path)
    print(f'Training finished:\nSeed {seed}, val loss {min_val_loss:.6f} at epoch {best_epoch}')

    # save training curves
    plot_history(train_history, validation_history, num_epochs, ckpt_dir, seed)

    return best_ckpt_info


def forward_pass(policy_config, data, policy):
    image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad = data
    
    if policy_config['use_depth_image']:
        image_depth_data = image_depth_data
    else:
        image_depth_data = None
    if policy_config['num_next_action'] != 0:
        return policy(image_data, image_depth_data, qpos_data, next_action_data, next_action_is_pad, action_data, action_is_pad)
    else:  # this branch
        return policy(image_data, image_depth_data, qpos_data, None, None, action_data, action_is_pad)


def main():
    print('scheduler:', args.scheduler, "args.gradient_accumulation_steps", args.gradient_accumulation_steps)
    print('whether use acclerator:', args.use_accelerate)
    train(args)


if __name__ == '__main__':
    main()

