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
class pomaria1IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_1_int/usd/Pomaria_1_int_quick.usd"),
        )
    )
@configclass
class pomaria1IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_1_int/usd/Pomaria_1_int_quick.usd"),
        )
    )
    armchairVzhxuf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.284467697143555, 0.8660444021224976, 0.4388193190097809),
            rot=(1.0, -0.0002936316595878452, -1.7585582099854946e-05, -6.344635039567947e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(1.4123287257084907, 1.0953886487199418, 0.946128678393195),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairVzhxuf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.354828834533691, -0.886446475982666, 0.43881934881210327),
            rot=(0.00785357691347599, 1.988327130675316e-05, -0.0002881483524106443, 0.9999691247940063),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(1.4123287257084907, 1.0953886487199418, 0.946128678393195),
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
            pos=(-8.2498140335083, -2.5902035236358643, 0.2982255518436432),
            rot=(3.2316893339157104e-07, -9.313225746154785e-10, -1.7447746358811855e-08, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/dnsjnv/usd/dnsjnv.usd"),
            visual_material_path="materials",
            scale=(0.9312730329431372, 0.824636258282742, 1.1644640369811154),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableUhrsex0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableUhrsex0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.41213738918304443, -1.9554641246795654, 0.6236165761947632),
            rot=(1.0000001192092896, -0.00011977603571722284, -0.0001592537882970646, 1.1767588148359209e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/uhrsex/usd/uhrsex.usd"),
            visual_material_path="materials",
            scale=(0.7033836759674414, 1.3223319472982742, 1.823940054857378),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableGcollb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableGcollb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.314801216125488, 0.06470133364200592, 0.23538440465927124),
            rot=(1.0000001192092896, -9.115774446399882e-06, 1.8996797734871507e-07, 1.949956640601158e-09),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/gcollb/usd/gcollb.usd"),
            visual_material_path="materials",
            scale=(0.696041720539009, 0.891389093656054, 0.8128166144099789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableGpkbiw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableGpkbiw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.607004165649414, -0.3543810546398163, 0.29471468925476074),
            rot=(0.7099297046661377, -8.955539669841528e-07, -1.04592277239135e-06, 0.7042726278305054),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/gpkbiw/usd/gpkbiw.usd"),
            visual_material_path="materials",
            scale=(1.75178643455621, 1.4141733491418633, 1.6752177076066683),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7271471619606018, -3.419099807739258, 0.5464226007461548),
            rot=(-1.5795230865478516e-06, -0.0004963069222867489, -0.0003635350149124861, 0.9999999403953552),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.8897637192170764, 1.8727922195270195, 1.7695231941538843),
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
            pos=(-1.730349063873291, -0.8603657484054565, 0.37365174293518066),
            rot=(-0.6812174320220947, -9.313225746154785e-09, 1.3969838619232178e-08, 0.7320812344551086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(0.9532846110721087, 0.9838056250084792, 0.9744446221841856),
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
            pos=(-1.7702574729919434, -1.3669779300689697, 0.37365174293518066),
            rot=(0.7099884152412415, -2.60770320892334e-08, -1.6763806343078613e-08, -0.7042133808135986),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(0.9532846110721087, 0.9838056250084792, 0.9744446221841856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7502574920654297, -1.816978096961975, 0.37365174293518066),
            rot=(0.7099884152412415, -2.60770320892334e-08, -1.6763806343078613e-08, -0.7042133808135986),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(0.9532846110721087, 0.9838056250084792, 0.9744446221841856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7306180000305176, -2.3419923782348633, 0.37365174293518066),
            rot=(0.750336766242981, -1.1175870895385742e-08, 1.862645149230957e-08, -0.6610556840896606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(0.9532846110721087, 0.9838056250084792, 0.9744446221841856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPmpwwi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPmpwwi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.37305977940559387, -1.4191088676452637, 0.4314139187335968),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(1.2548536771790368, 1.089088462775831, 1.0650818521688803),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPmpwwi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPmpwwi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.3965330719947815, -2.4412999153137207, 0.4314139187335968),
            rot=(1.94646418094635e-07, 0.0, 3.4415279515087605e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(1.2548536771790368, 1.089088462775831, 1.0650818521688803),
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
            pos=(-2.415330648422241, 2.327613353729248, 0.45514753460884094),
            rot=(0.7071069478988647, -4.656612873077393e-10, -3.4924596548080444e-10, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.1006794329814986, 1.1786464147715363, 1.6378318045020577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJrhgeu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJrhgeu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.56435227394104, 0.6901713609695435, 0.459918349981308),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.3556971960422377, 1.3131978772311286, 1.300756924519737),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopBmsclc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopBmsclc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.114680767059326, -2.685215473175049, 0.4771290421485901),
            rot=(1.9511207938194275e-07, -4.656612873077393e-10, 1.0077201295644045e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/bmsclc/usd/bmsclc.usd"),
            visual_material_path="materials",
            scale=(1.0842726490819774, 1.3640861055851237, 1.4873191692003036),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopBmsclc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopBmsclc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.549568176269531, -2.217616081237793, 0.4771290421485901),
            rot=(0.7054247856140137, 1.3969838619232178e-09, 5.413312464952469e-09, 0.7087849378585815),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/bmsclc/usd/bmsclc.usd"),
            visual_material_path="materials",
            scale=(0.8933073716431894, 1.2662887039385449, 1.4873191692003036),
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
            pos=(-4.554399490356445, -1.1859642267227173, 0.4752137064933777),
            rot=(0.7057815790176392, 0.0, -6.388290785253048e-09, 0.7084295749664307),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.627347294237456, 1.253925970216185, 1.44663790212104),
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
            pos=(0.7257447242736816, 2.160691499710083, 0.4752137064933777),
            rot=(0.7086536884307861, -6.984919309616089e-10, 9.313225746154785e-10, -0.7055564522743225),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.3880000887816517, 1.4073552922760877, 1.44663790212104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopSpojpj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopSpojpj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.14455243945121765, 0.6670510768890381, 0.47400104999542236),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.0823553280340823, 0.9020320754366918, 1.501383772171297),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopSpojpj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopSpojpj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7315117120742798, 1.4515360593795776, 0.47400104999542236),
            rot=(0.7072698473930359, -2.7939677238464355e-09, 3.92901711165905e-09, -0.7069436311721802),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.372999757872284, 1.4093423322535095, 1.501383772171297),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopUfhpbn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopUfhpbn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.8797435760498047, -2.69364595413208, 0.4895990490913391),
            rot=(1.9470712686597835e-07, 0.0, -1.8548528598477665e-12, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/ufhpbn/usd/ufhpbn.usd"),
            visual_material_path="materials",
            scale=(1.0664832984262582, 0.9851507440968973, 0.9729877712177613),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopVdedzt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopVdedzt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5953760147094727, 0.6641011834144592, 0.4740070700645447),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/vdedzt/usd/vdedzt.usd"),
            visual_material_path="materials",
            scale=(1.2223005723561045, 0.9020320754366918, 1.4747001769935286),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopVzzafs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopVzzafs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3176040649414062, -0.7145688533782959, 0.41422855854034424),
            rot=(0.7100717425346375, 3.725290298461914e-09, 3.725290298461914e-09, -0.7041294574737549),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/vzzafs/usd/vzzafs.usd"),
            visual_material_path="materials",
            scale=(0.9137338252221096, 0.8804583592930009, 1.0244098924770455),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    burnerPmntxh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/burnerPmntxh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.35677433013916, -1.4086010456085205, 0.9305217862129211),
            rot=(0.7071070075035095, 1.1641532182693481e-10, 2.0736479200422764e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/burner/pmntxh/usd/pmntxh.usd"),
            visual_material_path="materials",
            scale=(1.3353482357751698, 1.0991004084081568, 0.6398430614875542),
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
            pos=(-6.686223630117436, -0.8719468346631593, 0.002372852025),
            rot=(0.7124029353635258, 0.0, 0.0, -0.7017706588946507),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.7041761071919455, 3.050375494724209, 0.24480330607770978),
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
            pos=(-0.4985087415836018, -1.6834258345657769, 0.0023728520250000007),
            rot=(0.7128048469827513, 0.0, 0.0, -0.7013624242272297),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.298868059971997, 2.4231605588212637, 0.24480330607770978),
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
            pos=(0.03519791304837888, 0.6493060333406012, 0.9107998661420282),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.9813475745749152, 0.8194375277780452, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7802019805900001, -0.101375015255, 0.910799865725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5465617623821213, 1.959469891177468, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.519793945310018, -1.9229590306287014, 0.910799865725),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.6246839702239506, 3.758821868931493, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.13979663086, -2.6509067382850002, 0.910799865725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.17572601889233525, 1.1757537364613793, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.2247936997289885, -1.7225975036650483, 0.910799865725),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.8686445490984349, 4.364469671499538, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.774794799805001, -2.639566041708321, 0.910799865725),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.4978088056086489, 1.0687691216627562, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.69520162964, 1.69327389526, 0.910799865725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.673436926997423, 2.547346759408158, 0.5574803625793091),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    dishwasherDngvvi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/dishwasherDngvvi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.5506744384765625, -1.8178057670593262, 0.46027618646621704),
            rot=(0.7057815790176392, 0.0, -1.4406396076083183e-09, 0.7084294557571411),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/dngvvi/usd/dngvvi.usd"),
            visual_material_path="materials",
            scale=(1.2041546475659706, 0.983113061925905, 1.2446790448194136),
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
            pos=(-1.6141704320907593, 2.0247340202331543, 1.2662101984024048),
            rot=(1.9470462575554848e-07, 0.0, -5.435651928564766e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.175460897815606, 3.146742786073207, 4.9799425513765065),
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
            pos=(-3.784170627593994, 2.0247340202331543, 1.2662101984024048),
            rot=(1.9470462575554848e-07, 0.0, -5.435651928564766e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.175460897815606, 3.146742786073207, 4.9799425513765065),
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
            pos=(-4.654297828674316, 2.0247340202331543, 1.2662101984024048),
            rot=(1.9470462575554848e-07, 0.0, -4.867217739956686e-13, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.32963652457188, 3.146742786073207, 4.9799425513765065),
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
            pos=(-6.369140625, -3.0520873069763184, 1.0106627941131592),
            rot=(-1.1924880638503055e-08, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.112157820614232, 3.967250706182877, 2.89947329720228),
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
            pos=(1.119356632232666, -1.9446728229522705, 1.08461332321167),
            rot=(-0.7062960267066956, 0.0, 0.0, 0.7079166173934937),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.1732211254949245, 4.249801991942995, 3.111699687792625),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    clothesDryerZlmnfg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/clothesDryerZlmnfg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.4730077981948853, 3.714336395263672, 0.5285662412643433),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/zlmnfg/usd/zlmnfg.usd"),
            visual_material_path="materials",
            scale=(1.101007522032046, 1.2664452847806231, 1.1835704280242865),
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
            pos=(-9.51459125660082, -2.9530597250998745, 1.200281898479443),
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

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0278830046408205, 0.8366626564901257, 1.200281898479443),
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
            pos=(-4.819663794367681, -0.8750200349558268, 1.200281898479443),
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
            pos=(-0.9072611784708207, 1.0169386879851257, 1.200281898479443),
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

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1099396732726812, 2.1747609709041735, 1.200281898479443),
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
            pos=(-3.3218356413608205, 2.0769368569351254, 1.200281898479443),
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

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.299937231867681, 2.1689960783241733, 1.200281898479443),
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

    electricSwitchWseglt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.844901313966588, 1.0169404855260604, 1.200281910857951),
            rot=(0.9999999999988215, -1.527810589526929e-06, -2.3069298607652774e-13, 1.5099100571604893e-07),
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
            pos=(-7.34183295581582, -2.9530650961948743, 1.200281898479443),
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

    fridgeXyejdx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeXyejdx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.366483688354492, 0.5275813937187195, 0.894978940486908),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/xyejdx/usd/xyejdx.usd"),
            visual_material_path="materials",
            scale=(1.4122221063691378, 1.0827373794297392, 1.0901933062744449),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    fridgeXyejdx1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeXyejdx1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6601806879043579, 2.870018720626831, 0.894978940486908),
            rot=(0.7071070671081543, 5.820766091346741e-11, 4.5838532969355583e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/xyejdx/usd/xyejdx.usd"),
            visual_material_path="materials",
            scale=(1.349351368300355, 1.109761678753271, 1.0901933062744449),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    microwaveBfbeeb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/microwaveBfbeeb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4482274055480957, 0.5776987075805664, 1.714068055152893),
            rot=(1.000000238418579, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/microwave/bfbeeb/usd/bfbeeb.usd"),
            visual_material_path="materials",
            scale=(1.599758107358568, 2.213202323958883, 1.6572902969534204),
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
            pos=(-2.7548880613062825, 2.674793945315171, 1.5999998113860543),
            rot=(-0.7064730490957727, 0.0, 0.0, 0.7077399458143662),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.6750376910437605, 3.0791628402428755, 2.0728551254756105),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ovenFexqbj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ovenFexqbj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4547882080078125, 0.5630921721458435, 1.0869801044464111),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/fexqbj/usd/fexqbj.usd"),
            visual_material_path="materials",
            scale=(1.5051115165551598, 1.1014860930436383, 1.3443659129350742),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ovenFexqbj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ovenFexqbj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4547882080078125, 0.5630922913551331, 0.3619040846824646),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/fexqbj/usd/fexqbj.usd"),
            visual_material_path="materials",
            scale=(1.5051115165551598, 1.1014860930436383, 1.326251800759119),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ovenFexqbj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ovenFexqbj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.366499185562134, -1.4052133560180664, 0.45237997174263),
            rot=(0.7071069478988647, 2.3283064365386963e-09, 5.529727786779404e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/fexqbj/usd/fexqbj.usd"),
            visual_material_path="materials",
            scale=(1.6863800861426979, 1.1014860930436383, 1.6577213792366514),
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
            pos=(-12.868085896164605, -1.8702040665977633, 1.650449358469759),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qavxsz/usd/qavxsz.usd"),
            visual_material_path="materials",
            scale=(2.109662628933225, 1.1028412941285772, 2.53401298601099),
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
            pos=(-12.888073884698693, 1.9597959869681143, 1.650449488371676),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/rciuob/usd/rciuob.usd"),
            visual_material_path="materials",
            scale=(2.109662628933225, 1.1028412941285772, 2.112958815487256),
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
            pos=(0.9980388355636796, 0.07479698714417118, 1.780425202778155),
            rot=(-0.7068065782830458, 0.0, 0.0, 0.7074068566926763),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/tlwjpv/usd/tlwjpv.usd"),
            visual_material_path="materials",
            scale=(1.5567292111204805, 1.1028412941285772, 2.3969119147195124),
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
            pos=(-9.949796579110233, 2.9830846038184458, 1.700326686042061),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/zsirgc/usd/zsirgc.usd"),
            visual_material_path="materials",
            scale=(1.9495569082690916, 1.1028412941285772, 1.844065175761806),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.61540639695256, -1.9024097139840161, 0.2425317117206916),
            rot=(0.7078824971462865, 0.0, 0.0, 0.7063302133095665),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(3.660211110310575, 1.9589217559493675, 1.131487443800118),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.62540639659006, 1.9355546845440659, 0.24253171172069166),
            rot=(0.7078824971462865, 0.0, 0.0, 0.7063302133095665),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(3.660211110310575, 1.9589217559493675, 1.131487443800118),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVgzdul0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.1564795635685154, -1.993246854986521, 1.1307499451309508),
            rot=(-0.7059580429009392, 0.0, 0.0, 0.7082536563008169),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(3.120318119682288, 3.3817173744965605, 3.7607350436132996),
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
            pos=(-2.2886147499084473, 2.8973000049591064, 0.41527771949768066),
            rot=(0.70710688829422, -1.7462298274040222e-09, -1.8044374883174896e-09, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.418558232001259, 4.288009112061946, 4.033506276597152),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkZexzrc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkZexzrc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.5425195693969727, -2.6239824295043945, 0.40486428141593933),
            rot=(1.9471190171316266e-07, 0.0, 1.114131009671837e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(3.3439086058214915, 4.300362798288244, 4.025804422536481),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkZexzrc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkZexzrc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.9908735752105713, 2.6715757846832275, 0.40486451983451843),
            rot=(0.70710688829422, 2.3283064365386963e-10, -2.7895907805941533e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(4.083151636929867, 3.7896029847031554, 4.025804422536481),
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
            pos=(-3.0095021724700928, 3.7744739055633545, 0.3527521789073944),
            rot=(0.7110530734062195, 1.234002411365509e-08, 4.423782229423523e-09, -0.7031384110450745),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.3856158381015193, 1.0849791235150004, 1.3201314689565076),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.5609121322631836, 0.6988189220428467, 1.900869369506836),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.9131465292251533, 1.8496581394889902, 1.5829752665327066),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.709026336669922, -1.3964537382125854, 1.900869369506836),
            rot=(0.7071069478988647, 0.0, 8.733422873774543e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.1418741957200593, 1.4532397601903952, 1.5829752665327066),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.699026107788086, -2.446429491043091, 1.900869369506836),
            rot=(0.70710688829422, 0.0, 6.220943760126829e-10, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.1002115970871076, 1.4532397601903952, 1.5829752665327066),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.51245379447937, 2.638437032699585, 1.900869369506836),
            rot=(0.70710688829422, 0.0, 5.311449058353901e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.3289392635820136, 1.2771028633750952, 1.5829752665327066),
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
            pos=(0.878669023513794, 1.7417060136795044, 1.898733377456665),
            rot=(0.7080999612808228, 1.8917489796876907e-10, -3.637978807091713e-11, -0.706112265586853),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.432491999165532, 1.5477930103851, 2.4536891902018905),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLsyzkh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLsyzkh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.3459014892578125, 0.6360423564910889, 2.124849319458008),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.5712469692297244, 2.422746614482561, 2.6917473775351795),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLsyzkh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLsyzkh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.465827226638794, 0.6324058771133423, 2.1748859882354736),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.4652585756972236, 2.4660640937330984, 2.2022486827064003),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLsyzkh2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLsyzkh2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7748015522956848, 2.863919496536255, 2.124849319458008),
            rot=(0.7079858183860779, 1.8917489796876907e-09, 6.257323548197746e-10, -0.7062268257141113),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.546475057552679, 2.78618026539457, 2.6917473775351795),
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
            pos=(-2.215390682220459, 3.8206074237823486, 0.5255135297775269),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/omeuop/usd/omeuop.usd"),
            visual_material_path="materials",
            scale=(1.2580348440275781, 1.2895527379696934, 1.1947393947635878),
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
            pos=(-11.204122543334961, -3.0359859466552734, 1.324167013168335),
            rot=(1.9470462575554848e-07, 0.0, 1.1368683772161603e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(2.0555773622192137, 1.6715815117317196, 2.0018162620322),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5890811681747437, -3.8159866333007812, 1.4268529415130615),
            rot=(1.947337295860052e-07, 0.0, -1.5006662579253316e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(2.035957940273175, 1.6715815117317196, 2.2242904318207204),
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
            pos=(-7.904298305511475, -3.0240373611450195, 1.200500726699829),
            rot=(1.9471190171316266e-07, 0.0, -1.546140993013978e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.9728219537006403, 1.6789825025341452, 1.8887883806192287),
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
            pos=(-3.4158008098602295, -3.0240378379821777, 1.5689430236816406),
            rot=(1.9470462575554848e-07, 0.0, -4.5929482439532876e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.2970543219964004, 1.6789825025341452, 1.4030843474637498),
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
            pos=(-1.995273470878601, 4.2389020919799805, 1.8660284280776978),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0600912742392372, 1.798909824143727, 1.1871916334004826),
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
            pos=(-3.752488613128662, 4.2389020919799805, 1.3806008100509644),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.748343787279471, 1.798909824143727, 2.2665460567430746),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
