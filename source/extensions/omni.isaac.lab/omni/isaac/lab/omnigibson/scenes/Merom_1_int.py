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
class merom1IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Merom_1_int/usd/Merom_1_int_quick.usd"),
        )
    )
@configclass
class merom1IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Merom_1_int/usd/Merom_1_int_quick.usd"),
        )
    )
    armchairBslhmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.188450813293457, 6.250100135803223, 0.31537115573883057),
            rot=(-0.2606499493122101, -7.450580596923828e-09, 1.909211277961731e-08, 0.9654334783554077),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(1.0214093485760671, 1.0221800960050367, 0.9472551460249075),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQplklw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQplklw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2052067071199417, 7.69870138168335, 0.4564605951309204),
            rot=(-0.6988385319709778, -3.4924596548080444e-09, 8.87666828930378e-09, 0.7152795791625977),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qplklw/usd/qplklw.usd"),
            visual_material_path="materials",
            scale=(1.0948606215379704, 1.0911749473322405, 1.0188985856137562),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQplklw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQplklw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0965465307235718, 8.221463203430176, 0.4564605951309204),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qplklw/usd/qplklw.usd"),
            visual_material_path="materials",
            scale=(1.0948606215379704, 1.0911749473322405, 1.0188985856137562),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQplklw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQplklw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0654692649841309, 7.138555526733398, 0.4564605951309204),
            rot=(-0.012497058138251305, 0.0, 1.0912231118709315e-09, 0.9999220371246338),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qplklw/usd/qplklw.usd"),
            visual_material_path="materials",
            scale=(1.0948606215379704, 1.0911749473322405, 1.0188985856137562),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQplklw3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQplklw3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9280519485473633, 7.65247917175293, 0.4564605951309204),
            rot=(0.7232236862182617, 1.862645149230957e-09, -4.918547347187996e-09, 0.6906139254570007),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qplklw/usd/qplklw.usd"),
            visual_material_path="materials",
            scale=(1.0948606215379704, 1.0911749473322405, 1.0188985856137562),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairTcxiue0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5969250798225403, -1.0764169692993164, 0.5877618789672852),
            rot=(-0.20450997352600098, -8.982794679468498e-05, 0.0004362144973129034, 0.978864312171936),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/tcxiue/usd/tcxiue.usd"),
            visual_material_path="materials",
            scale=(1.1162991317147999, 1.107014773851473, 1.1976185558926673),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hamperClziqw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hamperClziqw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.521274447441101, -1.575561285018921, 0.27214011549949646),
            rot=(0.7090759873390198, -2.9296614229679108e-05, 2.0740553736686707e-06, 0.7051321268081665),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hamper/clziqw/usd/clziqw.usd"),
            visual_material_path="materials",
            scale=(2.9611516583652153, 2.7666237544961723, 4.1484814464954445),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hamperWdsnjy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hamperWdsnjy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5091334581375122, -1.0515010356903076, 0.2413567453622818),
            rot=(0.7067416906356812, -9.387469617649913e-05, -9.121013135882095e-05, 0.7074719071388245),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hamper/wdsnjy/usd/wdsnjy.usd"),
            visual_material_path="materials",
            scale=(3.866370512393275, 4.598979796791976, 4.1402324776032815),
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
            pos=(-2.0332133769989014, -0.8340015411376953, 0.3706377446651459),
            rot=(6.392227078322321e-06, 5.047675222158432e-05, -1.6739593775128014e-05, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(0.7786764718083705, 1.0190944556652923, 1.2924197806085451),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedZrumze1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedZrumze1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.120194435119629, -0.15002931654453278, 0.4042786657810211),
            rot=(0.7081106305122375, -1.7208745703101158e-05, 1.2624002920347266e-05, -0.7061015963554382),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.1903644638148212, 1.0399605967316474, 1.4099234327626151),
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
            pos=(-1.1752872467041016, -1.5989748239517212, 0.3331078290939331),
            rot=(1.9185245037078857e-07, 7.003545761108398e-07, 7.844646461308002e-07, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.1817381209136664, 0.8152727495319879, 1.20108894713315),
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
            pos=(-0.34463033080101013, 1.3833967447280884, 0.5804942846298218),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/dajebq/usd/dajebq.usd"),
            visual_material_path="materials",
            scale=(1.1902813860081658, 1.2568642179496852, 1.296478591411325),
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
            pos=(0.9149672985076904, 10.0697660446167, 0.34397149085998535),
            rot=(1.0000001192092896, -7.2177499532699585e-09, -3.746663423953578e-09, -3.14321368932724e-09),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(1.6188585077551148, 1.3394468440715956, 1.8424103959352263),
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
            pos=(1.484519362449646, 0.5255780816078186, 0.4985949397087097),
            rot=(0.7071046829223633, -0.003411264158785343, -0.0034206316340714693, 0.7070925235748291),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.1812304519083263, 1.4365645829128322, 1.416337549917975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJrhgeu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJrhgeu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.484519362449646, -0.3044220209121704, 0.4985949695110321),
            rot=(0.7071046829223633, -0.003411247394979, -0.0034206127747893333, 0.7070925831794739),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.1812304519083263, 1.4365645829128322, 1.416337549917975),
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
            pos=(4.874759674072266, -1.2227351665496826, 0.24946428835391998),
            rot=(0.7071068286895752, 3.731111064553261e-08, -1.9907020032405853e-08, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.822659722193189, 0.9583262945351637, 0.9098032374688488),
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
            pos=(4.904759407043457, 0.9372642636299133, 0.24946404993534088),
            rot=(0.7071069478988647, -6.51925802230835e-09, -2.991873770952225e-08, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.822659722193189, 0.9583262945351637, 0.9098032374688488),
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
            pos=(-1.066648244857788, 7.691315174102783, 0.6374815106391907),
            rot=(1.0000001192092896, -7.690214260946959e-07, 1.778666046448052e-06, -1.4519901014864445e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.2701490799451265, 1.844128847323326, 1.6386046200435262),
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
            pos=(3.5979461669921875, 7.816161632537842, 0.2598097026348114),
            rot=(0.7126520872116089, 2.2118911147117615e-09, 7.8580342233181e-10, -0.7015178799629211),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/fqluyq/usd/fqluyq.usd"),
            visual_material_path="materials",
            scale=(1.1676835450607288, 1.3449461483834082, 1.1178152121916918),
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
            pos=(4.714974403381348, 9.854828834533691, 0.8938339948654175),
            rot=(1.0000001192092896, 0.00013270930503495038, -0.00010823123011505231, 4.905202786176233e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.477800824518719, 1.4021072862248296, 1.4927383259357914),
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
            pos=(4.809939384460449, 5.90984582901001, 0.8346719741821289),
            rot=(1.0000001192092896, 0.00012427649926394224, -0.000122434736113064, -9.01294970390154e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.136974688413501, 1.1369773951508453, 1.3939416850771622),
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
            pos=(1.5168317556381226, -0.5059992074966431, 1.2595951557159424),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.0236220145759165, 0.9770912905441925, 0.8994343838960479),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.2980477809906006, 8.269325256347656, 0.6375112533569336),
            rot=(0.9999998807907104, -0.0002509593032300472, 0.00033702864311635494, 4.526282282313332e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.7322834092823203, 1.7914018579656539, 2.0643195912605883),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.7972917556762695, 6.938416957855225, 0.5464264750480652),
            rot=(0.9999999403953552, -0.0003839709097519517, 0.00046226964332163334, 1.2126092769904062e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.7716534867660094, 1.954182581088385, 1.7695231941538843),
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
            pos=(3.1176581382751465, 9.344093322753906, 0.34633275866508484),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/xhxdqf/usd/xhxdqf.usd"),
            visual_material_path="materials",
            scale=(1.3570904836172681, 1.18766775341794, 1.0017673300676708),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanXcmniq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanXcmniq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.30922770500183105, -0.3062654435634613, 0.20390534400939941),
            rot=(-0.1962723284959793, 2.4515022232662886e-05, -6.43742096144706e-05, 0.9805494546890259),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/xcmniq/usd/xcmniq.usd"),
            visual_material_path="materials",
            scale=(1.7108202876090577, 1.7288737737211175, 1.5088061555387409),
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
            pos=(-1.2446330785751343, -1.5549230575561523, 0.8227310180664062),
            rot=(1.0, 0.00011281759361736476, 0.00019508697732817382, 2.2013809939380735e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.4265409477706954, 1.5629037489120077, 1.4800593537848132),
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
            pos=(4.8454084396362305, 0.9401716589927673, 0.6508283615112305),
            rot=(0.9999999403953552, -0.00014031989849172533, 0.0002971068606711924, 7.537592409789795e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.5629215355116797, 1.7667904072561134, 1.3703121330705275),
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
            pos=(4.8154144287109375, -1.2198282480239868, 0.6508291363716125),
            rot=(1.0, -0.0001410841941833496, 0.0003140312619507313, 6.427138487197226e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.5629215355116797, 1.7667904072561134, 1.3703121330705275),
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
            pos=(1.5304254293441772, 0.7251328825950623, 1.1529473066329956),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.1739065685912893, 1.8342980299185432, 1.5375724542604012),
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
            pos=(-0.4043590724468231, 3.3311126232147217, 0.2598988115787506),
            rot=(0.9999877214431763, -0.004378893878310919, 0.00216378434561193, -0.0008941427804529667),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.926900454233605, 0.8428009012436855, 1.1783173801788387),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanZotrbg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanZotrbg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5256824493408203, 4.451229095458984, 0.2603476047515869),
            rot=(0.9999920725822449, -0.0035099510569125414, 0.001750150229781866, -0.000821359979454428),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.702205835625398, 0.7303149618050887, 1.1783173801788387),
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
            pos=(4.612729549407959, 4.226726055145264, 0.18866196274757385),
            rot=(-0.7058199644088745, -9.313225746154785e-10, 1.2164491636212915e-09, 0.7083913683891296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/fdjykf/usd/fdjykf.usd"),
            visual_material_path="materials",
            scale=(1.8160451138387237, 1.226343315110967, 1.11383127029956),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.38492751121521, 5.5549516677856445, 0.44999977946281433),
            rot=(0.7056798934936523, 0.0, 2.3283064365386963e-10, 0.7085309028625488),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(1.1506087701143586, 1.3543726830161782, 1.6378301847362213),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.38492751121521, 6.074952125549316, 0.44999977946281433),
            rot=(0.7056798934936523, 0.0, 2.3283064365386963e-10, 0.7085309028625488),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(1.1506087701143586, 1.3543726830161782, 1.6378301847362213),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.379021644592285, 3.642699956893921, 0.44999977946281433),
            rot=(0.7071070075035095, -3.2014213502407074e-10, -3.9381120586767793e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.6835368612124662, 1.3771111322990903, 1.6378301847362213),
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
            pos=(-0.723709938184135, -0.38627230814685576, 0.002372729955),
            rot=(0.708669315269169, 0.0, 0.0, 0.7055407866281914),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.4800886614591908, 1.5134604904960336, 0.24480330607770978),
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
            pos=(0.4254139785774999, 9.314999511718668, 0.0023727299549999997),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.6595133360503449, 0.6535046106356766, 0.24480330607770978),
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
            pos=(3.5853872089774814, 7.805293700379685, 0.002372729955),
            rot=(0.709429026564279, 0.0, 0.0, -0.704776884033564),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.0999283397151967, 2.0297175345123066, 0.24480330607770978),
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
            pos=(-2.3353335857391357, 4.092178821563721, 0.4602762758731842),
            rot=(0.7061682343482971, -2.3283064365386963e-10, -8.440110832452774e-10, 0.708044171333313),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/dngvvi/usd/dngvvi.usd"),
            visual_material_path="materials",
            scale=(1.1236640974626249, 1.0878896812507475, 1.2446790448194136),
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
            pos=(-2.670013666152954, 2.9193928241729736, 1.1510995626449585),
            rot=(0.7071069478988647, -2.9103830456733704e-11, -4.366285111245816e-12, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.06973285116014, 3.4302073318614217, 4.527199682615753),
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
            pos=(0.7105916142463684, 6.414919376373291, 1.1510995626449585),
            rot=(1.9470462575554848e-07, 0.0, 2.0605739337042905e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.594222289568975, 4.289190803946919, 4.527199682615753),
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
            pos=(1.7745543718338013, 2.3250746726989746, 1.1510995626449585),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.32963652457188, 3.716535155889921, 4.527199682615753),
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
            pos=(0.6894515156745911, 2.3250746726989746, 1.1510995626449585),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.017134476190838, 3.716535155889921, 4.527199682615753),
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
            pos=(2.280008554458618, 3.6394639015197754, 1.1510995626449585),
            rot=(0.7071069478988647, 0.0, -4.440892098500626e-12, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.594222289568975, 2.2877593139877095, 4.527199682615753),
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
            pos=(2.2801008224487305, 2.740598440170288, 1.1510995626449585),
            rot=(-0.7047299146652222, -1.4551915228366852e-11, 1.148414696672262e-11, 0.7094758152961731),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.0666446497253697, 2.2877593139877095, 4.527199682615753),
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
            pos=(2.2801008224487305, 5.190445899963379, 1.1510995626449585),
            rot=(-0.7047299146652222, -1.4551915228366852e-11, 1.0517808846088883e-11, 0.7094758152961731),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(2.9598540096361803, 2.2877593139877095, 4.527199682615753),
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
            pos=(0.03497256338596344, 9.311993598937988, 1.1510995626449585),
            rot=(0.7055813670158386, 2.9103830456733704e-11, 1.4580336937797256e-11, 0.7086290121078491),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.203088327092411, 4.289190803946919, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.714491069316864, 3.550058126449585, 1.1510995626449585),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.752548711193743, 2.860414962044708, 4.527199682615753),
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
            pos=(3.944476842880249, 2.3546133041381836, 0.9860121011734009),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.8572002767299063, 3.684699420422759, 2.8287788690487865),
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
            pos=(-1.5204061269760132, 1.5809431076049805, 0.9860121011734009),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.4809676034311376, 1.9836253530914385, 2.8287788690487865),
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
            pos=(-1.7349188750699398, 6.493134798348753, 1.200281898479443),
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
            pos=(-2.214635305734934, 1.6031354087037535, 1.200281898479443),
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

    electricSwitchWseglt10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1969183022451255, 6.216551705815821, 1.200281898479443),
            rot=(0.7071067811865477, 0.0, 0.0, -0.7071067811865474),
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
            pos=(2.38461504222918, 5.516872037595126, 1.200281898479443),
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

    electricSwitchWseglt12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3231842367635083, 5.409880424067259, 1.200281898479443),
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

    electricSwitchWseglt13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2885349823500605, 2.393133455573753, 1.200281898479443),
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

    electricSwitchWseglt14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3231861899448745, 5.74944829418918, 1.200281898479443),
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

    electricSwitchWseglt15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1131842291898744, 8.81652104808918, 1.200281898479443),
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

    electricSwitchWseglt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.2431861746848744, 2.0943079133291795, 1.200281898479443),
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
            pos=(1.3131861898935082, 2.0955869670372578, 1.200281898479443),
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

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.0791286088965886, 2.3931354086311103, 1.200281898479443),
            rot=(-3.1391647342098555e-07, 0.0, 0.0, 0.9999999999999507),
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
            pos=(2.4930198273891797, 3.106871915525126, 1.200281898479443),
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
            pos=(2.45368451848506, 3.2131334555737534, 1.200281898479443),
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

    electricSwitchWseglt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.011512988392254479, 2.3931393149053224, 1.200281898479443),
            rot=(-1.9470718387020827e-07, 0.0, 0.0, 0.9999999999999812),
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
            pos=(-1.7042071013208206, 6.336873990725126, 1.200281898479443),
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

    electricSwitchWseglt9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.24318517580865276, 3.717339163655202, 1.200281898479443),
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

    fridgeXyejdx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeXyejdx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.1851631999015808, 3.9132142066955566, 0.827250599861145),
            rot=(-0.705405056476593, 2.6193447411060333e-10, -5.820766091346741e-11, 0.7088045477867126),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/xyejdx/usd/xyejdx.usd"),
            visual_material_path="materials",
            scale=(1.2286648258768629, 1.0649475140459068, 1.0076950931765267),
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
            pos=(3.8350537109356515, 5.655453613279763, 1.7499998883490133),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.9715587235575123, 2.2000595480360157, 0.8636750573443404),
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
            pos=(3.6900535888657267, 3.2305634765600004, 1.6499997746129584),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.1984541684957635, 1.7582065844137194, 1.5545101396722316),
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
            pos=(-1.3099466705460354, 2.42671793346327, 1.7752653806623204),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/cltbty/usd/cltbty.usd"),
            visual_material_path="materials",
            scale=(1.367606151283157, 1.1028412941285772, 1.4026217972733064),
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
            pos=(4.54505339405094, 10.176722320072352, 1.6749255398491152),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/etixod/usd/etixod.usd"),
            visual_material_path="materials",
            scale=(0.7432230038479851, 1.22816416846137, 0.8520839234704635),
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
            pos=(1.3218346600911366, -1.2300404308069282, 1.6001635715016966),
            rot=(0.7070342684146042, 0.0, 0.0, 0.707179286523174),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fanvpf/usd/fanvpf.usd"),
            visual_material_path="materials",
            scale=(0.9310337217126514, 1.1028412941285772, 0.8633863620136316),
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
            pos=(-2.3299468336350873, 8.618242386569612, 1.700163398423771),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fhkzlm/usd/fhkzlm.usd"),
            visual_material_path="materials",
            scale=(0.5819507569859346, 1.1028412941285772, 0.3842008639082407),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureGwricv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureGwricv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.24994625072678697, 6.49434026062429, 1.4503674329935936),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/gwricv/usd/gwricv.usd"),
            visual_material_path="materials",
            scale=(1.1639015139718691, 1.1028412941285772, 1.9423722199807545),
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
            pos=(5.068629808911333, -0.20499468199121038, 1.7752652819955825),
            rot=(0.7084296883441372, 0.0, 0.0, -0.7057813943939218),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hhxttu/usd/hhxttu.usd"),
            visual_material_path="materials",
            scale=(0.7710738168232578, 1.1028412941285772, 1.4027757950693969),
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
            pos=(5.066338864778035, 0.5849957498888142, 1.7752656900099437),
            rot=(0.7084296883441372, 0.0, 0.0, -0.7057813943939218),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jpfyrq/usd/jpfyrq.usd"),
            visual_material_path="materials",
            scale=(0.7710738168232578, 1.1028412941285772, 1.2701513071183972),
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
            pos=(5.066319948517488, -0.9750041932321211, 1.7752655716646941),
            rot=(0.7084296883441372, 0.0, 0.0, -0.7057813943939218),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/lucjyq/usd/lucjyq.usd"),
            visual_material_path="materials",
            scale=(0.7710738168232578, 1.1028412941285772, 0.9363253191726996),
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
            pos=(-0.3449468429626835, 1.5182916481403335, 1.6502041706177657),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qavxsz/usd/qavxsz.usd"),
            visual_material_path="materials",
            scale=(0.7420564776500679, 1.1028412941285772, 1.1518452987337917),
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
            pos=(1.3203303937730673, 0.10992580603189904, 1.6251836520724243),
            rot=(0.70617812786105, 0.0, 0.0, 0.7080342164971001),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qjkajj/usd/qjkajj.usd"),
            visual_material_path="materials",
            scale=(1.2220820080929884, 1.1028412941285772, 0.9711861099903772),
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
            pos=(4.285053325688391, -1.8172867489938171, 1.7001633999170787),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qtvjzk/usd/qtvjzk.usd"),
            visual_material_path="materials",
            scale=(1.0329589482556654, 1.1028412941285772, 0.92208183810604),
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
            pos=(1.1967347367601655, 0.7524930924354442, 1.7001633781806251),
            rot=(0.7090318869027639, 0.0, 0.0, -0.7051764200220441),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/rciuob/usd/rciuob.usd"),
            visual_material_path="materials",
            scale=(0.8511266771553244, 1.1028412941285772, 0.7684017278164814),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureSzpupz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureSzpupz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3218221652317437, 1.4099594000623852, 1.600163287689289),
            rot=(0.7070342684146042, 0.0, 0.0, 0.707179286523174),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/szpupz/usd/szpupz.usd"),
            visual_material_path="materials",
            scale=(0.9310337217126514, 1.1028412941285772, 1.0245350825715738),
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
            pos=(1.19834222172642, -0.009997493922749633, 1.5751838516833736),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/tlwjpv/usd/tlwjpv.usd"),
            visual_material_path="materials",
            scale=(0.7420564776500679, 1.1028412941285772, 1.0371208577034945),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureWeqggl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureWeqggl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9249468380733468, 6.328299333779766, 1.7251837760686988),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/weqggl/usd/weqggl.usd"),
            visual_material_path="materials",
            scale=(0.6256954894078288, 1.1028412941285772, 1.152375931236345),
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
            pos=(3.3500532962007243, -1.8172822260591048, 1.695077700980354),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/wfdvzv/usd/wfdvzv.usd"),
            visual_material_path="materials",
            scale=(0.7274749001761031, 1.1028412941285772, 0.4106639237278676),
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
            pos=(5.067337612977139, 7.940001829784848, 1.8003268015379905),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yrgaal/usd/yrgaal.usd"),
            visual_material_path="materials",
            scale=(1.2220820080929884, 1.1028412941285772, 1.7262754749972833),
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
            pos=(-2.6506866006250194, -0.36249765305431125, 1.5751838461168353),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ytxhyl/usd/ytxhyl.usd"),
            visual_material_path="materials",
            scale=(0.9384703262243734, 1.1028412941285772, 0.43216516522674225),
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
            pos=(1.1962845594344502, -0.662485852225034, 1.6551674937338594),
            rot=(-0.7046975239415604, 0.0, 0.0, 0.7095078574269872),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/zsirgc/usd/zsirgc.usd"),
            visual_material_path="materials",
            scale=(0.8802898321032541, 1.1028412941285772, 0.945033780715212),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    rangeHoodIqbpie0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/rangeHoodIqbpie0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.15248733758926392, 5.917500019073486, 1.870776891708374),
            rot=(0.70710688829422, 0.0, -1.3751559890806675e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/range_hood/iqbpie/usd/iqbpie.usd"),
            visual_material_path="materials",
            scale=(1.121163838271375, 1.2280515619143206, 1.2774783578647764),
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
            pos=(-0.16995468916905127, 4.89994335437812, 0.43655594484039595),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.055440796149384, 2.2801315972588023, 2.036814882126215),
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
            pos=(0.08502709891058298, 5.153485150313767, 1.4569883978948837),
            rot=(0.7079834981732588, 0.0, 0.0, -0.7062289758388247),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(0.8964305137915224, 1.0666172532932467, 0.854680912407126),
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
            pos=(-2.300386905670166, 4.8284077644348145, 0.4877564311027527),
            rot=(0.70710688829422, -3.725290298461914e-09, -6.984919309616089e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/czyfhq/usd/czyfhq.usd"),
            visual_material_path="materials",
            scale=(6.159409157298392, 4.454470634666159, 4.931451850023588),
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
            pos=(3.8246729373931885, 3.3938941955566406, 0.48867157101631165),
            rot=(1.955777406692505e-07, 0.0, -1.1641532182693481e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/xiybkb/usd/xiybkb.usd"),
            visual_material_path="materials",
            scale=(3.0404037688899113, 3.590459005964615, 4.931910227494589),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    stoveRgpphy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/stoveRgpphy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.23843911290168762, 5.909679889678955, 0.5361154079437256),
            rot=(0.7071069478988647, 0.0, 2.7939677238464355e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stove/rgpphy/usd/rgpphy.usd"),
            visual_material_path="materials",
            scale=(1.0942524762940726, 1.5090151323610295, 1.270013669138372),
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
            pos=(3.685638904571533, 5.098461627960205, 0.330701619386673),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.1184611297481328, 1.0295598218379967, 1.2377172845579312),
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
            pos=(-2.512604236602783, 3.938934803009033, 1.8908520936965942),
            rot=(0.7071070075035095, 0.0, 2.017259248532355e-09, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.830029644952414, 1.2771028633750952, 1.5512484619195397),
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
            pos=(-2.4792513847351074, 5.838789463043213, 1.8908520936965942),
            rot=(0.70710688829422, 1.862645149230957e-09, -4.37012204201892e-10, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.0793802977706313, 1.3212474490430903, 1.5512484619195397),
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
            pos=(2.709549903869629, 4.545708656311035, 1.6241765022277832),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(1.343913343541297, 1.245825309086579, 1.5949600923449048),
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
            pos=(0.6850543390021323, 10.157961268187501, 1.8850734172566177),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(2.086424499375996, 1.0325864343157334, 1.0902741140345242),
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
            pos=(2.7484560012817383, 10.269660949707031, 1.4917824268341064),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.6169290822551112, 1.5526300183875148, 1.39012511162989),
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
            pos=(-1.2226735353469849, 8.703526496887207, 1.4917824268341064),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.0801836925608166, 1.4324264040607395, 1.39012511162989),
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
            pos=(-2.672874689102173, 0.858439028263092, 1.3946723937988281),
            rot=(0.7049476504325867, 9.313225746154785e-10, -3.303171070001554e-10, 0.709259569644928),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0288790708992528, 1.4391278593149817, 1.4571120994664377),
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
            pos=(-2.673232316970825, 4.778812885284424, 1.7359281778335571),
            rot=(0.7071068286895752, -1.862645149230957e-09, -5.591118679149076e-10, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0725761555752311, 1.4391278593149817, 0.8094339572766369),
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
            pos=(-2.6731643676757812, 7.464601039886475, 1.4932150840759277),
            rot=(0.7068098187446594, 7.450580596923828e-09, -1.529406290501356e-08, 0.707403838634491),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.409293405206985, 1.4391278593149817, 1.3491657424348042),
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
            pos=(0.44675517082214355, -1.9143784046173096, 1.3946723937988281),
            rot=(1.9471190171316266e-07, 0.0, -5.5933924159035087e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.9580039399239144, 1.9188371457533089, 1.4571120994664377),
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
            pos=(2.3539702892303467, -1.9143784046173096, 1.3946725130081177),
            rot=(1.9470462575554848e-07, 0.0, 4.547473508864641e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.6462564529641481, 1.9188371457533089, 1.4571120994664377),
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
            pos=(5.148268222808838, 1.7308183908462524, 1.3946725130081177),
            rot=(0.7089458703994751, -9.313225746154785e-10, 1.268745108973235e-10, -0.7052630186080933),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.160095173740548, 1.5590551809245634, 1.4571120994664377),
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
            pos=(5.148928642272949, 9.541916847229004, 1.4932150840759277),
            rot=(-0.7049543857574463, 0.0, 7.624976205988787e-10, 0.7092527151107788),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.910397547020671, 1.5590551809245634, 1.3491657424348042),
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
            pos=(5.1486124992370605, 6.369767189025879, 1.4932150840759277),
            rot=(0.7071069478988647, 9.313225746154785e-10, 1.7818706510297488e-09, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0476063929032433, 1.5590551809245634, 1.3491657424348042),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
