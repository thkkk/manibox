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
class pomaria0IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_0_int/usd/Pomaria_0_int_quick.usd"),
        )
    )
@configclass
class pomaria0IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_0_int/usd/Pomaria_0_int_quick.usd"),
        )
    )
    armchairTcxiue0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.56204605102539, -1.2313995361328125, 0.5224971771240234),
            rot=(0.9450710415840149, 0.00031242199474945664, 0.00011391635052859783, 0.3268650770187378),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/tcxiue/usd/tcxiue.usd"),
            visual_material_path="materials",
            scale=(1.1926878553665357, 1.287808643952844, 1.0646395568791862),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableIdnnmz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableIdnnmz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.113316535949707, -1.3303687572479248, 0.5830700397491455),
            rot=(0.7067782878875732, -2.7939677238464355e-09, 2.9103830456733704e-11, 0.7074351906776428),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/idnnmz/usd/idnnmz.usd"),
            visual_material_path="materials",
            scale=(1.403170034832211, 1.4413198555761049, 1.6306892566786615),
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
            pos=(-4.550439834594727, 0.0848013237118721, 0.5577864646911621),
            rot=(0.7092333436012268, -3.5017728805541992e-06, 1.0164876584894955e-07, 0.7049740552902222),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.7019619659658484, 0.9020610637675529, 1.4337530461454588),
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
            pos=(-10.941522598266602, 0.5305994153022766, 0.2636391818523407),
            rot=(0.9999995827674866, -0.0009682050440460443, -0.00032118347007781267, -3.65024789061863e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/fqluyq/usd/fqluyq.usd"),
            visual_material_path="materials",
            scale=(1.611457804945484, 1.2840533713000228, 1.1766632345298877),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    guitarCybisc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/guitarCybisc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.559803009033203, -2.7166314125061035, 0.3411424458026886),
            rot=(0.0015456080436706543, -0.0005463548004627228, 0.003512653522193432, 0.9999924898147583),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/guitar/cybisc/usd/cybisc.usd"),
            visual_material_path="materials",
            scale=(1.1427980864461271, 7.528028728122811, 0.9976954524183895),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    guitarCybisc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/guitarCybisc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3301734924316406, -2.6748368740081787, 0.3410450220108032),
            rot=(0.004605598747730255, -0.0007410570979118347, 0.003111776430159807, 0.9999843239784241),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/guitar/cybisc/usd/cybisc.usd"),
            visual_material_path="materials",
            scale=(1.5532065509101987, 9.45993211086115, 0.9976954524183895),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    monitorRbqanz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/monitorRbqanz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.347611427307129, -0.9636467695236206, 0.7699717283248901),
            rot=(0.7120685577392578, 7.450580596923828e-09, -5.820766091346741e-09, 0.7021101117134094),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/monitor/rbqanz/usd/rbqanz.usd"),
            visual_material_path="materials",
            scale=(1.8906713259316696, 0.9384100630329865, 1.179454119659372),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    monitorRbqanz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/monitorRbqanz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.657617568969727, 0.10635707527399063, 0.7849206924438477),
            rot=(0.7120687365531921, -9.998679161071777e-06, 4.744681064039469e-06, 0.7021097540855408),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/monitor/rbqanz/usd/rbqanz.usd"),
            visual_material_path="materials",
            scale=(1.8906713259316696, 0.9384100630329865, 1.179454119659372),
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
            pos=(-9.418414115905762, -2.228299617767334, 0.8714269399642944),
            rot=(-0.26410216093063354, -1.1641532182693481e-09, 4.226905048199114e-09, 0.9644948244094849),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/standing_tv/udotid/usd/udotid.usd"),
            visual_material_path="materials",
            scale=(1.4748149437708864, 0.9084401461536219, 1.0886063901177456),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairLafeot0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairLafeot0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.749905109405518, -1.3976010084152222, 0.39088037610054016),
            rot=(0.7544156312942505, -0.000540725770406425, 0.00036818068474531174, -0.6563970446586609),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/lafeot/usd/lafeot.usd"),
            visual_material_path="materials",
            scale=(0.9840625219955115, 0.9751164542281511, 1.0276236556776022),
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
            pos=(-0.02105630561709404, 1.8751466274261475, 0.18866220116615295),
            rot=(1.9470462575554848e-07, 0.0, 2.7284841053187847e-12, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/fdjykf/usd/fdjykf.usd"),
            visual_material_path="materials",
            scale=(1.386870338577056, 0.9955948558850597, 1.11383127029956),
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
            pos=(-3.4777588386642724, -1.809119006873711, 0.27468097042954287),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/mpgavt/usd/mpgavt.usd"),
            visual_material_path="materials",
            scale=(1.1004592824649164, 1.1266939954773696, 1.1847141759413378),
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
            pos=(-0.8963126430634276, -1.4492245756660547, 0.3181415084618674),
            rot=(0.7101391640793051, 0.0, 0.0, 0.7040613379818166),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.144568031065394, 1.0743602019330207, 1.1161643023774404),
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
            pos=(-5.097499370574951, -1.6060580015182495, 0.34787246584892273),
            rot=(-0.7065166234970093, 0.0, -3.026798367500305e-09, 0.7076965570449829),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(1.3855055844872277, 1.3691670931953726, 1.8424103959352263),
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
            pos=(-7.585563659667969, 0.7575123310089111, 0.4476684331893921),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.2762800199517248, 1.232070732504204, 1.4180110671968567),
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
            pos=(-6.745621204376221, 0.7575123310089111, 0.4476684331893921),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.3731614965644587, 1.232070732504204, 1.4180110671968567),
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
            pos=(-5.980220458985001, -2.1952001953100004, 0.0023729740950000004),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.0178007518103354, 0.7687152440232323, 0.24480330607770978),
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
            pos=(-0.7453982610285892, -0.20967827308860906, 0.0023729740949999995),
            rot=(-0.00042136114142229367, 0.0, 0.0, 0.9999999112273904),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.3286593709067227, 0.92078297041844, 0.24480330607770978),
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
            pos=(-0.5147985610949998, 3.009215820315, 0.002372974095),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.1480870848139684, 1.0506848926272276, 0.24480330607770978),
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
            pos=(-7.14980029297, 0.729136413575, 0.86036413574),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.6202036839376872, 1.1044904947247125, 0.5826772151252665),
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
            pos=(-6.22971773147583, 1.6679108142852783, 1.2662103176116943),
            rot=(0.70710688829422, 2.9103830456733704e-11, -8.377298854611581e-12, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.096297687003222, 4.0028629799184205, 4.9799425513765065),
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
            pos=(-2.495373249053955, 1.4298628568649292, 1.2662104368209839),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.8582767578492083, 3.4302073318614217, 4.9799425513765065),
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
            pos=(-1.405373454093933, 1.4298628568649292, 1.2662104368209839),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.8582767578492083, 3.4302073318614217, 4.9799425513765065),
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
            pos=(-2.5042335987091064, 2.4197516441345215, 1.2662105560302734),
            rot=(1.9470462575554848e-07, 0.0, -3.6770586575585185e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.752548711193743, 2.2877593139877095, 4.9799425513765065),
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
            pos=(-1.3742332458496094, 2.4197516441345215, 1.2662105560302734),
            rot=(1.9470462575554848e-07, 0.0, -3.6770586575585185e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.752548711193743, 2.2877593139877095, 4.9799425513765065),
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
            pos=(-0.0406821183860302, 0.6148461699485779, 1.1510998010635376),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(5.919708019272361, 2.5740871380162087, 4.527199682615753),
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
            pos=(-3.780618667602539, 0.5698405504226685, 1.1510998010635376),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(5.4967958326504975, 2.2877593139877095, 4.527199682615753),
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
            pos=(-11.359125137329102, -3.003919839859009, 1.08461332321167),
            rot=(1.9470718370939721e-07, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.1606922003899216, 4.817787739848537, 3.111699687792625),
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
            pos=(-5.99932861328125, -3.003919839859009, 0.98601233959198),
            rot=(1.9470718370939721e-07, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.505173973294201, 4.817787739848537, 2.8287788690487865),
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
            pos=(-1.9409280485908207, 2.3766631752951257, 1.200281898479443),
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
            pos=(-3.079660742607681, 1.2577094572341732, 1.200281898479443),
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

    electricSwitchWseglt10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.704834908940821, -2.8830604575198744, 1.200281898479443),
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

    electricSwitchWseglt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.1596628178026815, 2.1371984709041727, 1.200281898479443),
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

    electricSwitchWseglt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8896597660476813, 1.2539293058641732, 1.200281898479443),
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
            pos=(-0.8096602543276811, 0.7498908537141732, 1.200281898479443),
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

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8796606205376811, 2.5636286466841733, 1.200281898479443),
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
            pos=(-1.9899347904576812, 2.5548896330141733, 1.200281898479443),
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

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.394486763186599, 0.6069412514344548, 1.200281898479443),
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

    electricSwitchWseglt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.299938696712681, 2.159844466999173, 1.200281898479443),
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

    electricSwitchWseglt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.969938696712681, 0.8540348966841731, 1.200281898479443),
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
            pos=(-12.33620941943658, -2.8830609458305454, 1.200281898479443),
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

    pictureCltbty0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureCltbty0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5247954811739289, 0.5580806505217425, 2.2001228026437705),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/cltbty/usd/cltbty.usd"),
            visual_material_path="materials",
            scale=(0.7128933227021382, 1.1028412941285772, 0.6473134572515992),
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
            pos=(0.08520452088426467, 0.5580359656646124, 2.2001228082189392),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ytxhyl/usd/ytxhyl.usd"),
            visual_material_path="materials",
            scale=(0.7128933227021382, 1.1028412941285772, 0.2880776799271463),
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
            pos=(-0.9972537782834967, 1.9103027608375478, 1.0941618753066544),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.2362880144341448, 1.3595175053602375, 1.9232438648124432),
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
            pos=(-12.701035145107884, 2.1726632008043962, 1.1936310559874135),
            rot=(0.7055196396966977, 0.0, 0.0, 0.7086903682160791),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(2.457807701456045, 1.6571186271034446, 2.0980842161590285),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.279522976539957, -2.7117799610517537, 1.0941618753066544),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(0.6643509710144754, 1.8092258671055281, 1.9232438648124432),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.082518933305435, -0.7242708232115012, 0.9946926283552342),
            rot=(0.7083419009316202, 0.0, 0.0, -0.7058695002509875),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.702385378066059, 1.589567896295066, 1.7484035134658573),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.082518444972081, -2.4842708079513143, 0.9946926283552342),
            rot=(0.7083419009316202, 0.0, 0.0, -0.7058695002509875),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.702385378066059, 1.589567896295066, 1.7484035134658573),
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
            pos=(-9.417597110879742, -2.2149346866081507, 0.36864791353024073),
            rot=(-0.26201308673528806, 0.0, 0.0, 0.9650643203328193),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.548533588179003, 1.3577469167671181, 1.7199159078905804),
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
            pos=(-8.127885427558358, -2.5299482733333076, 0.3589458519746342),
            rot=(0.7076448062754433, 0.0, 0.0, 0.7065683464120017),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.1702522598456728, 2.6100903447517623, 1.6747755623197775),
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
            pos=(-8.220670651180738, -0.07574902465845476, 0.5335676694329707),
            rot=(0.7044831421514357, 0.0, 0.0, 0.7097207214281122),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.3960312488527553, 1.9626712871708785, 2.489593170694265),
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
            pos=(-9.765107385983054, 2.901813969872182, 1.2335468728870773),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(8.671442795115182, 3.2971744401341465, 4.102746437598094),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVgzdul1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.728117964541532, -0.37765594899098687, 1.2335468728870773),
            rot=(0.7073669671660169, 0.0, 0.0, -0.7068464994341779),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(4.400629121940049, 2.733882563510156, 4.102746437598094),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVgzdul2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.639342908917158, -0.6163351388018021, 0.3854828114223253),
            rot=(0.7070074132620073, 0.0, 0.0, 0.7072061351491269),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(7.297167016576133, 3.4534805629669822, 1.282021368610689),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVgzdul3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.145267843067021, 0.86033731393214, 1.4508430033337867),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(2.6730850729915576, 2.520559112851507, 1.9314606873714513),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVgzdul4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8207031835852275, -0.3453752187701503, 1.130750128235951),
            rot=(-0.7067885400109205, 0.0, 0.0, 0.7074248791986548),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(2.933861882427258, 4.21043474272348, 3.7607350436132996),
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
            pos=(-0.9491816163063049, 3.6788017749786377, 0.4498513340950012),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(6.441167290173745, 3.4982644128737306, 4.472965008294247),
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
            pos=(-10.81982760519508, 1.6257400513313236, 0.32944487410709217),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/mnfbbh/usd/mnfbbh.usd"),
            visual_material_path="materials",
            scale=(1.3061965963142035, 1.1578982370860895, 1.046816846111422),
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
            pos=(-12.043897974472113, 2.398548464785385, 0.42131020822469584),
            rot=(0.8238426353105573, 0.0, 0.0, 0.5668185884783208),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/vkgbbl/usd/vkgbbl.usd"),
            visual_material_path="materials",
            scale=(1.035526269958783, 1.0253454527952885, 1.0521335369379834),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletWusctd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletWusctd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.46521273255348206, 3.6173322200775146, 0.3653491139411926),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/wusctd/usd/wusctd.usd"),
            visual_material_path="materials",
            scale=(1.2695943718301623, 1.2696527592274995, 1.3080027152501013),
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
            pos=(-12.914621353149414, 0.014601003378629684, 1.5009843111038208),
            rot=(0.7068511843681335, 0.0, 4.916955731459893e-10, 0.7073623538017273),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.4567749492968685, 2.1586917889724724, 1.5542529060975336),
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
            pos=(-3.368805408477783, -2.9698588848114014, 1.5932152271270752),
            rot=(1.9471190171316266e-07, 0.0, 2.4783730623312294e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.9455190585879205, 2.0387644673628906, 1.3491657424348042),
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
            pos=(-1.4925018548965454, 3.9925343990325928, 1.5631152391433716),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.660949617927514, 1.199273216095818, 0.9714080663109586),
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
            pos=(-0.4525018632411957, 3.9925343990325928, 1.5631152391433716),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.660949617927514, 1.199273216095818, 0.9714080663109586),
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
            pos=(1.1182162761688232, -1.7834019660949707, 1.5009843111038208),
            rot=(0.7071069478988647, 0.0, 2.021920408878941e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.5215324884175696, 1.3192005377053997, 1.5542529060975336),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
