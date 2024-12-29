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
class rsIntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Rs_int/usd/Rs_int_quick.usd"),
        )
    )
@configclass
class rsIntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Rs_int/usd/Rs_int_quick.usd"),
        )
    )
    bottomCabinetBamfsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.786360740661621, -0.4619655907154083, 0.37486329674720764),
            rot=(0.7017709016799927, 0.0, 8.731149137020111e-11, 0.7124028205871582),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.0426144702793727, 0.9254328096501743, 1.2737257921324534),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetDajebq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetDajebq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.5546810626983643, 1.3098887205123901, 0.6295499801635742),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/dajebq/usd/dajebq.usd"),
            visual_material_path="materials",
            scale=(1.0769934234372787, 1.2925173863098627, 1.4045275874732728),
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
            pos=(1.659630298614502, -1.4950345754623413, 0.37349462509155273),
            rot=(0.7071070075035095, -2.3283064365386963e-08, 1.1328666005283594e-08, -0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(2.4062967691769317, 2.3137010379510268, 2.0005446215524776),
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
            pos=(1.4725978374481201, 0.4147590100765228, 0.5975964665412903),
            rot=(0.7117639183998108, -3.3937394618988037e-06, 5.397396307671443e-06, -0.702418863773346),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.8021465138530984, 1.5148273045439071, 1.536074847523986),
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
            pos=(0.17002037167549133, -3.765857219696045, 0.5976011157035828),
            rot=(-3.183959051966667e-07, -9.883660823106766e-06, 1.667037395236548e-06, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.1866340345909558, 0.9822755421368985, 1.536074847523986),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableFqluyq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableFqluyq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.47626304626464844, -1.219603180885315, 0.27633601427078247),
            rot=(0.7053368091583252, 2.3865140974521637e-09, -1.964508555829525e-09, 0.708872377872467),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/fqluyq/usd/fqluyq.usd"),
            visual_material_path="materials",
            scale=(1.242184319354393, 1.4171409939406037, 1.14723922336079),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.850145697593689, 0.01472057867795229, 1.0062870979309082),
            rot=(1.0000001192092896, 8.44790120027028e-05, -0.0001269269414478913, -1.4550377613886667e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(0.985200549679146, 1.174635729751024, 1.6805418495093234),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    laptopNvulcs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/laptopNvulcs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5805546641349792, -1.514533281326294, 0.43608567118644714),
            rot=(-0.7054606080055237, -6.184563972055912e-11, 5.768185928900493e-11, 0.7087491750717163),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/laptop/nvulcs/usd/nvulcs.usd"),
            visual_material_path="materials",
            scale=(1.1510150813951234, 1.1082439053332038, 0.4340804169046447),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    loudspeakerBmpdyv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/loudspeakerBmpdyv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.631622552871704, -0.9296356439590454, 0.8893634080886841),
            rot=(0.7097623348236084, 4.656612873077393e-10, -2.760316419880837e-10, -0.704441249370575),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/loudspeaker/bmpdyv/usd/bmpdyv.usd"),
            visual_material_path="materials",
            scale=(2.344000039918083, 1.1627985738505835, 1.692142849938602),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantJatssq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantJatssq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.419967919588089, -0.8405460715293884, 0.4753910303115845),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/jatssq/usd/jatssq.usd"),
            visual_material_path="materials",
            scale=(1.6543306558646158, 1.4616322224549858, 0.5569085083275235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantJatssq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantJatssq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6151849031448364, -2.159517526626587, 0.8371506333351135),
            rot=(-0.7004682421684265, 0.0, -2.7939677238464355e-09, 0.7136837244033813),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/jatssq/usd/jatssq.usd"),
            visual_material_path="materials",
            scale=(0.7775590303028597, 0.9079894827569798, 0.835715236230733),
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
            pos=(-1.7601534128189087, -0.46633026003837585, 1.0049697160720825),
            rot=(0.7027013301849365, -4.656612873077393e-10, 1.7462298274040222e-10, 0.7114850878715515),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(0.7480314721900928, 0.8143105674214616, 0.8551925799846326),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.345369815826416, -3.9017586708068848, 0.6449483633041382),
            rot=(9.583280188962817e-06, 7.976312190294266e-06, -0.003429061733186245, 0.9999942779541016),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.7048467659680997, 1.7629323592788069, 1.1364622837528071),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8612831830978394, -3.355351209640503, 0.817762017250061),
            rot=(0.7036992907524109, 7.038470357656479e-06, -7.0502833295904566e-06, 0.710498034954071),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.5873714342797873, 2.0510858263634995, 1.442388612806053),
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
            pos=(-1.0200212001800537, -3.7997872829437256, 0.36790287494659424),
            rot=(2.6600901037454605e-07, -1.0991469025611877e-05, 9.251602023141459e-06, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.5948303586703123, 1.5752197276147508, 1.7199159078905804),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaMnfbbh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaMnfbbh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.53611421585083, -1.721792221069336, 0.3889223039150238),
            rot=(0.706346869468689, 7.712515071034431e-10, -1.3269527698867023e-09, 0.707865834236145),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/mnfbbh/usd/mnfbbh.usd"),
            visual_material_path="materials",
            scale=(1.087136480065697, 1.2567400817266314, 1.1663794534625964),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    standingTvUdotid0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/standingTvUdotid0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5403779745101929, -1.6025664806365967, 0.8462978005409241),
            rot=(-0.7004681825637817, 0.0, 2.3739232801744947e-10, 0.7136837244033813),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/standing_tv/udotid/usd/udotid.usd"),
            visual_material_path="materials",
            scale=(0.7535377545757459, 0.4325285700645468, 0.6621512351044242),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanYcfbsd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanYcfbsd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.4307308793067932, -2.5186469554901123, 0.2765984535217285),
            rot=(1.9371509552001953e-07, -4.656612873077393e-10, -8.731149137020111e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/ycfbsd/usd/ycfbsd.usd"),
            visual_material_path="materials",
            scale=(2.206333978721449, 2.163139789921491, 1.7239684059824139),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairAmgwaw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairAmgwaw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.525443434715271, 1.051008939743042, 0.45048078894615173),
            rot=(0.9986976385116577, 8.063609129749238e-05, 6.0984864830970764e-05, 0.051019106060266495),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(1.060143331443293, 0.8901687838412987, 1.0767479288403528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairAmgwaw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairAmgwaw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5741584300994873, -0.18128417432308197, 0.4504806101322174),
            rot=(-0.013349480926990509, -5.7783909142017365e-05, 8.34673919598572e-05, 0.9999110102653503),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(1.060143331443293, 0.8901687838412987, 1.0767479288403528),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairAmgwaw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairAmgwaw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9688517451286316, 0.37503647804260254, 0.45048055052757263),
            rot=(0.6572745442390442, 1.2606848031282425e-05, 0.00010076595935970545, 0.7536512613296509),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(1.060143331443293, 0.8901687838412987, 1.0767479288403528),
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
            pos=(-0.40415289998054504, 1.1010076999664307, 0.48770344257354736),
            rot=(-0.004629313945770264, -3.725290298461914e-09, 1.3271346688270569e-08, 0.9999892711639404),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.3173687188267598, 1.3230489439769202, 1.2655857532169819),
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
            pos=(-1.2552380561828613, 1.1008754968643188, 0.4877033829689026),
            rot=(0.004901699721813202, 0.0, 3.026798367500305e-09, 0.9999880194664001),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.3173687188267598, 1.3230489439769202, 1.2655857532169819),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairQtqitn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairQtqitn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.11770259588956833, -3.4406189918518066, 0.3834041953086853),
            rot=(0.9970977306365967, -0.003017208306118846, -0.0008220402523875237, 0.07606854289770126),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/qtqitn/usd/qtqitn.usd"),
            visual_material_path="materials",
            scale=(0.6997532955864033, 0.6274184183564425, 0.7365306636217052),
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
            pos=(-0.41030097007751465, -3.9152567386627197, 0.9109634160995483),
            rot=(0.0558452345430851, -0.0003238606732338667, -0.00013375560229178518, 0.9984394907951355),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.3590325568389083, 1.1551304322237963, 1.3728127026564225),
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
            pos=(-1.7631481885910034, 2.6273183822631836, 0.20842580497264862),
            rot=(0.7070950865745544, -0.002171493601053953, -0.0015548653900623322, 0.7071134448051453),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.800632764928117, 0.8006186739542117, 0.9425743955479172),
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
            pos=(-3.0744731081338106, -0.924002297729366, 0.40185830843548254),
            rot=(0.0015872274399298103, 0.0, 0.0, 0.9999987403537336),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.110494936639548, 1.1072834292287559, 1.4099234327626151),
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
            pos=(-1.6444785594940186, 3.209651470184326, 0.4450327754020691),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.6915484934383318, 1.4320807815364218, 1.6013290245277887),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.67306649684906, 2.1950864791870117, 0.424999862909317),
            rot=(0.7071069478988647, 0.0, -2.099795892718248e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(2.5209341119946, 1.154804157271007, 1.5467576823431897),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7825934886932373, 1.713455319404602, 0.43999984860420227),
            rot=(0.7090088725090027, 8.731149137020111e-11, -2.091837814077735e-10, 0.7051995396614075),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.37672333975080535, 1.390577592554019, 1.6013274408620914),
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
            pos=(-0.4199644818588833, -1.2938668212900015, 0.002372790995),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.0259640558832448, 2.34480701844136, 0.24480330607770978),
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
            pos=(-2.9412170410199985, 3.0338121337899993, 0.002372790994999999),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.2696339335281952, 0.7471937946096732, 0.24480330607770978),
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
            pos=(-0.80497244263, 1.5344866943350002, 1.0582098999),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.7666583492652268, 0.5878768682306896, 1.3196851520945228),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    dishwasherXlmier0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/dishwasherXlmier0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8229074478149414, 3.130038261413574, 1.0864630937576294),
            rot=(0.7057077884674072, 9.313225746154785e-09, 2.561137080192566e-09, 0.7085031270980835),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/xlmier/usd/xlmier.usd"),
            visual_material_path="materials",
            scale=(1.1235344210397478, 1.2022450684448702, 0.7561288516529707),
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
            pos=(-2.600227117538452, 1.5574636459350586, 1.1368626356124878),
            rot=(-6.134909926913679e-05, 2.3283064365386963e-10, -2.8421709430404007e-12, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(4.792224196041988, 4.8188972783996435, 5.30375420379901),
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
            pos=(0.999351978302002, 3.514899253845215, 1.1510995626449585),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.545243412751305, 3.146742786073207, 4.527199682615753),
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
            pos=(-2.14292251803063, 1.7185664756687886, 1.200281898479443),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
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
            pos=(1.4368029084441793, 1.4528103920901256, 1.200281898479443),
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
            pos=(-2.0166565834951253, 0.33873195507417947, 1.200281898479443),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
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

    electricSwitchWseglt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3608021942650657, 1.6290743735437532, 1.200281898479443),
            rot=(4.371138834797026e-08, 0.0, 0.0, 0.9999999999999992),
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
            pos=(1.5029642853991794, 3.4567071206051256, 1.200281898479443),
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

    electricSwitchWseglt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.1429244711435085, 0.38196015210277295, 1.200281898479443),
            rot=(0.7071069600004625, 0.0, 0.0, -0.7071066023725875),
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
            pos=(0.09982478618621826, 3.1454217433929443, 0.7401729822158813),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/xyejdx/usd/xyejdx.usd"),
            visual_material_path="materials",
            scale=(1.255203227875746, 1.0555772796070941, 0.9015748320766012),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    microwaveAbzvij0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/microwaveAbzvij0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7708547115325928, 3.1185147762298584, 1.4579927921295166),
            rot=(0.7057077884674072, 0.0, 2.3283064365386963e-10, 0.7085030674934387),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/microwave/abzvij/usd/abzvij.usd"),
            visual_material_path="materials",
            scale=(1.2994693827886101, 1.3235008181196088, 0.9894409733422809),
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
            pos=(-2.3516954631085003, 3.281256810158919, 1.5399998310641831),
            rot=(0.913880458093932, 0.0, 0.0, -0.4059833842831809),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(0.963037335686256, 3.134394460695662, 1.174542097429593),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ovenWuinhm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ovenWuinhm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6611706018447876, 2.137333869934082, 0.6010547280311584),
            rot=(0.7054358124732971, -4.656612873077393e-10, -2.9103830456733704e-10, 0.7087739706039429),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/wuinhm/usd/wuinhm.usd"),
            visual_material_path="materials",
            scale=(1.459848580665202, 1.7994668270009395, 1.6359055363798596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureEtixod0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureEtixod0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0649314881487495, -1.9343045598871187, 1.5949468403369633),
            rot=(0.007811542655180038, 0.0, 0.0, 0.9999694894352259),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/etixod/usd/etixod.usd"),
            visual_material_path="materials",
            scale=(0.48090042509135855, 1.22816416846137, 0.6087720979245624),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureHhxttu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureHhxttu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.858185995529013, -0.002778152363568382, 1.3701061128041114),
            rot=(-0.7047457871242812, 0.0, 0.0, 0.7094599181987502),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hhxttu/usd/hhxttu.usd"),
            visual_material_path="materials",
            scale=(0.6181130691213672, 1.1028412941285772, 0.5612415003028587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureJpfyrq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureJpfyrq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.006126339844539, -2.2551509299458834, 1.370106324830349),
            rot=(0.704735470790484, 0.0, 0.0, 0.7094701658348397),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jpfyrq/usd/jpfyrq.usd"),
            visual_material_path="materials",
            scale=(0.843835888418342, 1.1028412941285772, 0.508179302583062),
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
            pos=(-3.5728377804025695, 2.153495833524545, 0.9829766699502275),
            rot=(0.7086558445537313, 0.0, 0.0, 0.7055543168175202),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.2061054670961109, 1.1289756151780281, 0.9468503634827227),
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
            pos=(-2.5112054347991943, 3.1871869564056396, 0.4721888601779938),
            rot=(0.9188988208770752, -1.0331859812140465e-09, 1.8917489796876907e-10, -0.39449381828308105),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.297375640554232, 3.013087099338791, 4.392322065776637),
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
            pos=(-0.812124490737915, 3.1134910583496094, 0.3958650529384613),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(3.1679320142861322, 4.73773758118582, 3.9365535254804738),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletVtqdev0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletVtqdev0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.596611499786377, 3.0539870262145996, 0.2803792655467987),
            rot=(0.7071069478988647, -1.7578713595867157e-08, -2.4563632905483246e-08, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/vtqdev/usd/vtqdev.usd"),
            visual_material_path="materials",
            scale=(1.3223548968641654, 1.404242491871651, 1.3098530964920507),
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
            pos=(-1.8650922775268555, 2.4932522773742676, 1.9940497875213623),
            rot=(0.7071070075035095, 1.1823431123048067e-10, -8.294591680169106e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.122126758273967, 1.8480923818421933, 1.8402047739377418),
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
            pos=(-1.1658738851547241, 3.3278470039367676, 2.104857921600342),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.288847176111409, 1.5572633790568222, 1.9089458210276173),
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
            pos=(-0.37599804997444153, 3.3278470039367676, 2.104857921600342),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.4652585756972236, 1.5572633790568222, 1.9089458210276173),
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
            pos=(-1.2446132898330688, 1.7284971475601196, 2.104857921600342),
            rot=(0.0029106857255101204, -7.275957614183426e-12, 1.3599787962448318e-11, 0.999995768070221),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.4288084770867144, 1.1795349599921354, 1.9089458210276173),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLsyzkh3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLsyzkh3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.4146133065223694, 1.7284972667694092, 2.104857921600342),
            rot=(0.0029106857255101204, -7.275957614183426e-12, 1.3599787962448318e-11, 0.999995768070221),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.4288084770867144, 1.1795349599921354, 1.9089458210276173),
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
            pos=(-2.1847664194732777, 2.4673368050272857, 1.3700419875999723),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.5068504170839685, 1.4629754018960728, 0.6218834932011146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    towelRackKqrmrh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/towelRackKqrmrh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2149664688832296, 3.407100292392994, 1.370041987599972),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.7070745903985425, 1.7215558703213572, 0.6218834932011146),
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
            pos=(-0.7426389455795288, 3.5272388458251953, 1.4766805171966553),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.1063647940874697, 1.3134749107165347, 0.9675144422445981),
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
            pos=(1.9242632389068604, -1.372214674949646, 1.4766803979873657),
            rot=(0.7086357474327087, 0.0, -1.5370460459962487e-10, 0.7055745124816895),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.3681758093540024, 1.6715815117317196, 0.9675144422445981),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.17208796739578247, -4.095999717712402, 1.4766803979873657),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.3681758093540024, 2.0296881127469044, 0.9675144422445981),
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
            pos=(-4.015869617462158, -0.7962621450424194, 1.6087427139282227),
            rot=(-0.7062044143676758, 0.0, -4.254445684637176e-10, 0.7080079913139343),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.8214193381081418, 1.6789825025341452, 0.6475689952160582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
