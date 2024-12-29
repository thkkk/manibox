from __future__ import annotations

import torch
import torch.nn as nn
from torch.distributions import Normal

from rsl_rl.modules.actor_critic import BaseActorCritic, ActorCritic

class MultiActorCritic(BaseActorCritic):
    def __init__(self, num_actor_obs, num_critic_obs, num_actions, num_actors = 1, max_low_count = 30, **kwargs) -> None:
        super().__init__()
        self.num_actors = num_actors
        self.max_low_count = max_low_count
        self.num_actions = num_actions
        self.actor_critics = nn.ModuleList([ActorCritic(num_actor_obs, num_critic_obs, num_actions, **kwargs) for _ in range(self.num_actors)])
        self.stable_count = 0
        self.register_buffer("reward", torch.zeros(self.num_actors))
        self.register_buffer("low_count", torch.zeros(self.num_actors, dtype=torch.long))
    
    def get_ac_id(self, batch_size):
        # split batch size to num_actors
        ac_id = torch.zeros(batch_size, dtype=torch.long)
        for i in range(self.num_actors):
            ac_id[i::self.num_actors] = i
        return ac_id
    
    def update_distribution(self, observations: torch.Tensor, ac_id: torch.Tensor = None):
        if ac_id is None:
            ac_id = torch.zeros(observations.shape[0], dtype=torch.long, device=observations.device)
        mean = torch.zeros(observations.shape[0], self.num_actions, device=observations.device)
        std = torch.zeros(observations.shape[0], self.num_actions, device=observations.device)
        for i in range(self.num_actors):
            mask = ac_id == i
            ac: ActorCritic = self.actor_critics[i]
            if mask.any():
                ac.update_distribution(observations[mask])
                mean[mask] = ac.action_mean
                std[mask] = ac.action_std
        self.distribution = Normal(mean, std)

    def act(self, observations: torch.Tensor, ac_id: torch.Tensor = None, **kwargs):
        self.update_distribution(observations, ac_id)
        return self.distribution.sample()
    
    def evaluate(self, critic_observations, ac_id: torch.Tensor = None, **kwargs):
        if ac_id is None:
            ac_id = torch.zeros(critic_observations.shape[0], dtype=torch.long, device=critic_observations.device)
        value = torch.zeros(critic_observations.shape[0], 1, device=critic_observations.device)
        for i in range(self.num_actors):
            mask = ac_id == i
            ac: ActorCritic = self.actor_critics[i]
            if mask.any():
                value[mask] = ac.evaluate(critic_observations[mask])
        return value
    
    def update_reward(self, reward: torch.Tensor):
        if self.num_actors == 1:
            return
        
        self.reward = reward
        max_actor = self.reward.argmax()
        mask = self.reward < self.reward[max_actor]
        self.low_count[mask] += 1
        self.low_count[~mask] = 0

        print(self.low_count)
        print(self.reward)

        for i in range(self.num_actors):
            if self.low_count[i] > self.max_low_count:
                # reset this network
                self.actor_critics[i].load_state_dict(self.actor_critics[max_actor].state_dict())
                self.low_count[i] = 0
                break
        
    @property
    def actor(self):
        return self.actor_critics[0].actor

    @property
    def mean_noise_std(self):
        return torch.stack([ac.mean_noise_std for ac in self.actor_critics]).mean()