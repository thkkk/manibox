
import argparse
import torch.nn as nn
from torch.nn import functional as F
import torchvision.transforms as transforms
import torch
from torch import nn

import IPython
from tqdm import tqdm

from ManiBox.yolo_process_data import YoloProcessDataByTimeStep
from transformers import get_cosine_schedule_with_warmup
e = IPython.embed


class RNNPolicy(nn.Module):
    """_summary_

    Args:
        model: ...
        optimizer: AdamW
        scheduler: cos
        loss_function: ...
        policy_config: see train.py
    """
    def __init__(self, policy_config):
        super().__init__()
        print("You are using RNNPolicy.")
        
        print("policy_config", policy_config)
        args = argparse.Namespace(**policy_config)
        camera_num = 0
        for _ in policy_config['camera_names']:
            camera_num += 1
        
        self.model = RNN(
            camera_num,
            policy_config,
        ) 
        
        param_dicts = [
            {"params": [p for n, p in self.model.named_parameters() if "backbone" not in n and p.requires_grad]},
            # temporal model
            {
                "params": [p for n, p in self.model.named_parameters() if "backbone" in n and p.requires_grad],
                "lr": policy_config['lr_backbone'],
            },  # backbone(visual encoder) model, using another lr
        ]
        self.optimizer = torch.optim.AdamW(param_dicts, lr=policy_config['lr'],
                                  weight_decay=policy_config['weight_decay'])
        if args.use_scheduler == 'cos':
            self.scheduler = get_cosine_schedule_with_warmup(self.optimizer, int(args.epochs * args.train_loader_len * args.warmup_ratio / args.gradient_accumulation_steps), 
                                                        int(args.epochs * args.train_loader_len / args.gradient_accumulation_steps))
        elif args.use_scheduler == 'none':
            self.scheduler = None
        
        self.loss_function = policy_config['loss_function']
        
        # n_parameters = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        # print("total number of parameters: %.2fM" % (n_parameters/1e6,))
        backbone_parameters = sum(p.numel() for n, p in self.model.named_parameters() if "backbone" in n and p.requires_grad)
        temporal_parameters = sum(p.numel() for n, p in self.model.named_parameters() if "backbone" not in n and p.requires_grad)
        print("backbone visual encoder. number of parameters: %.2fM" % (backbone_parameters/1e6,))
        print("temporal model. number of parameters: %.2fM" % (temporal_parameters/1e6,))
        

    def __call__(self, image, depth_image, robot_state, next_actions, next_actions_is_pad, actions=None,
                 action_is_pad=None):
        """forward process of whole trajectory. if actions == None, it will infer only one action. 
        `is_inference` means that it will recurrently infer actions using for-loop

        inference example:
        ```
        yolo_process_data = YoloProcessDataByTimeStep()
        yolo_process_data.reset_new_episode()
        
        policy = RNNPolicy(policy_config)
        policy.reset_recur(batch_size, image.device)
        for i in range(context_len):
            image_data = yolo_process_data.process(cam_high, cam_left_wrist, cam_right_wrist)
            action = policy(image_data, None, robot_state, None, None, actions=None,
                 action_is_pad=None)
        ```
        
        Args:
            image (torch.Tensor): batch_size * context_len * 24
            depth_image: None is ok
            robot_state (torch.Tensor): batch_size * context_len * 14
            next_actions: None is ok
            next_actions_is_pad: None is ok
            actions (torch.Tensor, optional): batch_size * context_len * 14. Defaults to None.
            action_is_pad: None is ok
            is_inference (bool, optional): inference or not. It makes difference when the model need recurrently inference. 
            Defaults to False.

        Notice: batch_size is at least 1. context_len is at least 1. 
        """
        depth_normalize = transforms.Normalize(mean=[0.5], std=[0.5])
        if depth_image is not None:
            depth_image = depth_normalize(depth_image)
        if actions is not None:  # training time
            bs, context_len, state_dim = robot_state.shape
            self.reset_recur(bs, image.device)  # h, c
            state = torch.cat([image, robot_state], dim=-1)  # (bs, context_len, 24+14)
            a_hat, _ = self.model(
                state, self.rnn_hidden
            )
            
            action_label = actions.reshape(a_hat.shape)
            # 
            if self.loss_function == 'l1':
                loss = F.l1_loss(action_label, a_hat)

            loss_dict = dict()
            loss_dict['loss'] = loss
            return loss_dict, a_hat

        else:  # inference time, infer an action at each timestep, based on history
            # image: (batch_size, 24), robot_state: (batch_size, 14)
            image = image.unsqueeze(dim=1)  # (bs, 1, 24)
            robot_state = robot_state.unsqueeze(dim=1)  # (bs, 1, 14)
            state = torch.cat([image, robot_state], dim=-1)  # (bs, 1, 24+14)
            a_hat, self.rnn_hidden = self.model(
                state, self.rnn_hidden
            )  # depth_image could be None
            return a_hat[:, 0, :]  # (bs, 14)

    def reset_recur(self, bs, device):
        self.rnn_hidden = self.model.init_hidden(bs, device)


class RNN(nn.Module):
    def __init__(self, camera_num, policy_config):
        """ Initializes the model.
        Parameters:
            backbones: torch module of the backbone to be used. See backbone.py
            transformer: torch module of the transformer architecture. See transformer.py
            state_dim: robot state dimension of the environment
            num_queries: number of object queries, ie detection slot. This is the maximal number of objects
                         DETR can detect in a single image. For COCO, we recommend 100 queries.
            aux_loss: True if auxiliary decoding losses (loss at each decoder layer) are to be used.
        """
        super().__init__()
        self.policy_config = policy_config
        self.camera_num = camera_num
        
        camera_names = policy_config['camera_names']
        num_next_action = policy_config['num_next_action']
        state_dim = policy_config['state_dim']
        
        self.state_dim = state_dim
        self.action_dim = policy_config['action_dim']
        self.device = policy_config['device']
        
        self.num_next_action = num_next_action
        self.camera_names = camera_names
        
        self.rnn_layers = policy_config['rnn_layers']
        self.rnn_hidden_dim = policy_config['rnn_hidden_dim']
        self.actor_hidden_dim = policy_config['actor_hidden_dim']
        
        visual_embedding_dim = len(YoloProcessDataByTimeStep.objects_names) * 4 * camera_num
        self.visual_embedding_dim = visual_embedding_dim

        state_total_dim = visual_embedding_dim + state_dim + state_dim * self.num_next_action
        self.rnn = nn.LSTM(state_total_dim, self.rnn_hidden_dim, num_layers=self.rnn_layers, batch_first=True)
        self.fc = nn.Linear(self.rnn_hidden_dim, self.actor_hidden_dim)
        self.dropout = nn.Dropout(p=0.1)
        self.action_head = nn.Linear(self.actor_hidden_dim, self.action_dim)
    
    def init_hidden(self, bs, device):
        h = torch.zeros(self.rnn_layers, bs, self.rnn_hidden_dim).to(device)
        c = torch.zeros(self.rnn_layers, bs, self.rnn_hidden_dim).to(device)
        return h, c
    
    def forward(self, all_state, hidden=None):
        """
        robot_state: batch, (context_len), qpos_dim
        image: batch, (context_len), image_dim(24)
        actions: batch, (context_len), action_dim
        env_state: None
        """
        self.rnn.flatten_parameters()
        if hidden is None:  # hidden could be None
            rnn_output, h = self.rnn(all_state)
        else:
            # hidden[0], hidden[1]: (num_layers * num_directions=2, bs, rnn_hidden_dim)
            rnn_output, h = self.rnn(all_state, hidden)  # h~hidden
            # rnn_output: (bs, 1, rnn_hidden_dim)
        actions = F.gelu(self.fc(rnn_output))
        actions = self.dropout(actions)
        actions = self.action_head(actions)
        
        if hidden is None:
            return actions
        else:
            return actions, h
