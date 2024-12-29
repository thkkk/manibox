from typing import TYPE_CHECKING

from ..rigid_object import RigidObject

import omni.kit.app
import omni.timeline
import weakref
import re
import torch
import os
import json

import carb
import omni.physics.tensors.impl.api as physx
import omni.isaac.lab.sim as sim_utils

from . import random_rigid_object_data

if TYPE_CHECKING:
    from .random_rigid_object_cfg import RandomRigidObjectCfg

from pxr import UsdPhysics



# class RandomRigidObject(RigidObject):
#     def __init__(self, cfg: "RandomRigidObjectCfg", num_envs: int):
#         ########
#         ### rigid object part
#         ########
        
#         carb.log_warn(f"RandomRigidObject num_envs: {num_envs}")
        
#         self._root_physx_view = None
#         self._device = "cpu"
#         self._data = random_rigid_object_data.RandomRigidObjectData(self.root_physx_view, self.device)
#         self._data.root_scales = torch.zeros((num_envs, 3), dtype=torch.float, device="cpu")
        
#         ########
#         ### asset base part
#         ########
#         self.cfg = cfg
#         # flag for whether the asset is initialized
#         self._is_initialized = False

#         # check if base asset path is valid
#         # note: currently the spawner does not work if there is a regex pattern in the leaf
#         #   For example, if the prim path is "/World/Robot_[1,2]" since the spawner will not
#         #   know which prim to spawn. This is a limitation of the spawner and not the asset.
#         asset_path = self.cfg.prim_path.split("/")[-1]
#         asset_path_is_regex = re.match(r"^[a-zA-Z0-9/_]+$", asset_path) is None
#         # spawn the asset
#         if self.cfg.spawn is not None and not asset_path_is_regex:
#             for env_id in range(num_envs):
#                 spawned_prim, extras = self.cfg.spawn.func(
#                     self.cfg.prim_path.replace("env_.*", f"env_{env_id}"),
#                     self.cfg.spawn,
#                     translation=self.cfg.init_state.pos,
#                     orientation=self.cfg.init_state.rot,
#                     chosen_index=env_id % len(self.cfg.spawn.usd_paths), # check obj size and test on table
#                 )
#                 self._data.root_scales[env_id, :] = torch.tensor(extras["chosen_scale"], dtype=torch.float, device="cpu")
#         # check that spawn was successful
#         matching_prims = sim_utils.find_matching_prims(self.cfg.prim_path)
#         if len(matching_prims) == 0:
#             raise RuntimeError(f"Could not find prim with path {self.cfg.prim_path}.")

#         # note: Use weakref on all callbacks to ensure that this object can be deleted when its destructor is called.
#         # add callbacks for stage play/stop
#         # The order is set to 10 which is arbitrary but should be lower priority than the default order of 0
#         timeline_event_stream = omni.timeline.get_timeline_interface().get_timeline_event_stream()
#         self._initialize_handle = timeline_event_stream.create_subscription_to_pop_by_type(
#             int(omni.timeline.TimelineEventType.PLAY),
#             lambda event, obj=weakref.proxy(self): obj._initialize_callback(event),
#             order=10,
#         )
#         self._invalidate_initialize_handle = timeline_event_stream.create_subscription_to_pop_by_type(
#             int(omni.timeline.TimelineEventType.STOP),
#             lambda event, obj=weakref.proxy(self): obj._invalidate_initialize_callback(event),
#             order=10,
#         )
#         # add handle for debug visualization (this is set to a valid handle inside set_debug_vis)
#         self._debug_vis_handle = None
#         # set initial state of debug visualization
#         self.set_debug_vis(self.cfg.debug_vis)


#     def _initialize_callback(self, event):
#         """Initializes the scene elements.

#         Note:
#             PhysX handles are only enabled once the simulator starts playing. Hence, this function needs to be
#             called whenever the simulator "plays" from a "stop" state.
#         """
#         if not self._is_initialized:
#             # obtain simulation related information
#             sim = sim_utils.SimulationContext.instance()
#             if sim is None:
#                 raise RuntimeError("SimulationContext is not initialized! Please initialize SimulationContext first.")
#             self._backend = sim.backend
#             self._device = sim.device
#             # initialize the asset
#             self._initialize_impl()
#             # set flag
#             self._is_initialized = True
            
#             # initialize the data
#             if self._data.root_scales is not None:
#                 self._data.root_scales = self._data.root_scales.to(self.device)

#     @property
#     def data(self) -> random_rigid_object_data.RandomRigidObjectData:
#         return self._data

#     def _initialize_impl(self):
#         # create simulation view
#         self._physics_sim_view = physx.create_simulation_view(self._backend)
#         self._physics_sim_view.set_subspace_roots("/")
#         # obtain the first prim in the regex expression (all others are assumed to be a copy of this)
#         template_prim = sim_utils.find_first_matching_prim(self.cfg.prim_path)
#         if template_prim is None:
#             raise RuntimeError(f"Failed to find prim for expression: '{self.cfg.prim_path}'.")
#         template_prim_path = template_prim.GetPath().pathString
#         # find rigid root prims
#         root_prims = sim_utils.get_all_matching_child_prims(
#             template_prim_path, predicate=lambda prim: prim.HasAPI(UsdPhysics.RigidBodyAPI)
#         )
#         if len(root_prims) != 1:
#             raise RuntimeError(
#                 f"Failed to find a single rigid body when resolving '{self.cfg.prim_path}'."
#                 f" Found multiple '{root_prims}' under '{template_prim_path}'."
#             )
#         # resolve root prim back into regex expression
#         root_prim_path = root_prims[0].GetPath().pathString
#         root_prim_path_expr = self.cfg.prim_path + root_prim_path[len(template_prim_path) :]
#         # -- object view
#         self._root_physx_view = self._physics_sim_view.create_rigid_body_view(root_prim_path_expr.replace(".*", "*"))
        
#         # carb.log_warn(f"RigidObject num_instances: {self.num_instances}, " + root_prim_path_expr.replace(".*", "*"))
#         # carb.log_warn(f"RigidObject self._root_physx_view.prim_paths: {len(self._root_physx_view.prim_paths)}")
#         # from pprint import pprint
        
#         if "Table" not in self._root_physx_view.prim_paths[0]:
#             with open("./tmp.log", "w") as f:
#                 json.dump(list(zip(self._root_physx_view.prim_paths, self.cfg.spawn.usd_paths)), f, indent=4)
        
#         self._body_physx_view = self._root_physx_view
#         # log information about the articulation
#         carb.log_info(f"Rigid body initialized at: {self.cfg.prim_path} with root '{root_prim_path_expr}'.")
#         carb.log_info(f"Number of instances: {self.num_instances}")
#         carb.log_info(f"Number of bodies: {self.num_bodies}")
#         carb.log_info(f"Body names: {self.body_names}")

#         # create buffers
#         self._create_buffers()
#         # process configuration
#         self._process_cfg()

class RandomRigidObject(RigidObject):
    def __init__(self, cfg: "RandomRigidObjectCfg", num_envs: int):
        ########
        ### rigid object part
        ########

        carb.log_warn(f"RandomRigidObject num_envs: {num_envs}")

        # 初始化 device 和 root_physx_view 为 None 和 "cpu"
        self._root_physx_view = None
        self._device = "cpu"  # 这将在 _initialize_impl 中根据仿真上下文更新
        
        self._num_envs = num_envs

        ########
        ### asset base part
        ########
        self.cfg = cfg
        # 标志资产是否已初始化
        self._is_initialized = False

        # 检查基础资产路径是否有效
        # 注意：目前，如果叶节点中有正则表达式模式，生成器不起作用
        # 例如，如果原语路径是 "/World/Robot_[1,2]"，因为生成器将不知道生成哪个原语。这是生成器的限制，而不是资产的限制。
        asset_path = self.cfg.prim_path.split("/")[-1]
        asset_path_is_regex = re.match(r"^[a-zA-Z0-9/_]+$", asset_path) is None
        # 生成资产
        if self.cfg.spawn is not None and not asset_path_is_regex:
            for env_id in range(num_envs):
                spawned_prim, extras = self.cfg.spawn.func(
                    self.cfg.prim_path.replace("env_.*", f"env_{env_id}"),
                    self.cfg.spawn,
                    translation=self.cfg.init_state.pos,
                    orientation=self.cfg.init_state.rot,
                    chosen_index=env_id % len(self.cfg.spawn.usd_paths),  # 检查 obj 大小并在桌子上测试
                )

        # 检查生成是否成功
        matching_prims = sim_utils.find_matching_prims(self.cfg.prim_path)
        if len(matching_prims) == 0:
            raise RuntimeError(f"Could not find prim with path {self.cfg.prim_path}.")

        # 注意：在所有回调上使用 weakref 确保在调用其析构函数时可以删除此对象。
        # 为阶段播放/停止添加回调
        # 订单设置为 10 是任意的，但优先级应低于默认的 0
        timeline_event_stream = omni.timeline.get_timeline_interface().get_timeline_event_stream()
        self._initialize_handle = timeline_event_stream.create_subscription_to_pop_by_type(
            int(omni.timeline.TimelineEventType.PLAY),
            lambda event, obj=weakref.proxy(self): obj._initialize_callback(event),
            order=10,
        )
        self._invalidate_initialize_handle = timeline_event_stream.create_subscription_to_pop_by_type(
            int(omni.timeline.TimelineEventType.STOP),
            lambda event, obj=weakref.proxy(self): obj._invalidate_initialize_callback(event),
            order=10,
        )
        # 为调试可视化添加句柄（在 set_debug_vis 中设置为有效句柄）
        self._debug_vis_handle = None
        # 设置调试可视化的初始状态
        self.set_debug_vis(self.cfg.debug_vis)


    def _initialize_callback(self, event):
        """初始化场景元素。

        注意：
            物理引擎句柄仅在模拟器开始播放时启用。因此，每当模拟器从“停止”状态“播放”时，都需要调用此函数。
        """
        if not self._is_initialized:
            # 获取与模拟相关的信息
            sim = sim_utils.SimulationContext.instance()
            if sim is None:
                raise RuntimeError("SimulationContext is not initialized! Please initialize SimulationContext first.")
            self._backend = sim.backend
            self._device = sim.device
            # 初始化资产
            self._initialize_impl()
            # 设置标志
            self._is_initialized = True

            # 初始化数据
            if self._data.root_scales is not None:
                self._data.root_scales = self._data.root_scales.to(self.device)

    @property
    def data(self) -> random_rigid_object_data.RandomRigidObjectData:
        return self._data

    def _initialize_impl(self):
        # 创建模拟视图
        self._physics_sim_view = physx.create_simulation_view(self._backend)
        self._physics_sim_view.set_subspace_roots("/")
        # 获取正则表达式中的第一个原语（所有其他的假定是它的副本）
        template_prim = sim_utils.find_first_matching_prim(self.cfg.prim_path)
        if template_prim is None:
            raise RuntimeError(f"Failed to find prim for expression: '{self.cfg.prim_path}'.")
        template_prim_path = template_prim.GetPath().pathString
        # 查找刚体根原语
        root_prims = sim_utils.get_all_matching_child_prims(
            template_prim_path, predicate=lambda prim: prim.HasAPI(UsdPhysics.RigidBodyAPI)
        )
        if len(root_prims) != 1:
            raise RuntimeError(
                f"Failed to find a single rigid body when resolving '{self.cfg.prim_path}'."
                f" Found multiple '{root_prims}' under '{template_prim_path}'."
            )
        # 将根原语解析回正则表达式
        root_prim_path = root_prims[0].GetPath().pathString
        root_prim_path_expr = self.cfg.prim_path + root_prim_path[len(template_prim_path) :]
        # -- 对象视图
        self._root_physx_view = self._physics_sim_view.create_rigid_body_view(root_prim_path_expr.replace(".*", "*"))

        # 在这里初始化数据对象，确保 root_physx_view 和 device 已正确设置
        self._data = random_rigid_object_data.RandomRigidObjectData(self.root_physx_view, self.device)
        self._data.root_scales = torch.zeros((self._num_envs, 3), dtype=torch.float, device=self.device)

        if "Table" not in self._root_physx_view.prim_paths[0]:
            with open("./tmp.log", "w") as f:
                json.dump(list(zip(self._root_physx_view.prim_paths, self.cfg.spawn.usd_paths)), f, indent=4)

        self._body_physx_view = self._root_physx_view
        # 记录关于关节的信息
        carb.log_info(f"Rigid body initialized at: {self.cfg.prim_path} with root '{root_prim_path_expr}'.")
        carb.log_info(f"Number of instances: {self.num_instances}")
        carb.log_info(f"Number of bodies: {self.num_bodies}")
        carb.log_info(f"Body names: {self.body_names}")

        # 创建缓冲区
        self._create_buffers()
        # 处理配置
        self._process_cfg()


        