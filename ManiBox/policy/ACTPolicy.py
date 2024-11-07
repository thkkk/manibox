
import argparse
import torch.nn as nn
from torch.nn import functional as F
import torchvision.transforms as transforms
import torch
from torch.autograd import Variable

import IPython

from ManiBox.policy.backbone import DepthNet, build_backbone
from ManiBox.policy.transformer import build_transformer, TransformerEncoder, TransformerEncoderLayer
import numpy as np

e = IPython.embed

def kl_divergence(mu, logvar):
    batch_size = mu.size(0)
    assert batch_size != 0
    if mu.data.ndimension() == 4:
        mu = mu.view(mu.size(0), mu.size(1))
    if logvar.data.ndimension() == 4:
        logvar = logvar.view(logvar.size(0), logvar.size(1))

    klds = -0.5 * (1 + logvar - mu.pow(2) - logvar.exp())
    total_kld = klds.sum(1).mean(0, True)
    dimension_wise_kld = klds.mean(0)
    mean_kld = klds.mean(1).mean(0, True)

    return total_kld, dimension_wise_kld, mean_kld


def build_encoder(args):
    
    d_model = args.hidden_dim  # 256
    dropout = args.dropout     # 0.1
    nhead = args.nheads        # 8
    dim_feedforward = args.dim_feedforward  # 2048
    num_encoder_layers = args.enc_layers  # 4 # TODO shared with VAE decoder
    normalize_before = args.pre_norm  # False
    activation = "relu"

    encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward,
                                            dropout, activation, normalize_before)
    
    encoder_norm = nn.LayerNorm(d_model) if normalize_before else None
    
    encoder = TransformerEncoder(encoder_layer, num_encoder_layers, encoder_norm)

    return encoder


def reparametrize(mu, logvar):
    std = logvar.div(2).exp()
    eps = Variable(std.data.new(std.size()).normal_())
    return mu + std * eps


def get_sinusoid_encoding_table(n_position, d_hid):
    def get_position_angle_vec(position):
        return [position / np.power(10000, 2 * (hid_j // 2) / d_hid) for hid_j in range(d_hid)]

    sinusoid_table = np.array([get_position_angle_vec(pos_i) for pos_i in range(n_position)])
    sinusoid_table[:, 0::2] = np.sin(sinusoid_table[:, 0::2])  # dim 2i
    sinusoid_table[:, 1::2] = np.cos(sinusoid_table[:, 1::2])  # dim 2i+1

    return torch.FloatTensor(sinusoid_table).unsqueeze(0)


class ACTPolicy(nn.Module):
    def __init__(self, policy_config):
        super().__init__()
        print("You are using ACTPolicy.")
        
        args = argparse.Namespace(**policy_config)
        # model, optimizer, scheduler = build_ACT_model_and_optimizer(policy_config)
        # model:
        if args.use_robot_base:
            state_dim = 16  # TODO hardcode
        else:
            state_dim = 14

        # From state
        # backbone = None # from state for now, no need for conv nets
        # From image
        backbones = []   # list
        depth_backbones = None
        if args.use_depth_image:
            depth_backbones = []

        for _ in args.camera_names:
            backbone = build_backbone(args)
            backbones.append(backbone)
            if args.use_depth_image:
                depth_backbones.append(DepthNet())

        transformer = build_transformer(args)  # trans

        encoder = None
        if args.kl_weight != 0:
            encoder = build_encoder(args)          # 

        model = DETRVAE(
            backbones,
            depth_backbones,
            transformer,
            encoder,
            state_dim=state_dim,
            num_queries=args.chunk_size,
            camera_names=args.camera_names,
            num_next_action=args.num_next_action,
            kl_weight=args.kl_weight
        )

        n_parameters = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print("number of parameters: %.2fM" % (n_parameters/1e6,))

        param_dicts = [
            {"params": [p for n, p in model.named_parameters() if "backbone" not in n and p.requires_grad]},
            {
                "params": [p for n, p in model.named_parameters() if "backbone" in n and p.requires_grad],
                "lr": args.lr_backbone,
            },
        ]

        # 
        from transformers import get_cosine_schedule_with_warmup

        optimizer = torch.optim.AdamW(param_dicts, lr=args.lr,
                                    weight_decay=args.weight_decay)
        if args.use_scheduler == 'cos':
            scheduler = get_cosine_schedule_with_warmup(optimizer, int(args.epochs * args.train_loader_len * args.warmup_ratio), 
                                                        int(args.epochs * args.train_loader_len))
        elif args.use_scheduler == 'none':
            scheduler = None
        else:
            raise NotImplementedError()
        
        self.model = model  # CVAE decoder
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.kl_weight = policy_config['kl_weight']
        self.loss_function = policy_config['loss_function']

        print(f'KL Weight {self.kl_weight}')

    def __call__(self, image, depth_image, robot_state, next_actions, next_actions_is_pad, actions=None,
                 action_is_pad=None, history_qpos=None):

        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])
        depth_normalize = transforms.Normalize(mean=[0.5], std=[0.5])

        image = normalize(image)  # 
        if depth_image is not None:
            depth_image = depth_normalize(depth_image)

        # max model.num_queries 
        if actions is not None:  # training time
            actions = actions[:, :self.model.num_queries]
            action_is_pad = action_is_pad[:, :self.model.num_queries]

            # import pdb
            # pdb.set_trace()
            robot_state = robot_state.to(dtype=image.dtype)
            actions = actions.to(dtype=image.dtype)
            image = image.requires_grad_()
            robot_state = robot_state.requires_grad_()
            
            # robot_state = robot_state.clone().detach().requires_grad_()
            # self.model.zero_grad()
            a_hat, (mu, logvar) = self.model(image, depth_image, robot_state,
                                             next_actions, next_actions_is_pad,
                                             actions, action_is_pad, history_qpos=history_qpos)

            loss_dict = dict()
            if self.loss_function == 'l1':
                all_l1 = F.l1_loss(actions, a_hat, reduction='none')
            elif self.loss_function == 'l2':
                all_l1 = F.mse_loss(actions, a_hat, reduction='none')
            else:
                all_l1 = F.smooth_l1_loss(actions, a_hat, reduction='none')

            l1 = (all_l1 * ~action_is_pad.unsqueeze(-1)).mean()
            
            # import pdb
            # pdb.set_trace()

            loss_dict['l1'] = l1
            if self.kl_weight != 0:
                total_kld, dim_wise_kld, mean_kld = kl_divergence(mu, logvar)
                loss_dict['kl'] = total_kld[0]
                loss_dict['loss'] = loss_dict['l1'] + loss_dict['kl'] * self.kl_weight
            else:
                loss_dict['loss'] = loss_dict['l1']

            return loss_dict, a_hat
        else:  # inference time
            a_hat, (_, _) = self.model(image, depth_image, robot_state, next_actions,
                                       next_actions_is_pad, history_qpos=history_qpos)  # no action, sample from prior
            return a_hat

class DETRVAE(nn.Module):
    """ This is the DETR module that performs object detection """
    def __init__(self, backbones, depth_backbones, transformer, encoder, state_dim, num_queries, camera_names,
                 num_next_action, kl_weight):
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
        self.num_queries = num_queries
        self.camera_names = camera_names
        self.transformer = transformer
        self.encoder = encoder
        hidden_dim = transformer.d_model
        self.action_head = nn.Linear(hidden_dim, state_dim)
        self.query_embed = nn.Embedding(num_queries, hidden_dim)
        self.kl_weight = kl_weight
        self.num_next_action = num_next_action
        
        if backbones is not None:
            # print("backbones[0]", backbones[0])
            if depth_backbones is not None:
                self.depth_backbones = nn.ModuleList(depth_backbones)
                self.input_proj = nn.Conv2d(backbones[0].num_channels + depth_backbones[0].num_channels, hidden_dim, kernel_size=1)
            else:
                self.depth_backbones = None
                self.input_proj = nn.Conv2d(backbones[0].num_channels, hidden_dim, kernel_size=1)
            self.backbones = nn.ModuleList(backbones)
            self.input_proj_robot_state = nn.Linear(state_dim, hidden_dim)
            if num_next_action != 0:
                self.input_proj_next_action = nn.Linear(state_dim, hidden_dim)
        
        else:
            # input_dim = 14 + 7 # robot_state + env_state
            self.input_proj_robot_state = nn.Linear(state_dim, hidden_dim)
            if num_next_action != 0:
                self.input_proj_next_action = nn.Linear(state_dim, hidden_dim)
            self.pos = torch.nn.Embedding(2, hidden_dim)
            self.backbones = None

        # encoder extra parameters
        self.latent_dim = 32  # final size of latent z # TODO tune
        self.cls_embed = nn.Embedding(1, hidden_dim)  # extra cls token embedding

        # decoder extra parameters
        self.latent_out_proj = nn.Linear(self.latent_dim, hidden_dim)  # project latent sample to embedding

        if num_next_action != 0:
            self.next_action_pos = nn.Embedding(num_next_action, hidden_dim)  # learned position embedding for proprio and latent
        else:
            self.next_action_pos = None
        self.latent_pos = nn.Embedding(1, hidden_dim)
        self.robot_state_pos = nn.Embedding(1, hidden_dim)

        if kl_weight != 0:
            self.encoder_action_proj = nn.Linear(state_dim, hidden_dim)  # project action to embedding
            self.encoder_joint_proj = nn.Linear(state_dim, hidden_dim)  # project qpos to embedding
            if num_next_action != 0:
                self.encoder_next_action_proj = nn.Linear(state_dim, hidden_dim)  # project action to embedding

            self.latent_proj = nn.Linear(hidden_dim, self.latent_dim*2)  # project hidden state to latent std, var
            self.register_buffer('pos_table', get_sinusoid_encoding_table(1+1+num_next_action+num_queries, hidden_dim))  # [CLS], qpos, a_seq

    def forward(self, image, depth_image, robot_state, next_actions, next_action_is_pad, 
                actions=None, action_is_pad=None, history_qpos=None):
        """
        qpos: batch, qpos_dim
        image: batch, num_cam, channel, height, width
        env_state: None                                   
        actions: batch, seq, action_dim                    
        """

        # print("forward: ", qpos.shape, image.shape, env_state, actions.shape, action_is_pad.shape)

        is_training = actions is not None  # train or val
        bs, _ = robot_state.shape

        # Obtain latent z from action sequence
        if is_training and self.kl_weight != 0:  # hidden_dim512
            action_embed = self.encoder_action_proj(actions)  # (bs, seq, hidden_dim)
            if self.num_next_action != 0 and next_actions is not None:
                next_action_embed = self.encoder_next_action_proj(next_actions)  # (bs, seq, hidden_dim)
            else:
                next_action_embed = None
            robot_state_embed = self.encoder_joint_proj(robot_state)  # (bs, hidden_dim)
            robot_state_embed = torch.unsqueeze(robot_state_embed, axis=1)  # (bs, 1, hidden_dim)
            cls_embed = self.cls_embed.weight  # (1, hidden_dim)
            cls_embed = torch.unsqueeze(cls_embed, axis=0).repeat(bs, 1, 1)  # (bs, 1, hidden_dim)

            if next_actions is not None:
                encoder_input = torch.cat([cls_embed, robot_state_embed, next_action_embed, action_embed], axis=1)
            else:
                encoder_input = torch.cat([cls_embed, robot_state_embed, action_embed], axis=1)  # (bs, seq+1, hidden_dim)
            encoder_input = encoder_input.permute(1, 0, 2)  # (seq+1, bs, hidden_dim)
            cls_joint_is_pad = torch.full((bs, 2), False).to(robot_state.device)  # False: not a padding
            if next_action_is_pad is not None:
                is_pad = torch.cat([cls_joint_is_pad, next_action_is_pad, action_is_pad], axis=1)  # (bs, seq+1)
            else:
                is_pad = torch.cat([cls_joint_is_pad, action_is_pad], axis=1)  # (bs, seq+1)

            # obtain position embedding  
            pos_embed = self.pos_table.clone().detach()
            pos_embed = pos_embed.permute(1, 0, 2)  # (seq+1, 1, hidden_dim)
            encoder_output = self.encoder(encoder_input, pos=pos_embed, src_key_padding_mask=is_pad)
            encoder_output = encoder_output[0]  # take cls output only
            
            #   hidden_dim64
            latent_info = self.latent_proj(encoder_output)
            mu = latent_info[:, :self.latent_dim]
            logvar = latent_info[:, self.latent_dim:]
            latent_sample = reparametrize(mu, logvar)
            latent_input = self.latent_out_proj(latent_sample)
        else:
            mu = logvar = None
            latent_sample = torch.zeros([bs, self.latent_dim], dtype=torch.float32).to(robot_state.device)
            latent_input = self.latent_out_proj(latent_sample)
        # Image observation features and position embeddings
        all_cam_features = []
        all_cam_depth_features = []
        all_cam_pos = []
        for cam_id, cam_name in enumerate(self.camera_names):
            # features, pos = self.backbones[0](image[:, cam_id])  # HARDCODED
            features, src_pos = self.backbones[cam_id](image[:, cam_id]) # HARDCODED
            # image_test = image[:, cam_id][:, 0].unsqueeze(dim=1)
            # print("depth_encoder:", self.depth_encoder(image_test))
            features = features[0]  # take the last layer feature
            src_pos = src_pos[0]
            if self.depth_backbones is not None and depth_image is not None:
                features_depth = self.depth_backbones[cam_id](depth_image[:, cam_id].unsqueeze(dim=1))
                all_cam_features.append(self.input_proj(torch.cat([features, features_depth], axis=1)))
            else:
                all_cam_features.append(self.input_proj(features))
            all_cam_pos.append(src_pos)
            
            # import pdb
            # pdb.set_trace()
            
        # proprioception features
        robot_state_input = self.input_proj_robot_state(robot_state)
        robot_state_input = torch.unsqueeze(robot_state_input, axis=0)
        if self.num_next_action != 0 and next_actions is not None:
            next_action_input = self.input_proj_next_action(next_actions).permute(1, 0, 2)
        else:
            next_action_input = None
        latent_input = torch.unsqueeze(latent_input, axis=0)
        # fold camera dimension into width dimension
        src = torch.cat(all_cam_features, axis=3)
        src_pos = torch.cat(all_cam_pos, axis=3)
        
        # import pdb
        # pdb.set_trace()
        if self.num_next_action != 0 and next_actions is not None:
            hs = self.transformer(self.query_embed.weight,
                                  src, src_pos, None,
                                  robot_state_input, self.robot_state_pos.weight,
                                  next_action_input, self.next_action_pos.weight, next_action_is_pad,
                                  latent_input, self.latent_pos.weight)[0]
        else:
            hs = self.transformer(self.query_embed.weight,
                                  src, src_pos, None,
                                  robot_state_input, self.robot_state_pos.weight,
                                  None, None, None,
                                  latent_input, self.latent_pos.weight)[0]
        a_hat = self.action_head(hs)
        return a_hat, [mu, logvar]