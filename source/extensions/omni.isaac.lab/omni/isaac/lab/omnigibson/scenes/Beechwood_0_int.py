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
class beechwood0IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Beechwood_0_int/usd/Beechwood_0_int_quick.usd"),
        )
    )
    
    breakfastTableSkczfi3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3609758847224382, 0.18461940718654588, 0.5524894393664023),
            rot=(-0.7066485412960432, 0.0, 0.0, 0.707564724307377),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.9359213658396688, 1.2227179384520295, 1.4337530461454588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )


@configclass
class beechwood0IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Beechwood_0_int/usd/Beechwood_0_int_quick.usd"),
        )
    )
    armchairBslhmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.995722770690918, 4.970620155334473, 0.32261669635772705),
            rot=(0.9246575832366943, -6.51925802230835e-09, -1.1175870895385742e-08, 0.38079968094825745),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(0.9150776159325086, 0.8728867415034302, 1.0322162861207331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairVzhxuf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.987375259399414, 5.004920959472656, 0.46623095870018005),
            rot=(0.9554652571678162, -0.00031119491904973984, 7.867440581321716e-05, -0.295104056596756),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(1.1447877851046122, 1.0881605292622818, 1.005231749661295),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetQacthv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetQacthv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4892301559448242, -5.467318534851074, 0.14820531010627747),
            rot=(0.7071056962013245, 1.0331859812140465e-07, -1.0642543202266097e-07, -0.7071079015731812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/qacthv/usd/qacthv.usd"),
            visual_material_path="materials",
            scale=(1.539953950106612, 1.2529400016803234, 0.8425464062783941),
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
            pos=(-9.104866981506348, -1.000379204750061, 0.5582724213600159),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/dnsjnv/usd/dnsjnv.usd"),
            visual_material_path="materials",
            scale=(1.3702178603077084, 2.7133322167254295, 2.1689140927565456),
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
            pos=(-2.154884099960327, -3.849635124206543, 0.5577882528305054),
            rot=(1.0000001192092896, -2.0213774405419827e-06, 8.572171282139607e-06, -4.2410101741552353e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.5933170172954779, 1.0423861412156812, 1.4337530461454588),
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
            pos=(-8.244890213012695, 5.710646152496338, 0.59759521484375),
            rot=(1.0000001192092896, 9.498626241111197e-08, 3.623315024015028e-06, -7.697599357925355e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.3453712572049512, 1.4432574942695036, 1.536074847523986),
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
            pos=(-6.399786949157715, 4.70012092590332, 0.39839616417884827),
            rot=(0.9951332807540894, -1.9185245037078857e-07, 7.552982424385846e-06, -0.09853804111480713),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.33422771410545765, 0.7217292665312045, 1.024049898349324),
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
            pos=(-3.3984949588775635, -5.5706353187561035, 0.5878925323486328),
            rot=(1.0000001192092896, -0.00011631243251031265, -8.995299867819995e-05, -1.262087607756257e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/uhrsex/usd/uhrsex.usd"),
            visual_material_path="materials",
            scale=(1.1470925400378877, 1.2722398084103754, 1.7314585872871446),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cedarChestFwstpx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cedarChestFwstpx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.23487663269043, -6.4902191162109375, 0.07892684638500214),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.0623027090369304, 0.802196663542049, 1.1507841888778216),
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
            pos=(-0.9796071648597717, -4.400035858154297, 0.27361631393432617),
            rot=(1.0, 1.1303207429591566e-05, -4.859862383455038e-05, -3.758914317586459e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qlmqyy/usd/qlmqyy.usd"),
            visual_material_path="materials",
            scale=(1.3728815073454046, 1.490944834307306, 1.0021386405861088),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampJcbvfi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampJcbvfi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.42198091745376587, -5.743961334228516, 0.847378134727478),
            rot=(2.086162567138672e-07, 0.0, 0.0, 0.9999999403953552),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/jcbvfi/usd/jcbvfi.usd"),
            visual_material_path="materials",
            scale=(1.5968677142668959, 1.7068482558809528, 1.712920136011723),
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
            pos=(-1.8649958372116089, -1.770521879196167, 0.8879084587097168),
            rot=(1.0000001192092896, 0.00011623523460002616, -0.00011545726738404483, -1.1035124771296978e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.2503298095734954, 1.4401460080431918, 1.482848672300802),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.699974060058594, 0.35944893956184387, 0.9826587438583374),
            rot=(1.0, 0.0001238716213265434, -0.00010650027979863808, -3.818964614765719e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.5915363319913307, 1.591540120880273, 1.6410831304606293),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.789918422698975, 0.5445188879966736, 0.8287506103515625),
            rot=(1.0, 9.94741712929681e-05, -8.988424815470353e-05, 6.110274739512533e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.5915363319913307, 1.4021072862248296, 1.384052031442173),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.219945907592773, 5.169431686401367, 1.0418200492858887),
            rot=(1.0000001192092896, 0.00012824160512536764, -9.703396790428087e-05, 4.112407623324543e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.970401099358292, 1.7429342337173546, 1.7398797713192584),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pianoBnxcvw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pianoBnxcvw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.86778450012207, 1.2125247716903687, 0.6070976853370667),
            rot=(1.628650352358818e-07, -3.259629011154175e-08, -3.0962291930336505e-07, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/piano/bnxcvw/usd/bnxcvw.usd"),
            visual_material_path="materials",
            scale=(0.9226416478000183, 0.7352756015939127, 1.08349441210333),
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
            pos=(-5.349847793579102, -5.926223278045654, 0.38726362586021423),
            rot=(0.7106190919876099, -2.330634742975235e-06, 1.9461000192677602e-05, 0.7035770416259766),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.2195970388896735, 1.6277131647159035, 1.8104257378421895),
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
            pos=(-0.8248081207275391, -1.810386061668396, 0.12101597338914871),
            rot=(1.0000001192092896, 1.3813242730975617e-05, 5.910396794206463e-06, 1.245189196197316e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.9237669079596422, 2.2388867538221824, 0.565743721900059),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanMiftfy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanMiftfy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.296513080596924, 4.53009557723999, 0.23465336859226227),
            rot=(0.9549878835678101, 0.0006014109239913523, 0.00017932677292264998, -0.296644389629364),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/miftfy/usd/miftfy.usd"),
            visual_material_path="materials",
            scale=(1.3996481000002892, 1.1904527702923642, 1.2327056495617417),
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
            pos=(-6.85340690612793, 1.5491573810577393, 0.31794822216033936),
            rot=(1.0, 8.313103171531111e-05, 2.5789428036659956e-05, 8.306233212351799e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(1.5794812898819692, 0.6619086486219729, 0.7599668677420659),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDmcixv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDmcixv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.81745433807373, -1.5382957458496094, 0.49228566884994507),
            rot=(0.7167900204658508, 3.364402800798416e-08, 1.1641532182693481e-09, 0.697289228439331),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dmcixv/usd/dmcixv.usd"),
            visual_material_path="materials",
            scale=(1.1862941774349038, 1.1196697015309731, 1.1598212301724813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDmcixv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDmcixv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.807364463806152, -1.013819932937622, 0.49228569865226746),
            rot=(0.6898730993270874, 2.130400389432907e-08, -9.487848728895187e-09, 0.7239303588867188),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dmcixv/usd/dmcixv.usd"),
            visual_material_path="materials",
            scale=(1.1862941774349038, 1.1196697015309731, 1.1598212301724813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDmcixv2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDmcixv2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.797249794006348, -0.46422749757766724, 0.49228569865226746),
            rot=(0.735982358455658, -1.2223608791828156e-08, -4.0745362639427185e-09, 0.677000880241394),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dmcixv/usd/dmcixv.usd"),
            visual_material_path="materials",
            scale=(1.1862941774349038, 1.1196697015309731, 1.1598212301724813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDmcixv3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDmcixv3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.361712455749512, -0.5242475271224976, 0.49228566884994507),
            rot=(-0.6835263967514038, -1.792795956134796e-08, 1.5774276107549667e-08, 0.7299258708953857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dmcixv/usd/dmcixv.usd"),
            visual_material_path="materials",
            scale=(1.1862941774349038, 1.1196697015309731, 1.1598212301724813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDmcixv4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDmcixv4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.39160442352295, -1.5417324304580688, 0.49228569865226746),
            rot=(-0.6960195899009705, -3.4924596548080444e-09, 7.101334631443024e-09, 0.7180228233337402),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dmcixv/usd/dmcixv.usd"),
            visual_material_path="materials",
            scale=(1.1862941774349038, 1.1196697015309731, 1.1598212301724813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDmcixv5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDmcixv5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.391603469848633, -1.0217324495315552, 0.49228569865226746),
            rot=(-0.6960195899009705, -3.4924596548080444e-09, 7.101334631443024e-09, 0.7180228233337402),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dmcixv/usd/dmcixv.usd"),
            visual_material_path="materials",
            scale=(1.1862941774349038, 1.1196697015309731, 1.1598212301724813),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairVkgbbl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairVkgbbl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.605079412460327, -5.019624710083008, 0.40597447752952576),
            rot=(1.0000001192092896, -3.787066088989377e-05, 1.6366131603717804e-05, 2.2631138563156128e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/vkgbbl/usd/vkgbbl.usd"),
            visual_material_path="materials",
            scale=(0.9829103405662826, 0.9239218355745668, 1.0141864762661614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairVkgbbl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairVkgbbl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1350793838500977, -5.019624710083008, 0.405974417924881),
            rot=(1.0000001192092896, -3.784208092838526e-05, 1.6392674297094345e-05, 2.873130142688751e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/vkgbbl/usd/vkgbbl.usd"),
            visual_material_path="materials",
            scale=(0.9829103405662826, 0.9239218355745668, 1.0141864762661614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairVkgbbl2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairVkgbbl2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6346683502197266, -6.051092147827148, 0.4059743285179138),
            rot=(0.004738934338092804, -1.6162171959877014e-05, -3.8377183955162764e-05, 0.9999887943267822),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/vkgbbl/usd/vkgbbl.usd"),
            visual_material_path="materials",
            scale=(0.9829103405662826, 0.9239218355745668, 1.0141864762661614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairVkgbbl3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairVkgbbl3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1746675968170166, -6.05109167098999, 0.405974417924881),
            rot=(0.004738873802125454, -1.6106292605400085e-05, -3.825681051239371e-05, 0.9999887943267822),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/vkgbbl/usd/vkgbbl.usd"),
            visual_material_path="materials",
            scale=(0.9829103405662826, 0.9239218355745668, 1.0141864762661614),
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
            pos=(0.6637774109840393, 0.5358966588973999, 0.44245636463165283),
            rot=(0.4264349639415741, -0.0007502473890781403, -0.002728434279561043, 0.904513955116272),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/qtqitn/usd/qtqitn.usd"),
            visual_material_path="materials",
            scale=(0.7974160025768295, 0.762943510615647, 0.8498210481907039),
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
            pos=(0.004603661131113768, -1.2139490842819214, 0.34181496500968933),
            rot=(1.94646418094635e-07, -9.313225746154785e-10, -4.3655745685100555e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/immwzb/usd/immwzb.usd"),
            visual_material_path="materials",
            scale=(1.737766279170859, 0.9475089740025162, 1.2737255122042237),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetImmwzb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetImmwzb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4741864204406738, -2.153531312942505, 0.41506049036979675),
            rot=(-0.7059402465820312, 0.0, 9.561063052387908e-11, 0.7082715034484863),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/immwzb/usd/immwzb.usd"),
            visual_material_path="materials",
            scale=(2.8867544886146224, 1.1740104202575445, 1.5467588721078935),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNddvba0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNddvba0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4433799982070923, -0.7879114747047424, 0.35168302059173584),
            rot=(-0.7059941291809082, 4.656612873077393e-10, -4.874891601502895e-10, 0.7082178592681885),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nddvba/usd/nddvba.usd"),
            visual_material_path="materials",
            scale=(1.8158136723572353, 1.336049290800766, 1.6958290425891183),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvpunw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvpunw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.944893836975098, -1.8122186660766602, 0.13851937651634216),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvpunw/usd/rvpunw.usd"),
            visual_material_path="materials",
            scale=(1.2075251351887801, 1.4987285125588725, 0.7233251943754399),
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
            pos=(-0.48961207270622253, 4.089244365692139, 0.44999951124191284),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.9731632512674934, 1.277989154357075, 1.6378301847362213),
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
            pos=(-4.220363616943359, -1.7598994970321655, 0.4488133192062378),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.333772987545571, 1.276002131663653, 1.3663142960012475),
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
            pos=(-4.985448360443115, -3.9081616401672363, 0.4488133192062378),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.5739215787339282, 1.3199336929441143, 1.3663142960012475),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQudfwe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQudfwe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.7557172775268555, -3.9291481971740723, 0.4249957203865051),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qudfwe/usd/qudfwe.usd"),
            visual_material_path="materials",
            scale=(1.3031906246819012, 1.2327823682772658, 1.3923039335339182),
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
            pos=(-7.827822208404541, -3.6410467624664307, 0.4476679563522339),
            rot=(0.7073922753334045, -5.587935447692871e-09, -5.238689482212067e-09, 0.7068212628364563),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.1946019804034267, 1.3433346008400073, 1.4180110671968567),
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
            pos=(-7.82762336730957, -4.425972938537598, 0.4476679563522339),
            rot=(0.707392156124115, -2.7939677238464355e-09, 5.3551048040390015e-09, 0.7068213224411011),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.2757948038752003, 1.342672315909437, 1.4180110671968567),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopSpojpj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopSpojpj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.59439754486084, -5.802371501922607, 0.4476679563522339),
            rot=(1.9371509552001953e-07, 0.0, 1.2922100722789764e-08, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(0.8238968979386752, 1.430093926744711, 1.4180110671968567),
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
            pos=(-6.379940509796143, -3.896937131881714, 0.46239542961120605),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/ufhpbn/usd/ufhpbn.usd"),
            visual_material_path="materials",
            scale=(0.9410331698672731, 0.9851507440968973, 0.9188539118547409),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3609758847224382, 0.18461940718654588, 0.5524894393664023),
            rot=(-0.7066485412960432, 0.0, 0.0, 0.707564724307377),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.9359213658396688, 1.2227179384520295, 1.4337530461454588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.39510710328408083, 1.309476335332554, 0.5524894393664024),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.0946585884536644, 1.2028150979543726, 1.4337530461454588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3659759173234955, 1.1796204691395502, 0.5524894393664023),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.7019619659658484, 1.2227179384520295, 1.4337530461454588),
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
            pos=(-5.751643180847168, -3.9581527709960938, 0.8939363360404968),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/burner/pmntxh/usd/pmntxh.usd"),
            visual_material_path="materials",
            scale=(1.277964935174815, 1.0611152551885903, 0.7468475325213091),
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
            pos=(-4.824897583005, 3.6337363281249995, 0.002372485815),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.4738029173230507, 1.601608223423425, 0.24480330607770978),
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
            pos=(-9.033685069849245, 3.22463941325247, 0.0023724858150000003),
            rot=(0.7004413028263442, 0.0, 0.0, 0.7137100120461626),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.8645802832932203, 2.190935098682141, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0048957519500004, 3.5092104492200007, 0.0023724858150000003),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.8712694437016129, 0.7431987950179347, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.974441650392446, -5.338779296876711, 0.0023724858149999995),
            rot=(0.7160360605658164, 0.0, 0.0, 0.6980632922374493),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.0035149696827441, 0.7701328245235266, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.974896728515002, -1.06196441269, 0.0023724858150000003),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.327189976173599, 2.8700850292776874, 0.24480330607770978),
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
            pos=(-4.719898193360001, -1.8010174560549999, 0.86036364746),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.542179373599419, 1.0687691216627562, 0.5826772151252665),
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
            pos=(-7.87941402695614, -4.861396195928406, 0.86036364746),
            rot=(0.9207635658750977, 0.0, 0.0, 0.39012107832950355),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.6024612369155605, 0.9163698968908918, 0.5826772151252665),
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
            pos=(-7.754895019535001, -4.037027954105, 0.86036364746),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5954126166591549, 2.761136484618158, 0.5826772151252665),
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
            pos=(-6.239897216799999, -5.7360703125, 0.86036364746),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.229788439735663, 1.1579828021240242, 0.5826772151252665),
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
            pos=(-6.897010742182505, -5.788636962892367, 0.86036364746),
            rot=(0.9187195701232532, 0.0, 0.0, 0.394910561358575),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5890492789276776, 0.8339773831449723, 0.5826772151252665),
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
            pos=(-7.801471543164013, -5.851282810623055, 0.86036364746),
            rot=(0.9316247769206889, 0.0, 0.0, -0.3634216215740013),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.3814316727519458, 1.261018320403235, 0.5826772151252665),
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
            pos=(-5.614899169925001, -3.82634741211, 0.8651575012200001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.8057194531861414, 1.6211041212187354, 0.2929134108467556),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.422003030595745, 3.234632760732456, 1.315957214355),
            rot=(0.7079612631042325, 0.0, 0.0, 0.7062512654458467),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.9610827913377493, 0.5343845608313781, 0.8503937734260647),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    dishwasherZnfvmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/dishwasherZnfvmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.986103534698486, -5.7885942459106445, 0.47428905963897705),
            rot=(1.9371509552001953e-07, 0.0, -2.240994945168495e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/znfvmj/usd/znfvmj.usd"),
            visual_material_path="materials",
            scale=(1.1802305077412816, 1.0908682807967713, 1.112041362142423),
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
            pos=(-2.719823122024536, -0.7444625496864319, 1.2662099599838257),
            rot=(-0.7049739360809326, 0.0, -9.85522774499259e-12, 0.7092332243919373),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.9634735077878127, 3.4302073318614217, 4.9799425513765065),
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
            pos=(-1.6513299942016602, 1.1081490516662598, 1.2662099599838257),
            rot=(0.9151540994644165, 2.9103830456733704e-11, -1.5781154161231825e-11, 0.40310439467430115),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(6.1221320683966445, 2.482462234327089, 4.9799425513765065),
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
            pos=(-1.4259370565414429, 2.0328528881073, 1.2662098407745361),
            rot=(0.3919946253299713, 2.9103830456733704e-11, -5.282885240376345e-12, 0.9199674725532532),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6468206645382772, 3.0493913259035175, 4.9799425513765065),
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
            pos=(-2.412421464920044, 2.1029579639434814, 1.2662100791931152),
            rot=(-0.3849916458129883, 5.820766091346741e-11, 2.525979425627156e-12, 0.9229201078414917),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6468206645382772, 4.108804274808964, 4.9799425513765065),
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
            pos=(-4.124839782714844, -0.8344624042510986, 1.2662099599838257),
            rot=(-0.7049739360809326, 5.820766091346741e-11, 1.3960388400846568e-11, 0.7092332243919373),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.9634735077878127, 2.5740871380162087, 4.9799425513765065),
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
            pos=(0.32953643798828125, 3.6546711921691895, 1.2662100791931152),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.805678382879907, 2.5740871380162087, 4.9799425513765065),
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
            pos=(-4.825575351715088, 4.4087724685668945, 1.0846128463745117),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.1970625752092983, 4.249801991942995, 3.111699687792625),
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
            pos=(-9.235522270202637, 0.9751263856887817, 1.0846128463745117),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.0271314259696025, 2.551611100996981, 3.111699687792625),
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
            pos=(-4.215477466583252, -6.764873504638672, 1.0846128463745117),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.8815282866425327, 2.551611100996981, 3.111699687792625),
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
            pos=(1.1596776247024536, 2.1380441188812256, 0.673663318157196),
            rot=(0.7074529528617859, 0.0, -4.278035703464411e-10, -0.7067606449127197),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/zlmnfg/usd/zlmnfg.usd"),
            visual_material_path="materials",
            scale=(1.083918345605087, 1.4410889651582905, 1.5085205058206472),
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
            pos=(-4.290373098704935, -1.397247892081247, 1.200281898479443),
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

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.1144344266188986, 2.513467501461666, 1.200281898479443),
            rot=(-0.38684205339300726, 0.0, 0.0, 0.9221459893784073),
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
            pos=(-2.656760343311492, -1.2505423054227731, 1.200281898479443),
            rot=(0.7071066023725878, 0.0, 0.0, 0.7071069600004621),
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

    electricSwitchWseglt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.8975474151099343, -1.397245573695734, 1.2002818983068801),
            rot=(4.371138834797026e-08, 1.8422972313731837e-15, 4.214684778958138e-08, 0.9999999999999983),
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
            pos=(-0.19676524182646307, 3.789227597499162, 1.2002818984794414),
            rot=(0.7071067215818923, -9.996003484842205e-08, 9.995999932128478e-08, 0.7071068407911837),
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
            pos=(-1.526760587417248, 2.7062400425552053, 1.200281898479443),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
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
            pos=(-0.9338197111858206, 1.6064881259903818, 1.2002818985511725),
            rot=(0.9999999999999998, -2.1073424255447017e-08, 0.0, 0.0),
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
            pos=(-8.190998101009885, 1.0027540609226828, 1.200281898479443),
            rot=(-5.523350525225252e-07, 0.0, 0.0, 0.9999999999998475),
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
            pos=(-2.6118029265208205, -1.5135156622931372, 1.200281899270871),
            rot=(0.9999999999999793, -2.03224743857768e-07, 0.0, 0.0),
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
            pos=(-4.0998085417508205, -1.5135118742062637, 1.2002818985908708),
            rot=(0.9999999999999996, -2.980232238769531e-08, 0.0, 0.0),
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
            pos=(-8.236547311280821, 0.906488059084714, 1.2002818996064735),
            rot=(0.9999999999999574, -2.9200193199910547e-07, 0.0, 0.0),
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
            pos=(-4.184204643974885, 1.0027540609226828, 1.200281898479443),
            rot=(-5.523350525225252e-07, 0.0, 0.0, 0.9999999999998475),
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

    electricSwitchWseglt9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8014358032709545, 2.340157796195566, 1.200281898479443),
            rot=(0.9206034973241998, 0.0, 0.0, -0.39049865648226256),
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

    fridgeDszchb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeDszchb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.848034381866455, -1.78300940990448, 0.8840968608856201),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/dszchb/usd/dszchb.usd"),
            visual_material_path="materials",
            scale=(1.5726437906460011, 1.0545133587440572, 1.0333452968150696),
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
            pos=(-5.944876194000244, -1.7721790075302124, 1.561263084411621),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/microwave/bfbeeb/usd/bfbeeb.usd"),
            visual_material_path="materials",
            scale=(1.599758107358568, 2.2510904495116977, 1.3256971690788772),
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
            pos=(-3.0098937988257264, 4.264389404295001, 1.6749995703665468),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.1984541684957635, 3.0791628402428755, 2.3319401487543154),
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
            pos=(-5.947904109954834, -1.7742741107940674, 0.911696195602417),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/wuinhm/usd/wuinhm.usd"),
            visual_material_path="materials",
            scale=(1.8835435340503508, 1.5455672835021272, 1.635748056062534),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureFanvpf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureFanvpf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.96489321237222, 1.0113364791192656, 1.7251838348379633),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fanvpf/usd/fanvpf.usd"),
            visual_material_path="materials",
            scale=(0.9747784541345458, 1.1028412941285772, 0.971173010905179),
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
            pos=(-1.0098919685806478, -1.3899480159264066, 1.5002855521566867),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hhxttu/usd/hhxttu.usd"),
            visual_material_path="materials",
            scale=(1.2804083179888477, 1.1028412941285772, 1.510782534901735),
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
            pos=(0.00010658752288490982, -1.3876566252874685, 1.500285953990995),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jpfyrq/usd/jpfyrq.usd"),
            visual_material_path="materials",
            scale=(1.2804083179888477, 1.1028412941285772, 1.367946622847276),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureLucjyq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureLucjyq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.689893625481751, 1.5978803842420182, 1.6251836601157421),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/lucjyq/usd/lucjyq.usd"),
            visual_material_path="materials",
            scale=(0.843835888418342, 1.1028412941285772, 0.6482476726566602),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQjkajj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQjkajj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.06014376812731, -0.47289530735736407, 1.525183468967424),
            rot=(0.7067145633175063, 0.0, 0.0, 0.7074987816208212),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qjkajj/usd/qjkajj.usd"),
            visual_material_path="materials",
            scale=(1.5058395057363432, 1.1028412941285772, 0.9711861099903772),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQtvjzk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQtvjzk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6720282034872158, 3.854623760234454, 1.7251836646915697),
            rot=(-0.706589820079402, 0.0, 0.0, 0.7076233646228469),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qtvjzk/usd/qtvjzk.usd"),
            visual_material_path="materials",
            scale=(0.843835888418342, 1.1028412941285772, 1.0371961318984628),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureWfdvzv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureWfdvzv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.656692980031922, 3.134610414038596, 1.7251834793170049),
            rot=(0.7092462027373855, 0.0, 0.0, 0.7049608669299308),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/wfdvzv/usd/wfdvzv.usd"),
            visual_material_path="materials",
            scale=(0.7128933227021382, 1.1028412941285772, 0.9723716147117206),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceQmsnld0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceQmsnld0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6607718470058903, -4.690186629944085, 0.5033036491817225),
            rot=(0.7077941949257269, 0.0, 0.0, 0.7064186985276097),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/qmsnld/usd/qmsnld.usd"),
            visual_material_path="materials",
            scale=(2.1016777995441447, 1.1163769241224564, 2.22882705393993),
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
            pos=(-1.971030778571239, -0.7715042044967949, 1.1936305677024135),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(2.7455663234582732, 1.7397856053654466, 2.0980842161590285),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.439802490235091, -1.902932575195403, 2.0653416013814034),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(3.1894832181354307, 1.9072615480085504, 1.4708420214161517),
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
            pos=(1.5462261832809063, -2.1589193969205978, 1.6467140853561824),
            rot=(-0.7065749675287271, 0.0, 0.0, 0.7076381951688153),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(2.0377587720374124, 2.6090342767191492, 2.6495455857175765),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkCzyfhq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkCzyfhq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.369039058685303, -5.35038948059082, 0.39907267689704895),
            rot=(0.3743709325790405, -3.725290298461914e-09, 1.0128132998943329e-08, 0.9272791147232056),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/czyfhq/usd/czyfhq.usd"),
            visual_material_path="materials",
            scale=(5.8631355533028024, 4.356009441224845, 4.034865427313741),
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
            pos=(-1.1148877143859863, 3.9468467235565186, 0.48448964953422546),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.585029258444575, 4.648487691226112, 4.705832831069821),
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
            pos=(-3.012913703918457, 4.04862642288208, 0.40486419200897217),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(4.435104820000586, 3.4982644128737306, 4.025804422536481),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaXhxdqf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaXhxdqf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1961156004106481, -5.524217738821677, 0.34308805107864065),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/xhxdqf/usd/xhxdqf.usd"),
            visual_material_path="materials",
            scale=(1.3989173980926983, 1.2997975258199648, 1.0273866407009256),
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
            pos=(-2.0242300033569336, 3.98357892036438, 0.35275179147720337),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.2677388072702211, 1.252613905606309, 1.3201314689565076),
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
            pos=(-5.0011305809021, -1.6255013942718506, 1.8759126663208008),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.1210428964035835, 1.4973843458583902, 1.6621320416786889),
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
            pos=(-4.2204999923706055, -1.6288539171218872, 1.8759126663208008),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.0396901488853156, 1.5415289315263854, 1.6621320416786889),
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
            pos=(-6.253450393676758, -5.9461822509765625, 1.8759126663208008),
            rot=(1.947337295860052e-07, 4.656612873077393e-10, 1.2494183465605602e-10, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.4745500458041807, 1.6293766570056951, 1.6621320416786889),
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
            pos=(-7.952447414398193, -3.674903631210327, 1.8759126663208008),
            rot=(0.7071070075035095, 4.656612873077393e-10, -7.30722149455687e-11, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.7571200973447483, 1.4753120530243928, 1.6621320416786889),
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
            pos=(-0.9221690893173218, 4.185327529907227, 1.898733139038086),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.210423368995113, 1.245825309086579, 2.4536891902018905),
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
            pos=(-1.5087915249128647, 3.3596340134029847, 0.9650311855233124),
            rot=(0.7074914542792097, 0.0, 0.0, 0.7067218987139773),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.2222324931626198, 0.6907048753910284, 0.4668082200873506),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvYlvjhb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvYlvjhb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.8653278946876526, -1.5804638862609863, 1.2952812910079956),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/ylvjhb/usd/ylvjhb.usd"),
            visual_material_path="materials",
            scale=(1.1537297148610486, 0.256671814610001, 0.9676656669256155),
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
            pos=(1.2480360269546509, 2.830386161804199, 0.6697707176208496),
            rot=(0.7074529528617859, -4.656612873077393e-10, -3.7834979593753815e-10, -0.7067605257034302),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/omeuop/usd/omeuop.usd"),
            visual_material_path="materials",
            scale=(1.0775891107598332, 1.6533615386746414, 1.522625690199947),
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
            pos=(-8.135035514831543, -5.0877885818481445, 1.5674535036087036),
            rot=(0.70710688829422, 1.862645149230957e-09, 1.0841176845133305e-09, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.2307086221401211, 1.0743198030455545, 1.4457436540770203),
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
            pos=(1.759078025817871, 0.16620537638664246, 1.3233150243759155),
            rot=(0.7074571847915649, -1.862645149230957e-09, -1.5218120097415522e-09, -0.7067562341690063),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.3944753914302592, 1.798909824143727, 1.7269234185586502),
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
            pos=(1.7592133283615112, 2.569976568222046, 1.3233150243759155),
            rot=(0.7071070075035095, 0.0, -1.21985976875294e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.5838320462841788, 1.798909824143727, 1.7269234185586502),
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
            pos=(-5.334045886993408, -6.782914638519287, 1.5689427852630615),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.5986500600609047, 1.0793458944862362, 1.4030843474637498),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.154046058654785, -6.782914638519287, 1.5689427852630615),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.5986500600609047, 1.0793458944862362, 1.4030843474637498),
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
            pos=(-0.7152137160301208, -6.05764102935791, 1.4718575477600098),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.758495536174733, 1.199273216095818, 1.6189770615270167),
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
            pos=(0.8047861456871033, -6.05764102935791, 1.4718575477600098),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.758495536174733, 1.199273216095818, 1.6189770615270167),
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
            pos=(-8.290804862976074, 6.162359237670898, 1.2291431427001953),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.2947211895556685, 1.199273216095818, 2.1585996997114414),
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
            pos=(-10.53727912902832, 4.784852981567383, 1.2291431427001953),
            rot=(0.7066448330879211, -4.656612873077393e-10, 4.857838575844653e-10, 0.707568347454071),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0476063929032433, 1.0793458944862362, 2.1585996997114414),
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
            pos=(-10.53727912902832, 1.6048527956008911, 1.2291431427001953),
            rot=(0.7066448330879211, -4.656612873077393e-10, 4.857838575844653e-10, 0.707568347454071),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0476063929032433, 1.0793458944862362, 2.1585996997114414),
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
            pos=(-10.289480209350586, -3.2029144763946533, 1.4233149290084839),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.833279975377336, 1.0793458944862362, 1.7269234185586502),
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
            pos=(-11.131333351135254, -2.1757919788360596, 1.4233149290084839),
            rot=(0.7071070075035095, 1.4901161193847656e-08, 3.728928277269006e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.833279975377336, 1.5590551809245634, 1.7269234185586502),
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
            pos=(-7.541004180908203, -6.108188152313232, 1.5689427852630615),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.4217782865429789, 0.9594185728766544, 1.4030843474637498),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
