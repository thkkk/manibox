
import argparse
import torch.nn as nn
from torch.nn import functional as F
import torchvision.transforms as transforms
import torch
from torch import nn

import IPython

from ManiBox.policy.backbone import DepthNet, build_backbone
from transformers import get_cosine_schedule_with_warmup
e = IPython.embed

class CNNRNNPolicy(nn.Module):
    """_summary_

    Args:
        model: CNNMLP
        optimizer: AdamW
        scheduler: TODO
        loss_function: MSELoss
        policy_config: see train.py
    """
    def __init__(self, policy_config):
        super().__init__()
        print("You are using CNNRNNPolicy.")
        
        backbones = []   # list
        depth_backbones = None
        if policy_config['use_depth_image']:
            depth_backbones = []

        args = argparse.Namespace(**policy_config)
        for _ in policy_config['camera_names']:
            backbone = build_backbone(args)  # policy from detr need args.xxx
            backbones.append(backbone)
            if policy_config['use_depth_image']:
                depth_backbones.append(DepthNet())
        
        self.model = CNNRNN(
            backbones,
            depth_backbones,
            policy_config,
        ).to(policy_config['device'])  # decoder
        
        param_dicts = [
            {"params": [p for n, p in self.model.named_parameters() if "backbone" not in n and p.requires_grad]},
            {
                "params": [p for n, p in self.model.named_parameters() if "backbone" in n and p.requires_grad],
                "lr": policy_config['lr_backbone'],
            },
        ]
        self.optimizer = torch.optim.AdamW(param_dicts, lr=policy_config['lr'],
                                  weight_decay=policy_config['weight_decay'])
        if args.use_scheduler == 'cos':
            self.scheduler = get_cosine_schedule_with_warmup(self.optimizer, int(args.epochs * args.train_loader_len * args.warmup_ratio), 
                                                        int(args.epochs * args.train_loader_len))
        elif args.use_scheduler == 'none':
            self.scheduler = None
        
        self.loss_function = policy_config['loss_function']
        
        n_parameters = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print("number of parameters: %.2fM" % (n_parameters/1e6,))

    def __call__(self, image, depth_image, robot_state, next_actions, next_actions_is_pad, actions=None,
                 action_is_pad=None):
        env_state = None  # TODO

        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])
        depth_normalize = transforms.Normalize(mean=[0.5], std=[0.5])
        image = normalize(image)  # 
        if depth_image is not None:
            depth_image = depth_normalize(depth_image)
        if actions is not None:  # training time
            # actions = actions[:, 0]  # 
            
            bs, context_len, state_dim = robot_state.shape
            rnn_hidden = self.model.init_hidden(bs)  # h, c
            a_hat = torch.zeros((bs, context_len, self.model.action_dim)).to(self.model.device)
            for i in range(context_len):
                action, rnn_hidden = self.model(
                    image[:, i, :], depth_image, robot_state[:, i, :],
                    None, None,
                    actions[:, i], action_is_pad[:, i], rnn_hidden
                )
                a_hat[:, i, :] = action
            
                                            
            # a_hat = self.model(image, depth_image, robot_state,
            #                    next_actions, next_actions_is_pad,
            #                    actions, action_is_pad)
            action_label = actions.reshape(a_hat.shape)
            # 
            if self.loss_function == 'l1':
                loss = F.l1_loss(action_label, a_hat)
            elif self.loss_function == 'l2':
                loss = F.mse_loss(action_label, a_hat)
            else:
                loss = F.smooth_l1_loss(action_label, a_hat)

            loss_dict = dict()
            loss_dict['loss'] = loss
            return loss_dict, a_hat

        else:  # inference time
            a_hat = self.model(image, depth_image, robot_state,
                               next_actions, next_actions_is_pad)  # no action, sample from prior
            return a_hat


def MLP_block(input_dim, hidden_dim, output_dim, hidden_depth):
    if hidden_depth == 0:
        mods = [nn.Linear(input_dim, output_dim)]
    else:
        mods = [nn.Linear(input_dim, hidden_dim), nn.ReLU(inplace=True)]
        for i in range(hidden_depth - 1):
            mods += [nn.Linear(hidden_dim, hidden_dim), nn.ReLU(inplace=True)]
        mods.append(nn.Linear(hidden_dim, output_dim))
    trunk = nn.Sequential(*mods)
    return trunk

    
class CNNRNN(nn.Module):
    def __init__(self, backbones, depth_backbones, policy_config):
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
        
        camera_names = policy_config['camera_names']
        num_next_action = policy_config['num_next_action']
        state_dim = policy_config['state_dim']
        
        self.state_dim = state_dim
        self.action_dim = policy_config['action_dim']
        self.device = policy_config['device']
        
        self.num_next_action = num_next_action
        self.camera_names = camera_names
        self.depth_backbones = depth_backbones
        self.action_head = nn.Linear(1000, state_dim) # TODO add more
        
        self.rnn_layers = policy_config['rnn_layers']
        self.rnn_hidden_dim = policy_config['rnn_hidden_dim']
        self.hidden_dim = policy_config['hidden_dim']
        
        if backbones is not None:
            self.backbones = nn.ModuleList(backbones)
            backbone_down_projs = []
            
            for i, backbone in enumerate(backbones):
                num_channels = backbone.num_channels
                if self.depth_backbones is not None:
                    num_channels += depth_backbones[i].num_channels
                down_proj = nn.Sequential(
                    nn.Conv2d(num_channels, 128, kernel_size=5),
                    nn.Conv2d(128, 64, kernel_size=5),
                    nn.Conv2d(64, 32, kernel_size=5)
                )
                backbone_down_projs.append(down_proj)
            self.backbone_down_projs = nn.ModuleList(backbone_down_projs)

            state_total_dim = 768 * len(backbones) + state_dim + state_dim * self.num_next_action
            self.rnn = nn.LSTM(state_total_dim, self.rnn_hidden_dim, num_layers=self.rnn_layers, batch_first=True)
            self.fc = nn.Linear(self.rnn_hidden_dim, self.hidden_dim)
            self.actor = nn.Linear(self.hidden_dim, self.action_dim)
        else:
            raise NotImplementedError
        # TODO: extract the vision encoder, try to feed the whole trajectory and preprocess the images

    def visual_encoder(self, image, depth_image):
        # bs, context_len, state_dim = robot_state.shape
        bs, cam_num, channel, height, width = image.shape
        # _, _, action_dim = actions.shape
        # merge the first 2 dim
        # image = image.reshape((bs * context_len, ) + image.shape[2:])
        # if depth_image is not None:
        #     depth_image = depth_image.reshape((bs * context_len, ) + depth_image.shape[2:])
        # print(f"image, robot_state, actions: {image.shape}, {robot_state.shape}, {actions.shape}")
        
        # Image observation features and position embeddings
        flattened_visual_features = []
        for cam_id, cam_name in enumerate(self.camera_names):
            feature, pos = self.backbones[cam_id](image[:, cam_id])
            feature = feature[0]  # take the last layer feature
            
            if self.depth_backbones is not None and depth_image is not None:
                features_depth = self.depth_backbones[cam_id](depth_image[:, :, cam_id].unsqueeze(dim=1))
                cur_cam_feature = self.backbone_down_projs[cam_id](torch.cat([feature, features_depth], axis=1))
            else:
                cur_cam_feature = self.backbone_down_projs[cam_id](feature)
                
            # cur_cam_feature [bs * context_len, 32, 3, 8]
            
            # flatten everything
            flattened_visual_features.append(cur_cam_feature.reshape([bs, -1]))
            
        flattened_visual_features = torch.cat(flattened_visual_features, axis=1)  # 768 = 32 * 3 * 8 for each cam
        return flattened_visual_features
    
    def init_hidden(self, bs):
        h = torch.zeros(self.rnn_layers, bs, self.rnn_hidden_dim).to(self.device)
        c = torch.zeros(self.rnn_layers, bs, self.rnn_hidden_dim).to(self.device)
        return h, c
    
    def forward(self, image, depth_image, robot_state, next_actions, next_action_is_pad, actions=None, action_is_pad=None, hidden=None):
        """
        qpos: batch, context_len, qpos_dim
        image: batch, context_len, num_cam, channel, height, width
        actions: batch, context_len, action_dim
        env_state: None
        """
        # print("image, robot_state, actions: ", image.shape, robot_state.shape, actions.shape)
        bs, state_dim = robot_state.shape
        # _, _, cam_num, channel, height, width = image.shape
        _, action_dim = actions.shape
        
        flattened_visual_features = self.visual_encoder(image, depth_image)
        # import pdb; pdb.set_trace()
        
        # concat visual features and robot state
        if self.num_next_action != 0 and next_actions is not None:
            all_feature = torch.cat([flattened_visual_features, robot_state, next_actions], axis=1)  # qpos: 14
        else:  # this branch
            all_feature = torch.cat([flattened_visual_features, robot_state], axis=1)  # qpos: 14
        all_feature = all_feature.unsqueeze(dim=1)
        # all_feature: (bs, 1, 768 * cam_num + state_dim)
        # the dim-1 is context_len
        
        self.rnn.flatten_parameters()
        if hidden is None:  # hidden could be None
            rnn_output, h = self.rnn(all_feature)
        else:
            # import pdb; pdb.set_trace()
            # hidden[0], hidden[1]: (num_layers * num_directions=2, bs, rnn_hidden_dim)
            rnn_output, h = self.rnn(all_feature, hidden)  # h~hidden
            # rnn_output: (bs, 1, rnn_hidden_dim)
            rnn_output = rnn_output.squeeze(dim=1)
        actions = F.gelu(self.fc(rnn_output))
        actions = self.actor(actions)
        
        if hidden is None:
            return actions
        else:
            return actions, h
        
        # import pdb; pdb.set_trace()
        # return a_hat
