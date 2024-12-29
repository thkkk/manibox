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
class wainscott1IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Wainscott_1_int/usd/Wainscott_1_int_quick.usd"),
        )
    )
@configclass
class wainscott1IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Wainscott_1_int/usd/Wainscott_1_int_quick.usd"),
        )
    )
    armchairXqovyv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairXqovyv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.976426839828491, 13.188451766967773, 0.5037330985069275),
            rot=(0.9458731412887573, 0.00010925577953457832, 0.00044288113713264465, 0.3245364725589752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/xqovyv/usd/xqovyv.usd"),
            visual_material_path="materials",
            scale=(1.0653901967901593, 1.051966451932081, 1.067092165025067),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairXqovyv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairXqovyv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6723597049713135, 13.227959632873535, 0.5037329196929932),
            rot=(0.9785997867584229, 0.0003195367753505707, 0.0003260597586631775, -0.20577269792556763),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/xqovyv/usd/xqovyv.usd"),
            visual_material_path="materials",
            scale=(1.0653901967901593, 1.051966451932081, 1.067092165025067),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.413046360015869, 12.596630096435547, 0.40376898646354675),
            rot=(0.7094755172729492, 1.9371509552001953e-07, 1.708976924419403e-07, 0.704730212688446),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.6959614306036934, 1.1625308147943265, 1.4558709770545644),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.403046131134033, 9.726630210876465, 0.4037688970565796),
            rot=(0.7094756960868835, 2.8312206268310547e-07, 1.8347054719924927e-07, 0.7047300338745117),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.6959614306036934, 1.1625308147943265, 1.4558709770545644),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJhymlr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJhymlr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.280307292938232, -0.8498238921165466, 0.3931105434894562),
            rot=(1.7881393432617188e-07, -1.862645149230957e-09, 2.391607267782092e-08, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(1.954202877761251, 2.1919701545536383, 2.10561188106883),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJhymlr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJhymlr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6846587657928467, 8.740154266357422, 0.439089298248291),
            rot=(1.94646418094635e-07, 0.0, -3.2741809263825417e-11, 0.9999999403953552),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(2.581347991515647, 2.0702392711562503, 2.368813366202434),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableDnsjnv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableDnsjnv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2847623825073242, -1.6902034282684326, 0.5193579792976379),
            rot=(0.9999999403953552, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/dnsjnv/usd/dnsjnv.usd"),
            visual_material_path="materials",
            scale=(1.7161421511343942, 1.6758306352575485, 2.0378860083311876),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.191714286804199, -6.184265613555908, 0.8771560788154602),
            rot=(0.9999993443489075, 2.635750570334494e-05, 0.0011972991051152349, 3.548739186953753e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.7103386004045816, 1.3831468951907206, 2.252951370596715),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.704794406890869, 0.3856378495693207, 0.6274601817131042),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.4958156117246009, 1.1827112186638098, 1.5976343052639128),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3197860717773438, 13.35555648803711, 0.6374841332435608),
            rot=(1.0000001192092896, -3.937864676117897e-06, 8.288345270557329e-06, 3.6909909795213025e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.38440375439346997, 1.062490020506244, 1.6386046200435262),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableQlmqyy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableQlmqyy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.505349636077881, 7.8450446128845215, 0.2736164927482605),
            rot=(1.0, 2.023531123995781e-06, -8.976482786238194e-05, 9.016948752105236e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qlmqyy/usd/qlmqyy.usd"),
            visual_material_path="materials",
            scale=(0.8580900599820149, 1.039763746344229, 1.0021386405861088),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableQlmqyy1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableQlmqyy1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.185351371765137, 7.835045337677002, 0.2736165523529053),
            rot=(1.0000001192092896, 1.7440179362893105e-06, -8.980440907180309e-05, 1.756416168063879e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qlmqyy/usd/qlmqyy.usd"),
            visual_material_path="materials",
            scale=(0.8580900599820149, 1.039763746344229, 1.0021386405861088),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    poolTableAtjfhn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/poolTableAtjfhn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.629546642303467, -3.4802441596984863, 0.4312194287776947),
            rot=(0.7085225582122803, 2.3283064365386963e-10, -1.4915713109076023e-10, 0.7056881785392761),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pool_table/atjfhn/usd/atjfhn.usd"),
            visual_material_path="materials",
            scale=(1.2734743688067784, 1.1887675964027986, 0.8155046423241394),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4555890560150146, -6.196287155151367, 0.5868791937828064),
            rot=(0.7196151614189148, 8.381903171539307e-09, 0.0, -0.6943732500076294),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.2108832970862606, 1.2296845433719306, 1.5186516240486598),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.200064659118652, -5.561992168426514, 0.5868791937828064),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.2334796730524142, 1.2369333322387774, 1.5186516240486598),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPsoizi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPsoizi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1313962936401367, -1.6256394386291504, 0.4814831614494324),
            rot=(0.7946242690086365, -0.0004918844206258655, -0.0006600120104849339, 0.6071012616157532),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.2708396448290338, 1.240858742004809, 1.2673806434713333),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPsoizi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPsoizi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.18447436392307281, -0.7385860681533813, 0.48148229718208313),
            rot=(0.9998366832733154, -0.0008237062720581889, -0.000239458866417408, -0.018062492832541466),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.2708396448290338, 1.240858742004809, 1.2673806434713333),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPsoizi2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPsoizi2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.571789026260376, -1.735537052154541, 0.4814837872982025),
            rot=(-0.6924378275871277, 0.0007059494964778423, -0.0004140096716582775, 0.721477210521698),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.2708396448290338, 1.240858742004809, 1.2673806434713333),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPsoizi3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPsoizi3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.314862996339798, -2.5417981147766113, 0.4814816415309906),
            rot=(0.056687526404857635, 0.00019920035265386105, -0.0008252728148363531, 0.9983916282653809),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.2708396448290338, 1.240858742004809, 1.2673806434713333),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairDxusxd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairDxusxd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4787631034851074, -0.4171038568019867, 0.5545871257781982),
            rot=(-0.40985435247421265, 5.587935447692871e-09, -5.587935447692871e-09, 0.9121510982513428),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/dxusxd/usd/dxusxd.usd"),
            visual_material_path="materials",
            scale=(1.045781273375033, 1.0196103949959114, 1.028562649929374),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.205495357513428, 2.494927406311035, 0.8789052963256836),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.698620220313959, 1.8342980299185432, 1.6723253708336383),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.155430793762207, -0.3751048147678375, 0.8847981691360474),
            rot=(1.0, 8.621453889645636e-05, -0.00016861213953234255, -8.57508712215349e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.698620220313959, 1.8342980299185432, 1.6723253708336383),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.525525093078613, 7.919893264770508, 0.5844506621360779),
            rot=(1.0, 0.00010224386642221361, 2.8489073883974925e-05, -2.661518010427244e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.242096862461781, 1.9024875477593812, 1.644819105388792),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.165523052215576, 7.929888725280762, 0.5844438076019287),
            rot=(1.0000001192092896, 0.00011048910528188571, 2.3066564608598128e-05, -4.4939861254533753e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.242096862461781, 1.9024875477593812, 1.644819105388792),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.31937837600708, 12.574899673461914, 0.9807142019271851),
            rot=(1.0, 9.460534784011543e-05, 0.00012329296441748738, -1.1660862583084963e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.1739065685912893, 1.970677065600219, 1.644819105388792),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.37937593460083, 9.84489631652832, 0.9807167649269104),
            rot=(1.0000001192092896, 9.74280119407922e-05, 0.00012720286031253636, 6.920799933141097e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.1739065685912893, 1.970677065600219, 1.644819105388792),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanZotrbg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanZotrbg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.75571346282959, 4.5710883140563965, 0.21713608503341675),
            rot=(0.999994158744812, -0.0032271798700094223, 0.0011698298621922731, -1.6262210920103826e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.5337551766187446, 0.5618672674957903, 0.9819311501490322),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bathtubFdjykf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bathtubFdjykf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6574103832244873, 12.019161224365234, 0.18866202235221863),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/fdjykf/usd/fdjykf.usd"),
            visual_material_path="materials",
            scale=(2.1879447530298433, 1.8054165161411644, 1.11383127029956),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedMpgavt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedMpgavt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.315899617386012, 0.9794631449292319, 0.25257996463365595),
            rot=(0.7077896693683555, 0.0, 0.0, -0.7064232328678285),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/mpgavt/usd/mpgavt.usd"),
            visual_material_path="materials",
            scale=(1.1137794920135646, 1.1034353598689528, 1.0893923456931842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedZrumze0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedZrumze0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.342912285349026, 7.276208581206683, 0.2679111301919306),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(0.7313032157756549, 0.9602854024240317, 0.9399088241463356),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedZrumze2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedZrumze2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.529324069374593, 11.149224091048241, 0.46883183932167793),
            rot=(0.7080113282184949, 0.0, 0.0, 0.7062010755544647),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.3664887688047582, 1.171850356302006, 1.6449307370707549),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2755436897277832, 7.9173173904418945, 0.45514747500419617),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.1817381209136664, 1.3219207214182356, 1.6378318045020577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetImmwzb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetImmwzb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.224557399749756, 2.3294425010681152, 0.3418152630329132),
            rot=(-0.7039146423339844, 0.0, 1.9690560293383896e-10, 0.7102845311164856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/immwzb/usd/immwzb.usd"),
            visual_material_path="materials",
            scale=(2.090568601819955, 0.9179269137703779, 1.2737255122042237),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNnvyol0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNnvyol0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.3719162940979004, 13.314373016357422, 0.9642347097396851),
            rot=(0.9177242517471313, 0.0, 4.979483492206782e-11, -0.3972181975841522),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nnvyol/usd/nnvyol.usd"),
            visual_material_path="materials",
            scale=(2.086316253085988, 1.3442141681415012, 2.052493346058203),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNnvyol1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNnvyol1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.4203731417655945, 8.522993087768555, 0.4567427635192871),
            rot=(1.9371509552001953e-07, 0.0, 1.4551915228366852e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nnvyol/usd/nnvyol.usd"),
            visual_material_path="materials",
            scale=(1.4157810293972815, 1.4959612739268746, 0.9722221785196837),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNnvyol2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNnvyol2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6503585577011108, 8.522993087768555, 0.4567427635192871),
            rot=(1.9371509552001953e-07, -2.3283064365386963e-10, 0.0, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nnvyol/usd/nnvyol.usd"),
            visual_material_path="materials",
            scale=(1.2927100706342596, 1.4959612739268746, 0.9722221785196837),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNnvyol3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNnvyol3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.480358123779297, 8.522993087768555, 0.4567427635192871),
            rot=(1.9371509552001953e-07, -2.3283064365386963e-10, 0.0, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nnvyol/usd/nnvyol.usd"),
            visual_material_path="materials",
            scale=(1.2927100706342596, 1.4959612739268746, 0.9722221785196837),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNnvyol4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNnvyol4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.6903581619262695, 8.522993087768555, 0.4567427635192871),
            rot=(1.9371509552001953e-07, -2.3283064365386963e-10, 0.0, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nnvyol/usd/nnvyol.usd"),
            visual_material_path="materials",
            scale=(1.2927100706342596, 1.4959612739268746, 0.9722221785196837),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNyfebf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNyfebf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.206735610961914, -0.296407014131546, 0.35660192370414734),
            rot=(-0.7039147615432739, 0.0, 5.704805516870692e-10, 0.7102846503257751),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nyfebf/usd/nyfebf.usd"),
            visual_material_path="materials",
            scale=(0.8162314571030223, 1.0050646348679133, 0.7561242004820128),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQohxjq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQohxjq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.373946189880371, 11.390183448791504, 0.3696109354496002),
            rot=(0.7071069478988647, -9.313225746154785e-09, 3.841705620288849e-09, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.0938915249347312, 1.2320705703831916, 1.1251808792489149),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQohxjq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQohxjq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.383945941925049, 12.500182151794434, 0.3696109354496002),
            rot=(0.7071069478988647, -9.313225746154785e-09, 3.841705620288849e-09, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.0938915249347312, 1.2320705703831916, 1.1251808792489149),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.7048009033200002, -3.41239715576, 0.0023727909950000004),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.9786216411917639, 3.9719316908700826, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6447995605500005, -0.151392181395, 0.0023727909950000004),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.4900478924281402, 2.1525315542196224, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.34520288086, 11.943168945310001, 0.710799804685),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5758331159469169, 2.725594615943448, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorKtydvs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorKtydvs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9598032236099243, 0.8431292176246643, 1.1368626356124878),
            rot=(1.9470462575554848e-07, 0.0, 2.4101609596982598e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(4.423307309596909, 6.806012377157428, 5.30375420379901),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorKtydvs1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorKtydvs1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.079792022705078, 4.851316928863525, 1.1368626356124878),
            rot=(1.9470462575554848e-07, 0.0, -5.9117155615240335e-12, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(4.546484901064382, 4.8188972783996435, 5.30375420379901),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.089634895324707, 3.024858236312866, 1.1510995626449585),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.805678382879907, 3.146742786073207, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9409489035606384, 5.4047136306762695, 1.1510995626449585),
            rot=(1.9470462575554848e-07, 5.820766091346741e-11, 3.410605131648481e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.968155599373168, 4.289190803946919, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2847319841384888, 4.715266227722168, 1.1510995626449585),
            rot=(-0.705750048160553, 2.9103830456733704e-11, -1.1453948900452815e-11, 0.7084610462188721),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.0692015544432785, 3.146742786073207, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.695830225944519, 11.279740333557129, 1.1510995626449585),
            rot=(1.9470462575554848e-07, 0.0, 1.0658141036401503e-14, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.175460897815606, 2.860414962044708, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.9702630043029785, 10.572954177856445, 1.1510995626449585),
            rot=(-0.7051827907562256, 0.0, -1.0247802606500045e-11, 0.7090255618095398),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.4077371419505402, 2.860414962044708, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5991144180297852, 7.7497076988220215, 1.1510995626449585),
            rot=(1.9470462575554848e-07, 0.0, -2.1316282072803006e-14, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.545243412751305, 4.575518627975419, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.590150833129883, 3.544266700744629, 1.1510995626449585),
            rot=(0.7059391140937805, -2.9103830456733704e-11, 1.4583889651476056e-12, 0.7082725763320923),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.5373735408647797, 2.860414962044708, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.635143518447876, 3.5492584705352783, 1.1510995626449585),
            rot=(0.7071069478988647, 0.0, 2.0955681634404755e-11, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.594222289568975, 3.146742786073207, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorOhagsq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorOhagsq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.3001580238342285, 7.09414529800415, 0.9860121011734009),
            rot=(0.70710688829422, 0.0, 0.0, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.0999938156579185, 3.1167136725172164, 2.8287788690487865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorOhagsq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorOhagsq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.8805105686187744, 7.786242961883545, 0.9860121011734009),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.306416979766554, 4.53523645408842, 2.8287788690487865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorOhagsq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorOhagsq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.262861967086792, 0.9042901992797852, 0.9860121011734009),
            rot=(0.7084882855415344, 0.0, 0.0, 0.7057226300239563),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.9785970461939126, 3.4021481346626414, 2.8287788690487865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    clothesDryerXsuyua0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/clothesDryerXsuyua0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.003837823867798, 6.984320640563965, 0.7101234197616577),
            rot=(-0.7048938274383545, -2.3283064365386963e-10, -4.656612873077393e-10, 0.709312915802002),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/xsuyua/usd/xsuyua.usd"),
            visual_material_path="materials",
            scale=(1.4266580571529268, 1.4888615578962798, 1.5060525305462447),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.210062890207319, 11.420816146684174, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.4968219208941794, 0.6966678139651257, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3399346683876812, 5.178303451374173, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8118559038065807, 7.826941861784454, 1.200281898479443),
            rot=(0.9999999999999887, 0.0, 0.0, 1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.142059231890222e-05, 8.009210189654173, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1703389674723189, 9.929921615434173, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.12261723949918, 11.066664273925126, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.450061181222319, 0.6083472746141732, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1264011750441796, 1.8166637725174835, 1.2002819007724825),
            rot=(0.9999999999998241, -5.93058727447138e-07, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.600339013252319, 2.8477411955141734, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.7796189497034205, 3.076945890104455, 1.200281898479443),
            rot=(0.9999999999999887, 0.0, 0.0, 1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.53563725902918, 4.9169418618151255, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4950769562941795, 5.476941861815125, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.450061425362319, 3.072122054889173, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.229664404717681, 5.1929982755941735, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.615203609108226, 4.724346923829999, 1.749999778780986),
            rot=(0.9999999999999962, 0.0, 0.0, 8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(3.19298046338702, 2.2000595480360157, 1.9000151504591616),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.694795166014533, 8.574248046875002, 1.3699998356479581),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.4133294523177589, 2.2000595480360157, 1.5545101396722316),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0302050632458097, 8.369918945314982, 1.5499998356479583),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.686882913497767, 3.5164131688274387, 1.5545101396722316),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.100204833985888, 8.369919921875049, 1.5499998356479583),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.686882913497767, 3.5164131688274387, 1.5545101396722316),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.650863037110001, 11.86879638672097, 1.4999997461830266),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.931272224661018, 2.637309876620579, 1.7273501146886807),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureCltbty0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureCltbty0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.443489217540142, 1.2447938985087459, 1.5002451780425092),
            rot=(0.7074963391820771, 0.0, 0.0, -0.7067170084580952),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/cltbty/usd/cltbty.usd"),
            visual_material_path="materials",
            scale=(0.9457611149613558, 1.1028412941285772, 1.294845527626215),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureFhkzlm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureFhkzlm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.443442823692684, 0.5347939169295639, 1.4002450671247302),
            rot=(0.7074963391820771, 0.0, 0.0, -0.7067170084580952),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fhkzlm/usd/fhkzlm.usd"),
            visual_material_path="materials",
            scale=(0.9457611149613558, 1.1028412941285772, 0.5762526505263383),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQavxsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQavxsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.0952042638501, 4.738085898630334, 1.5502859609412212),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qavxsz/usd/qavxsz.usd"),
            visual_material_path="materials",
            scale=(0.8292543109443772, 1.1028412941285772, 1.612490075820604),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureRciuob0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureRciuob0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.105204520806223, 8.138073643024399, 1.6001635002506251),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/rciuob/usd/rciuob.usd"),
            visual_material_path="materials",
            scale=(0.6838759835289483, 1.1028412941285772, 0.7684017278164814),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureTlwjpv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureTlwjpv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.760840122939657, 6.277359814902612, 1.5701389874711076),
            rot=(0.7076938516759036, 0.0, 0.0, 0.7065192228808245),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/tlwjpv/usd/tlwjpv.usd"),
            visual_material_path="materials",
            scale=(1.1713381184835912, 1.1028412941285772, 0.783560918156895),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureYrgaal0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureYrgaal0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5847954997593365, -6.591918734932306, 1.5502859742332074),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yrgaal/usd/yrgaal.usd"),
            visual_material_path="materials",
            scale=(1.818614342552888, 1.1028412941285772, 1.5105183654845165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureYtxhyl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureYtxhyl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.815218743829871, 3.0665560362625714, 1.600163398423771),
            rot=(0.0037822194860828284, 0.0, 0.0, 0.9999928473822995),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ytxhyl/usd/ytxhyl.usd"),
            visual_material_path="materials",
            scale=(1.062122103203595, 1.1028412941285772, 0.3842008639082407),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureZsirgc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureZsirgc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.595204278217325, 8.138086190733446, 1.6001632819826692),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/zsirgc/usd/zsirgc.usd"),
            visual_material_path="materials",
            scale=(0.6838759835289483, 1.1028412941285772, 0.9221493452049351),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerStallInvgma0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerStallInvgma0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.10686442358426, 3.9120420196837333, 1.2098174125871806),
            rot=(0.7075436673911081, 0.0, 0.0, -0.7066696248847413),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.986398639172925, 0.8556179512331232, 1.1653542935171972),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerStallInvgma1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerStallInvgma1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5692794104622196, 8.95923381401341, 1.1594082136386044),
            rot=(0.002551152047363437, 0.0, 0.0, 0.9999967458063209),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.6441287336647967, 2.0145770695771557, 1.1167814604216957),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkKsecxq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkKsecxq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5902115106582642, 7.7751994132995605, 0.4614205062389374),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.796921625945516, 4.809057214239104, 4.481572962832644),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkKsecxq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkKsecxq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.090198516845703, 8.64120101928711, 0.5075593590736389),
            rot=(1.9441358745098114e-07, 0.0, 1.9906565285054967e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.37242822081821, 4.087297208295706, 4.930092699306999),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkKsecxq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkKsecxq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0401990413665771, 8.641200065612793, 0.5075593590736389),
            rot=(1.9441358745098114e-07, 0.0, 1.9906565285054967e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.37242822081821, 4.087297208295706, 4.930092699306999),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkXiybkb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkXiybkb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.9655628204345703, 4.417100429534912, 0.4886716306209564),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/xiybkb/usd/xiybkb.usd"),
            visual_material_path="materials",
            scale=(4.129707364029457, 6.139766422136052, 4.931910227494589),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkXiybkb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkXiybkb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.885562896728516, 4.417100429534912, 0.4886716306209564),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/xiybkb/usd/xiybkb.usd"),
            visual_material_path="materials",
            scale=(4.129707364029457, 6.139766422136052, 4.931910227494589),
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
            pos=(6.085764408111572, 4.474066257476807, 0.30865731835365295),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.0688680448952188, 1.0467707850917245, 1.1551359314283232),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetFqhdne0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetFqhdne0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.485077381134033, -0.2348051816225052, 1.3989812135696411),
            rot=(0.70710688829422, 7.275957614183426e-11, -3.892637323588133e-10, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(3.147712240718385, 1.370532964733344, 2.9419422796952284),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetFqhdne1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetFqhdne1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.2679202556610107, 6.50524377822876, 1.8488599061965942),
            rot=(-0.7067137360572815, 8.803908713161945e-10, -6.293703336268663e-10, 0.7074998021125793),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(3.5286793807637324, 1.925669719468609, 2.2084445086090536),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetFqhdne2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetFqhdne2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8511313199996948, 8.031608581542969, 1.8488599061965942),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.4404546193708456, 1.4122412107690514, 2.2084445086090536),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetJvdbxh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetJvdbxh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.3828630447387695, -0.5282030701637268, 0.4090116620063782),
            rot=(0.7080984115600586, 4.656612873077393e-10, -1.0186340659856796e-10, 0.7061139345169067),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/jvdbxh/usd/jvdbxh.usd"),
            visual_material_path="materials",
            scale=(2.0762400829889174, 2.535514573883518, 1.914003081394182),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    towelRackKqrmrh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/towelRackKqrmrh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.785203779877553, 3.111838652156476, 1.3150314907033125),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(2.3813806577466754, 1.0325864343157334, 0.4668082200873506),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treadmillAckppx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treadmillAckppx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.779195785522461, 5.713918209075928, 0.415105938911438),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/treadmill/ackppx/usd/ackppx.usd"),
            visual_material_path="materials",
            scale=(1.1848596654001546, 1.0245382767658384, 1.2398714421297121),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treadmillAckppx1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treadmillAckppx1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6195733547210693, 5.708856105804443, 0.4151059687137604),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/treadmill/ackppx/usd/ackppx.usd"),
            visual_material_path="materials",
            scale=(1.1049545514021675, 1.0016320495730413, 1.2398714421297121),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    washerOmeuop0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/washerOmeuop0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.0276567935943604, 6.099041938781738, 0.6697710156440735),
            rot=(-0.7048938274383545, 9.313225746154785e-10, -8.731149137020111e-11, 0.709312915802002),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/omeuop/usd/omeuop.usd"),
            visual_material_path="materials",
            scale=(1.417975380333079, 1.566236986201212, 1.522625690199947),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5879735946655273, 12.801702499389648, 1.518796682357788),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.3158136063006958, 1.790533005075924, 1.5569807389712804),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.7516374588012695, -4.837796211242676, 1.5204005241394043),
            rot=(0.7071069478988647, 0.0, -1.2448708730516955e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1848152387858157, 2.9969716531525794, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.7516374588012695, -1.7377954721450806, 1.5204005241394043),
            rot=(0.7071070075035095, 0.0, -6.639311322942376e-11, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1848152387858157, 2.9969716531525794, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.4478650093078613, 13.764177322387695, 1.371857762336731),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.244906513025053, 1.9188371457533089, 1.6189770615270167),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.7516374588012695, -3.2777953147888184, 1.5204005241394043),
            rot=(0.7071070075035095, 0.0, -6.639311322942376e-11, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1848152387858157, 2.9969716531525794, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.7516374588012695, 4.833585739135742, 1.5204005241394043),
            rot=(0.7071069478988647, 0.0, -5.009042070014402e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.9853068350366341, 2.9969716531525794, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.751867294311523, 12.557870864868164, 1.5204005241394043),
            rot=(0.7088380455970764, -4.656612873077393e-10, -2.927436071331613e-10, 0.7053714394569397),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.8231282264820741, 2.9969716531525794, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.751867294311523, 9.66787052154541, 1.5204005241394043),
            rot=(0.7088380455970764, -4.656612873077393e-10, -2.927436071331613e-10, 0.7053714394569397),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.8231282264820741, 2.9969716531525794, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.381237030029297, -1.1340363025665283, 1.5204005241394043),
            rot=(1.9472645362839103e-07, 0.0, -7.275957614183426e-12, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.7709804175107267, 1.6789825025341452, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.458587169647217, 2.3523991107940674, 1.5204005241394043),
            rot=(0.708029568195343, 9.313225746154785e-10, 5.849756234965753e-10, -0.7061830163002014),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1848152387858157, 1.5590551809245634, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.458991527557373, 6.00095272064209, 1.5204005241394043),
            rot=(-0.7058907747268677, 0.0, -2.9103830456733704e-11, 0.7083209156990051),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1598454761138282, 1.5590551809245634, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.458991527557373, 6.980953216552734, 1.5204005241394043),
            rot=(-0.7058907747268677, 0.0, -2.9103830456733704e-11, 0.7083209156990051),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1598454761138282, 1.5590551809245634, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
