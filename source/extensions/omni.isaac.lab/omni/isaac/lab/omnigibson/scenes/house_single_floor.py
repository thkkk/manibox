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
class houseSingleFloorquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/house_single_floor/usd/house_single_floor_quick.usd"),
        )
    )
@configclass
class houseSingleFloorfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/house_single_floor/usd/house_single_floor_quick.usd"),
        )
    )
    bidetLcyvov0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bidetLcyvov0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.025285720825195, 11.229304313659668, 0.13989873230457306),
            rot=(1.0, -2.4010660126805305e-09, -2.3283064365386963e-10, 1.4831312000751495e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bidet/lcyvov/usd/lcyvov.usd"),
            visual_material_path="materials",
            scale=(1.4009721334287302, 0.6421069767251831, 0.7927430845230101),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.022454261779785, -2.0457229614257812, 0.5102150440216064),
            rot=(0.7071068286895752, 0.0, -3.521563485264778e-09, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(1.1551119961379417, 1.4341782608450264, 0.9998075722908952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.0076727867126465, -2.0457229614257812, 0.5102150440216064),
            rot=(0.7071068286895752, 0.0, -3.521563485264778e-09, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(1.1551119961379417, 1.4341782608450264, 0.9998075722908952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.69867706298828, -2.1056764125823975, 0.4670519232749939),
            rot=(0.7071068286895752, 0.0, -4.0381564758718014e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.6609985016751424, 1.3799090006790344, 1.20352024757076),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.992876052856445, -2.0457229614257812, 0.5102150440216064),
            rot=(0.7071068286895752, 0.0, -3.521563485264778e-09, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(1.1551119961379417, 1.4341782608450264, 0.9998075722908952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.123225212097168, 0.7399530410766602, 0.5102111101150513),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9249415167283926, 1.3249331095212973, 0.9998075722908952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.123225212097168, -0.19750270247459412, 0.5102111101150513),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9249415167283926, 1.3249331095212973, 0.9998075722908952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.123225212097168, -1.1349585056304932, 0.5102111101150513),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9249415167283926, 1.3249331095212973, 0.9998075722908952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.57786750793457, 1.6779897212982178, 0.4670558273792267),
            rot=(-2.8265640139579773e-07, 3.725290298461914e-09, -2.9103830456733704e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9997887578847033, 1.4230134911754604, 1.20352024757076),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.57786750793457, 0.6711459159851074, 0.4670558273792267),
            rot=(-2.8265640139579773e-07, 3.725290298461914e-09, -2.9103830456733704e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9997887578847033, 1.4230134911754604, 1.20352024757076),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.57786750793457, -0.33572909235954285, 0.4670558273792267),
            rot=(-2.8265640139579773e-07, 3.725290298461914e-09, -2.9103830456733704e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9997887578847033, 1.4230134911754604, 1.20352024757076),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopGjrero9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopGjrero9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.57786750793457, -1.3425729274749756, 0.4670558273792267),
            rot=(-2.8265640139579773e-07, 3.725290298461914e-09, -2.9103830456733704e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/gjrero/usd/gjrero.usd"),
            visual_material_path="materials",
            scale=(0.9997887578847033, 1.4230134911754604, 1.20352024757076),
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
            pos=(-14.292358598473188, 30.41016779986024, 0.8203938463656807),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(1.0000016665651164, 1.000010898539796, 0.9999892908641306),
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
            pos=(14.134653120281813, 25.31890608111024, 0.8203938463656807),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(1.0000016665651164, 1.000010898539796, 0.9999892908641306),
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
            pos=(4.793243486955137, 25.338485984320457, 1.8793334086221711),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.541268644996004, 0.5412584763808281, 0.5412585108063313),
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
            pos=(16.505980175584316, 26.852083880071856, 0.6635492722090152),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(1.0000226509484111, 0.9999972567468606, 1.0000313144307793),
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
            pos=(15.312060619924301, 27.492005543640406, 0.6635492722090152),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(1.0000226509484111, 0.9999972567468606, 1.0000313144307793),
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
            pos=(18.17805048808432, 28.040954973821854, 0.6635492722090152),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(1.0000226509484111, 0.9999972567468606, 1.0000313144307793),
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
            pos=(16.492501659964315, 28.083544817571855, 0.6635492722090153),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(1.0000226509484111, 0.9999972567468606, 1.0000313144307793),
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
            pos=(-0.21719291369011529, 26.61368513326834, 0.7614416455488756),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(1.0000228776896547, 1.00000235275531, 1.0000069752160938),
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
            pos=(-5.981217327760117, 28.33823200826838, 0.7614416455488756),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(1.0000228776896547, 1.00000235275531, 1.0000069752160938),
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
            pos=(-14.470451977301416, 39.140461500453384, 0.7614416455488756),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.9999722077019323, 1.00000235275531, 1.0000069752160938),
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
            pos=(12.785992358638417, 27.20013825826838, 0.23636359493387543),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.9999722077019323, 1.00000235275531, 1.0000069752160938),
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
            pos=(-3.7121479265106303, 26.006385591747875, 0.6680187341141673),
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
            pos=(-6.488466285885631, 25.749494966747875, 0.6680187341141673),
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

    bushLfyqkj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.000302223385631, 31.779541841747875, 0.6680187341141673),
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

    bushLfyqkj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.27891892260563, 28.234037935497877, 0.6680187341141672),
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

    bushLfyqkj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.90718503588563, 35.77112289643288, 0.6680187341141673),
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

    bushLfyqkj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLfyqkj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.328997535885631, 39.671951021432875, 0.6680187341141672),
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

    bushPjhpwk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushPjhpwk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9756593528071595, 27.92214175946809, 2.5338797834862015),
            rot=(0.6899669835574462, 0.7238408399645869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.9999929572923731, 0.9999954558318918, 0.9999949091043528),
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
            pos=(-2.8474968971928405, 37.145259923528094, 2.533879783486202),
            rot=(0.6899669835574462, 0.7238408399645869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.9999929572923731, 0.9999954558318918, 0.9999949091043528),
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
            pos=(-16.22965784689784, 29.725924962593094, 2.533879783486202),
            rot=(0.6899669835574462, 0.7238408399645869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.9999929572923731, 0.9999954558318918, 0.9999949091043528),
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
            pos=(10.093650815330445, 28.7400761804938, 1.8268804522539017),
            rot=(0.6899669835574462, 0.7238408399645869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.720986602050522, 0.7209813641477417, 0.7209926090549035),
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
            pos=(2.2289796483217352, 25.863353733411696, 0.28934163028516374),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(1.0000121778929023, 0.9999859052181417, 1.0000078629917677),
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
            pos=(-23.359554104123266, 27.945088108411696, 0.28934163028516374),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(1.0000121778929023, 0.9999859052181417, 1.0000078629917677),
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
            pos=(-18.623704494753262, 29.733800999036696, 0.28934163028516374),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(1.0000121778929023, 0.9999859052181417, 1.0000078629917677),
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
            pos=(-15.052393947873265, 34.566616428721694, 0.28934163028516374),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/xsqlhv/usd/xsqlhv.usd"),
            visual_material_path="materials",
            scale=(1.0000121778929023, 0.9999859052181417, 1.0000078629917677),
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
            pos=(7.748737522903855, 26.647059430025518, 0.5183791030078275),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.9999842670853416, 0.9999970521446234, 0.9999811926197563),
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
            pos=(-21.030582515156766, 29.032695237959615, 0.5183791030078275),
            rot=(-0.21643950565904907, 0.0, 0.0, 0.9762960311248156),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/yhjhta/usd/yhjhta.usd"),
            visual_material_path="materials",
            scale=(0.9999842670853416, 0.9999970521446234, 0.9999811926197563),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    fridgeDszchb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeDszchb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.819438457489014, -1.829745888710022, 0.9841838479042053),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/dszchb/usd/dszchb.usd"),
            visual_material_path="materials",
            scale=(0.9783052287015833, 1.0120731904233917, 1.0187902975411056),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletKfmkbm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletKfmkbm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.025466918945312, 10.649158477783203, 0.380855530500412),
            rot=(1.0000001192092896, -5.584297468885779e-10, -2.3283064365386963e-10, 1.490407157689333e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.2879249372857289, 0.5980809730670409, 1.44300048626473),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletKfmkbm1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletKfmkbm1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.472023010253906, 21.443445205688477, 0.380855530500412),
            rot=(0.7071070671081543, 1.7462298274040222e-09, 3.3760443329811096e-09, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.2879249372857289, 0.5980809730670409, 1.44300048626473),
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
            pos=(21.132622997947465, 32.07646704456467, 5.023830930233841),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.999996367163718, 1.0000029542129951, 0.9999996674004449),
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
            pos=(1.0103498771681132, -9.961493534896626, 4.103806694982209),
            rot=(0.9421626041375452, 0.0, 0.0, 0.3351561238658178),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.8115609453088171, 0.8115536896806336, 0.8115533242307884),
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
            pos=(10.987813239792871, 26.12237330012079, 4.566895857811405),
            rot=(0.9721131955454293, 0.0, 0.0, 0.23451212132095417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.8801290492790311, 0.8801221054261636, 0.88012066042033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeDyymaq3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeDyymaq3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.849889646919931, 34.3788497484272, 4.314124391079105),
            rot=(0.9377091592423643, 0.0, 0.0, 0.3474212611124688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.8311364546952451, 0.8311408377501852, 0.8311323167030957),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeDyymaq4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeDyymaq4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.338557286124228, 38.221265073656944, 5.164088986873843),
            rot=(0.8102243987447835, 0.0, 0.0, 0.5861198031790551),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.999996367163718, 1.0000029542129951, 0.9999996674004449),
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
            pos=(-13.833162849718354, 32.91124356563923, 3.493253761288809),
            rot=(0.9775486719687262, 0.0, 0.0, 0.21070973857935413),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.6828617756251455, 0.6828612497844128, 0.6828724319687489),
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
            pos=(-14.429511864504512, -11.342931019845214, 4.144958983900311),
            rot=(0.9042948220476961, 0.0, 0.0, 0.4269085087202241),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.8179780441793841, 0.8179672332540282, 0.8179809634460647),
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
            pos=(11.28090091829131, -11.001828397185752, 3.6867624263771437),
            rot=(0.9421626041375452, 0.0, 0.0, 0.3351561238658178),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.7062019868334054, 0.7061948593326175, 0.7062073710490011),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.43763362543603, -12.26820109374678, 5.2393252267822685),
            rot=(0.33577142252354325, 0.0, 0.0, 0.9419434971464671),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(1.029015427887096, 1.0290170523930615, 1.0290237716022508),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.573790793109894, 26.235169741657533, 3.961298822401919),
            rot=(0.9123868733566445, 0.0, 0.0, 0.4093289549085019),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.752477940758039, 0.7524723730503513, 0.7524724706131767),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.600859087463167, 38.20600879354473, 4.107597775462336),
            rot=(0.9966437857639949, 0.0, 0.0, -0.08186063949183504),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.7990156095891872, 0.7990178092159246, 0.7990110692289258),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.279150751791968, 40.92523721921679, 4.252384947777107),
            rot=(-0.6328609560403394, 0.0, 0.0, 0.7742654650181083),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.8244971245780214, 0.8244947983468454, 0.8245011808355772),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeFlkzbo7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeFlkzbo7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-21.24845115247714, 41.196463524191, 3.899612054821919),
            rot=(-0.6328609560403394, 0.0, 0.0, 0.7742654650181083),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.752477940758039, 0.7524723730503513, 0.7524724706131767),
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
            pos=(17.939327723380647, -11.513519555479164, 6.755156883002421),
            rot=(0.9299236992622086, 0.0, 0.0, 0.3677525167153712),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(1.0415375461669119, 1.0415475333376825, 1.041539784099004),
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
            pos=(15.413042336863082, 39.06940234039384, 5.165378500876312),
            rot=(0.9911865243391035, 0.0, 0.0, -0.13247367273752103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.7750551780084498, 0.7750499079430622, 0.7750435196489146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.99323507211857, 26.4335979136206, 4.2781099617495295),
            rot=(0.8524125810397328, 0.0, 0.0, 0.522869765510668),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6568446327783384, 0.6568429218554743, 0.6568325706786017),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.722020924528513, -10.897346642851558, 4.130835280241613),
            rot=(0.8440619971793116, 0.0, 0.0, 0.5362456013037978),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6341900881403496, 0.634205962401698, 0.6341961121329214),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0560177290232398, -10.544415183008848, 3.1896943758706784),
            rot=(0.6509244459050978, 0.0, 0.0, 0.7591425200337163),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.48443234654250406, 0.4844309323108114, 0.4844397270659591),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.71876196727375, -10.59271506182124, 2.952132697044749),
            rot=(0.9254569996663962, 0.0, 0.0, 0.3788526649879502),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.45185643724973507, 0.45187329445160973, 0.45186604334969505),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.531849822483345, -11.687906124479172, 4.292904936616575),
            rot=(0.9254569996663962, 0.0, 0.0, 0.3788526649879502),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6672003428903556, 0.6672089174960559, 0.6671976069026018),
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
            pos=(4.857352121894269, 40.54788368282887, 4.916062841445803),
            rot=(0.8102243987447835, 0.0, 0.0, 0.5861198031790551),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.7416791586628759, 0.7416758551527407, 0.7416742574824378),
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
            pos=(0.7604794009966729, 41.29987814056622, 4.617644863964055),
            rot=(0.8102243987447835, 0.0, 0.0, 0.5861198031790551),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.7013993325759572, 0.7013993852174973, 0.7014074802617565),
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
            pos=(-5.389442050999904, 38.281785850590126, 3.748877910259692),
            rot=(0.8263685105074552, 0.0, 0.0, 0.5631297229250911),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.5636889623446306, 0.5636974001686246, 0.56369735380415),
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
            pos=(-14.529866202905596, 40.77714490177417, 4.878969328970069),
            rot=(-0.6328609560403394, 0.0, 0.0, 0.7742654650181083),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.7524692142321299, 0.7524624281820811, 0.7524746102169317),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.719339356757358, 36.916478777049726, 4.862486476247416),
            rot=(-0.5214184831950065, 0.0, 0.0, 0.8533010988992213),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.7363984323143637, 0.7363815280236607, 0.7363904156998917),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.634435421447855, 29.925530121128844, 4.650746607184928),
            rot=(-0.49689552302069223, 0.0, 0.0, 0.8678103705314848),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.7061999928927863, 0.7061989154186258, 0.7062034673342663),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8040460722360556, 26.147470912626478, 4.217268156354463),
            rot=(0.9721131955454293, 0.0, 0.0, 0.23451212132095417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6405452479883424, 0.6405641029258735, 0.6405532342775471),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeRrhqpw9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeRrhqpw9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.051288574432025, 25.940786395779423, 4.330551131608729),
            rot=(0.9170766216423691, 0.0, 0.0, 0.398711010679438),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/rrhqpw/usd/rrhqpw.usd"),
            visual_material_path="materials",
            scale=(0.6513581638448195, 0.6513506759552139, 0.651353587012041),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    baseboardAxyzbi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/baseboardAxyzbi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.89549091012432, 15.835763777111943, 0.41440650874229484),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/baseboard/axyzbi/usd/axyzbi.usd"),
            visual_material_path="materials",
            scale=(0.9999654237916885, 1.000011842533381, 0.9991655642911452),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    baseboardGmhhek0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/baseboardGmhhek0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.841079960843004, 11.73034936523054, 0.6554137294928724),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/baseboard/gmhhek/usd/gmhhek.usd"),
            visual_material_path="materials",
            scale=(1.0000550725066715, 1.0000129353087992, 1.0000215481892716),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    saunaHeaterEtqusf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/saunaHeaterEtqusf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.163701726452231, 5.499348606419113, 0.532529480876765),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sauna_heater/etqusf/usd/etqusf.usd"),
            visual_material_path="materials",
            scale=(0.9999455800745867, 0.9999434185652895, 1.0000093250339626),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coatrackGypwkr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coatrackGypwkr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1683994443606167, -1.225093915509627, 1.4657068345750186),
            rot=(-4.571286092006821e-13, -8.781764223086344e-07, 0.999999999999479, 5.205485536562985e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coatrack/gypwkr/usd/gypwkr.usd"),
            visual_material_path="materials",
            scale=(0.9992898705573384, 0.9999550839572388, 0.9999756818077384),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coatrackGypwkr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coatrackGypwkr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1673058083113548, -1.6559293645849944, 1.4657100830412428),
            rot=(1.9304567907042195e-06, -0.0005687030332827884, 0.9999997325487362, -0.0004598647513561158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coatrack/gypwkr/usd/gypwkr.usd"),
            visual_material_path="materials",
            scale=(0.9992898705573384, 0.9999550839572388, 0.9999756818077384),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskBhkhxo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskBhkhxo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.9094519810308, 13.200728759800011, 0.4939129493841572),
            rot=(0.9999991910549354, 0.0, 0.0, -0.0012719628433290671),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/bhkhxo/usd/bhkhxo.usd"),
            visual_material_path="materials",
            scale=(1.0000342760885437, 0.9999953138152106, 1.0000052588315416),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskBvhpnd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskBvhpnd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.281270247354435, 19.01219954723227, 0.32034866333042783),
            rot=(0.7080054051704394, 0.0, 0.0, 0.7062070137356624),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/bvhpnd/usd/bvhpnd.usd"),
            visual_material_path="materials",
            scale=(0.9999885560391689, 0.9999881984196134, 0.999997846086365),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskNbpuns0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskNbpuns0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.95346384267184, 7.6662499180641515, 0.42346164840545136),
            rot=(0.9999991913581663, 0.0, 0.0, -0.0012717244251529397),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/nbpuns/usd/nbpuns.usd"),
            visual_material_path="materials",
            scale=(1.0000795878767508, 0.9999758963554835, 0.9999654425398565),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskXhjsub0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskXhjsub0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.719300738215267, 18.511400344546114, 0.41470381447812005),
            rot=(-5.205485537560791e-07, 0.0, 0.0, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/xhjsub/usd/xhjsub.usd"),
            visual_material_path="materials",
            scale=(1.0000199630685669, 0.999974995272036, 1.0000512477675945),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hammockAiftuk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hammockAiftuk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(16.85271374384994, 21.64841227718206, 0.9105566108424822),
            rot=(0.840862165905923, -0.07356590128336396, -0.046735212815180956, 0.5341860125457106),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hammock/aiftuk/usd/aiftuk.usd"),
            visual_material_path="materials",
            scale=(0.999987013259035, 0.9999943298921651, 0.9999842356729467),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingMkhabj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingMkhabj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.914696998171644, -0.4754721569672225, 1.3737187201276506),
            rot=(-0.7062067750142306, 0.0, 0.0, 0.708005643285419),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/mkhabj/usd/mkhabj.usd"),
            visual_material_path="materials",
            scale=(0.9999919258817944, 0.9993465111346642, 1.0004176338714177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingOzuykd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingOzuykd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.053323670527483, 23.744293946027515, 1.8969711758809844),
            rot=(0.9999991913581663, 0.0, 0.0, -0.0012717244251529397),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/ozuykd/usd/ozuykd.usd"),
            visual_material_path="materials",
            scale=(0.9999817444380412, 0.9990232690583518, 0.9990244249197844),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingOzuykd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingOzuykd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.672580196329193, 19.95856445214614, 1.8969683072259371),
            rot=(0.999999193479171, 3.205894059921345e-10, 1.995372621794016e-07, -0.0012700554978939762),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/ozuykd/usd/ozuykd.usd"),
            visual_material_path="materials",
            scale=(0.9999817444380412, 0.9990232690583518, 0.9990244249197844),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    rangeHoodBeanpv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/rangeHoodBeanpv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.055932334021863, -0.505980666382744, 1.4849475857143193),
            rot=(2.145821253189594e-06, 0.9999991908048824, 0.0012721576058303786, -4.098160250652074e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/range_hood/beanpv/usd/beanpv.usd"),
            visual_material_path="materials",
            scale=(0.9999140065854364, 0.9999754058747888, 1.0005643397993131),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    rangeHoodUokzpw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/rangeHoodUokzpw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.055176734924316, -1.6233526468276978, 1.4874216318130493),
            rot=(4.644257955987996e-08, 0.0012722015380859375, 0.9999992251396179, 2.145709913747851e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/range_hood/uokzpw/usd/uokzpw.usd"),
            visual_material_path="materials",
            scale=(1.0000019763746781, 0.9999862598080846, 0.9980920649841474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    rangeHoodUokzpw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/rangeHoodUokzpw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.0608954429626465, 0.6266942620277405, 1.487425446510315),
            rot=(4.644257955987996e-08, 0.0012722015380859375, 0.9999992251396179, 2.145709913747851e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/range_hood/uokzpw/usd/uokzpw.usd"),
            visual_material_path="materials",
            scale=(1.0000019763746781, 0.9999862598080846, 0.9980920649841474),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    saunaBenchGlyeot0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/saunaBenchGlyeot0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.29859176563895, 3.8881779272837944, 0.5733862316450824),
            rot=(0.8660253998985326, 0.0, 0.0, 0.5000000067305868),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sauna_bench/glyeot/usd/glyeot.usd"),
            visual_material_path="materials",
            scale=(0.9999980569146143, 0.9999847008029383, 1.0000000771701407),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfHibwic0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfHibwic0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.122638376951084, 15.905878300159275, 1.544764375803355),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/hibwic/usd/hibwic.usd"),
            visual_material_path="materials",
            scale=(1.0000341654867804, 1.0000226362849454, 1.0000045758818779),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfJaysra0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfJaysra0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.892943744692428, 12.474979138016336, 0.9082358178183592),
            rot=(0.7080054051704394, 0.0, 0.0, 0.7062070137356624),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/jaysra/usd/jaysra.usd"),
            visual_material_path="materials",
            scale=(0.9999809052038738, 0.9999681143117684, 0.9999980565977618),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfRkagxx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfRkagxx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.252656038952498, 18.972253663138186, 1.3062577131978024),
            rot=(0.708005524227939, 0.0, 0.0, 0.7062068943749567),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/rkagxx/usd/rkagxx.usd"),
            visual_material_path="materials",
            scale=(1.0000891598247217, 0.999993874846123, 1.000010695044414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfSclnqc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfSclnqc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.485589239573105, 4.465053207820195, 1.5163209759006337),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/sclnqc/usd/sclnqc.usd"),
            visual_material_path="materials",
            scale=(0.9999236307963029, 0.9999691813708527, 1.0000043236382248),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfZfpyqe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfZfpyqe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.439529063371143, 7.7956804805644175, 0.7794621852612411),
            rot=(0.9999999999999319, 3.0428954147666166e-07, 6.347974510004021e-14, 2.0861739564801046e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/zfpyqe/usd/zfpyqe.usd"),
            visual_material_path="materials",
            scale=(0.9999043318044665, 1.0000400038229695, 0.9999983371532631),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfZfpyqe1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfZfpyqe1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.439527110241187, 6.925741246358037, 0.7794622272212413),
            rot=(0.9999999999999889, 0.0, 0.0, 1.4901161193847614e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/zfpyqe/usd/zfpyqe.usd"),
            visual_material_path="materials",
            scale=(0.9999043318044665, 1.0000400038229695, 0.9999983371532631),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightQhvhzq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightQhvhzq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.48421564572601, 16.755834764360323, 2.516401480139552),
            rot=(0.46174837477950803, 0.0, 0.0, 0.8870109573102708),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/qhvhzq/usd/qhvhzq.usd"),
            visual_material_path="materials",
            scale=(0.9999796888125491, 1.0003056098148941, 1.0000614374063799),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightQhvhzq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightQhvhzq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.246777501207827, 16.753881203560866, 2.5164053863895517),
            rot=(0.4617487284302988, 0.0, 0.0, 0.8870107732113529),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/qhvhzq/usd/qhvhzq.usd"),
            visual_material_path="materials",
            scale=(0.9999796888125491, 1.0003056098148941, 1.0000614374063799),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightQhvhzq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightQhvhzq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.791108568377442, 16.777133974709134, 2.516401480139552),
            rot=(0.8870108713639837, 0.0, 0.0, -0.4617485398808602),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/qhvhzq/usd/qhvhzq.usd"),
            visual_material_path="materials",
            scale=(0.9999796888125491, 1.0003056098148941, 1.0000614374063799),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightQhvhzq3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightQhvhzq3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.43149919337745, 16.777133974709134, 2.516401480139552),
            rot=(0.8870108713639837, 0.0, 0.0, -0.4617485398808602),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/qhvhzq/usd/qhvhzq.usd"),
            visual_material_path="materials",
            scale=(0.9999796888125491, 1.0003056098148941, 1.0000614374063799),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    structuralElementBmcetq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/structuralElementBmcetq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.45154326785106, 16.77143583808851, 2.6896132885587134),
            rot=(0.03374786169630212, 0.0, 0.0, 0.9994303786812404),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/structural_element/bmcetq/usd/bmcetq.usd"),
            visual_material_path="materials",
            scale=(0.9999887931447798, 1.0001434200710748, 0.9991729208643437),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wardrobePyuwgc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wardrobePyuwgc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.985013225079022, 0.03717687809643135, 1.504867838145335),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wardrobe/pyuwgc/usd/pyuwgc.usd"),
            visual_material_path="materials",
            scale=(0.999989590543974, 0.9999774223845515, 0.9999811143633515),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wardrobeUzdupi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wardrobeUzdupi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9496401401955153, -0.5022935410280572, 0.9685120164118817),
            rot=(0.000898314358755427, 0.000898259294307655, 0.7071059423873072, 0.7071064788291163),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wardrobe/uzdupi/usd/uzdupi.usd"),
            visual_material_path="materials",
            scale=(1.000113530349796, 1.0000041557611083, 1.0000402870042473),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairJzthdw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairJzthdw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.447434902191162, 8.492096900939941, 0.47906413674354553),
            rot=(0.7680711150169373, 3.8743019104003906e-07, 2.8777867555618286e-07, 0.6403647661209106),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/jzthdw/usd/jzthdw.usd"),
            visual_material_path="materials",
            scale=(0.9999898917147156, 1.0000642944551363, 0.9999972073012078),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairJzthdw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairJzthdw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.5386950969696045, 8.766280174255371, 0.47906410694122314),
            rot=(0.9272984266281128, 6.854534149169922e-07, 4.423782229423523e-08, 0.3743230700492859),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/jzthdw/usd/jzthdw.usd"),
            visual_material_path="materials",
            scale=(0.9999898917147156, 1.0000642944551363, 0.9999972073012078),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.8105785846710205, 1.585667371749878, 0.49113941192626953),
            rot=(0.7324182987213135, 1.4901161193847656e-08, 0.0, 0.6808549761772156),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.966419219970703, 2.4371535778045654, 0.4911423623561859),
            rot=(0.974720299243927, 4.1350722312927246e-07, 8.102506399154663e-08, 0.22342854738235474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.998846054077148, 3.247643232345581, 0.4911423325538635),
            rot=(0.9993351697921753, 5.606561899185181e-07, -2.6583438739180565e-07, -0.036460913717746735),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.912980079650879, 4.015918254852295, 0.4911423325538635),
            rot=(0.9967935681343079, 4.5821070671081543e-07, -4.0117811295203865e-09, -0.08001656085252762),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.940257549285889, 4.8835835456848145, 0.4911423921585083),
            rot=(0.9860265254974365, 4.0978193283081055e-07, -1.979060471057892e-08, -0.16658835113048553),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.883685827255249, 5.745140075683594, 0.49114227294921875),
            rot=(0.7941557765007019, 4.76837158203125e-07, -3.878958523273468e-07, -0.6077142357826233),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.8112964630126953, 4.772987365722656, 0.49114230275154114),
            rot=(0.12341976165771484, 8.940696716308594e-08, 6.025657057762146e-07, 0.9923545122146606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.626166582107544, 4.042455196380615, 0.4911423325538635),
            rot=(-0.007164936512708664, 2.086162567138672e-07, 4.954636096954346e-07, 0.9999743700027466),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.7508296966552734, 3.189042329788208, 0.49114230275154114),
            rot=(0.12341989576816559, 8.940696716308594e-08, 6.537884473800659e-07, 0.9923546314239502),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQhcrgb9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQhcrgb9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.4984543323516846, 2.2419867515563965, 0.48228296637535095),
            rot=(0.29386547207832336, 8.940696716308594e-08, 3.688037395477295e-07, 0.9558468461036682),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qhcrgb/usd/qhcrgb.usd"),
            visual_material_path="materials",
            scale=(0.9999896152609897, 1.0000641026523753, 0.9999970695674039),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableRhjoby0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableRhjoby0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.294749736785889, 3.5005764961242676, 0.7426828742027283),
            rot=(-2.1781692339573056e-05, -0.7062069773674011, 0.7080055475234985, -3.9663384086452425e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/rhjoby/usd/rhjoby.usd"),
            visual_material_path="materials",
            scale=(0.9999759423703778, 0.9999861507775536, 0.9999518834573518),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    capTkwpyr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/capTkwpyr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.757524490356445, 19.02189064025879, 0.9563401341438293),
            rot=(0.7080055475234985, -5.093170329928398e-11, -8.731149137020111e-11, 0.7062069177627563),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cap/tkwpyr/usd/tkwpyr.usd"),
            visual_material_path="materials",
            scale=(0.9987610303409111, 0.9987612287074082, 1.00081748595427),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableQtwqqb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableQtwqqb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.316454529762268, 4.242106914520264, 0.2910210192203522),
            rot=(-4.0133926404450904e-07, 0.9999992847442627, 0.0012725034030154347, -5.422648996500357e-10),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qtwqqb/usd/qtwqqb.usd"),
            visual_material_path="materials",
            scale=(0.999983725954601, 0.9999822827199182, 0.9999867611772334),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableRlsebe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableRlsebe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.890363693237305, 1.0128507614135742, 0.13793502748012543),
            rot=(0.9993909001350403, 1.2164491636212915e-11, -1.1368683772161603e-13, -0.03489954024553299),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/rlsebe/usd/rlsebe.usd"),
            visual_material_path="materials",
            scale=(0.9999920096688708, 1.0000126553184019, 0.9998551159919425),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableWgtaip0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableWgtaip0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.860642671585083, 3.644289255142212, 0.6904381513595581),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/wgtaip/usd/wgtaip.usd"),
            visual_material_path="materials",
            scale=(0.9999978082156306, 1.0000022374884763, 0.9999971477922046),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    eamesChairHndxiw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/eamesChairHndxiw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.08364486694336, 13.292463302612305, 0.5130184888839722),
            rot=(0.9238795638084412, 0.0, -1.1757947504520416e-08, 0.3826834261417389),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/eames_chair/hndxiw/usd/hndxiw.usd"),
            visual_material_path="materials",
            scale=(0.9999954104961, 1.0000274491967533, 0.9999750425492278),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    eamesChairUbmrms0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/eamesChairUbmrms0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2613638937473297, 22.622690200805664, 0.3695724308490753),
            rot=(-0.6299298405647278, -1.4901161193847656e-08, 5.238689482212067e-09, 0.7766520380973816),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/eames_chair/ubmrms/usd/ubmrms.usd"),
            visual_material_path="materials",
            scale=(0.9999972814777855, 0.9999995912826029, 0.9999687805254563),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    eamesChairUbmrms1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/eamesChairUbmrms1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.435006141662598, 20.827253341674805, 0.36818960309028625),
            rot=(0.9778611063957214, -2.868473529815674e-07, -1.7197453416883945e-07, -0.20925551652908325),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/eames_chair/ubmrms/usd/ubmrms.usd"),
            visual_material_path="materials",
            scale=(0.9999972814777855, 0.9999995912826029, 0.9999687805254563),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    eamesChairUbmrms2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/eamesChairUbmrms2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.99227237701416, 22.489551544189453, 0.36818957328796387),
            rot=(0.7809475064277649, -3.2782554626464844e-07, -4.7730281949043274e-08, -0.6245965957641602),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/eames_chair/ubmrms/usd/ubmrms.usd"),
            visual_material_path="materials",
            scale=(0.9999972814777855, 0.9999995912826029, 0.9999687805254563),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    eamesChairUbmrms3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/eamesChairUbmrms3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6054328680038452, 23.386140823364258, 0.3707364499568939),
            rot=(-0.6360722184181213, 3.2782554626464844e-07, -3.294553607702255e-08, 0.7716295719146729),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/eames_chair/ubmrms/usd/ubmrms.usd"),
            visual_material_path="materials",
            scale=(0.9999972814777855, 0.9999995912826029, 0.9999687805254563),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampDisyzd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampDisyzd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.480209350585938, 5.662053108215332, 0.20996075868606567),
            rot=(-0.3833925724029541, 0.0005868729203939438, -0.0022712433710694313, 0.9235826134681702),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/disyzd/usd/disyzd.usd"),
            visual_material_path="materials",
            scale=(1.000095930307741, 0.9999827818797092, 0.9999766129966442),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    waterGlassBbpraa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/waterGlassBbpraa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.925058841705322, -2.10381817817688, 0.9489089846611023),
            rot=(0.00127372145652771, -2.701929770410061e-05, 1.5374351278296672e-05, 0.9999992847442627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/water_glass/bbpraa/usd/bbpraa.usd"),
            visual_material_path="materials",
            scale=(1.0000676965796824, 1.0000731757195458, 0.9999059262302981),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandWbxekb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandWbxekb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.671358108520508, 25.408493041992188, 0.15502329170703888),
            rot=(4.906759443201736e-10, 0.0012724836124107242, 0.9999992847442627, 4.0134182199835777e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/wbxekb/usd/wbxekb.usd"),
            visual_material_path="materials",
            scale=(0.9999954430769802, 0.9999978773100596, 0.9999998199836988),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandWbxekb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandWbxekb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.663957595825195, 22.49925422668457, 0.15502330660820007),
            rot=(2.5279476290052116e-09, 0.0012724836124107242, 0.9999992847442627, 4.013381840195507e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/wbxekb/usd/wbxekb.usd"),
            visual_material_path="materials",
            scale=(0.9999954430769802, 0.9999978773100596, 0.9999998199836988),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandWxzubg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandWxzubg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.552570343017578, 13.901435852050781, 0.2974851727485657),
            rot=(1.0, 9.640399366617203e-05, -0.00010871539416257292, 0.0003105987561866641),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/wxzubg/usd/wxzubg.usd"),
            visual_material_path="materials",
            scale=(1.0000836772705415, 0.9999725753537742, 0.999922729238511),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanLsaxch0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanLsaxch0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.4966888129711151, 21.36858558654785, 0.23512215912342072),
            rot=(0.9946035742759705, 4.656612873077393e-10, -9.313225746154785e-10, -0.10374819487333298),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/lsaxch/usd/lsaxch.usd"),
            visual_material_path="materials",
            scale=(1.0000508470170824, 0.9999374587710657, 1.0001606363511517),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanLsaxch1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanLsaxch1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6840803623199463, 21.25132179260254, 0.23373934626579285),
            rot=(0.9938699007034302, 2.3283064365386963e-10, -1.3969838619232178e-09, 0.11055667698383331),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/lsaxch/usd/lsaxch.usd"),
            visual_material_path="materials",
            scale=(1.0000508470170824, 0.9999374587710657, 1.0001606363511517),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanLsaxch2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanLsaxch2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.259360313415527, 20.33123016357422, 0.23373936116695404),
            rot=(0.839418351650238, -1.3969838619232178e-09, -1.1641532182693481e-09, 0.5434859991073608),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/lsaxch/usd/lsaxch.usd"),
            visual_material_path="materials",
            scale=(1.0000508470170824, 0.9999374587710657, 1.0001606363511517),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanLsaxch3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanLsaxch3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8208354711532593, 22.128442764282227, 0.2362862229347229),
            rot=(0.9953954815864563, -1.862645149230957e-09, -2.561137080192566e-09, -0.0958537682890892),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/lsaxch/usd/lsaxch.usd"),
            visual_material_path="materials",
            scale=(1.0000508470170824, 0.9999374587710657, 1.0001606363511517),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanLsaxch4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanLsaxch4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.868142604827881, 21.63593101501465, 0.23373934626579285),
            rot=(0.9938699007034302, 2.3283064365386963e-10, -1.3969838619232178e-09, 0.11055667698383331),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/lsaxch/usd/lsaxch.usd"),
            visual_material_path="materials",
            scale=(1.0000508470170824, 0.9999374587710657, 1.0001606363511517),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanWkmbra0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanWkmbra0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.11432332545518875, -1.7056533098220825, 0.1582280546426773),
            rot=(-0.7062069177627563, -9.313225746154785e-10, -4.656612873077393e-10, 0.7080055475234985),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/wkmbra/usd/wkmbra.usd"),
            visual_material_path="materials",
            scale=(1.0000683126869085, 0.9999892308103429, 0.999888534191706),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantBjwskl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantBjwskl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.167898178100586, 6.912317752838135, 0.4653093218803406),
            rot=(0.8863635063171387, 0.0055569838732481, -0.00996822863817215, -0.4628494381904602),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/bjwskl/usd/bjwskl.usd"),
            visual_material_path="materials",
            scale=(0.9999642009070153, 0.9999891273803572, 1.000029992550093),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantBjwskl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantBjwskl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.907569885253906, 6.846793174743652, 0.5248417258262634),
            rot=(0.2887730300426483, 0.01830197125673294, 0.029750198125839233, 0.9567603468894958),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/bjwskl/usd/bjwskl.usd"),
            visual_material_path="materials",
            scale=(0.9999642009070153, 0.9999891273803572, 1.000029992550093),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantLligdl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantLligdl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.255252361297607, 3.5543460845947266, 0.7896942496299744),
            rot=(0.9999359846115112, 0.0009812373900786042, 0.003293620888143778, 0.010785272344946861),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/lligdl/usd/lligdl.usd"),
            visual_material_path="materials",
            scale=(0.9999939254436748, 1.0000128215650632, 1.0000044040475302),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantLligdl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantLligdl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.279479503631592, 2.7440061569213867, 0.7967004179954529),
            rot=(0.9110575318336487, 0.004301862791180611, 0.0013883761130273342, 0.4122547507286072),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/lligdl/usd/lligdl.usd"),
            visual_material_path="materials",
            scale=(0.9999939254436748, 1.0000128215650632, 1.0000044040475302),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantLligdl2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantLligdl2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.262399196624756, 1.9663002490997314, 0.798952579498291),
            rot=(0.9783895611763, 0.006330564618110657, 0.0001452743890695274, -0.20667390525341034),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/lligdl/usd/lligdl.usd"),
            visual_material_path="materials",
            scale=(0.9999939254436748, 1.0000128215650632, 1.0000044040475302),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantRkqvba0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantRkqvba0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5554790496826172, 2.1975419521331787, 0.6952952146530151),
            rot=(-0.10381139069795609, -0.002438740339130163, 0.0009059631265699863, 0.9945937395095825),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/rkqvba/usd/rkqvba.usd"),
            visual_material_path="materials",
            scale=(0.9999597425298039, 0.9999465082965598, 0.9999991643603101),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaBskyog0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaBskyog0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.12004899978637695, 4.238096237182617, 0.3177341818809509),
            rot=(2.306748569935735e-09, 2.822544047376141e-07, 1.0000001192092896, 2.821470843628049e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/bskyog/usd/bskyog.usd"),
            visual_material_path="materials",
            scale=(0.9999763382220713, 0.999999061829047, 0.9999567971819253),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaCozrjc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaCozrjc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.4872493743896484, 4.98220682144165, 0.30958157777786255),
            rot=(1.2269083526916802e-08, 0.9961947798728943, 0.08715564012527466, 4.909452400170267e-09),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/cozrjc/usd/cozrjc.usd"),
            visual_material_path="materials",
            scale=(1.000036570853365, 1.0000290465619632, 1.0000556679903934),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaCozrjc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaCozrjc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5351576805114746, 3.66676664352417, 0.3095720410346985),
            rot=(-3.046940400963649e-05, 0.9990485310554504, -0.043613236397504807, -0.00011303237988613546),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/cozrjc/usd/cozrjc.usd"),
            visual_material_path="materials",
            scale=(1.000036570853365, 1.0000290465619632, 1.0000556679903934),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaHiphpn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaHiphpn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.022258758544922, -1.111728310585022, 0.2440476268529892),
            rot=(0.7077363729476929, -0.0008014701306819916, 0.0008964166045188904, 0.7064757347106934),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/hiphpn/usd/hiphpn.usd"),
            visual_material_path="materials",
            scale=(1.0000189022351123, 1.0000083625438676, 1.0000444121781973),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretIvtoxu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretIvtoxu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.236361503601074, 0.9723858833312988, 0.46434497833251953),
            rot=(0.7372773289680481, -9.313225746154785e-10, 1.979060471057892e-09, 0.6755903363227844),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/ivtoxu/usd/ivtoxu.usd"),
            visual_material_path="materials",
            scale=(1.0000831256740106, 1.0000840015007504, 0.9999554512021614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretIvtoxu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretIvtoxu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.743645191192627, 0.8805880546569824, 0.46434497833251953),
            rot=(0.7372773289680481, 2.1606683731079102e-07, -1.2264354154467583e-07, 0.6755903363227844),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/ivtoxu/usd/ivtoxu.usd"),
            visual_material_path="materials",
            scale=(1.0000831256740106, 1.0000840015007504, 0.9999554512021614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretIvtoxu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretIvtoxu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.226862907409668, 0.9280000925064087, 0.46434497833251953),
            rot=(0.7372773289680481, 2.1606683731079102e-07, -1.2264354154467583e-07, 0.6755903363227844),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/ivtoxu/usd/ivtoxu.usd"),
            visual_material_path="materials",
            scale=(1.0000831256740106, 1.0000840015007504, 0.9999554512021614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretIvtoxu3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretIvtoxu3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.724739074707031, 0.9513068199157715, 0.46434497833251953),
            rot=(0.7372773289680481, 2.1606683731079102e-07, -1.2264354154467583e-07, 0.6755903363227844),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/ivtoxu/usd/ivtoxu.usd"),
            visual_material_path="materials",
            scale=(1.0000831256740106, 1.0000840015007504, 0.9999554512021614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretIvtoxu4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretIvtoxu4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.22973918914795, 0.9246505498886108, 0.46434497833251953),
            rot=(0.7372773289680481, 2.1606683731079102e-07, -1.2264354154467583e-07, 0.6755903363227844),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/ivtoxu/usd/ivtoxu.usd"),
            visual_material_path="materials",
            scale=(1.0000831256740106, 1.0000840015007504, 0.9999554512021614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairGktknj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairGktknj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.626365661621094, 7.4562087059021, 0.3403583765029907),
            rot=(0.9994497895240784, -0.011940007098019123, 0.027179747819900513, 0.014798466116189957),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/gktknj/usd/gktknj.usd"),
            visual_material_path="materials",
            scale=(0.9999232304209734, 1.0000268849647826, 1.0000270253793744),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairJgoolz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairJgoolz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.276880264282227, 2.908891201019287, 0.31706246733665466),
            rot=(0.5011012554168701, 0.0, -1.862645149230957e-09, 0.865388810634613),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/jgoolz/usd/jgoolz.usd"),
            visual_material_path="materials",
            scale=(0.9999509151790076, 1.0000683968238853, 0.9999845192352206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairJgoolz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairJgoolz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.163782119750977, 4.046059608459473, 0.3170624077320099),
            rot=(0.8427073955535889, 1.1920928955078125e-07, -5.8673322200775146e-08, -0.5383720993995667),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/jgoolz/usd/jgoolz.usd"),
            visual_material_path="materials",
            scale=(0.9999509151790076, 1.0000683968238853, 0.9999845192352206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairJgoolz2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairJgoolz2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.25508975982666, 4.027687072753906, 0.3170623779296875),
            rot=(0.7925785183906555, 7.450580596923828e-08, 8.754432201385498e-08, -0.6097699999809265),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/jgoolz/usd/jgoolz.usd"),
            visual_material_path="materials",
            scale=(0.9999509151790076, 1.0000683968238853, 0.9999845192352206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairJgoolz3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairJgoolz3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.437380790710449, 4.110445976257324, 0.3170624077320099),
            rot=(0.7364175319671631, 1.043081283569336e-07, 5.4016709327697754e-08, -0.6765274405479431),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/jgoolz/usd/jgoolz.usd"),
            visual_material_path="materials",
            scale=(0.9999509151790076, 1.0000683968238853, 0.9999845192352206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairJgoolz4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairJgoolz4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.403810501098633, 2.8983376026153564, 0.3170623481273651),
            rot=(0.7381360530853271, -1.4901161193847656e-07, 1.6391277313232422e-07, 0.6746519804000854),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/jgoolz/usd/jgoolz.usd"),
            visual_material_path="materials",
            scale=(0.9999509151790076, 1.0000683968238853, 0.9999845192352206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairJgoolz5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairJgoolz5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.2552032470703125, 2.6935791969299316, 0.3170662820339203),
            rot=(0.7381360530853271, -1.4901161193847656e-07, 1.6391277313232422e-07, 0.6746519804000854),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/jgoolz/usd/jgoolz.usd"),
            visual_material_path="materials",
            scale=(0.9999509151790076, 1.0000683968238853, 0.9999845192352206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairRljebp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairRljebp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.3800048828125, 5.619802951812744, 0.19042636454105377),
            rot=(0.7656948566436768, -1.4901161193847656e-08, 0.0, 0.6432041525840759),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/rljebp/usd/rljebp.usd"),
            visual_material_path="materials",
            scale=(1.0000435906520102, 1.000118659891056, 0.9999748898467403),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairRljebp1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairRljebp1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.101482391357422, 5.593684196472168, 0.19042587280273438),
            rot=(0.7656948566436768, 3.5762786865234375e-07, -7.450580596923828e-09, 0.6432040929794312),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/rljebp/usd/rljebp.usd"),
            visual_material_path="materials",
            scale=(1.0000435906520102, 1.000118659891056, 0.9999748898467403),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairTbzfgf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairTbzfgf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.804689407348633, 18.55786895751953, 0.40791741013526917),
            rot=(-0.12659162282943726, 0.14717943966388702, 0.017631344497203827, 0.9808171391487122),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/tbzfgf/usd/tbzfgf.usd"),
            visual_material_path="materials",
            scale=(1.0000078902177143, 0.999925240279037, 0.9999786005270513),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampBtdcou0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampBtdcou0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.01646614074707, 12.889187812805176, 1.0416967868804932),
            rot=(0.386508971452713, -0.0042993128299713135, 0.0006261244416236877, 0.9222754240036011),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/btdcou/usd/btdcou.usd"),
            visual_material_path="materials",
            scale=(1.0001169619140189, 0.9999785692341313, 1.0000814173597081),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampJbjckk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampJbjckk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(16.98285675048828, -1.793992280960083, 0.9690092206001282),
            rot=(-0.4082767367362976, 3.4924596548080444e-10, 7.275957614183426e-10, 0.9128583669662476),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/jbjckk/usd/jbjckk.usd"),
            visual_material_path="materials",
            scale=(0.999987565541148, 0.9999865541322868, 1.0000113788705594),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampQgdwbh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampQgdwbh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.76480484008789, 22.259645462036133, 0.6182289123535156),
            rot=(0.991445004940033, -2.3283064365386963e-10, -1.1641532182693481e-10, -0.13052625954151154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/qgdwbh/usd/qgdwbh.usd"),
            visual_material_path="materials",
            scale=(0.9999096123309037, 0.9999096123309037, 0.9999114939849185),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampQgdwbh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampQgdwbh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.707101821899414, 25.62198829650879, 0.6182289123535156),
            rot=(0.991445004940033, 5.9371814131736755e-09, 1.9266735762357712e-08, -0.13052625954151154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/qgdwbh/usd/qgdwbh.usd"),
            visual_material_path="materials",
            scale=(0.9999096123309037, 0.9999096123309037, 0.9999114939849185),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampUupwiq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampUupwiq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.48379898071289, 13.814037322998047, 0.8009881377220154),
            rot=(0.7069061398506165, 0.00021203141659498215, -0.00024756789207458496, 0.7073072791099548),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/uupwiq/usd/uupwiq.usd"),
            visual_material_path="materials",
            scale=(0.9999484639847153, 0.9999411959276208, 0.9999746513639658),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanGvnfgj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanGvnfgj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.503482818603516, 19.868927001953125, 0.16213922202587128),
            rot=(-0.7062070369720459, 0.0, 2.9103830456733704e-11, 0.7080056071281433),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/gvnfgj/usd/gvnfgj.usd"),
            visual_material_path="materials",
            scale=(1.0001263835031564, 1.0001263835031564, 0.999959276435221),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    barUdatjt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/barUdatjt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.286928958284566, 0.188510010265593, 0.6611177666304813),
            rot=(-0.7062071330963108, 2.3011149376874498e-07, -2.306974073391551e-07, 0.7080052861128817),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bar/udatjt/usd/udatjt.usd"),
            visual_material_path="materials",
            scale=(0.9999762546396523, 1.0000068849243222, 0.9999702845365193),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    baseboardDsajeh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/baseboardDsajeh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.875560456087871, -1.926008712816112, 0.057825336117371576),
            rot=(0.6755901869956726, 5.90619580223429e-08, 6.445482082733042e-08, 0.7372773557048559),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/baseboard/dsajeh/usd/dsajeh.usd"),
            visual_material_path="materials",
            scale=(0.9999978587879822, 1.0000023233441495, 1.0001334814448881),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bathtubEuxylv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bathtubEuxylv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.32311418422115, 20.579836451423905, 0.2389076465368662),
            rot=(0.708005524227939, 0.0, 0.0, 0.7062068943749567),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/euxylv/usd/euxylv.usd"),
            visual_material_path="materials",
            scale=(0.9999974859856843, 1.0000371630339069, 1.0000545003377603),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bathtubPdcrfs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bathtubPdcrfs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.50232892811548, 10.373845782344574, 0.2568515058741067),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/pdcrfs/usd/pdcrfs.usd"),
            visual_material_path="materials",
            scale=(1.000012249474283, 1.0000422670283526, 1.0000076097675106),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedGxfipj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedGxfipj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.886598172307856, 23.958678269649095, 0.26620994281589117),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/gxfipj/usd/gxfipj.usd"),
            visual_material_path="materials",
            scale=(0.999981632253862, 0.9999985284068891, 1.0000233401992917),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedIvdnny0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedIvdnny0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.279968798078986, 7.7856934822266215, 0.33833592185632594),
            rot=(-4.013392642053105e-07, 0.0, 0.0, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/ivdnny/usd/ivdnny.usd"),
            visual_material_path="materials",
            scale=(0.9999994634686702, 1.0000116522863356, 0.9999883374122287),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedRrcvaq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedRrcvaq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.190313187576727, 17.83208176495184, 0.40365304410428804),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/rrcvaq/usd/rrcvaq.usd"),
            visual_material_path="materials",
            scale=(0.9999768275387361, 0.9999691135413935, 1.000010236828753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedTptswe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedTptswe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.27327541108822, 13.015635755769335, 0.13153109090889814),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/tptswe/usd/tptswe.usd"),
            visual_material_path="materials",
            scale=(1.000014546476087, 1.0000170509504958, 1.0000790598765912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    blanketDnypbe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/blanketDnypbe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.350460072872114, 13.013593008525326, 0.26911209291633775),
            rot=(0.9999896909854802, 0.0, 0.0, 0.004540696286237549),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/blanket/dnypbe/usd/dnypbe.usd"),
            visual_material_path="materials",
            scale=(0.9999803850232278, 1.0000101772703684, 0.9999810614398893),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    quiltGetwzm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/quiltGetwzm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.185712867816274, 7.701146422322503, 0.456867546139468),
            rot=(-4.013392642053105e-07, 0.0, 0.0, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/quilt/getwzm/usd/getwzm.usd"),
            visual_material_path="materials",
            scale=(0.9999818963802372, 0.9999951216252825, 0.9999221345988577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    benchAdrvdv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/benchAdrvdv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.59649533593348, 16.19542378603324, 0.37493649917768007),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bench/adrvdv/usd/adrvdv.usd"),
            visual_material_path="materials",
            scale=(1.0000753817684356, 0.9999693438349354, 0.9999970735985266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    benchPfjnnj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/benchPfjnnj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.974586950848966, 24.237080215661994, 0.16368524056464578),
            rot=(0.9999991910548823, -3.258411598260721e-07, 4.1445807237512316e-10, -0.0012719628433151525),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bench/pfjnnj/usd/pfjnnj.usd"),
            visual_material_path="materials",
            scale=(0.9999908984377718, 1.0000400526622266, 0.9999966422256952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    chandelierKnunaz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/chandelierKnunaz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.28615894043421, 13.787203179297281, 2.0467752891785196),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/chandelier/knunaz/usd/knunaz.usd"),
            visual_material_path="materials",
            scale=(1.0000131969646981, 0.999974197900956, 1.0000492674968056),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    chandelierObxeem0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/chandelierObxeem0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.97324415833626, 23.97549492604222, 1.7788825078027748),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/chandelier/obxeem/usd/obxeem.usd"),
            visual_material_path="materials",
            scale=(0.999972105570393, 1.0000364562553032, 1.0000270209727185),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopFjkase0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopFjkase0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.92742906503425, 0.47523176087227753, 0.8967929735882814),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/fjkase/usd/fjkase.usd"),
            visual_material_path="materials",
            scale=(1.0000094773354182, 1.0000580968748582, 0.9999767820922868),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopGjeoer0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopGjeoer0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.181303506201173, -0.4952336368598911, 0.8694859107126056),
            rot=(0.9990482256845203, 8.733957137874462e-08, -3.813319364626932e-09, -0.043619293398725154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/gjeoer/usd/gjeoer.usd"),
            visual_material_path="materials",
            scale=(1.0000286337307729, 1.0000066204785778, 1.0006281172152807),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopIkwqer0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopIkwqer0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.515068958630373, 0.017834818207872707, 0.8967754309960202),
            rot=(0.0012717244251360124, -4.407014698188872e-08, -2.820741731491566e-07, 0.9999991913581255),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/ikwqer/usd/ikwqer.usd"),
            visual_material_path="materials",
            scale=(1.0000537898314228, 1.000008613581726, 0.9999600734019979),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopRkgjer0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopRkgjer0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.029464279314774, -1.9918608830748892, 0.8694864963239243),
            rot=(0.6755901869956725, 5.9061958022342886e-08, 6.445482082733043e-08, 0.737277355704856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/rkgjer/usd/rkgjer.usd"),
            visual_material_path="materials",
            scale=(1.0000115088676846, 1.0000107511292238, 1.0006911484065133),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopSjxber0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopSjxber0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.697965365230235, -2.0618456216221475, 0.8967888782915445),
            rot=(0.7080054051704191, -1.6880169955391158e-07, -1.6837284433113177e-07, 0.7062070137356424),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/sjxber/usd/sjxber.usd"),
            visual_material_path="materials",
            scale=(1.0000239080887858, 1.0000120681246414, 0.9999535866491793),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorAgrzdb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorAgrzdb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.879404067993164, 2.411328077316284, 2.3100547790527344),
            rot=(0.708005428314209, 2.479391696397215e-07, 2.5783819523894635e-07, 0.7062070369720459),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/agrzdb/usd/agrzdb.usd"),
            visual_material_path="materials",
            scale=(0.9997624140497173, 0.9999794273556797, 1.0000181955059781),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorArkmpj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorArkmpj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.21036148071289, 17.419092178344727, 2.3100621700286865),
            rot=(0.001272515393793583, 1.516957254255047e-10, 1.1920926823449918e-07, 0.9999992847442627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/arkmpj/usd/arkmpj.usd"),
            visual_material_path="materials",
            scale=(0.9997383693241546, 0.9999743075520651, 1.0000161608006501),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorCrtrpa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorCrtrpa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.909822940826416, 4.798995018005371, 1.161303997039795),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/crtrpa/usd/crtrpa.usd"),
            visual_material_path="materials",
            scale=(1.0000363727262065, 0.9999788317775475, 0.9999873576918082),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorEduavq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorEduavq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.740840911865234, 9.156760215759277, 1.1608809232711792),
            rot=(-0.3826834559440613, 3.345468257975881e-08, -8.076828805769765e-08, 0.9238796234130859),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/eduavq/usd/eduavq.usd"),
            visual_material_path="materials",
            scale=(0.9997964177193384, 0.9999880545747377, 1.0000107505515985),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorEgqeue0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorEgqeue0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.42770767211914, 21.78680992126465, 2.310056447982788),
            rot=(-0.7062067985534668, -1.00000761449337e-07, 6.865316493076534e-08, 0.7080057859420776),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/egqeue/usd/egqeue.usd"),
            visual_material_path="materials",
            scale=(0.9997387194817619, 0.9999826406645197, 1.0000166694762058),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorEngzvq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorEngzvq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.868700937259222, 5.780714686160727, 1.4153878234301265),
            rot=(-0.4993638078128093, 0.5006353835070831, 0.49936362899887465, 0.5006355623210179),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/engzvq/usd/engzvq.usd"),
            visual_material_path="materials",
            scale=(0.9999836689951883, 1.0000085855089955, 0.9999983551296132),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorFnvpyu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorFnvpyu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.023588180541992, 17.786283493041992, 1.3550734519958496),
            rot=(-0.08715569972991943, 5.820766091346741e-11, 7.73070496506989e-12, 0.9961948394775391),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/fnvpyu/usd/fnvpyu.usd"),
            visual_material_path="materials",
            scale=(0.9998995290836103, 1.0000291200224887, 1.0000143619645048),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorFstpos0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorFstpos0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.065462112426758, 3.9811205863952637, 2.310046911239624),
            rot=(0.7080056071281433, 1.0555467611084168e-07, 1.473798647566582e-07, 0.7062068581581116),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/fstpos/usd/fstpos.usd"),
            visual_material_path="materials",
            scale=(0.9997668496108855, 1.000048922288303, 1.0000207388992821),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorHkxqfh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorHkxqfh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.438146591186523, 21.793916702270508, 2.3100621700286865),
            rot=(-0.7062067985534668, -6.318441592156887e-08, 2.1157447349651193e-08, 0.7080057859420776),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/hkxqfh/usd/hkxqfh.usd"),
            visual_material_path="materials",
            scale=(0.9997386027625321, 1.0000185355729212, 1.0000169746817877),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorIuuykr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorIuuykr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.699346542358398, 18.719667434692383, 1.9441781044006348),
            rot=(0.7250999212265015, -7.450580596923828e-09, -5.231413524597883e-09, 0.6886436939239502),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/iuuykr/usd/iuuykr.usd"),
            visual_material_path="materials",
            scale=(1.0001280999885978, 1.000007152927262, 0.9999889957599261),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorJpubcg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorJpubcg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.094023704528809, 5.592834949493408, 1.2591899633407593),
            rot=(0.7933534979820251, 4.656612873077393e-10, 4.0745362639427185e-10, 0.6087614893913269),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/jpubcg/usd/jpubcg.usd"),
            visual_material_path="materials",
            scale=(0.9999287873430814, 0.9999962030090606, 1.000006563088795),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLrvyvc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLrvyvc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.74913215637207, 4.04660701751709, 1.3547335863113403),
            rot=(0.7071067094802856, 9.98261384665966e-09, 1.1859810911118984e-09, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lrvyvc/usd/lrvyvc.usd"),
            visual_material_path="materials",
            scale=(1.0000410893160558, 1.0000076531922426, 0.9999840692312364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorMqlbnj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorMqlbnj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.74050521850586, 15.204798698425293, 2.3100547790527344),
            rot=(0.0008991069626063108, 0.0008991074864752591, 0.7071064710617065, 0.7071059346199036),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/mqlbnj/usd/mqlbnj.usd"),
            visual_material_path="materials",
            scale=(0.9999869582812374, 1.0000167712113792, 0.9997419876312578),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorMtufto0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorMtufto0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.743518829345703, 2.32835054397583, 2.3100228309631348),
            rot=(-0.706206738948822, -1.4737980791323935e-07, 1.0555469742712376e-07, 0.7080057263374329),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/mtufto/usd/mtufto.usd"),
            visual_material_path="materials",
            scale=(0.9997666161593164, 1.000029669491192, 0.9999787607442531),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorNhcpvf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorNhcpvf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.196086883544922, 6.370924949645996, 2.310023307800293),
            rot=(0.5006356835365295, 0.5006359815597534, 0.499363511800766, 0.4993631839752197),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/nhcpvf/usd/nhcpvf.usd"),
            visual_material_path="materials",
            scale=(1.000023597460426, 0.9999817687855131, 0.9997358015091962),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorRyflkw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorRyflkw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.26681900024414, 9.721426963806152, 2.31005597114563),
            rot=(-0.706206738948822, -1.0001156880434792e-07, 6.861589696427473e-08, 0.7080057263374329),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ryflkw/usd/ryflkw.usd"),
            visual_material_path="materials",
            scale=(0.9997668496108855, 1.0000108101417904, 1.0000165677410533),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorTfdrhh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorTfdrhh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0912725925445557, 0.04531905800104141, 1.46956467628479),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/tfdrhh/usd/tfdrhh.usd"),
            visual_material_path="materials",
            scale=(0.9998987658452759, 1.0000167177210817, 1.0000051891047617),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorTonlzz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorTonlzz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.557377338409424, 3.022390365600586, 1.353929877281189),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/tonlzz/usd/tonlzz.usd"),
            visual_material_path="materials",
            scale=(0.9999824564138413, 1.0000029669329198, 1.00001051915487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorTprpvb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorTprpvb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.722097396850586, 22.48230743408203, 2.310018301010132),
            rot=(0.9990475177764893, 5.561132638831623e-05, 0.04361922666430473, -0.0012705203844234347),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/tprpvb/usd/tprpvb.usd"),
            visual_material_path="materials",
            scale=(0.9998722245104055, 0.9999828534649552, 0.999984048552145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorVgjnsq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorVgjnsq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.728492736816406, 25.388851165771484, 2.3100504875183105),
            rot=(0.0005109746707603335, 2.3283064365386963e-10, 1.192100853586453e-07, 0.9999999403953552),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/vgjnsq/usd/vgjnsq.usd"),
            visual_material_path="materials",
            scale=(0.9985633780286063, 0.999983450194979, 1.0000018163630358),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorWhqaxp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorWhqaxp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.86705207824707, 16.45783805847168, 2.3100554943084717),
            rot=(-0.7062067985534668, -5.7945726439356804e-08, 2.6436575595312206e-08, 0.7080057859420776),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/whqaxp/usd/whqaxp.usd"),
            visual_material_path="materials",
            scale=(0.9997388362010188, 0.9999868643663481, 1.0000163642708102),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.803123893323903, 11.025563726580701, 2.750001872347368),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.43378600256832, 11.02702271094615, 2.750001871574753),
            rot=(-4.013392642053105e-07, -1.019427475767916e-08, -4.091362682890831e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.605639898460703, -0.63264751399423, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.170512945330707, -0.6275711895242301, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.736343023460702, -0.6199308391842301, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.745093023460702, 2.99361609685077, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.179655523460703, 2.98969617497577, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.616452398460703, 2.98385047185077, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.42437389308389, 1.1046884519061493, 2.7500018712939966),
            rot=(-4.013392642053105e-07, -1.3898720396808831e-08, -5.578102017192677e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.416381705712016, -1.5485009707038506, 2.7500018716064316),
            rot=(-4.013392642053105e-07, -9.77628999976253e-09, -3.92360907821095e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.41888170571201, -1.5541572207038505, 2.7500018716064316),
            rot=(-4.013392642053105e-07, -9.77628999976253e-09, -3.92360907821095e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.426850455712035, 1.0990302487811494, 2.750001871606432),
            rot=(-4.013392642053105e-07, -9.77628999976253e-09, -3.92360907821095e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.77573912762885, 13.85649146094615, 2.750001871606432),
            rot=(-5.205485537560791e-07, -9.776289999762008e-09, -5.089033663525015e-15, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.755405143083916, 5.601750982426148, 2.750001871293997),
            rot=(-4.013392642053105e-07, -1.3898720396808831e-08, -5.578102017192677e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.42846387305114986, 1.6717901533166748, 2.7630565598473678),
            rot=(0.7071071388143317, 0.0, 0.0, -0.7071064235585824),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.02709862695385, 1.661508903316598, 2.7630565598473678),
            rot=(0.7071071388143317, 0.0, 0.0, -0.7071064235585824),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.186239251953849, 1.6610401533166594, 2.7630565598473678),
            rot=(0.7071071388143317, 0.0, 0.0, -0.7071064235585824),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.76693443994017, 9.728618414066151, 2.750001871262318),
            rot=(-4.013392642053105e-07, -1.4316704266547034e-08, -5.7458556218725655e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.43695635046614983, -1.578399299820346, 2.7630565598068575),
            rot=(0.7071071388143317, 3.77958442594403e-10, 3.77958803416914e-10, -0.7071064235585824),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.786295768083914, 17.98221900000615, 2.7500018712939966),
            rot=(-4.013392642053105e-07, -1.3898720396808831e-08, -5.578102017192677e-15, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.7970225911153, 22.110305414049297, 2.7502284346120764),
            rot=(0.9999999999999999, -4.5289020706470845e-17, 3.0392947312837363e-09, 1.4587915973895046e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.692998893130614, 0.6835849209824878, 2.763056557635425),
            rot=(-1.7126413924196592e-06, -2.9185480698813934e-08, -4.9984261252186173e-14, 0.9999999999985332),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.693155631867613, -1.792381830117509, 2.76305655875374),
            rot=(-1.7126413924196592e-06, -1.4429874184408382e-08, -2.471319928842064e-14, 0.9999999999985335),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.396218023460712, -1.9873663250293123, 2.7630565598473678),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.457348762774277, 20.68292357812385, 2.7626346848473675),
            rot=(0.9999999999999469, 0.0, 0.0, 3.257872329514497e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightFisfbn9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightFisfbn9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.156426887774284, 20.677189203123852, 2.7626346848473675),
            rot=(0.9999999999999469, 0.0, 0.0, 3.257872329514497e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/fisfbn/usd/fisfbn.usd"),
            visual_material_path="materials",
            scale=(1.0000341480983783, 1.0000472467227906, 0.9996582126459833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightNlhffs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightNlhffs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.63613971633609, 12.03641789230348, 2.2508199833116227),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/nlhffs/usd/nlhffs.usd"),
            visual_material_path="materials",
            scale=(1.0003278061596415, 1.0003278061596415, 0.9992020773755405),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightNlhffs1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightNlhffs1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.069170966336085, 12.044308517303481, 2.250819983311614),
            rot=(0.9914448655597188, 2.6426637544637947e-14, 1.9450205444678906e-13, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/nlhffs/usd/nlhffs.usd"),
            visual_material_path="materials",
            scale=(1.0003278061596415, 1.0003278061596415, 0.9992020773755405),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightNlhffs2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightNlhffs2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.85267096633609, 12.040371017303482, 2.2508199833116227),
            rot=(0.9914448655597188, 3.0646487064021156e-17, -4.034685564406309e-18, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/nlhffs/usd/nlhffs.usd"),
            visual_material_path="materials",
            scale=(1.0003278061596415, 1.0003278061596415, 0.9992020773755405),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightNlhffs3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightNlhffs3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.8911714553833, 1.0280604362487793, 2.3841981887817383),
            rot=(0.9914448857307434, -2.3638131096959114e-07, 3.109744284301996e-08, -0.13052617013454437),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/nlhffs/usd/nlhffs.usd"),
            visual_material_path="materials",
            scale=(1.6001259528808605, 1.6001259528808605, 1.6000889758428358),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightNlhffs4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightNlhffs4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.839937210083008, 1.0368261337280273, 2.3841981887817383),
            rot=(0.9914448857307434, -2.3638131096959114e-07, 3.109744284301996e-08, -0.13052617013454437),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/nlhffs/usd/nlhffs.usd"),
            visual_material_path="materials",
            scale=(1.6001259528808605, 1.6001259528808605, 1.6000889758428358),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightNlhffs5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightNlhffs5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.802906036376953, 1.0373417139053345, 2.3841981887817383),
            rot=(0.9914448857307434, -2.3638131096959114e-07, 3.109744284301996e-08, -0.13052617013454437),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/nlhffs/usd/nlhffs.usd"),
            visual_material_path="materials",
            scale=(1.6001259528808605, 1.6001259528808605, 1.6000889758428358),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightZojpvs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightZojpvs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6537015438079834, 5.905586242675781, 2.8316361904144287),
            rot=(3.900495357811451e-07, -0.7062070965766907, 0.7080054879188538, -4.530884325504303e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/zojpvs/usd/zojpvs.usd"),
            visual_material_path="materials",
            scale=(0.9999967937770963, 1.0002958725517725, 0.9983471610122905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightZojpvs1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightZojpvs1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.563357949256897, 5.908351898193359, 2.8316361904144287),
            rot=(5.360343493521214e-07, -0.7062068581581116, 0.7080057263374329, -4.755565896630287e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/zojpvs/usd/zojpvs.usd"),
            visual_material_path="materials",
            scale=(0.9999967937770963, 1.0002958725517725, 0.9983471610122905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightZojpvs2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightZojpvs2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.4726235270500183, 5.9111175537109375, 2.8316361904144287),
            rot=(5.360343493521214e-07, -0.7062068581581116, 0.7080057263374329, -4.755565896630287e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/zojpvs/usd/zojpvs.usd"),
            visual_material_path="materials",
            scale=(0.9999967937770963, 1.0002958725517725, 0.9983471610122905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightZojpvs3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightZojpvs3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.466920405626297, 3.6677424907684326, 2.8316361904144287),
            rot=(5.360343493521214e-07, -0.7062068581581116, 0.7080057263374329, -4.755565896630287e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/zojpvs/usd/zojpvs.usd"),
            visual_material_path="materials",
            scale=(0.9999967937770963, 1.0002958725517725, 0.9983471610122905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightZojpvs4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightZojpvs4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5576703548431396, 3.664992570877075, 2.8316361904144287),
            rot=(5.360343493521214e-07, -0.7062068581581116, 0.7080057263374329, -4.755565896630287e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/zojpvs/usd/zojpvs.usd"),
            visual_material_path="materials",
            scale=(0.9999967937770963, 1.0002958725517725, 0.9983471610122905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightZojpvs5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightZojpvs5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6480140686035156, 3.6622114181518555, 2.8316361904144287),
            rot=(5.360343493521214e-07, -0.7062068581581116, 0.7080057263374329, -4.755565896630287e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/zojpvs/usd/zojpvs.usd"),
            visual_material_path="materials",
            scale=(0.9999967937770963, 1.0002958725517725, 0.9983471610122905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drawerUnitTodoac0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drawerUnitTodoac0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5480118021094942, 2.7995105086363754, 0.41918650812065905),
            rot=(0.7080055837566814, 0.0, 0.0, 0.7062068346945962),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/drawer_unit/todoac/usd/todoac.usd"),
            visual_material_path="materials",
            scale=(0.9999158532716625, 1.0000296859035829, 1.0000529690068853),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drawerUnitTodopf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drawerUnitTodopf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.974987236051078, 11.396543224905008, 0.29328382146258886),
            rot=(0.9999991916613404, 0.0, 0.0, -0.001271486006889538),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/drawer_unit/todopf/usd/todopf.usd"),
            visual_material_path="materials",
            scale=(1.0000066586644565, 0.9999656082623168, 0.999983353394055),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drawerUnitTodoph0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drawerUnitTodoph0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.806231335675747, 21.160393855718784, 0.18065007926433843),
            rot=(0.001272125824503029, 0.0, 0.0, 0.9999991908476161),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/drawer_unit/todoph/usd/todoph.usd"),
            visual_material_path="materials",
            scale=(0.9998185842147495, 0.999986707556274, 0.9999644347014782),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drawerUnitTodopi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drawerUnitTodopi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.933898680865, -1.4416505556730144, 0.22030778960506672),
            rot=(2.5674479563329357e-13, 6.397578432072088e-07, 0.9999999999997148, 4.013392641056485e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/drawer_unit/todopi/usd/todopi.usd"),
            visual_material_path="materials",
            scale=(1.0000673797615878, 1.0000353768377526, 0.9998718681557309),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drawerUnitTodopi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drawerUnitTodopi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9388518668885293, 0.5046777000157563, 0.22030770427407376),
            rot=(1.4683271619540307e-13, 5.205485536564785e-07, 0.9999999999998247, 2.821299745549182e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/drawer_unit/todopi/usd/todopi.usd"),
            visual_material_path="materials",
            scale=(1.0000673797615878, 1.0000353768377526, 0.9998718681557309),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drivewayHmbdky0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drivewayHmbdky0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.967340977195049, 22.83179162979126, -0.16123436909105393),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/driveway/hmbdky/usd/hmbdky.usd"),
            visual_material_path="materials",
            scale=(1.0000028276162196, 1.000000527667165, 0.9998961238462729),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    clothesDryerJasnzj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/clothesDryerJasnzj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.06136131286621, 0.9434047937393188, 0.46387985348701477),
            rot=(0.0012724809348583221, -3.725290298461914e-09, -4.819594323635101e-07, 0.9999992251396179),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/jasnzj/usd/jasnzj.usd"),
            visual_material_path="materials",
            scale=(0.9999536801010748, 1.0000269475250667, 0.999945988751496),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.44696044921875, 15.13455581665039, 1.4417191743850708),
            rot=(0.7071070671081543, 8.847564458847046e-09, 9.74978320300579e-09, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.28666877746582, 14.081750869750977, 1.4417191743850708),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.60979461669922, 8.411507606506348, 1.441723108291626),
            rot=(1.0, 5.371475708670914e-09, -2.0372681319713593e-10, 1.430511474609375e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.72205352783203, 9.639646530151367, 1.4417191743850708),
            rot=(0.707105815410614, 1.30385160446167e-08, -4.831235855817795e-09, 0.7071077823638916),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.6455135345459, 22.264461517333984, 1.441723108291626),
            rot=(1.0, 5.371475708670914e-09, -2.0372681319713593e-10, 1.430511474609375e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.624235153198242, 14.110898971557617, 1.4417190551757812),
            rot=(1.0, 2.4468863557558507e-07, 1.7462298274040222e-10, 1.6689300537109375e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.79057502746582, 25.10515594482422, 1.4417152404785156),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.800701141357422, 22.26495361328125, 1.4417191743850708),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.800701141357422, 22.149093627929688, 1.4417191743850708),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.947940826416016, 21.874601364135742, 1.4417191743850708),
            rot=(-0.7071067094802856, -4.889443516731262e-09, -2.9103830456733704e-10, 0.7071069478988647),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.09515953063965, 16.540069580078125, 1.4417191743850708),
            rot=(-0.7071067094802856, -4.889443516731262e-09, -2.9103830456733704e-10, 0.7071069478988647),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.29729461669922, 17.573469161987305, 1.4417152404785156),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.845184326171875, 10.753438949584961, 1.441723108291626),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.947805404663086, 21.70330238342285, 1.4417191743850708),
            rot=(0.7071068286895752, 9.313225746154785e-09, 2.4709152057766914e-08, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.3182430267334, 2.1839938163757324, 1.441723108291626),
            rot=(0.7071070671081543, 8.847564458847046e-09, 9.74978320300579e-09, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.632532119750977, 17.56800651550293, 1.4417191743850708),
            rot=(1.0, 6.266645868890919e-09, -5.820766091346741e-11, 1.6689300537109375e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.267230987548828, 6.52656364440918, 1.441723108291626),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.4011287689209, 5.436415672302246, 1.4417270421981812),
            rot=(-0.7071067094802856, -5.122274160385132e-09, -2.764863893389702e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.470243453979492, 3.9644927978515625, 1.4417191743850708),
            rot=(0.707107424736023, -7.450580596923828e-09, -5.2677933126688e-09, 0.7071062922477722),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.6551194190979, 2.4431638717651367, 1.441719651222229),
            rot=(5.9167505241930485e-06, -4.76837158203125e-07, -6.547679731738754e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.6551384925842285, 2.319110631942749, 1.441723108291626),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.891435384750366, 1.1462044715881348, 0.9493715167045593),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchGashan9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchGashan9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.8914196491241455, 1.0620325803756714, 0.9493715167045593),
            rot=(1.94646418094635e-07, 0.0, -4.6172772272257134e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/gashan/usd/gashan.usd"),
            visual_material_path="materials",
            scale=(1.004664748837811, 0.9999999292194893, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceRoemfr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceRoemfr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(27.885487209150032, 13.490895143809878, 1.1597107234571407),
            rot=(-0.7071067215818997, -2.4532693839753217e-17, 2.4532697975656544e-17, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/roemfr/usd/roemfr.usd"),
            visual_material_path="materials",
            scale=(0.9999992686114536, 0.9999009665642957, 1.000014744215367),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceRoemfr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceRoemfr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.842877847492694, 13.764378278970717, 1.1597115169121404),
            rot=(0.7071067811865477, 3.925231146709437e-17, 3.9252311467094367e-17, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/roemfr/usd/roemfr.usd"),
            visual_material_path="materials",
            scale=(0.9999992686114536, 0.9999009665642957, 1.000014744215367),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceWvfgad0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceWvfgad0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3805855681300023, 42.978290278927204, 1.1597068580271612),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/wvfgad/usd/wvfgad.usd"),
            visual_material_path="materials",
            scale=(0.9999997514286633, 1.0000384261642918, 0.9999990661947705),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceWvfgad1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceWvfgad1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6605667763928453, -15.742574874871458, 1.159709192627161),
            rot=(7.54979013252756e-08, 9.78166814425852e-24, 1.2956211990734808e-16, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/wvfgad/usd/wvfgad.usd"),
            visual_material_path="materials",
            scale=(0.9999997514286633, 1.0000384261642918, 0.9999990661947705),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceYzplpe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceYzplpe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.999049146504843, 0.6363769139352348, 1.034725463851305),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/yzplpe/usd/yzplpe.usd"),
            visual_material_path="materials",
            scale=(1.0000769409068713, 1.0000038047128892, 0.9999771303852167),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    fireplaceGwqitr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fireplaceGwqitr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.879458504948552, 0.12692351496405757, 0.7666960094284417),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fireplace/gwqitr/usd/gwqitr.usd"),
            visual_material_path="materials",
            scale=(1.0000822542065952, 1.000018865706556, 1.0000482993274953),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.921090199188741, 22.84370620624087, 0.25792479467169316),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.921105702118771, 16.52687762566941, 0.25792479467169316),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.244498548241467, 19.75966997155456, 0.3066669849890923),
            rot=(0.9659259007874373, 3.413173633956131e-08, 7.627255927677637e-09, -0.25881876707066),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.316701673241464, 13.03691899498956, 0.3066669849890581),
            rot=(0.9659259007874373, 3.413173633956131e-08, 7.627255927677637e-09, -0.25881876707066),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.390270039230515, 6.315741249010674, 0.30666698563459893),
            rot=(0.9659259007874372, 3.313103286909131e-08, -5.484887400110327e-09, -0.2588187670706606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.492139172834943, 0.03160651858368681, 0.30666698498906086),
            rot=(0.9659259007874373, 3.413173633956131e-08, 7.627255927677637e-09, -0.25881876707066),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.771893809601569, 9.52080047722816, 0.26580760717169316),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.92111351460042, 10.378407899109334, 0.2579247949624072),
            rot=(0.9914448655597188, 4.5993458788625545e-10, 3.4931490728757503e-09, -0.13052616042491688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.32851195211877, 9.520800477229411, 0.25792479467169316),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.393918690398767, 9.520816102229414, 0.25792479467169316),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.903261914877628, 27.987754484485993, 0.3066669853251705),
            rot=(0.9659259007874372, 3.308017575291947e-08, -4.0924040633732044e-09, -0.2588187670706606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.365536451049842, 11.169265015259032, 0.30666698476218684),
            rot=(0.9659259007874376, 3.413172214207277e-08, 4.108778581655744e-09, -0.2588187670706592),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.830980664877629, 34.708677336045994, 0.3066669853251101),
            rot=(0.9659259007874372, 3.308017575291947e-08, -4.0924040633732044e-09, -0.2588187670706606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.14380128254601, 26.230584034028585, 0.30666698563458483),
            rot=(0.9659259007874372, 3.313103286909131e-08, -5.484887400110327e-09, -0.2588187670706606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gardenLightUmyzpg9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gardenLightUmyzpg9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.759771680612852, 41.4309507736317, 0.3066669863198064),
            rot=(0.965925837190079, 4.332960500336593e-08, 1.85467013150777e-08, -0.2588190044193874),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/garden_light/umyzpg/usd/umyzpg.usd"),
            visual_material_path="materials",
            scale=(0.999955076860118, 0.9999206143944336, 1.0000173273625177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    radiatorLwgvaq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/radiatorLwgvaq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.761296722185755, 20.65602795268162, 1.583991980894313),
            rot=(0.9999991913581409, 2.2565927030508633e-07, -2.8697652684434874e-10, -0.0012717244251238392),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/radiator/lwgvaq/usd/lwgvaq.usd"),
            visual_material_path="materials",
            scale=(1.0002709353858912, 0.9999741275326028, 1.0000751379569162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lawnWwoqjw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lawnWwoqjw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.064220629692077, 14.226392125129701, -0.16119530089348869),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/lawn/wwoqjw/usd/wwoqjw.usd"),
            visual_material_path="materials",
            scale=(1.0, 1.0, 0.9999286473384057),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorCatitv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorCatitv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.87897021933452, 25.909185573923416, 1.3448078559336538),
            rot=(0.7071067811865462, 5.751611578560099e-17, 6.181724044288383e-08, -0.7071067811865461),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/catitv/usd/catitv.usd"),
            visual_material_path="materials",
            scale=(0.9965281310843142, 1.0000154081575783, 0.9999790192053576),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorFfoudz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorFfoudz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.79331795511634, 21.000643799860164, 1.197874709370663),
            rot=(0.9999979164659538, 0.0, 0.0, -0.002041338715463537),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/ffoudz/usd/ffoudz.usd"),
            visual_material_path="materials",
            scale=(0.9958469556493751, 1.0000268017732024, 0.9999947533894448),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorJpktmn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorJpktmn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.844154095064294, 12.104085520238112, 1.5723491667045155),
            rot=(0.7372771578185687, -2.6964164515913096e-09, 6.175840703081427e-08, -0.6755904029506115),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/jpktmn/usd/jpktmn.usd"),
            visual_material_path="materials",
            scale=(0.9999487237628958, 1.0000149389190929, 1.0000358582442346),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorKglofh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorKglofh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.271667847840114, 12.290367923984359, 1.1978719819667976),
            rot=(0.6755901869956753, 0.0, 0.0, 0.7372773557048585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/kglofh/usd/kglofh.usd"),
            visual_material_path="materials",
            scale=(1.0000767669331208, 1.0000215010858933, 0.9999949699541909),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorKglofh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorKglofh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.561667847840113, 12.292164798984361, 1.197875888216798),
            rot=(0.6755901869956753, 0.0, 0.0, 0.7372773557048585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/kglofh/usd/kglofh.usd"),
            visual_material_path="materials",
            scale=(1.0000767669331208, 1.0000215010858933, 0.9999949699541909),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorKglofh2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorKglofh2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.980511597840117, 12.288555423984363, 1.1978719819667976),
            rot=(0.6755901869956753, 0.0, 0.0, 0.7372773557048585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/kglofh/usd/kglofh.usd"),
            visual_material_path="materials",
            scale=(1.0000767669331208, 1.0000215010858933, 0.9999949699541909),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorLobucc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorLobucc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.31731099828786, 19.605112304374163, 1.5156662902818534),
            rot=(0.7080055837566612, -1.6837283010911983e-07, 1.6880169951559282e-07, 0.7062068346945762),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/lobucc/usd/lobucc.usd"),
            visual_material_path="materials",
            scale=(0.9970119614821815, 0.9999978089030528, 0.9999793043188948),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorNdvgah0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorNdvgah0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.186636479413974, 0.5051443069762007, 1.1967615850266957),
            rot=(4.013392641057306e-07, -3.508619281607837e-14, -8.742277657346845e-08, 0.9999999999999157),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/ndvgah/usd/ndvgah.usd"),
            visual_material_path="materials",
            scale=(1.003425656222792, 0.9999895272714487, 1.0000184327183947),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorTytkbq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorTytkbq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.233740230935766, 11.970767253731267, 1.1181115180509),
            rot=(0.7125503358214907, -0.026221032955304896, -0.0005715328684144526, -0.701130622424679),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/tytkbq/usd/tytkbq.usd"),
            visual_material_path="materials",
            scale=(1.0001634525309442, 0.9999787069013265, 1.00001241696448),
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
            pos=(8.432286262512207, -1.813930630683899, 1.1463956832885742),
            rot=(0.7071068286895752, -1.4901161193847656e-08, 1.4668330550193787e-08, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/ffitak/usd/ffitak.usd"),
            visual_material_path="materials",
            scale=(0.9999301411551824, 0.9999408217041598, 1.000005271797336),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingFmlmox0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingFmlmox0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.299624966483655, 18.34242515492261, 1.462589233397479),
            rot=(0.9990482217883634, 0.0, 0.0, 0.043619382635579296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/fmlmox/usd/fmlmox.usd"),
            visual_material_path="materials",
            scale=(1.001037123377308, 0.9997768480200291, 0.9999546950638419),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingFqlxxd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingFqlxxd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.607748431319205, 10.970518508271326, 1.409995730572724),
            rot=(0.0020928160845497742, -0.00037338134965759476, -0.0008978199552334894, 0.9999973373097211),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/fqlxxd/usd/fqlxxd.usd"),
            visual_material_path="materials",
            scale=(1.000718507052983, 1.0000260838362576, 0.9999678524326941),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingFwuole0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingFwuole0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.808601364093743, 21.875156876701457, 1.5914195484376208),
            rot=(0.7085846732041219, -0.0008990094153868685, -0.0003706991010393667, 0.7056251237480532),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/fwuole/usd/fwuole.usd"),
            visual_material_path="materials",
            scale=(0.9981372291657159, 0.9999709975198092, 0.9999943602528484),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingGardkz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingGardkz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.83817010170852, 8.222786181301238, 1.1013033806048136),
            rot=(0.7353605599333108, 0.00484880011500249, 0.006126957455968028, -0.6776310179030658),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/gardkz/usd/gardkz.usd"),
            visual_material_path="materials",
            scale=(0.999543231097551, 0.999854689284559, 0.9998830129069737),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingIfdzgs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingIfdzgs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.543471705927526, 8.221050522771437, 1.1846750720330155),
            rot=(-0.7064697234088609, 0.001289044872090831, -0.001292361777481569, 0.7077409116837611),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/ifdzgs/usd/ifdzgs.usd"),
            visual_material_path="materials",
            scale=(1.0031053592498231, 1.000125343407831, 0.9999606187691952),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingJreujf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingJreujf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.32175002148614, -2.0658240586508048, 1.005289028285382),
            rot=(0.6975262099600039, 0.1140133653310705, -0.05472393655077246, 0.705310874517828),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/jreujf/usd/jreujf.usd"),
            visual_material_path="materials",
            scale=(0.9998386556464486, 0.9999746572518512, 1.0000244496244497),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingJwqlzb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingJwqlzb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.300195924672003, 18.4139875270193, 1.1004098762066092),
            rot=(0.9990482217883634, 0.0, 0.0, 0.043619382635579296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/jwqlzb/usd/jwqlzb.usd"),
            visual_material_path="materials",
            scale=(0.9990237537066972, 0.9998288781037786, 0.9999171907725006),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingMsquxr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingMsquxr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.298586919496472, 18.405525298594476, 1.2878431091225617),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/msquxr/usd/msquxr.usd"),
            visual_material_path="materials",
            scale=(1.0000406995215718, 0.9996459139338962, 1.0003259850119683),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingTkcdhf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingTkcdhf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.303056316442838, 18.849695315837025, 1.4363820526408222),
            rot=(0.9994086911073096, -0.024008074035053593, -0.007815759388013658, 0.023340831722334913),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/tkcdhf/usd/tkcdhf.usd"),
            visual_material_path="materials",
            scale=(1.0008451474370086, 1.0000342612192163, 0.9999245387392224),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingWduwwo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingWduwwo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.280959522234564, 8.222298858122127, 1.5043619707167863),
            rot=(0.7356670088126096, -0.036250391813836005, -0.025474993952414184, -0.675892732555378),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/wduwwo/usd/wduwwo.usd"),
            visual_material_path="materials",
            scale=(1.000473293711388, 1.0001676729898303, 1.0000276389791771),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingWwnloz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingWwnloz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.299367651109453, 18.54601523333352, 1.2878430175800002),
            rot=(0.9990482217883634, 0.0, 0.0, 0.043619382635579296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/wwnloz/usd/wwnloz.usd"),
            visual_material_path="materials",
            scale=(1.0001646962947957, 0.9998723264490217, 1.0003259850119683),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingXpxncg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingXpxncg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.300828490140553, 18.536361334714744, 1.5599447077082818),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/xpxncg/usd/xpxncg.usd"),
            visual_material_path="materials",
            scale=(0.9993111258116488, 0.999750079943331, 0.9999079093297704),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swimmingPoolVnvmkx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swimmingPoolVnvmkx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.134987275041294, 16.055174666878045, -0.8614273107027657),
            rot=(0.9990482219507036, 0.0, 0.0, 0.04361937891737566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swimming_pool/vnvmkx/usd/vnvmkx.usd"),
            visual_material_path="materials",
            scale=(1.0000013379006665, 1.0000015108745663, 0.9999877912907638),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.952869193622254, 21.13251392749202, 0.06688842311298378),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.952884818460582, 19.56248267749202, 0.06688842295525566),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.952900443402466, 17.99971705249202, 0.06688842289855795),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.952900443402466, 13.36773267749202, 0.06688842289855793),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.952869193622256, 14.93777955249202, 0.06688842311298375),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.952884818402467, 11.80496705249202, 0.06688842289855784),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.235809289117906, 15.949061910228485, 0.06688842201112119),
            rot=(0.9994748682809426, 3.1023734258413343e-09, -1.0058050558647464e-10, -0.032403513309400625),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.438747205389014, 12.822780278566613, 0.06688842201112175),
            rot=(0.9994748682809426, 3.1023734258413343e-09, -1.0058050558647464e-10, -0.032403513309400625),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantXcybvc8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantXcybvc8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.337512440533859, 14.382311503261388, 0.06688842201112165),
            rot=(0.9994748682809426, 3.1023734258413343e-09, -1.0058050558647464e-10, -0.032403513309400625),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/xcybvc/usd/xcybvc.usd"),
            visual_material_path="materials",
            scale=(0.9999784574369428, 0.9999896516711168, 0.9999874389733833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    boulderVxbkjq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/boulderVxbkjq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.29715648199185, 39.024158691080856, 0.18012029228242055),
            rot=(-0.16334801901481774, -2.7110345175960697e-10, 1.6373760149557627e-09, 0.9865685098785257),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/boulder/vxbkjq/usd/vxbkjq.usd"),
            visual_material_path="materials",
            scale=(1.0000059500091607, 1.0000156007544982, 1.0000170580343248),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roofAmxayl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roofAmxayl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.121409431381894, 6.8734844400509125, 2.6166608844399453),
            rot=(-0.7062068943749574, 0.0, 0.0, 0.7080055242279383),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/roof/amxayl/usd/amxayl.usd"),
            visual_material_path="materials",
            scale=(0.9999984275453009, 0.999997513273028, 0.9999135512917519),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roofJqqtaq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roofJqqtaq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.604042722914224, 8.079193102911102, 3.178764243662982),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/roof/jqqtaq/usd/jqqtaq.usd"),
            visual_material_path="materials",
            scale=(1.0000015714768435, 1.0000007978458163, 0.9999506899386823),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightDddvjo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightDddvjo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.05372616925605, 19.765605936776506, 1.741994025233689),
            rot=(0.7080055837566814, 0.0, 0.0, 0.7062068346945962),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/dddvjo/usd/dddvjo.usd"),
            visual_material_path="materials",
            scale=(1.0000173741113667, 1.0000087821079557, 1.0000241050449203),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightDddvjo1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightDddvjo1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.69477109139669, 19.760863749274414, 1.8123856267766998),
            rot=(0.7080055837566814, 5.712500341515312e-10, 5.69798724321891e-10, 0.7062068346945962),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/dddvjo/usd/dddvjo.usd"),
            visual_material_path="materials",
            scale=(1.0000173741113667, 1.0000087821079557, 1.0000241050449203),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightDnrcpt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightDnrcpt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.1943609476287, 6.766677445788189, 1.8521206996429949),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/dnrcpt/usd/dnrcpt.usd"),
            visual_material_path="materials",
            scale=(1.000077294690019, 1.0000763406206963, 0.9999844620375334),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightHqxyvs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightHqxyvs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.270393914211049, 3.519957028828432, 1.8985086712852843),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/hqxyvs/usd/hqxyvs.usd"),
            visual_material_path="materials",
            scale=(1.000062751356276, 0.9999337620582391, 1.0000017270573833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightHqxyvs1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightHqxyvs1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.58670235358429, 0.2761205718214169, 1.8979266400352843),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/hqxyvs/usd/hqxyvs.usd"),
            visual_material_path="materials",
            scale=(1.000062751356276, 0.9999337620582391, 1.0000017270573833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightHqxyvs2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightHqxyvs2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.814936728584289, 0.27612057182141686, 1.8979266400352843),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/hqxyvs/usd/hqxyvs.usd"),
            visual_material_path="materials",
            scale=(1.000062751356276, 0.9999337620582391, 1.0000017270573833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightPodyre0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightPodyre0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.587283756155986, 0.2760919282946415, 2.1367601127646387),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/podyre/usd/podyre.usd"),
            visual_material_path="materials",
            scale=(0.9999229110273024, 0.9999229110273024, 1.000024993927349),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightPodyre1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightPodyre1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.815518131155987, 0.2760919282946415, 2.136760112764639),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/podyre/usd/podyre.usd"),
            visual_material_path="materials",
            scale=(0.9999229110273024, 0.9999229110273024, 1.000024993927349),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerQkgvsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerQkgvsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.900747595968792, 1.9988203536423341, 0.06350336431336912),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower/qkgvsz/usd/qkgvsz.usd"),
            visual_material_path="materials",
            scale=(0.999999045337586, 0.9999734130023439, 0.9996344873588806),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerheadKdvrbf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerheadKdvrbf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.80539977755153, 11.460543678875588, 1.4970434084535427),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/showerhead/kdvrbf/usd/kdvrbf.usd"),
            visual_material_path="materials",
            scale=(1.0000854002659767, 1.0000293006874454, 0.9999934895484207),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerheadLrfpvk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerheadLrfpvk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.386465892283255, 21.587368183620693, 0.5167538995135034),
            rot=(-0.7062067153338603, 0.0, 0.0, 0.7080057028141512),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/showerhead/lrfpvk/usd/lrfpvk.usd"),
            visual_material_path="materials",
            scale=(1.0000188332714188, 0.9999326498757942, 1.000013938003796),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerheadVbijwn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerheadVbijwn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.344175317441325, 1.835207967497294, 1.519082842830515),
            rot=(0.9905985015903491, 0.0, 0.0, 0.13680134738720626),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/showerhead/vbijwn/usd/vbijwn.usd"),
            visual_material_path="materials",
            scale=(1.0001138758930843, 1.000110515112989, 0.9999863841737922),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerheadVuswbv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerheadVuswbv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.072821601806073, 5.570324740832367, 1.4394325692691938),
            rot=(0.49999991386579, 0.0, 0.0, 0.8660254535140425),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/showerhead/vuswbv/usd/vuswbv.usd"),
            visual_material_path="materials",
            scale=(0.9999322066798352, 1.000065860847104, 1.000006299951903),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkAwvzkn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkAwvzkn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.799565835340221, -1.889879687739913, 0.868158649401087),
            rot=(0.7080055539544371, 1.7610260428494733e-07, 1.3512827605650214e-07, 0.7062068645727124),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/awvzkn/usd/awvzkn.usd"),
            visual_material_path="materials",
            scale=(1.0000105153402437, 0.9999997970853343, 0.9999061058759314),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkQnequy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkQnequy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.32362348924825, 11.733788865881007, 0.7453889785868508),
            rot=(0.8977357813708943, 0.0, 0.0, -0.4405342970148748),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/qnequy/usd/qnequy.usd"),
            visual_material_path="materials",
            scale=(1.0000110620620237, 0.9999940319654079, 1.0000564829884109),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkQnequy1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkQnequy1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.347132994466172, 11.730473694182624, 0.7462639785868508),
            rot=(-0.28170555609367, 0.0, 0.0, 0.9595009013367087),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/qnequy/usd/qnequy.usd"),
            visual_material_path="materials",
            scale=(1.0000110620620237, 0.9999940319654079, 1.0000564829884109),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkUpwldu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkUpwldu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.898523500520003, 19.848796965232932, 0.5935004944202941),
            rot=(0.7080055837566814, 0.0, 0.0, 0.7062068346945962),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/upwldu/usd/upwldu.usd"),
            visual_material_path="materials",
            scale=(1.0000431714844202, 0.9999859414571284, 1.0000105706101867),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkVekaaf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkVekaaf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.507453657530245, -1.23034928036716, 0.8872538473644391),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/vekaaf/usd/vekaaf.usd"),
            visual_material_path="materials",
            scale=(1.0000905454940436, 1.0000030777294882, 1.0000265112389422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorXqdonc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorXqdonc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.626646041870117, 5.38101863861084, 2.310051441192627),
            rot=(0.7071068286895752, -9.87816606290437e-10, 9.878164952681345e-10, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/xqdonc/usd/xqdonc.usd"),
            visual_material_path="materials",
            scale=(1.0014057783068908, 0.9999763460103728, 1.0000104010562796),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorZlxolj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorZlxolj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.203454971313477, 14.708863258361816, 2.310055732727051),
            rot=(0.001272515393793583, 1.516957254255047e-10, 1.1920926823449918e-07, 0.9999992847442627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/zlxolj/usd/zlxolj.usd"),
            visual_material_path="materials",
            scale=(0.9997383693241546, 0.9999972722342985, 1.0000175850935105),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaLugrhk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaLugrhk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.471776130512676, -1.2558359557617604, 0.26915415668142695),
            rot=(0.7080054051704394, 0.0, 0.0, 0.7062070137356624),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/lugrhk/usd/lugrhk.usd"),
            visual_material_path="materials",
            scale=(1.000007247878313, 0.9999845566735166, 1.0000678659900866),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaLugrhk1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaLugrhk1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.68603497549371, 0.535771361075905, 0.2700291318998377),
            rot=(0.9999991909437012, 2.2573958996150572e-07, -2.8715222790492345e-10, -0.001272050271081854),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/lugrhk/usd/lugrhk.usd"),
            visual_material_path="materials",
            scale=(1.000007247878313, 0.9999845566735166, 1.0000678659900866),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaWnzdke0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaWnzdke0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.710139519730259, -1.2195643674386019, 0.3036534557375244),
            rot=(0.9243654233532242, 0.0, 0.0, 0.3815082752824826),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/wnzdke/usd/wnzdke.usd"),
            visual_material_path="materials",
            scale=(1.0000060252060672, 1.0000182564363194, 0.9999432245604599),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    stoveMjvqii0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/stoveMjvqii0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.168539047241211, -0.5106414556503296, 0.8938388228416443),
            rot=(0.9999992251396179, -2.4716068764973897e-06, -3.143944660166653e-09, 0.001272039138711989),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stove/mjvqii/usd/mjvqii.usd"),
            visual_material_path="materials",
            scale=(1.0000826952676296, 1.0000149695592808, 0.9986960392917755),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLkxmne0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLkxmne0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.9836559295654297, -0.49994713068008423, 1.7917757034301758),
            rot=(1.0000001192092896, 8.715869626030326e-08, -5.820766091346741e-11, 8.917072591430042e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lkxmne/usd/lkxmne.usd"),
            visual_material_path="materials",
            scale=(1.000083933756752, 1.0000014693204056, 1.0000300302062857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallClockOqmbtp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallClockOqmbtp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.23630702383129, 13.85559771606564, 1.7556825951641841),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_clock/oqmbtp/usd/oqmbtp.usd"),
            visual_material_path="materials",
            scale=(1.0004311680106215, 1.000060602427561, 0.9999595277766573),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightBkaivt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightBkaivt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.86226093794089, 21.017440448802816, 2.4293787610828876),
            rot=(0.999999981838895, 0.0, 0.0, -0.0001905838649430557),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/bkaivt/usd/bkaivt.usd"),
            visual_material_path="materials",
            scale=(1.0000906625384185, 0.9999916952584763, 0.999689787425001),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightCstgzt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightCstgzt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.32542465254631, 0.7616910403939053, 2.577210648910906),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/cstgzt/usd/cstgzt.usd"),
            visual_material_path="materials",
            scale=(0.9999949001035905, 1.0000593726167024, 0.9999984186050545),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightCstgzt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightCstgzt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.3015965275463115, 0.7578629153939054, 2.577210648910906),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/cstgzt/usd/cstgzt.usd"),
            visual_material_path="materials",
            scale=(0.9999949001035905, 1.0000593726167024, 0.9999984186050545),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightCstgzt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightCstgzt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.255244720830058, 0.7527868040067035, 2.577210648910906),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/cstgzt/usd/cstgzt.usd"),
            visual_material_path="materials",
            scale=(0.9999949001035905, 1.0000593726167024, 0.9999984186050545),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightCstgzt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightCstgzt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2778384708300576, 0.7551930540067034, 2.577210648910906),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/cstgzt/usd/cstgzt.usd"),
            visual_material_path="materials",
            scale=(0.9999949001035905, 1.0000593726167024, 0.9999984186050545),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightJhpygl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightJhpygl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.878094757960216, 25.839395312474807, 2.4293708024846317),
            rot=(-0.6994095896157515, -0.004091330253701571, 0.019630387019661875, 0.7144397349502193),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/jhpygl/usd/jhpygl.usd"),
            visual_material_path="materials",
            scale=(1.000209451917065, 0.9999209603191888, 0.9997438461862799),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightUrhftt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightUrhftt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.225087095847538, 11.902282669967637, 2.429977194853727),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/urhftt/usd/urhftt.usd"),
            visual_material_path="materials",
            scale=(1.0001216242910669, 0.9999912108336884, 0.999689787425001),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightYylrlu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightYylrlu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.323356583876652, 2.5607690810902337, 1.918542705149098),
            rot=(0.0012722450335955259, 0.0, 0.0, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/yylrlu/usd/yylrlu.usd"),
            visual_material_path="materials",
            scale=(0.9999976940506227, 1.00005758140228, 1.000000410110114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightYylrlu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightYylrlu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.701934708876652, 2.559815956090234, 2.256210734934098),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/yylrlu/usd/yylrlu.usd"),
            visual_material_path="materials",
            scale=(0.9999976940506227, 1.00005758140228, 1.000000410110114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightYylrlu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightYylrlu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5283803265508746, 2.5628025280496285, 1.918562236399098),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/yylrlu/usd/yylrlu.usd"),
            visual_material_path="materials",
            scale=(0.9999976940506227, 1.00005758140228, 1.000000410110114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightYylrlu3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightYylrlu3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9077865765508746, 2.561833778049629, 2.256210734934098),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/yylrlu/usd/yylrlu.usd"),
            visual_material_path="materials",
            scale=(0.9999976940506227, 1.00005758140228, 1.000000410110114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightYylrlu4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightYylrlu4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.110794144910862, 2.563878455779629, 2.256210734934098),
            rot=(0.0012722450335955259, 3.2605751867817936e-22, 2.5628494998092716e-19, 0.9999991906959598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/yylrlu/usd/yylrlu.usd"),
            visual_material_path="materials",
            scale=(0.9999976940506227, 1.00005758140228, 1.000000410110114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfAmyper0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfAmyper0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.96145898437476, 13.162423828127508, 1.3974018554700005),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/amyper/usd/amyper.usd"),
            visual_material_path="materials",
            scale=(1.0000263829497356, 1.0000686757459558, 1.00001542088881),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfFjozhc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfFjozhc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.291356186808787, 19.64774071841008, 1.0456051635704149),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/fjozhc/usd/fjozhc.usd"),
            visual_material_path="materials",
            scale=(1.0004445849641312, 1.0000022396007089, 1.001001656000789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfPfusrd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfPfusrd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.122431367063153, -2.0285329430266943, 1.8042776010631039),
            rot=(0.6755901869956726, 5.90619580223429e-08, 6.445482082733044e-08, 0.7372773557048559),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/pfusrd/usd/pfusrd.usd"),
            visual_material_path="materials",
            scale=(0.9999751441014201, 0.9999593333504073, 0.999617959948723),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfPfusrd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfPfusrd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.122423808431071, -2.0285335419694914, 1.5033001204863912),
            rot=(0.6755899683298132, 1.757806673229002e-07, -1.610732003044668e-07, 0.7372775560750953),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/pfusrd/usd/pfusrd.usd"),
            visual_material_path="materials",
            scale=(0.9999751441014201, 0.9999593333504073, 0.999617959948723),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfZlaser0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfZlaser0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.946971679689998, 7.466675781250003, 1.3974018554700012),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/zlaser/usd/zlaser.usd"),
            visual_material_path="materials",
            scale=(1.0000226078700813, 1.0000668661663035, 1.00001542088881),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvLeeqgt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvLeeqgt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.83782969658321, 24.247353636990823, 1.6184247580330673),
            rot=(0.9999991915501732, 0.0, 0.0, -0.0012715734347293131),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/leeqgt/usd/leeqgt.usd"),
            visual_material_path="materials",
            scale=(1.0002857857614826, 0.9999994884314137, 0.9999710464014786),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvOvzajm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvOvzajm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.7933146291299, 3.895817133202975, 1.1424780760802509),
            rot=(-0.7062068346945962, 0.0, 0.0, 0.7080055837566814),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/ovzajm/usd/ovzajm.usd"),
            visual_material_path="materials",
            scale=(1.0003140029611912, 0.99999894574961, 0.9999706603335277),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wardrobeBhyopq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wardrobeBhyopq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.257492065429688, 15.460380554199219, 1.0635321140289307),
            rot=(0.6617242693901062, -0.031081967055797577, -0.0037925904616713524, 0.7490931749343872),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wardrobe/bhyopq/usd/bhyopq.usd"),
            visual_material_path="materials",
            scale=(0.9999341078451317, 0.9999822801027052, 0.9999850513819595),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wardrobeKtworp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wardrobeKtworp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.017996446729295, 20.40069147956394, 1.578610298154863),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wardrobe/ktworp/usd/ktworp.usd"),
            visual_material_path="materials",
            scale=(1.0000056994794648, 1.0000173616371864, 1.0000042395570352),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wardrobeLrokhl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wardrobeLrokhl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(20.283897542053015, 24.147379385440352, 1.5562389435752502),
            rot=(-0.7062068943749571, 0.0, 0.0, 0.7080055242279386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wardrobe/lrokhl/usd/lrokhl.usd"),
            visual_material_path="materials",
            scale=(0.9999758756375281, 1.0000305219888712, 1.0000043236382248),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    washerYnwamu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/washerYnwamu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.996631622314453, 0.3348013460636139, 0.4679093658924103),
            rot=(0.9999993443489075, -7.275957614183426e-12, -5.484537268785061e-10, -0.0012717247009277344),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/ynwamu/usd/ynwamu.usd"),
            visual_material_path="materials",
            scale=(1.0000297699772112, 0.9999531503248864, 0.9999463216280942),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowBvqijp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowBvqijp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(23.3700247448134, 3.191020960578006, 1.1523086714205106),
            rot=(0.9961946944266231, 0.0, 0.0, 0.08715578464018893),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/bvqijp/usd/bvqijp.usd"),
            visual_material_path="materials",
            scale=(1.0000364110963353, 0.9999880648156821, 1.000001381911285),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowDbqbzg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowDbqbzg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0744428230919383, 2.9993278907971055, 1.41687553578512),
            rot=(-0.08715568851837911, 0.0, 0.0, 0.9961947028361913),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/dbqbzg/usd/dbqbzg.usd"),
            visual_material_path="materials",
            scale=(1.0001573112064412, 1.0000402648675397, 0.9999837534451943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowDbqbzg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowDbqbzg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0744428230919383, 3.9430271095471054, 1.41687553578512),
            rot=(-0.08715568851837911, 0.0, 0.0, 0.9961947028361913),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/dbqbzg/usd/dbqbzg.usd"),
            visual_material_path="materials",
            scale=(1.0001573112064412, 1.0000402648675397, 0.9999837534451943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowDbqbzg2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowDbqbzg2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0744428230919383, 4.886616953297105, 1.41687553578512),
            rot=(-0.08715568851837911, 0.0, 0.0, 0.9961947028361913),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/dbqbzg/usd/dbqbzg.usd"),
            visual_material_path="materials",
            scale=(1.0001573112064412, 1.0000402648675397, 0.9999837534451943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowDbqbzg3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowDbqbzg3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0744428230919385, 5.830409922047106, 1.41687553578512),
            rot=(-0.08715568851837911, 0.0, 0.0, 0.9961947028361913),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/dbqbzg/usd/dbqbzg.usd"),
            visual_material_path="materials",
            scale=(1.0001573112064412, 1.0000402648675397, 0.9999837534451943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowDfdweq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowDfdweq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.01099305748523, 4.765551165506976, 1.354684115969907),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/dfdweq/usd/dfdweq.usd"),
            visual_material_path="materials",
            scale=(0.9996206170178713, 0.9999915527907073, 1.0000181676715605),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEyvzfu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEyvzfu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.09288223141299, 9.738027151167563, 1.3183471537306906),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/eyvzfu/usd/eyvzfu.usd"),
            visual_material_path="materials",
            scale=(0.9997859201033653, 1.0000057989860371, 1.0000066953138886),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowGlimdy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowGlimdy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.684081289319744, -2.4223924402500843, 1.6306275540577786),
            rot=(0.7372772716061827, 0.0, 0.0, -0.6755902787732688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/glimdy/usd/glimdy.usd"),
            visual_material_path="materials",
            scale=(0.9999683135009969, 1.000001861777883, 0.9999930931258357),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowHkuyre0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowHkuyre0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.027753753037537, 6.937985114713445, 1.3581678474691552),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/hkuyre/usd/hkuyre.usd"),
            visual_material_path="materials",
            scale=(1.0004198886917093, 0.9999981190595686, 0.999996905330817),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowHohdkt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowHohdkt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.550095579874245, 3.433888343394459, 2.1099599558115005),
            rot=(0.9396926455845855, 0.0, 0.0, -0.3420200751918555),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/hohdkt/usd/hohdkt.usd"),
            visual_material_path="materials",
            scale=(1.0000807070914697, 0.9999710749213174, 1.0000693189351075),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowHwunjt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowHwunjt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.670357681003896, -2.452131213116282, 2.2008329681164316),
            rot=(0.6755901869956753, 0.0, 0.0, 0.7372773557048585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/hwunjt/usd/hwunjt.usd"),
            visual_material_path="materials",
            scale=(0.9999821410241122, 0.9999964989514851, 1.0000465474009748),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIggzsd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIggzsd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.469130627905539, 3.16642308388079, 1.0049960888006715),
            rot=(0.9659258371900801, 0.0, 0.0, -0.2588190044193875),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/iggzsd/usd/iggzsd.usd"),
            visual_material_path="materials",
            scale=(1.0001310298896706, 0.999986318854417, 1.0000012040955977),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIjpvgf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIjpvgf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0740694690388721, 1.7310319961695257, 1.3547644539406851),
            rot=(0.9990482217883634, 0.0, 0.0, 0.043619382635579296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ijpvgf/usd/ijpvgf.usd"),
            visual_material_path="materials",
            scale=(0.9998350177622288, 0.9999640877549244, 0.9999891087431797),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowJrnfkt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowJrnfkt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.687888973034745, 18.773949315408334, 2.17554748032659),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/jrnfkt/usd/jrnfkt.usd"),
            visual_material_path="materials",
            scale=(1.0000863344664535, 1.0000105073669692, 1.0000578308924757),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowKwbnhy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowKwbnhy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.388048532945927, 16.863650155930184, 1.325033327331605),
            rot=(0.9914448327776861, 2.7794490451105347e-08, 2.1111975598162927e-07, -0.1305264094288226),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/kwbnhy/usd/kwbnhy.usd"),
            visual_material_path="materials",
            scale=(1.0001006250454398, 0.9999593591874798, 1.0000000460121818),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowKwbnhy1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowKwbnhy1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.382730417943183, 14.77245357473745, 1.3237602560414725),
            rot=(0.9914448655597188, 0.0, 0.0, -0.13052616042491694),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/kwbnhy/usd/kwbnhy.usd"),
            visual_material_path="materials",
            scale=(1.0001006250454398, 0.9999593591874798, 1.0000000460121818),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowKwbnhy2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowKwbnhy2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.359885142048864, 5.7921753840838, 1.3235922262564708),
            rot=(0.9914448655597188, 9.980958722195155e-10, 7.581289708355555e-09, -0.13052616042491672),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/kwbnhy/usd/kwbnhy.usd"),
            visual_material_path="materials",
            scale=(1.0001006250454398, 0.9999593591874798, 1.0000000460121818),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowKwbnhy3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowKwbnhy3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.466947855533647, -2.4836977925949486, 1.3304368310952752),
            rot=(-0.6087613358817373, -2.7337321157914313e-08, -3.214966986821764e-07, 0.7933534117500085),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/kwbnhy/usd/kwbnhy.usd"),
            visual_material_path="materials",
            scale=(1.0001006250454398, 0.9999593591874798, 1.0000000460121818),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowNruots0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowNruots0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.2727305356056827, 2.381993888945816, 1.354776660931485),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/nruots/usd/nruots.usd"),
            visual_material_path="materials",
            scale=(0.9996579061114627, 0.999956526235931, 0.9999891964628922),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowNszybf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowNszybf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(22.72819915685968, -2.4949862942403143, 1.3258356443075463),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/nszybf/usd/nszybf.usd"),
            visual_material_path="materials",
            scale=(1.0000511164212724, 0.9999686508053647, 0.9999891395832432),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowQfifse0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowQfifse0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(21.868302153414202, 9.057649512886968, 1.3236859506558702),
            rot=(4.013392641057306e-07, 0.0, 0.0, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/qfifse/usd/qfifse.usd"),
            visual_material_path="materials",
            scale=(0.9997061913945171, 0.9999776463019807, 1.00001360266049),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowQvqecb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowQvqecb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.963960673864015, -1.226465478982207, 1.6539055153148672),
            rot=(-0.043619338017151635, 0.0, 0.0, 0.999048223736445),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/qvqecb/usd/qvqecb.usd"),
            visual_material_path="materials",
            scale=(1.0000010724393913, 0.9999863381160738, 1.000027164317384),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowRopopf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowRopopf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(17.95866854952183, 14.767534708699108, 1.3581847954786777),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ropopf/usd/ropopf.usd"),
            visual_material_path="materials",
            scale=(1.0004198886917093, 0.9999982161351815, 0.999996905330817),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowRopopf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowRopopf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(18.030557221401825, 20.82100297041911, 1.3586257134486774),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ropopf/usd/ropopf.usd"),
            visual_material_path="materials",
            scale=(1.0004198886917093, 0.9999982161351815, 0.999996905330817),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowTojcni0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowTojcni0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.234834282280673, 0.6965777920368854, 2.121430953679594),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/tojcni/usd/tojcni.usd"),
            visual_material_path="materials",
            scale=(1.000090880233006, 0.9999944937395576, 1.0000553798907827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowTspbac0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowTspbac0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.39209398912973, 18.777831970438452, 1.5710137640206558),
            rot=(0.9990482217883634, 0.0, 0.0, 0.043619382635579296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/tspbac/usd/tspbac.usd"),
            visual_material_path="materials",
            scale=(1.0000911401608097, 1.0000349865043903, 0.9999941887340685),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowTspbac1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowTspbac1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.376862739933365, 12.788807559071726, 1.5577272235516175),
            rot=(0.999048229580669, 3.6141873778845123e-09, 1.282992481939676e-07, 0.043619204161865203),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/tspbac/usd/tspbac.usd"),
            visual_material_path="materials",
            scale=(1.0000911401608097, 1.0000349865043903, 0.9999941887340685),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowTspbac2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowTspbac2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.3639103877814, 7.702086751779939, 1.5713182357975184),
            rot=(0.9990482230870844, 9.399797288679108e-09, 1.751396705179131e-08, 0.04361935288995962),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/tspbac/usd/tspbac.usd"),
            visual_material_path="materials",
            scale=(1.0000911401608097, 1.0000349865043903, 0.9999941887340685),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUsynui0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUsynui0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(25.048371107758367, 25.4022745730142, 1.3585501183151456),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/usynui/usd/usynui.usd"),
            visual_material_path="materials",
            scale=(1.0000148116908552, 1.00001988976408, 1.0000128359138194),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUsynui1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUsynui1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(25.034716810834418, 20.104881994923865, 1.3062913433235066),
            rot=(0.9999999999999996, 2.29105835580273e-09, 6.827885972865612e-17, 2.97141291528194e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/usynui/usd/usynui.usd"),
            visual_material_path="materials",
            scale=(1.0000148116908552, 1.00001988976408, 1.0000128359138194),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUsynui2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUsynui2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(25.04095118583442, 22.492610510548865, 1.3062913433235066),
            rot=(0.9999999999999996, 2.29105835580273e-09, 6.827885972865612e-17, 2.97141291528194e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/usynui/usd/usynui.usd"),
            visual_material_path="materials",
            scale=(1.0000148116908552, 1.00001988976408, 1.0000128359138194),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowWogynv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowWogynv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.22554088997579322, -2.376129481256982, 1.317461754897141),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/wogynv/usd/wogynv.usd"),
            visual_material_path="materials",
            scale=(0.9998391827898311, 1.0000006943119741, 0.9999936648689252),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowXkxvpp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowXkxvpp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(19.534403288610278, -2.474242969005051, 1.4008891171253683),
            rot=(0.6755901869956753, 0.0, 0.0, 0.7372773557048585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/xkxvpp/usd/xkxvpp.usd"),
            visual_material_path="materials",
            scale=(1.0000355228513431, 1.000014851105149, 0.9999888185023038),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowXucvcj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowXucvcj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(24.488319574308708, 10.923111396987471, 1.2675708953759095),
            rot=(0.6427875280052628, -3.723212387480123e-08, -2.581970594224418e-08, 0.7660445116576984),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/xucvcj/usd/xucvcj.usd"),
            visual_material_path="materials",
            scale=(1.0002734489301581, 0.9999584017202491, 0.9999849266453342),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYikxbf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYikxbf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.5026506525488745, 5.366275570115623, 1.3521471985252635),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/yikxbf/usd/yikxbf.usd"),
            visual_material_path="materials",
            scale=(0.9999464425200615, 1.0000432823175196, 0.9999891964628922),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYjbico0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYjbico0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1294606508878502, -2.1550340788927738, 1.3154539975769464),
            rot=(4.013392641057306e-07, 0.0, 0.0, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/yjbico/usd/yjbico.usd"),
            visual_material_path="materials",
            scale=(0.9996865517129523, 1.0000629978891602, 0.9999936648689252),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYzxhbp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYzxhbp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.791370085137123, 2.0573630270506733, 1.0101655133191012),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/yzxhbp/usd/yzxhbp.usd"),
            visual_material_path="materials",
            scale=(1.0002671891311397, 1.0000014854651753, 0.9999809394934648),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
