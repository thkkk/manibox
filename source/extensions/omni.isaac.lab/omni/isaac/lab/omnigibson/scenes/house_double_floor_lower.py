from __future__ import annotations

from dataclasses import MISSING

# import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg, OmniGibsonObjectCfg
# from omni.isaac.lab.envs import RLTaskEnvCfg
# from omni.isaac.lab.managers import CurriculumTermCfg as CurrTerm
# from omni.isaac.lab.managers import ObservationGroupCfg as ObsGroup
# from omni.isaac.lab.managers import ObservationTermCfg as ObsTerm
# from omni.isaac.lab.managers import RandomizationTermCfg as RandTerm
# from omni.isaac.lab.managers import RewardTermCfg as RewTerm
# from omni.isaac.lab.managers import SceneEntityCfg
# from omni.isaac.lab.managers import TerminationTermCfg as DoneTerm
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import FrameTransformerCfg
from omni.isaac.lab.sim.spawners.from_files.from_files_cfg import GroundPlaneCfg, UsdFileCfg, OmniGibsonUsdFileCfg
from omni.isaac.lab.utils import configclass
# from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR
from omni.isaac.lab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg

# from omni.isaac.lab.sensors import CameraCfg
# from omni.isaac.lab.scene import InteractiveScene

# from omni.isaac.lab_tasks.manipulation.lift import x_scene_object_offset, y_scene_object_offset

import os
import json
@configclass
class houseDoubleFloorLowerquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/house_double_floor_lower/usd/house_double_floor_lower_quick.usd"),
        )
    )
@configclass
class houseDoubleFloorLowerfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/house_double_floor_lower/usd/house_double_floor_lower_quick.usd"),
        )
    )
    bushCwsigt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.309932003611086, -3.0563852125552153, 0.21787312781990448),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.137619503611086, -3.686838337555215, 0.21787312781990448),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.967835437985326, -2.8315068265904446, 0.21787312781990448),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.805499115490395, 14.304633284693198, 0.41204500281990447),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.457202240490389, 15.742340315943197, 0.4459200028199045),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.47276278736039, 15.066285628443199, 0.44592000281990446),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.748868880173331, 14.890145704982894, 0.44592000281990446),
            rot=(0.4226183289610028, 0.0, 0.0, 0.9063077556913047),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.7012947714920936, -3.1027264863150608, 0.21787312781990448),
            rot=(0.9396926168497417, 0.0, 0.0, -0.3420201541401976),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.227132367539839, -3.816257796417879, 0.2178731278199045),
            rot=(0.9396926168497417, 0.0, 0.0, -0.3420201541401976),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.08637888967637, -3.0896210480748683, 0.21787312781990448),
            rot=(0.9990482219507036, 0.0, 0.0, 0.04361937891737566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.202367980547387, -3.9031917359381185, 0.2178731278199045),
            rot=(0.9914448617030149, 0.0, 0.0, -0.13052618971949495),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.230740219655925, -3.7464023192725304, 0.2178731278199045),
            rot=(0.9990482219507036, 0.0, 0.0, 0.04361937891737566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.961774157060441, -3.71669921546976, 0.2178731278199045),
            rot=(0.9990482219507036, 0.0, 0.0, 0.04361937891737566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.226040188464532, -2.983616431007002, 0.21787312781990445),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushCwsigt9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.6754194223553265, -3.2170380765904447, 0.2178731278199045),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.35597500472743, 0.3559921538822102, 0.3559795742447996),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.07323889425745, 15.330465925327436, 0.40207269479166186),
            rot=(0.9961946976610734, 0.0, 0.0, 0.08715574767026325),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.7579891734261925, 0.7580121348963498, 0.7579734682276364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.90650451925745, 14.895669050327438, 0.4020726947916618),
            rot=(0.9961946976610734, 0.0, 0.0, 0.08715574767026325),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.7579891734261925, 0.7580121348963498, 0.7579734682276364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.782559206757448, 14.312762800327436, 0.4020726947916618),
            rot=(0.9961946976610734, 0.0, 0.0, 0.08715574767026325),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.7579891734261925, 0.7580121348963498, 0.7579734682276364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.164606081757448, 13.750981550327436, 0.4020726947916618),
            rot=(0.9961946976610734, 0.0, 0.0, 0.08715574767026325),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.7579891734261925, 0.7580121348963498, 0.7579734682276364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.439331602800662, 14.284735481782498, 0.40207269479166186),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.7579891734261925, 0.7580121348963498, 0.7579734682276364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushFrqici0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushFrqici0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.758735447468872, 9.862234142927454, 0.985636916608419),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.33737424426337964, 0.3373841531927589, 0.33737380790989674),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushFrqici1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushFrqici1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.027298679888874, 13.455773205427453, 0.985636916608419),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.33737424426337964, 0.3373841531927589, 0.33737380790989674),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushFrqici2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushFrqici2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2988921857488736, 15.796577892927454, 0.9856369166084189),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.33737424426337964, 0.3373841531927589, 0.33737380790989674),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushFrqici3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushFrqici3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.242819240036125, 0.4882162596224531, 0.985636916608419),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.33737424426337964, 0.3373841531927589, 0.33737380790989674),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushFrqici4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushFrqici4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.850188572468873, -3.3603072389125472, 0.9856369166084191),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.33737424426337964, 0.3373841531927589, 0.33737380790989674),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKjakgd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKjakgd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.703477723538875, -3.291834986027931, 2.0558624348615444),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kjakgd/usd/kjakgd.usd"),
            visual_material_path="materials",
            scale=(0.46275203365221507, 0.46274264549807553, 0.46275040410705687),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKjakgd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKjakgd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.769996297968855, -3.5569610307844224, 2.0558624348615444),
            rot=(0.7660444283313821, 0.0, 0.0, -0.6427876273097095),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kjakgd/usd/kjakgd.usd"),
            visual_material_path="materials",
            scale=(0.46275203365221507, 0.46274264549807553, 0.46275040410705687),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5200528427898092, -3.211221664543157, 0.252044813903061),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.711075150210459, 0.7110503447398733, 0.7110764997948243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.599127046281057, -3.128002940972088, 0.25204481390306105),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.711075150210459, 0.7110503447398733, 0.7110764997948243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.925740327531058, -3.5986123159720886, 0.252044813903061),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.711075150210459, 0.7110503447398733, 0.7110764997948243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.483966462786066, -2.894784085256363, 0.252044813903061),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.711075150210459, 0.7110503447398733, 0.7110764997948243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.084032869036065, -3.583034085256361, 0.252044813903061),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.711075150210459, 0.7110503447398733, 0.7110764997948243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.486013337786066, -2.9638465852563622, 0.25204481390306105),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.711075150210459, 0.7110503447398733, 0.7110764997948243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.670629020047078, -2.0950729526555665, 0.37075933340174755),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.879707145047076, -2.000932327655567, 0.37075933340174755),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.005314784399497, -2.1172352936697516, 0.3707593334017476),
            rot=(0.923879611244086, 0.0, 0.0, 0.38268324228724265),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.021189784399497, -2.1722196686697504, 0.1769858978117475),
            rot=(0.923879611244086, 0.0, 0.0, 0.38268324228724265),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.041856417413037, -2.1108734610913187, 0.3707593334017475),
            rot=(0.17364831259951158, 0.0, 0.0, 0.9848077292199439),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.0507021348175347, -2.192154671858751, 0.3707593334017475),
            rot=(0.17364831259951158, 0.0, 0.0, 0.9848077292199439),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.612599930041013, -2.1862550237338265, 0.3707593334017476),
            rot=(0.9659258595418148, 0.0, 0.0, 0.2588189210015495),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.238264762237076, -2.1379948276556093, 0.37075933340174755),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKyghri8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKyghri8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.20728059707629, -2.092863622402319, 0.37075933340174755),
            rot=(0.9914448539896045, 0.0, 0.0, -0.130526248308652),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.5210901537373535, 0.5210830902621125, 0.5210502783264743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.51816550463563, 0.8348048727478765, 0.4482394327041673),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.260203059690404, 0.7563336404784752, 0.44823943270416733),
            rot=(0.9537169346918781, 0.0, 0.0, -0.30070585042850073),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.046333029977391, 0.7652434283828529, 0.4482394327041673),
            rot=(-0.5735763596999339, 0.0, 0.0, 0.819152097960673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.830375984015583, -0.49171354718681104, 0.44823943270416716),
            rot=(-0.5735763596999339, 0.0, 0.0, 0.819152097960673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.958502799635077, 14.836938566525728, 0.4482394327041673),
            rot=(-0.5735763596999339, 0.0, 0.0, 0.819152097960673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.425064674234765, 6.322130266823468, 0.44823943270416733),
            rot=(-0.5735763596999339, 0.0, 0.0, 0.819152097960673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLfyqkj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.74822165098457, 13.789289736698528, 0.4482394327041672),
            rot=(-0.5735763596999339, 0.0, 0.0, 0.819152097960673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(1.0000326607542802, 0.9999884338066302, 1.0000217583485587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushOedeqi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushOedeqi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.990391286179424, 1.044600450667415, 0.802406847804355),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/oedeqi/usd/oedeqi.usd"),
            visual_material_path="materials",
            scale=(0.5401318355258385, 0.5401250140967634, 0.5401371923588743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushOedeqi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushOedeqi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.749436594680577, 11.006834398422415, 0.8024068478043551),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/oedeqi/usd/oedeqi.usd"),
            visual_material_path="materials",
            scale=(0.5401318355258385, 0.5401250140967634, 0.5401371923588743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushOedeqi2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushOedeqi2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.704163401320578, -0.180505079117585, 0.8024068478043551),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/oedeqi/usd/oedeqi.usd"),
            visual_material_path="materials",
            scale=(0.5401318355258385, 0.5401250140967634, 0.5401371923588743),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushPjhpwk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.009402548729124, 7.0192662604117695, 1.0555439818794023),
            rot=(0.6899669835574462, 0.7238408399645869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.5033132981020135, 0.5033035820828197, 0.5033060628538621),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushPjhpwk1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.21720059780319, 8.513960975873509, 1.0555440061014065),
            rot=(0.6794848063478286, 0.7128440936584081, 0.12569367185242203, 0.11981150585412192),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.5033132981020135, 0.5033035820828197, 0.5033060628538621),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushPjhpwk2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.916981530610531, 8.005023005801219, 1.0555439901239592),
            rot=(0.6794848063478286, 0.7128440936584081, 0.12569367185242203, 0.11981150585412192),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.5033132981020135, 0.5033035820828197, 0.5033060628538621),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushPjhpwk3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(16.462997198386915, 14.776241882414094, 1.055543995126991),
            rot=(0.6794848063478286, 0.7128440936584081, 0.12569367185242203, 0.11981150585412192),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.5033132981020135, 0.5033035820828197, 0.5033060628538621),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushPjhpwk4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.339566648235244, 10.511612663203563, 1.0555439751549929),
            rot=(0.6794848063478286, 0.7128440936584081, 0.12569367185242203, 0.11981150585412192),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.5033132981020135, 0.5033035820828197, 0.5033060628538621),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushPjhpwk5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.568257038622644, -2.3731215427784416, 1.0555439709186303),
            rot=(0.6794848063478286, 0.7128440936584081, 0.12569367185242203, 0.11981150585412192),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.5033132981020135, 0.5033035820828197, 0.5033060628538621),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushXsqlhv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushXsqlhv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.260369546463714, 15.86106745763123, 0.3039426401020033),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(0.7417081749671752, 0.7417076815233943, 0.7416515376266649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushXsqlhv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushXsqlhv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.196490376688319, 15.596501434592351, 0.3039426401020032),
            rot=(0.9762960059348095, 0.0, 0.0, 0.21643961928385122),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(0.7417081749671752, 0.7417076815233943, 0.7416515376266649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushXsqlhv2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushXsqlhv2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.228209313712325, 16.260954646803082, 0.3039426401020032),
            rot=(0.9762960059348095, 0.0, 0.0, 0.21643961928385122),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(0.7417081749671752, 0.7417076815233943, 0.7416515376266649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushXsqlhv3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushXsqlhv3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.129284054133149, 15.962079385111277, 0.3039426401020033),
            rot=(0.9990482213013427, 0.0, 0.0, 0.04361939379018578),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(0.7417081749671752, 0.7417076815233943, 0.7416515376266649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.279953554630954, 9.903784288817157, 0.04630507612492063),
            rot=(0.9659258257467466, 0.0, 0.0, 0.25881904712649295),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.86444228474185, 9.898185255894099, 0.046305076124920685),
            rot=(0.49999998092101916, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3883559047380802, 14.274356893033717, 0.04630507612492063),
            rot=(0.49999998092101916, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.401631573367091, 11.404739603595981, 0.04630507612492063),
            rot=(0.21643950565904896, 0.0, 0.0, 0.9762960311248154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.5533462154068323, 10.410915513212647, 0.046305076124920685),
            rot=(0.49999998092101916, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.099978540801965, 8.831196728356993, 0.04630507612492063),
            rot=(0.21643950565904896, 0.0, 0.0, 0.9762960311248154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushYhjhta6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushYhjhta6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.159997885029947, 15.53623929603674, 0.046305076124920574),
            rot=(0.21643950565904896, 0.0, 0.0, 0.9762960311248154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.5133016082295836, 0.5133182154492312, 0.5133031439393787),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carSupuws0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carSupuws0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.808757781982422, 6.831541061401367, 0.5490351915359497),
            rot=(0.7070193886756897, -0.01111534982919693, -0.01111535169184208, 0.707019567489624),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/car/supuws/usd/supuws.usd"),
            visual_material_path="materials",
            scale=(0.36415854021043337, 1.9759347249540005, 0.8421838782550876),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ovenFfitak0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ovenFfitak0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.908407211303711, -0.6371550559997559, 0.5357411503791809),
            rot=(0.7071069478988647, 1.4901161193847656e-08, -1.30385160446167e-08, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/ffitak/usd/ffitak.usd"),
            visual_material_path="materials",
            scale=(1.2165486707440476, 0.9933197932538756, 0.9863268872292447),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeDyymaq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeDyymaq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.067145893158404, 13.150478675605118, 3.7187507452961657),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.7470371138984071, 0.7470313195691696, 0.7470372166565661),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeDyymaq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeDyymaq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(25.856598491611596, 8.246013831855118, 3.718750745296166),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.7470371138984071, 0.7470313195691696, 0.7470372166565661),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeDyymaq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeDyymaq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.861209819736597, 0.7766780164201166, 3.718750745296166),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.7470371138984071, 0.7470313195691696, 0.7470372166565661),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.045403752059993, 10.942528184900699, 3.78224683666491),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.7470295122496888, 0.7470408543350594, 0.7470353094678952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.477926212994995, 15.627621934900699, 3.7822468366649105),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.7470295122496888, 0.7470408543350594, 0.7470353094678952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.009891736979304, 15.848331486434995, 3.78224683666491),
            rot=(0.7071067811865477, 0.0, 0.0, -0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.7470295122496888, 0.7470408543350594, 0.7470353094678952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeGmzozb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeGmzozb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.84862857575467, -3.852986092929447, 4.967669929503339),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/gmzozb/usd/gmzozb.usd"),
            visual_material_path="materials",
            scale=(0.4867135762913413, 0.48672477622042765, 0.4867151413937108),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeGmzozb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeGmzozb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.211123889627792, -3.8487190041033967, 4.967669929503339),
            rot=(0.9848077514032422, 0.0, 0.0, 0.1736481867918291),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/gmzozb/usd/gmzozb.usd"),
            visual_material_path="materials",
            scale=(0.4867135762913413, 0.48672477622042765, 0.4867151413937108),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeGmzozb2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeGmzozb2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.947091188760716, -3.6955471764430046, 4.967669929503339),
            rot=(0.2588190749324381, 0.0, 0.0, 0.9659258182961655),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/gmzozb/usd/gmzozb.usd"),
            visual_material_path="materials",
            scale=(0.4867135762913413, 0.48672477622042765, 0.4867151413937108),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeGmzozb3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeGmzozb3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.340720686200225, -3.824536295436548, 4.96766992950334),
            rot=(0.9063078119968713, 0.0, 0.0, 0.42261820821332796),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/gmzozb/usd/gmzozb.usd"),
            visual_material_path="materials",
            scale=(0.4867135762913413, 0.48672477622042765, 0.4867151413937108),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeGmzozb4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeGmzozb4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.140123214325123, -3.8487188471748297, 4.967669929503339),
            rot=(0.9848077514032422, 0.0, 0.0, 0.1736481867918291),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/gmzozb/usd/gmzozb.usd"),
            visual_material_path="materials",
            scale=(0.4867135762913413, 0.48672477622042765, 0.4867151413937108),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(25.264881157939666, -3.177268952129709, 3.858327326568442),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6139130133735524, 0.613919288355691, 0.6139238725666474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.350632124684275, 7.4205414797266975, 3.8583273265684426),
            rot=(0.8870108347450367, 0.0, 0.0, 0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6139130133735524, 0.613919288355691, 0.6139238725666474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.967728847766903, 12.327771690871343, 3.858327326568442),
            rot=(0.7933533320874723, 0.0, 0.0, 0.6087614397000725),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6139130133735524, 0.613919288355691, 0.6139238725666474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.980721001689666, -0.17172995066470903, 3.858327326568442),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6139130133735524, 0.613919288355691, 0.6139238725666474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(27.556486626689665, 4.171019988300292, 3.8583273265684426),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6139130133735524, 0.613919288355691, 0.6139238725666474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(27.302701959421498, 15.761834532654747, 3.8583273265684426),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6139130133735524, 0.613919288355691, 0.6139238725666474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.631489512233657, 13.495408521373186, 2.2087224478755996),
            rot=(0.9238795411027497, 0.0, 0.0, 0.3826834116234627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.842702989188342, 11.820091591306031, 2.2087224478755996),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.20345243707659, -1.4958886030417748, 2.2087224478755996),
            rot=(0.9537169603327441, 0.0, 0.0, 0.30070576910606656),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.616432506284894, 13.147073565997283, 2.2087224478755996),
            rot=(0.8870108347450367, 0.0, 0.0, -0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(26.92012922260544, 0.15607561661330052, 2.2087224478755996),
            rot=(0.8870108347450367, 0.0, 0.0, 0.4617486102252103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(27.229632427105905, 11.735794198628916, 2.2087224478755996),
            rot=(0.7933533320874723, 0.0, 0.0, -0.6087614397000725),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.196400390727764, -3.271135789421943, 2.2087224478755996),
            rot=(0.9396926072714594, 0.0, 0.0, -0.3420201804563099),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.324193417633587, 16.046733811862953, 2.2087224478755996),
            rot=(0.8191519943362758, 0.0, 0.0, -0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.983068006911658, 9.985493935056033, 2.2087224478755996),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.5642494963803129, 0.5642530297662507, 0.5642628970567528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetByvbuc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetByvbuc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.748001021057176, -0.7065366305784763, 0.4014303496181428),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/byvbuc/usd/byvbuc.usd"),
            visual_material_path="materials",
            scale=(0.9999271520599631, 1.000006572809436, 1.0000348963888803),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTjextj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTjextj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.444510931832215, -0.7712124998639553, 0.4259219155917787),
            rot=(7.589671327580123e-07, 0.0, 0.0, 0.999999999999712),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/tjextj/usd/tjextj.usd"),
            visual_material_path="materials",
            scale=(0.9999991164594453, 1.00003998159333, 1.000023739583624),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bowlGwhcty0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bowlGwhcty0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.020232164281023, 3.018749917936856, 0.5720725981830987),
            rot=(0.6300366112667556, 0.630036730476037, 0.3210200459385583, 0.3210198075199946),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bowl/gwhcty/usd/gwhcty.usd"),
            visual_material_path="materials",
            scale=(1.0001275025789036, 0.99940059642665, 0.9999648181749619),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    flowerQokboq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/flowerQokboq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.2638493981119145, 1.1572982317231035, 0.9279957930372159),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/flower/qokboq/usd/qokboq.usd"),
            visual_material_path="materials",
            scale=(1.0000665119396945, 0.9998893524195818, 0.999896563585286),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVanltx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVanltx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.0983345123647323, 7.467352375802115, 1.1991249555568289),
            rot=(0.7071067215818995, 0.7071068407911907, 7.894597701486207e-24, 7.894596370556643e-24),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vanltx/usd/vanltx.usd"),
            visual_material_path="materials",
            scale=(0.9999753016524112, 0.9999773991423724, 0.9998713624125601),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    stoveMdanhg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/stoveMdanhg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.905571937561035, -0.6749039888381958, 0.8940384387969971),
            rot=(0.7071069478988647, 0.0, 6.465938895416912e-13, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stove/mdanhg/usd/mdanhg.usd"),
            visual_material_path="materials",
            scale=(1.0000689904337214, 1.000029976760544, 0.9988557633781321),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableXftrki0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableXftrki0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.291088104248047, 1.1092184782028198, 0.6454222798347473),
            rot=(-0.7071071267127991, -2.566722105257213e-05, -4.1353014239575714e-05, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/xftrki/usd/xftrki.usd"),
            visual_material_path="materials",
            scale=(1.0000032022463494, 1.0000521525950798, 1.0000182903502344),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableKoagbh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableKoagbh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2643425464630127, 5.2902960777282715, 0.3607046604156494),
            rot=(-0.7071065306663513, -6.174537702463567e-05, -0.000106336701719556, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/koagbh/usd/koagbh.usd"),
            visual_material_path="materials",
            scale=(1.0000183792897899, 0.9999994635584848, 1.0000920133732243),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenChairCottya0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenChairCottya0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.191068649291992, 9.651857376098633, 0.4436939060688019),
            rot=(-0.3539190888404846, 0.00056873494759202, -0.0012742235558107495, 0.9352750778198242),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_chair/cottya/usd/cottya.usd"),
            visual_material_path="materials",
            scale=(1.000019596374227, 1.0000269595727551, 0.9999681960969528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenChairCottya1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenChairCottya1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.798120498657227, 11.159017562866211, 0.4501733183860779),
            rot=(-0.6849028468132019, -0.0003113655839115381, -0.0005163061432540417, 0.7286341786384583),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_chair/cottya/usd/cottya.usd"),
            visual_material_path="materials",
            scale=(1.000019596374227, 1.0000269595727551, 0.9999681960969528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenChairCottya2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenChairCottya2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.393800735473633, 12.776665687561035, 0.457216739654541),
            rot=(0.8946806192398071, -0.0007121223025023937, 0.001455753343179822, -0.44670370221138),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_chair/cottya/usd/cottya.usd"),
            visual_material_path="materials",
            scale=(1.000019596374227, 1.0000269595727551, 0.9999681960969528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenChairLraplz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenChairLraplz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.069694519042969, 11.154224395751953, 0.4317042827606201),
            rot=(0.6993147134780884, 0.0041026282124221325, -0.006562575697898865, 0.71477210521698),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_chair/lraplz/usd/lraplz.usd"),
            visual_material_path="materials",
            scale=(1.000019839257668, 1.0000390621727706, 0.9999556188047467),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    grillSxfjac0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/grillSxfjac0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.779531478881836, 11.215051651000977, 0.7867223620414734),
            rot=(0.05842304602265358, -4.3682754039764404e-05, 0.0002913418866228312, 0.9982919692993164),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grill/sxfjac/usd/sxfjac.usd"),
            visual_material_path="materials",
            scale=(1.0000414252957335, 0.999976909659204, 0.999995663554436),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorWwkuuf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorWwkuuf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0449129343032837, 2.344085216522217, 0.7049516439437866),
            rot=(-0.3921512961387634, 0.46583423018455505, 0.6073353886604309, -0.510254442691803),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/wwkuuf/usd/wwkuuf.usd"),
            visual_material_path="materials",
            scale=(1.0000314647385649, 0.9999986334953804, 1.0000010708756075),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanWxodip0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanWxodip0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.760769844055176, 6.775586128234863, 0.2169422060251236),
            rot=(0.9999997019767761, -0.0007324765319935977, 5.6563818361610174e-05, 0.00011928226740565151),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/wxodip/usd/wxodip.usd"),
            visual_material_path="materials",
            scale=(1.0000017502523426, 0.999957776624915, 0.999907468776651),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaFrlxgz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaFrlxgz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.971545696258545, 6.052009105682373, 0.2779788672924042),
            rot=(1.0, -0.00022765411995351315, -0.0005337276961654425, -6.704738189000636e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/frlxgz/usd/frlxgz.usd"),
            visual_material_path="materials",
            scale=(0.9999724502151209, 1.0000096964586114, 1.000029794308244),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    washerZiomqg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/washerZiomqg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.8017830848693848, -0.5677242875099182, 0.537432074546814),
            rot=(1.0000001192092896, -1.998171796913084e-07, -2.4485852918587625e-06, 1.3993593711347785e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/ziomqg/usd/ziomqg.usd"),
            visual_material_path="materials",
            scale=(0.9999995808561432, 0.9999709279169309, 1.000023958191614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairHgunnf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairHgunnf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.886148853351066, 1.7929712207951625, 0.46520255980329966),
            rot=(7.052580151601934e-07, 7.052583561877121e-07, 0.7071069003954774, 0.7071066619768941),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/hgunnf/usd/hgunnf.usd"),
            visual_material_path="materials",
            scale=(1.000017756333427, 0.9999611145678563, 0.9999877200791857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairHgunnf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairHgunnf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.886146900221066, 0.43004156381516223, 0.4652025598033022),
            rot=(7.052580151601934e-07, 7.052583561877121e-07, 0.7071069003954774, 0.7071066619768941),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/hgunnf/usd/hgunnf.usd"),
            visual_material_path="materials",
            scale=(1.000017756333427, 0.9999611145678563, 0.9999877200791857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUofiqj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUofiqj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.4944533004477725, 0.23984719275464816, 0.46520261251496964),
            rot=(0.683012713028927, 0.6830128322382145, 0.18301246768400745, 0.18301240807936348),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/uofiqj/usd/uofiqj.usd"),
            visual_material_path="materials",
            scale=(1.0000685266122178, 0.9999607528296444, 0.9999877200791857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUofiqj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUofiqj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.685437779650283, 1.7886753400331363, 0.4652025609382054),
            rot=(0.7071067215818961, 0.7071068407911886, -6.181724033636146e-08, -6.181724043437327e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/uofiqj/usd/uofiqj.usd"),
            visual_material_path="materials",
            scale=(1.0000685266122178, 0.9999607528296444, 0.9999877200791857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZdhnyg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZdhnyg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.886147939577059, 1.111506382061935, 0.4652025709791807),
            rot=(7.052580151601934e-07, 7.052583561877121e-07, 0.7071069003954774, 0.7071066619768941),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zdhnyg/usd/zdhnyg.usd"),
            visual_material_path="materials",
            scale=(1.000017756333427, 0.9999611145678563, 0.9999877200791857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZdhnyg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZdhnyg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.679700964194897, 1.1072122357944365, 0.4652025683890996),
            rot=(0.7071067215818959, 0.7071068407911888, -6.181724033636146e-08, -6.181724043437328e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zdhnyg/usd/zdhnyg.usd"),
            visual_material_path="materials",
            scale=(1.000017756333427, 0.9999611145678563, 0.9999877200791857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    backgroundVtfqjb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/backgroundVtfqjb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.78292350769043, 5.434154922485343, -0.13667323273455492),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/background/vtfqjb/usd/vtfqjb.usd"),
            visual_material_path="materials",
            scale=(0.9999997609281823, 0.9999997609281823, 0.9998332665025739),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bidetLcyvov0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bidetLcyvov0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.7335877044780403, 0.4325773622816424, 0.41366104900922895),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bidet/lcyvov/usd/lcyvov.usd"),
            visual_material_path="materials",
            scale=(1.0000360294540607, 1.0000269649055216, 1.0000060665452475),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRhdbzv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRhdbzv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.260105609893799, 4.522088527679443, 0.21441006660461426),
            rot=(-0.7071067094802856, 3.4924596548080444e-10, -3.5652192309498787e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rhdbzv/usd/rhdbzv.usd"),
            visual_material_path="materials",
            scale=(0.9999962897304194, 0.9999143050350148, 0.9999282391386514),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoxz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoxz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.400440863697888, -0.689635012779627, 1.2041295976619655),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoxz/usd/todoxz.usd"),
            visual_material_path="materials",
            scale=(1.0000738166439107, 1.0000201395110238, 0.9999957886024031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorBexenl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorBexenl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.8864684104919434, 2.3801538944244385, 1.1881195306777954),
            rot=(1.2357922969385982e-06, 0.0, 5.115907697472721e-13, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/bexenl/usd/bexenl.usd"),
            visual_material_path="materials",
            scale=(1.000030611247557, 0.9996929314404115, 0.9999773953994178),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorBexenl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorBexenl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.001831293106079, 0.776175320148468, 1.1881195306777954),
            rot=(1.0000001192092896, 5.684341886080802e-14, -5.1318949090273236e-12, -5.642892801915877e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/bexenl/usd/bexenl.usd"),
            visual_material_path="materials",
            scale=(1.000030611247557, 0.9996929314404115, 0.9999773953994178),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorVudhlc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorVudhlc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5263960361480713, 7.679533958435059, 1.1762324571609497),
            rot=(-1.1874362826347351e-08, 0.0, -1.4551915228366852e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/vudhlc/usd/vudhlc.usd"),
            visual_material_path="materials",
            scale=(1.0000278892111578, 1.0000199558262346, 1.000015391050588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorVudhlc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorVudhlc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.27708256244659424, -1.0874780416488647, 1.1762324571609497),
            rot=(1.0, 0.0, -1.3812950783176348e-11, -3.018067218363285e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/vudhlc/usd/vudhlc.usd"),
            visual_material_path="materials",
            scale=(1.0000278892111578, 1.0000199558262346, 1.000015391050588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorVudhlc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorVudhlc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.516416072845459, 6.150399208068848, 1.1762324571609497),
            rot=(0.7071070075035095, 3.725290298461914e-09, -2.4519977159798145e-09, 0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/vudhlc/usd/vudhlc.usd"),
            visual_material_path="materials",
            scale=(1.0000278892111578, 1.0000199558262346, 1.000015391050588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorVudhlc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorVudhlc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.594970226287842, 7.679533958435059, 1.1762324571609497),
            rot=(-1.1874362826347351e-08, 0.0, -1.4551915228366852e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/vudhlc/usd/vudhlc.usd"),
            visual_material_path="materials",
            scale=(1.0000278892111578, 1.0000199558262346, 1.000015391050588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorVudhlc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorVudhlc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.921923637390137, 3.434858560562134, 1.1762324571609497),
            rot=(-1.1874362826347351e-08, 0.0, -1.4551915228366852e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/vudhlc/usd/vudhlc.usd"),
            visual_material_path="materials",
            scale=(1.0000278892111578, 1.0000199558262346, 1.000015391050588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.651690211348929, 6.911736184847499, 2.1672100152177673),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6516902113504542, 2.7649080598430174, 2.1672100152177673),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.769117530705134, 7.305008839968893, 2.3400928277177773),
            rot=(0.92683088503753, 8.102612954631403e-08, 3.2825422327820875e-08, 0.3754790414131544),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.952663091781349, 7.304923325390377, 2.340092827717784),
            rot=(0.9360372949765179, 8.183097513158099e-08, 3.0764144847538755e-08, 0.3519008133168146),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.552382395843327, 6.5636057734916005, 2.3400928277177684),
            rot=(0.342020154140196, 2.9900352421070384e-08, 8.215053529983874e-08, 0.9396926168497383),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5522300220393996, 5.746275335185115, 2.340092827717733),
            rot=(0.38986468486186915, 3.4083054735785915e-08, 8.050520996920086e-08, 0.9208721558921997),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5523154441396243, 4.929816900390902, 2.340092827717767),
            rot=(0.41304680672025895, 3.610970006728872e-08, 7.961678244674177e-08, 0.9107097976074429),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.119497493467222, 3.702452588786823, 2.3400928277177715),
            rot=(0.9848077768857153, 8.609462191343033e-08, -1.5180795012920643e-08, -0.1736480422734663),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.119530880594223, 4.5198471815203085, 2.340092827717778),
            rot=(0.9029901085225923, 7.8941909519142e-08, -3.756218825266494e-08, -0.4296613362991245),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.119431626173207, 5.336265130868852, 2.3400928277177915),
            rot=(0.9107097863968288, 7.961678147584543e-08, -3.6109688944435116e-08, -0.41304683143807663),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6516902113489285, 5.8944354035975, 2.167210015217768),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6516902113489289, 4.915513528597499, 2.167210015217768),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.9079089660043327, 0.3754295458016699, 2.165252983967765),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.9079070175292488, -0.6004337338677272, 2.1652529839677674),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.0120574658317776, 1.5348768534035622, 2.337745171467762),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6700339799649617, 1.5348729099255842, 2.337745171467769),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6516902113504541, 3.740775247343018, 2.167210015217768),
            rot=(0.16326357904696623, 1.4272955617052936e-08, 8.624977964699864e-08, 0.9865824870515224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPawfmw9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPawfmw9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.586459921258759, 7.304887177788779, 2.3400928277177897),
            rot=(0.8870107605029302, 7.754494710899795e-08, 4.0367357786246076e-08, 0.461748752842935),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pawfmw/usd/pawfmw.usd"),
            visual_material_path="materials",
            scale=(1.0000346961391637, 1.0000973890709837, 1.0005180292214055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPxrmnt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPxrmnt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.254535436630249, 0.054847270250320435, 2.2443196773529053),
            rot=(-1.1516385711729527e-07, -0.7071068286895752, 0.70710688829422, -2.220040187239647e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pxrmnt/usd/pxrmnt.usd"),
            visual_material_path="materials",
            scale=(1.0005497683534192, 0.9999146647432396, 0.9988291504802495),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPxrmnt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPxrmnt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.948420286178589, 0.054847270250320435, 2.2443196773529053),
            rot=(-1.1516385711729527e-07, -0.7071068286895752, 0.70710688829422, -2.220040187239647e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pxrmnt/usd/pxrmnt.usd"),
            visual_material_path="materials",
            scale=(1.0005497683534192, 0.9999146647432396, 0.9988291504802495),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPxrmnt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPxrmnt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.642568588256836, 0.054847270250320435, 2.2443196773529053),
            rot=(-1.1516385711729527e-07, -0.7071068286895752, 0.70710688829422, -2.220040187239647e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pxrmnt/usd/pxrmnt.usd"),
            visual_material_path="materials",
            scale=(1.0005497683534192, 0.9999146647432396, 0.9988291504802495),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPxrmnt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPxrmnt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.254535436630249, -0.7104808688163757, 2.2443196773529053),
            rot=(-1.1516385711729527e-07, -0.7071068286895752, 0.70710688829422, -2.220040187239647e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pxrmnt/usd/pxrmnt.usd"),
            visual_material_path="materials",
            scale=(1.0005497683534192, 0.9999146647432396, 0.9988291504802495),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPxrmnt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPxrmnt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.948420286178589, -0.7104808688163757, 2.2443196773529053),
            rot=(-1.1516385711729527e-07, -0.7071068286895752, 0.70710688829422, -2.220040187239647e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pxrmnt/usd/pxrmnt.usd"),
            visual_material_path="materials",
            scale=(1.0005497683534192, 0.9999146647432396, 0.9988291504802495),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightPxrmnt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightPxrmnt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.642568588256836, -0.7104808688163757, 2.2443196773529053),
            rot=(-1.1516385711729527e-07, -0.7071068286895752, 0.70710688829422, -2.220040187239647e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/pxrmnt/usd/pxrmnt.usd"),
            visual_material_path="materials",
            scale=(1.0005497683534192, 0.9999146647432396, 0.9988291504802495),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drivewayQbxmgb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drivewayQbxmgb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.911641414956225, 7.121470243492333, -0.003990936279999999),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/driveway/qbxmgb/usd/qbxmgb.usd"),
            visual_material_path="materials",
            scale=(0.9999942949797943, 0.999989739055688, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchStrbnw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchStrbnw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4436038732528687, 3.9397168159484863, 1.1495717763900757),
            rot=(7.549533620476723e-08, 0.0, -6.739355740137398e-10, 1.000000238418579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/strbnw/usd/strbnw.usd"),
            visual_material_path="materials",
            scale=(1.0013957018592636, 1.0000000223517422, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchStrbnw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchStrbnw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7511518001556396, 7.5699591636657715, 1.1495717763900757),
            rot=(0.7071070671081543, -9.313225746154785e-10, -4.256435204297304e-10, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/strbnw/usd/strbnw.usd"),
            visual_material_path="materials",
            scale=(1.0013957018592636, 1.0000000223517422, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchStrbnw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchStrbnw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6418158411979675, 7.5699591636657715, 1.1495717763900757),
            rot=(0.7071070671081543, -9.313225746154785e-10, -4.256435204297304e-10, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/strbnw/usd/strbnw.usd"),
            visual_material_path="materials",
            scale=(1.0013957018592636, 1.0000000223517422, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchStrbnw3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchStrbnw3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4436038732528687, 4.028298854827881, 1.1495717763900757),
            rot=(7.549533620476723e-08, 0.0, -6.739355740137398e-10, 1.000000238418579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/strbnw/usd/strbnw.usd"),
            visual_material_path="materials",
            scale=(1.0013957018592636, 1.0000000223517422, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceOwbrvb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceOwbrvb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.939154575942936, 17.68097468733999, 0.6696558417070717),
            rot=(-0.7071067215818457, -2.753575122041247e-07, 2.7535756898854575e-07, 0.7071068407911372),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/owbrvb/usd/owbrvb.usd"),
            visual_material_path="materials",
            scale=(0.9998958837344823, 1.0000014991522257, 0.9999983459738433),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceOwbrvb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceOwbrvb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(29.42284018627239, 6.001977327410826, 0.6695226658406606),
            rot=(2.821299745549564e-07, 1.7713049322651668e-13, 6.27832946520208e-07, 0.9999999999997633),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/owbrvb/usd/owbrvb.usd"),
            visual_material_path="materials",
            scale=(0.9998958837344823, 1.0000014991522257, 0.9999983459738433),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceOwbrvb2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceOwbrvb2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.045508556444652, -5.468862912779087, 0.6697242621120382),
            rot=(0.707106781186494, 2.753575405963362e-07, 2.753575405963361e-07, 0.7071067811864938),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/owbrvb/usd/owbrvb.usd"),
            visual_material_path="materials",
            scale=(0.9998958837344823, 1.0000014991522257, 0.9999983459738433),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceOwbrvb3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceOwbrvb3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.005268588198355, -5.468210569029087, 0.6693980292068833),
            rot=(0.707106781186494, 2.753575405963362e-07, 2.753575405963361e-07, 0.7071067811864938),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/owbrvb/usd/owbrvb.usd"),
            visual_material_path="materials",
            scale=(0.9998958837344823, 1.0000014991522257, 0.9999983459738433),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceOwbrvb4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceOwbrvb4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.111195078465072, 17.680974687339997, 0.6696598089920366),
            rot=(-0.7071067215818457, -2.753575122041247e-07, 2.7535756898854575e-07, 0.7071068407911372),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/owbrvb/usd/owbrvb.usd"),
            visual_material_path="materials",
            scale=(0.9998958837344823, 1.0000014991522257, 0.9999983459738433),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    flowerLdkhmx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/flowerLdkhmx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.134043358049955, -0.8172783145234026, 1.0181037891497435),
            rot=(0.7876552970046564, -6.885900227225067e-08, 5.3862582225384796e-08, -0.616116168510857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/flower/ldkhmx/usd/ldkhmx.usd"),
            visual_material_path="materials",
            scale=(1.0000215728352262, 1.0000342961986766, 1.0000554385094818),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    flowerTfvsai0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/flowerTfvsai0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2128765723705983, -0.7059438141122315, 1.6439933758972514),
            rot=(-0.04361963175513177, 0.0, 0.0, 0.9990482109115391),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/flower/tfvsai/usd/tfvsai.usd"),
            visual_material_path="materials",
            scale=(1.000075852854329, 1.0000382920375441, 0.9997988373959308),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.082374530763206, 10.527153679209123, 0.44061978114073147),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.416495624513203, 13.705216179209122, 0.4406197811407316),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.119112812013205, 13.437567741709122, 0.4406197811407315),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(16.393651874513207, 8.330528679209122, 0.5437486873907316),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.723386249513204, 10.621942741709121, 0.4406197811407315),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.549521015143204, 7.668270866709122, 0.5439923397307315),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.080020000486796, 2.111551872559122, 0.5089493709807316),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.549521015143204, 7.668270866709122, 0.5439923397307315),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightQyfrwj8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightQyfrwj8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.549521015143204, -1.1384246899408779, 0.5439923397307316),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/qyfrwj/usd/qyfrwj.usd"),
            visual_material_path="materials",
            scale=(1.000000005418604, 1.000000005418604, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hallTreeDaxzaw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hallTreeDaxzaw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.149791970850131, -0.20872016423534406, 0.8931085028629628),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hall_tree/daxzaw/usd/daxzaw.usd"),
            visual_material_path="materials",
            scale=(0.9999413220881447, 0.9999738634976771, 1.0000082352097175),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hallTreeUpkvgr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hallTreeUpkvgr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0774564590475975, 5.377695836304681, 1.1423905911433117),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hall_tree/upkvgr/usd/upkvgr.usd"),
            visual_material_path="materials",
            scale=(1.0000102179114942, 0.999999349834924, 0.9999828466858699),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hookAkwlam0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hookAkwlam0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4231229294064383, 0.6632356344908475, 1.0937547513684258),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hook/akwlam/usd/akwlam.usd"),
            visual_material_path="materials",
            scale=(0.9996859003305063, 0.9994481709832832, 0.9989967511602638),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lawnOgzsvf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lawnOgzsvf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.431265624999999, 6.111179199219999, -0.08381396483999998),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/lawn/ogzsvf/usd/ogzsvf.usd"),
            visual_material_path="materials",
            scale=(1.000001001814728, 1.0000003291522757, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorEdxfnt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorEdxfnt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.4870393529500423, -0.9680357186672339, 1.4609740050074589),
            rot=(-8.78176422630378e-07, 0.0, 0.0, 0.9999999999996144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/edxfnt/usd/edxfnt.usd"),
            visual_material_path="materials",
            scale=(1.000062400763936, 0.9987480676065599, 0.9999229975239352),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    motionSensorAecflf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/motionSensorAecflf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0119996545657637, 0.647351025100082, 1.1200054522788705),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/motion_sensor/aecflf/usd/aecflf.usd"),
            visual_material_path="materials",
            scale=(0.9996377590176516, 0.9992834768567213, 0.9996712823421333),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureEkagyj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureEkagyj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.227926951062359, 5.644687616995554, 1.5177956611122325),
            rot=(-0.5002176213215641, -0.49978220938733364, 0.4997822987943017, 0.5002176809262098),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ekagyj/usd/ekagyj.usd"),
            visual_material_path="materials",
            scale=(1.000038287050533, 1.0000139372955785, 1.0004165412378299),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureGgajdz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureGgajdz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.9067560771735583, 7.554505827035634, 1.0780335180367493),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ggajdz/usd/ggajdz.usd"),
            visual_material_path="materials",
            scale=(1.0001703263784367, 1.0000000223517422, 1.0001243389328816),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureHffaxw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureHffaxw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6240008715595655, 0.6331615567330537, 1.6850852067141786),
            rot=(0.70849399736195, 0.7057168381880122, 1.2074746407542462e-08, -1.0091583468806683e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hffaxw/usd/hffaxw.usd"),
            visual_material_path="materials",
            scale=(0.999992370470471, 1.0000428282016587, 1.0003692590366817),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureJnecmu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureJnecmu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9959434154470749, 4.372142820737634, 1.502115040838339),
            rot=(-0.500217621321564, -0.4997822093873336, 0.4997822987943016, 0.5002176809262097),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jnecmu/usd/jnecmu.usd"),
            visual_material_path="materials",
            scale=(1.0000501254821117, 0.9999763326477249, 1.0017815363302607),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureOshvew0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureOshvew0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.381181083999269, 4.435207520376192, 0.5965740700766909),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/oshvew/usd/oshvew.usd"),
            visual_material_path="materials",
            scale=(1.0001632535976104, 0.9983729216328704, 1.0000450683086775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQlkknu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQlkknu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9959467998953615, 6.643790976641916, 1.3490976103310584),
            rot=(-0.5002176213085805, -0.49978217957203835, 0.49978226897900657, 0.5002177405178713),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qlkknu/usd/qlkknu.usd"),
            visual_material_path="materials",
            scale=(1.0000168905026485, 0.999987063158421, 0.9985832555540717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQlsyco0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQlsyco0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1341903731186425, 7.547607934886811, 1.0924082484604853),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qlsyco/usd/qlsyco.usd"),
            visual_material_path="materials",
            scale=(0.9999669031601902, 0.9997374829199873, 0.9999107305612301),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureTveyoh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureTveyoh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9959513206629245, 5.612115486504527, 1.446016481297049),
            rot=(-0.5002176213215641, -0.49978220938733364, 0.49978229879430164, 0.5002176809262098),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/tveyoh/usd/tveyoh.usd"),
            visual_material_path="materials",
            scale=(1.000158142217255, 0.9999849526538228, 0.9978188090052488),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureYzbpie0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureYzbpie0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9959473912073672, 5.087585963825938, 1.1189172065568238),
            rot=(-0.500217621321564, -0.4997822093873336, 0.4997822987943016, 0.5002176809262097),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yzbpie/usd/yzbpie.usd"),
            visual_material_path="materials",
            scale=(0.9999330031092536, 0.9999998863627177, 0.9977826280888519),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    playgroundXdlcdi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/playgroundXdlcdi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.41695751402372, 13.086625138445518, 2.0535555717913936),
            rot=(0.9999686877135523, -9.536445115245682e-07, 7.546910069622554e-09, -0.007913506904440756),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/playground/xdlcdi/usd/xdlcdi.usd"),
            visual_material_path="materials",
            scale=(1.0000079493139076, 1.0000006832498136, 0.9999991255780298),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    rangeHoodXvdfpp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/rangeHoodXvdfpp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.909779261739351, -0.9177923865160386, 1.8215603075038402),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/range_hood/xvdfpp/usd/xvdfpp.usd"),
            visual_material_path="materials",
            scale=(0.9999729749939457, 0.9999891650238342, 0.9999650987301697),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightEqbjaz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightEqbjaz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2761651007841883, 5.593558722521193, 1.7559910399923164),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/eqbjaz/usd/eqbjaz.usd"),
            visual_material_path="materials",
            scale=(0.9999229110273024, 0.9999229110273024, 1.000024993927349),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKiuayi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKiuayi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.220687106614142, 1.1139496352398741, 2.0094308044000737),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/kiuayi/usd/kiuayi.usd"),
            visual_material_path="materials",
            scale=(0.9999221691013783, 0.9999225079040341, 0.9999570831098695),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightLtnnrc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightLtnnrc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.647058869964029, 1.9744320803981357, 2.2930740407150645),
            rot=(-7.549789409738357e-08, -4.0068883329662575e-08, 1.1920927533992533e-07, 0.9999999999999895),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ltnnrc/usd/ltnnrc.usd"),
            visual_material_path="materials",
            scale=(0.9999815708237637, 1.0000463904675965, 1.0001251508255735),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightLtnnrc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightLtnnrc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.647058869964027, 0.5482797533644367, 2.2930740407150676),
            rot=(-7.549789409738357e-08, -4.0068883329662575e-08, 1.1920927533992533e-07, 0.9999999999999895),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ltnnrc/usd/ltnnrc.usd"),
            visual_material_path="materials",
            scale=(0.9999815708237637, 1.0000463904675965, 1.0001251508255735),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    posterHgonwj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/posterHgonwj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.910258125028691, 7.547130733963158, 1.4864342729041022),
            rot=(0.7071067215818995, 0.7071068407911907, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/poster/hgonwj/usd/hgonwj.usd"),
            visual_material_path="materials",
            scale=(0.9999220533828841, 1.0000003418386756, 0.9999982838858809),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    posterRypeha0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/posterRypeha0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3227729018153984, 0.2101389602131846, 1.5350165833213067),
            rot=(0.49999999999999994, 0.5000000000000001, 0.5, 0.5000000000000001),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/poster/rypeha/usd/rypeha.usd"),
            visual_material_path="materials",
            scale=(1.0001134424167917, 1.000165567547869, 0.9984207903519836),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    posterXzsmxq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/posterXzsmxq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3330680243958026, 3.4776423880635012, 1.7149019824556644),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/poster/xzsmxq/usd/xzsmxq.usd"),
            visual_material_path="materials",
            scale=(0.9996131285323309, 0.9999772592033231, 1.0000522377696488),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkEgwapq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkEgwapq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.132995969671493, 0.26009261801005107, 0.40831877922584536),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/egwapq/usd/egwapq.usd"),
            visual_material_path="materials",
            scale=(0.9999971612622622, 0.9999875532712265, 1.000025292877313),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkHecjnt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkHecjnt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.487202971791434, -0.6329183064321716, 0.8735276787865365),
            rot=(7.589671327580123e-07, 0.0, 0.0, 0.999999999999712),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/hecjnt/usd/hecjnt.usd"),
            visual_material_path="materials",
            scale=(1.00005898073544, 0.9999884127862505, 0.9999572259424813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    stairsTikozn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/stairsTikozn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.0505896743168437, 0.6643689630204594, 1.4507977302707733),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stairs/tikozn/usd/tikozn.usd"),
            visual_material_path="materials",
            scale=(0.999996447385544, 1.000011004713109, 0.9999957382606783),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swingYzhrgz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swingYzhrgz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9367267920152286, 13.046010343401067, 1.2857532784331829),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swing/yzhrgz/usd/yzhrgz.usd"),
            visual_material_path="materials",
            scale=(1.0000140348020714, 0.9999916959025457, 0.9999931525764916),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletEssgie0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletEssgie0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.011976957321167, 0.40608900785446167, 0.39874768257141113),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/essgie/usd/essgie.usd"),
            visual_material_path="materials",
            scale=(1.0000360294540607, 1.0000356139397713, 1.0001188158551786),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetTynnnw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetTynnnw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.246416452503226, 0.22125855725535715, 1.8861040282913752),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/tynnnw/usd/tynnnw.usd"),
            visual_material_path="materials",
            scale=(0.9999917496947183, 0.999966644795944, 1.0000149324851784),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightMbhxbg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightMbhxbg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.492829254742185, -0.9520182920589438, 1.8020007210608715),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/mbhxbg/usd/mbhxbg.usd"),
            visual_material_path="materials",
            scale=(1.0001022629232403, 0.9992985287082558, 0.9997318021132363),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvDxyfxf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvDxyfxf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.384062294948728, 4.489275450866508, 1.30205289380393),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/dxyfxf/usd/dxyfxf.usd"),
            visual_material_path="materials",
            scale=(1.0000019489638452, 1.0007862363063031, 0.9999944860890104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallSocketNujxel0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallSocketNujxel0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0073962855010166, 7.370497434928778, 0.17663566892421345),
            rot=(0.9999999999999887, 0.0, 0.0, -1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_socket/nujxel/usd/nujxel.usd"),
            visual_material_path="materials",
            scale=(0.9969293984695493, 1.000093975483903, 1.0000929380862313),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowKvdqep0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowKvdqep0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.0960148023254295, -1.0693227694208591, 1.1894695118038894),
            rot=(0.9999999999999545, 0.0, 0.0, -3.017255176799947e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/kvdqep/usd/kvdqep.usd"),
            visual_material_path="materials",
            scale=(0.9999765956231336, 0.9996518446722387, 0.9999945917856793),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowLhzwtz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowLhzwtz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.539037519209087, 1.871965628881307, 1.1419931439155053),
            rot=(0.7071067811865477, 0.0, 0.0, -0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/lhzwtz/usd/lhzwtz.usd"),
            visual_material_path="materials",
            scale=(0.9999639513116041, 1.0003947409155876, 0.9999814355365522),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
