from typing import Sequence

from omni.isaac.lab.envs import ManagerBasedEnv

import builtins
import torch
from pprint import pprint

from omni.isaac.lab.envs.common import VecEnvStepReturn

import carb

from omni.isaac.lab.managers import ActionManager, ObservationManager, RandomizationManager
from omni.isaac.lab.scene import InteractiveScene, CloneDiffScene, CloneDiffSceneCfg
from omni.isaac.lab.sim import SimulationContext
from omni.isaac.lab.utils.timer import Timer
from omni.isaac.lab.envs.ui import ViewportCameraController


from .manager_based_rl_env import ManagerBasedRLEnv, ManagerBasedRLEnvCfg

from omni.isaac.lab.managers import RewardManager, CommandManager, TerminationManager, ObservationManager, \
    CurriculumManager, RandomizationManager, ActionManager


def nan_to_num(x: dict | torch.Tensor):
    if isinstance(x, dict):
        for k, v in x.items():
            x[k] = nan_to_num(v)
    elif isinstance(x, torch.Tensor):
        x = torch.nan_to_num(x, nan=0, posinf=0, neginf=0)
    else:
        raise ValueError("x should be either dict or torch.Tensor")
    return x

def replace_nan_inf_with_random(tensor):
    nan_mask = torch.isnan(tensor) | torch.isinf(tensor)
    random_values = torch.randn(nan_mask.sum(), device=tensor.device)
    new_tensor = tensor.clone()
    new_tensor[nan_mask] = random_values
    
    return new_tensor

def nan_inf_to_randn(x: dict | torch.Tensor):
    if isinstance(x, dict):
        for k, v in x.items():
            x[k] = nan_inf_to_randn(v)
    elif isinstance(x, torch.Tensor):
        x = replace_nan_inf_with_random(x)
    else:
        raise ValueError("x should be either dict or torch.Tensor")
    return x

class NoNanObservationManager(ObservationManager):
    def __init__(self, cfg: object, env: ManagerBasedRLEnv):
        super().__init__(cfg, env)
        self._episode_sums = dict()
        
        for group_name, group_dim in self._group_obs_dim.items():
            obs_terms = zip(
                self._group_obs_term_names[group_name],
                self._group_obs_term_dim[group_name],
            )
            for index, (name, dims) in enumerate(obs_terms):
                if sum(dims) > 0:
                    self._episode_sums[name] = torch.zeros(self.num_envs, sum(dims), dtype=torch.float, device=self.device)
    
    def compute_group(self, group_name: str) -> torch.Tensor | dict[str, torch.Tensor]:
        # check ig group name is valid
        if group_name not in self._group_obs_term_names:
            raise ValueError(
                f"Unable to find the group '{group_name}' in the observation manager."
                f" Available groups are: {list(self._group_obs_term_names.keys())}"
            )
        # iterate over all the terms in each group
        group_term_names = self._group_obs_term_names[group_name]
        # buffer to store obs per group
        group_obs = dict.fromkeys(group_term_names, None)
        # read attributes for each term
        obs_terms = zip(group_term_names, self._group_obs_term_cfgs[group_name])
        # evaluate terms: compute, add noise, clip, scale.
        for name, term_cfg in obs_terms:
            # compute term's value
            obs: torch.Tensor = term_cfg.func(self._env, **term_cfg.params)
            # apply post-processing
            if term_cfg.noise:
                obs = term_cfg.noise.func(obs, term_cfg.noise)
            if term_cfg.clip:
                obs = obs.clip_(min=term_cfg.clip[0], max=term_cfg.clip[1])
            if term_cfg.scale:
                obs = obs.mul_(term_cfg.scale)
            # TODO: Introduce delay and filtering models.
            # Ref: https://robosuite.ai/docs/modules/sensors.html#observables
            # add value to list
            group_obs[name] = obs
        # concatenate all observations in the group together
        if self._group_obs_concatenate[group_name]:
            return torch.cat(list(group_obs.values()), dim=-1), group_obs
        else:
            return group_obs
    
    def compute(self) -> dict[str, torch.Tensor | dict[str, torch.Tensor]]:
        """Compute the observations per group for all groups.

        The method computes the observations for all the groups handled by the observation manager.
        Please check the :meth:`compute_group` on the processing of observations per group.

        Returns:
            A dictionary with keys as the group names and values as the computed observations.
        """
        # create a buffer for storing obs from all the groups
        obs_buffer = dict()
        # iterate over all the terms in each group
        for group_name in self._group_obs_term_names:
            group_cat, group_obs = self.compute_group(group_name)
            obs_buffer[group_name] = nan_inf_to_randn(group_cat)
            
            for name, obs in group_obs.items():
                if name in self._episode_sums:
                    self._episode_sums[name] += obs
        # otherwise return a dict with observations of all groups
        return obs_buffer
    
    def reset(self, env_ids: Sequence[int] | None = None) -> dict[str, float]:
        extras = {}
        
        # for key in self._episode_sums.keys():
        #     # store information
        #     # r_1 + r_2 + ... + r_n
        #     episodic_sum_avg = torch.mean(self._episode_sums[key][env_ids, :], dim=0)
        #     for index in range(episodic_sum_avg.shape[0]):
        #         extras[f"Episode Observation {key}/{str(index)}"] = episodic_sum_avg[index] / self._env.max_episode_length_s
        #     # reset episodic sum
        #     self._episode_sums[key][env_ids, :] = 0.0
        
        # call all terms that are classes
        for group_cfg in self._group_obs_class_term_cfgs.values():
            for term_cfg in group_cfg:
                term_cfg.func.reset(env_ids=env_ids)
        
        return extras


class NoNanRewardManager(RewardManager):
    def __init__(self, cfg: object, env: ManagerBasedRLEnv):
        super().__init__(cfg, env)
        
        # self._rew_overall_factor = 0.1
    
    def compute(self, dt: float) -> torch.Tensor:
        """Computes the reward signal as a weighted sum of individual terms.

        This function calls each reward term managed by the class and adds them to compute the net
        reward signal. It also updates the episodic sums corresponding to individual reward terms.

        Args:
            dt: The time-step interval of the environment.

        Returns:
            The net reward signal of shape (num_envs,).
        """
        # reset computation
        self._reward_buf[:] = 0.0
        # iterate over all the reward terms
        for name, term_cfg in zip(self._term_names, self._term_cfgs):
            # skip if weight is zero (kind of a micro-optimization)
            if term_cfg.weight == 0.0:
                continue
            # compute term's value
            # value = nan_inf_to_randn(term_cfg.func(self._env, **term_cfg.params)) * term_cfg.weight * dt * self._rew_overall_factor
            value = nan_inf_to_randn(term_cfg.func(self._env, **term_cfg.params)) * term_cfg.weight * dt
            # update total reward
            self._reward_buf += value
            # update episodic sum
            self._episode_sums[name] += value
        
        return self._reward_buf


class LogActionManager(ActionManager):
    def __init__(self, cfg: object, env: ManagerBasedEnv):
        super().__init__(cfg, env)
        self._episode_sums = dict()
        
        for index, (name, term) in enumerate(self._terms.items()):
            self._episode_sums[name] = torch.zeros(self.num_envs, term.action_dim, dtype=torch.float, device=self.device)

    def process_action(self, action: torch.Tensor):
        # check if action dimension is valid
        if self.total_action_dim != action.shape[1]:
            raise ValueError(f"Invalid action shape, expected: {self.total_action_dim}, received: {action.shape[1]}.")
        # store the input actions
        self._prev_action[:] = self._action
        self._action[:] = action.to(self.device)

        # split the actions and apply to each tensor
        idx = 0
        for term_name, term in self._terms.items():
            term_actions = action[:, idx : idx + term.action_dim]
            term.process_actions(term_actions)
            idx += term.action_dim
            
            self._episode_sums[term_name] += term_actions

    def reset(self, env_ids: Sequence[int] | None = None) -> dict[str, torch.Tensor]:
        extras = {}
        
        # for key in self._episode_sums.keys():
        #     # store information
        #     # r_1 + r_2 + ... + r_n
        #     episodic_sum_avg = torch.mean(self._episode_sums[key][env_ids, :], dim=0)
        #     for index in range(episodic_sum_avg.shape[0]):
        #         extras[f"Episode Action {key}/{str(index)}"] = episodic_sum_avg[index] / self._env.max_episode_length_s
        #     # reset episodic sum
        #     self._episode_sums[key][env_ids, :] = 0.0
        
        # resolve environment ids
        if env_ids is None:
            env_ids = slice(None)
        # reset the action history
        self._prev_action[env_ids] = 0.0
        self._action[env_ids] = 0.0
        # reset all action terms
        for term in self._terms.values():
            term.reset(env_ids=env_ids)

        return extras


class NoNanManagerBasedRLEnv(ManagerBasedRLEnv):
    def __init__(self, cfg: ManagerBasedRLEnvCfg, render_mode: str | None = None, **kwargs):
        ########
        ### ManagerBasedEnv part
        ########
        
        # store inputs to class
        self.cfg = cfg
        # initialize internal variables
        self._is_closed = False

        # create a simulation context to control the simulator
        if SimulationContext.instance() is None:
            self.sim = SimulationContext(self.cfg.sim)
        else:
            raise RuntimeError("Simulation context already exists. Cannot create a new one.")

        # print useful information
        print("[INFO]: Base environment:")
        print(f"\tEnvironment device    : {self.device}")
        print(f"\tPhysics step-size     : {self.physics_dt}")
        # print(f"\tRendering step-size   : {self.physics_dt * self.cfg.sim.substeps}")
        print(f"\tEnvironment step-size : {self.step_dt}")
        print(f"\tPhysics GPU pipeline  : {self.cfg.sim.use_gpu_pipeline}")
        print(f"\tPhysics GPU simulation: {self.cfg.sim.physx.use_gpu}")

        # generate scene
        with Timer("[INFO]: Time taken for scene creation"):
            self.scene = CloneDiffScene(self.cfg.scene)
            # self.scene = InteractiveScene(self.cfg.scene)
        print("[INFO]: Scene manager: ", self.scene)

        # set up camera viewport controller
        # viewport is not available in other rendering modes so the function will throw a warning
        # FIXME: This needs to be fixed in the future when we unify the UI functionalities even for
        # non-rendering modes.
        if self.sim.render_mode >= self.sim.RenderMode.PARTIAL_RENDERING:
            self.viewport_camera_controller = ViewportCameraController(self, self.cfg.viewer)
        else:
            self.viewport_camera_controller = None

        # play the simulator to activate physics handles
        # note: this activates the physics simulation view that exposes TensorAPIs
        # note: when started in extension mode, first call sim.reset_async() and then initialize the managers
        if builtins.ISAAC_LAUNCHED_FROM_TERMINAL is False:
            print("[INFO]: Starting the simulation. This may take a few seconds. Please wait...")
            with Timer("[INFO]: Time taken for simulation start"):
                self.sim.reset()
            # add timeline event to load managers
            self.load_managers()

        # extend UI elements
        # we need to do this here after all the managers are initialized
        # this is because they dictate the sensors and commands right now
        if self.sim.has_gui() and self.cfg.ui_window_class_type is not None:
            self._window = self.cfg.ui_window_class_type(self, window_name="lab")
        else:
            # if no window, then we don't need to store the window
            self._window = None

        # allocate dictionary to store metrics
        self.extras = {}
    
        ########
        ### RLEnv part
        ########
        
        self.render_mode = render_mode

        # initialize data and constants
        # -- counter for curriculum
        self.common_step_counter = 0
        # -- init buffers
        self.episode_length_buf = torch.zeros(self.num_envs, device=self.device, dtype=torch.long)

        # setup the action and observation spaces for Gym
        self._configure_gym_env_spaces()
        # perform randomization at the start of the simulation
        if "startup" in self.event_manager.available_modes:
            self.event_manager.apply(mode="startup")
        # print the environment information
        print("[INFO]: Completed setting up the environment...")


    def load_managers(self):
        # prepare the managers
        
        # -- command manager
        self.command_manager: CommandManager = CommandManager(self.cfg.commands, self)
        print("[INFO] Command Manager: ", self.command_manager)
        
        # -- action manager
        self.action_manager = LogActionManager(self.cfg.actions, self)
        print("[INFO] Action Manager: ", self.action_manager)
        
        # -- observation manager
        self.observation_manager = NoNanObservationManager(self.cfg.observations, self)
        print("[INFO] NoNanObservation Manager:", self.observation_manager)
        
        # -- randomization manager
        self.event_manager = RandomizationManager(self.cfg.randomization, self)
        print("[INFO] Event Manager: ", self.event_manager)
        
        # -- reward manager
        self.reward_manager = NoNanRewardManager(self.cfg.rewards, self)
        print("[INFO] NoNanReward Manager: ", self.reward_manager)
        
        # -- termination manager
        self.termination_manager = TerminationManager(self.cfg.terminations, self)
        print("[INFO] Termination Manager: ", self.termination_manager)
        
        # -- curriculum manager
        self.curriculum_manager = CurriculumManager(self.cfg.curriculum, self)
        print("[INFO] Curriculum Manager: ", self.curriculum_manager)
    
    def step(self, action: torch.Tensor) -> VecEnvStepReturn:
        # process actions
        self.action_manager.process_action(action)
        # perform physics stepping
        for _ in range(self.cfg.decimation):
            # set actions into buffers
            self.action_manager.apply_action()
            # set actions into simulator
            self.scene.write_data_to_sim()
            # simulate
            self.sim.step(render=False)
            # update buffers at sim dt
            self.scene.update(dt=self.physics_dt)
        # perform rendering if gui is enabled
        if self.sim.has_gui():
            self.sim.render()

        # post-step:
        # -- update env counters (used for curriculum generation)
        self.episode_length_buf += 1  # step in current episode (per env)
        self.common_step_counter += 1  # total step (common for all envs)
        # -- check terminations
        self.reset_buf = self.termination_manager.compute()
        self.reset_terminated = self.termination_manager.terminated
        self.reset_time_outs = self.termination_manager.time_outs
        # -- reward computation
        self.reward_buf = self.reward_manager.compute(dt=self.step_dt)

        # -- reset envs that terminated/timed-out and log the episode information
        reset_env_ids = self.reset_buf.nonzero(as_tuple=False).squeeze(-1)
        if len(reset_env_ids) > 0:
            self._reset_idx(reset_env_ids)
        # -- update command
        self.command_manager.compute(dt=self.step_dt)
        # -- step interval randomization
        if "interval" in self.event_manager.available_modes:
            self.event_manager.apply(mode="interval", dt=self.step_dt)
        # -- compute observations
        # note: done after reset to get the correct observations for reset envs
        self.obs_buf = self.observation_manager.compute()
        
        # obs_tensor: torch.Tensor = self.obs_buf["policy"]
        # # if torch.sum(obs_tensor.isnan()) > 0:
        # print("[WARNING] nan in obs_buf")
        # pprint(str(obs_tensor.tolist()))

        # return observations, rewards, resets and extras
        return self.obs_buf, self.reward_buf, self.reset_terminated, self.reset_time_outs, self.extras