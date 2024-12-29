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
class pomaria0GardenquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_0_garden/usd/Pomaria_0_garden_quick.usd"),
        )
    )
@configclass
class pomaria0GardenfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_0_garden/usd/Pomaria_0_garden_quick.usd"),
        )
    )
    armchairTcxiue0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.7954516410827637, 7.393714904785156, 0.5224971771240234),
            rot=(-0.32686516642570496, -0.00011387187987565994, 0.00031243436387740076, 0.9450709819793701),
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
            pos=(0.34672310948371887, 7.492685794830322, 0.5830700397491455),
            rot=(0.7074350714683533, -1.862645149230957e-09, -3.4924596548080444e-10, -0.7067784070968628),
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
            pos=(-3.2161521911621094, 6.0775146484375, 0.55778568983078),
            rot=(-0.7049733996391296, -1.1771917343139648e-06, -1.6007070371415466e-06, 0.7092339396476746),
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
            pos=(3.174943208694458, 5.6317458152771, 0.26363956928253174),
            rot=(1.1187512427568436e-06, 0.0003392196667846292, -0.0009186585666611791, 0.9999995827674866),
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

    standingTvUdotid0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/standingTvUdotid0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6518234014511108, 8.679012298583984, 0.8714269399642944),
            rot=(0.9644948244094849, 4.71482053399086e-09, 1.109128788812086e-09, 0.26410213112831116),
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

    straightChairVkgbbl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairVkgbbl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.277328014373779, 3.763744592666626, 0.42116451263427734),
            rot=(-0.566818356513977, 7.482245564460754e-06, -3.815954551100731e-05, 0.8238428831100464),
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

    swivelChairLafeot0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairLafeot0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.01668430306017399, 7.559916973114014, 0.3908800780773163),
            rot=(0.6563969254493713, -0.00036791968159377575, -0.0005404707044363022, 0.7544156908988953),
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
            pos=(-7.934074878692627, 4.287168979644775, 0.18866220116615295),
            rot=(1.0000001192092896, 1.8189894035458565e-12, -1.5422330079672975e-11, -2.3837367280066246e-07),
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
            pos=(-4.288830353238399, 8.232433551553704, 0.27468097042954287),
            rot=(0.9999999999999716, 0.0, 0.0, -2.3841857910156083e-07),
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
            pos=(-6.870285589540956, 7.611540360571855, 0.3181415084618674),
            rot=(-0.7040612781221107, 0.0, 0.0, 0.7101392234266882),
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
            pos=(-2.669093608856201, 7.768373012542725, 0.34787246584892273),
            rot=(0.7076966762542725, -1.862645149230957e-09, 9.822542779147625e-10, 0.7065165042877197),
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
            pos=(-0.18102586269378662, 5.40480375289917, 0.4476684629917145),
            rot=(1.6344711184501648e-07, 0.0, -3.0995579436421394e-09, 1.0),
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
            pos=(-1.0209680795669556, 5.40480375289917, 0.4476684331893921),
            rot=(1.62515789270401e-07, 0.0, -2.9176590032875538e-09, 1.0000001192092896),
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

    bushCwsigt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushCwsigt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7859925301937803, -7.713679555087657, 0.48694191235257),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.4224843830021843, 0.42248508632624243, 0.4224825231728788),
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
            pos=(-0.7702977814792861, -6.23801243777877, 0.4869419123525699),
            rot=(0.8660253998985326, 0.0, 0.0, 0.5000000067305868),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.4224843830021843, 0.42248508632624243, 0.4224825231728788),
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
            pos=(-0.7859925301937802, -3.8522154437626566, 0.48694191235257),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.4224843830021843, 0.42248508632624243, 0.4224825231728788),
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
            pos=(-0.8010702832364417, -3.1295912473249325, 0.48694191235257),
            rot=(0.9659258182961655, 0.0, 0.0, 0.2588190749324381),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.4224843830021843, 0.42248508632624243, 0.4224825231728788),
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
            pos=(-3.0799607744609814, -2.8085699714890735, 0.48694191235257),
            rot=(0.9990482219507036, 0.0, 0.0, -0.04361937891737566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/cwsigt/usd/cwsigt.usd"),
            visual_material_path="materials",
            scale=(0.4224843830021843, 0.42248508632624243, 0.4224825231728788),
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
            pos=(-3.399004099680411, -0.25727136476782186, 0.4707422014938542),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
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
            pos=(-4.5812001542618095, -0.261578509366123, 0.4707422014938542),
            rot=(0.7933532745138058, 0.0, 0.0, -0.608761514731526),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
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
            pos=(-5.7820016253994275, -0.3002928382429954, 0.4707422014938542),
            rot=(0.9238795603683573, 0.0, 0.0, -0.38268336511216533),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
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
            pos=(-7.719310618240412, -0.6445877710178218, 0.4707422014938542),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
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
            pos=(-7.644033274490411, -1.129054552637822, 0.4707422014938542),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.720794883406228, -1.6231220364897008, 0.4707422014938542),
            rot=(0.6427875280052637, 0.0, 0.0, 0.7660445116576988),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.652399215164133, -3.1875077615735266, 0.4707422014938542),
            rot=(0.8660253740889632, 0.0, 0.0, 0.5000000514340688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.644887185896619, -5.519538714489473, 0.4707422014938542),
            rot=(0.9063077442763514, 0.0, 0.0, -0.4226183534404435),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.59885060572677, -6.7133836777674825, 0.4707422014938542),
            rot=(-0.46174858677709474, 0.0, 0.0, 0.8870108469513526),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushEbuvur9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushEbuvur9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.603410986771987, -7.270641642191039, 0.4707422014938542),
            rot=(0.8660253740889632, 0.0, 0.0, 0.5000000514340688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ebuvur/usd/ebuvur.usd"),
            visual_material_path="materials",
            scale=(0.5738351532232469, 0.5737786128570597, 0.5737712079650281),
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
            pos=(-2.3298389715325687, -5.03457041317007, 1.2916543433959295),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/frqici/usd/frqici.usd"),
            visual_material_path="materials",
            scale=(0.36386991220024695, 0.3638692474182108, 0.36387078555201),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushHnzfgt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushHnzfgt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7336981860163787, -7.060564239439605, 0.22186465930682858),
            rot=(8.781764223087535e-07, 0.0, 0.0, 0.9999999999996144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/hnzfgt/usd/hnzfgt.usd"),
            visual_material_path="materials",
            scale=(0.3267064635080271, 0.32672705437321414, 0.32670546798910527),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushHnzfgt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushHnzfgt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7336981860163787, -5.418163848814604, 0.22186465930682864),
            rot=(8.781764223087535e-07, 0.0, 0.0, 0.9999999999996144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/hnzfgt/usd/hnzfgt.usd"),
            visual_material_path="materials",
            scale=(0.3267064635080271, 0.32672705437321414, 0.32670546798910527),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushHnzfgt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushHnzfgt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7700760976052285, -4.581787737412687, 0.22186471271682867),
            rot=(0.04361945812038009, 0.0, 0.0, 0.9990482184926235),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/hnzfgt/usd/hnzfgt.usd"),
            visual_material_path="materials",
            scale=(0.3267064635080271, 0.32672705437321414, 0.32670546798910527),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushHnzfgt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushHnzfgt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3853467686148375, -2.882975042483436, 0.22186471271682862),
            rot=(0.9914448742886123, 0.0, 0.0, 0.13052609412235472),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/hnzfgt/usd/hnzfgt.usd"),
            visual_material_path="materials",
            scale=(0.3267064635080271, 0.32672705437321414, 0.32670546798910527),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushHnzfgt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushHnzfgt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.2725850132121597, -2.88297506537092, 0.22186471271682862),
            rot=(0.9914448742886123, 0.0, 0.0, 0.13052609412235472),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/hnzfgt/usd/hnzfgt.usd"),
            visual_material_path="materials",
            scale=(0.3267064635080271, 0.32672705437321414, 0.32670546798910527),
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
            pos=(-4.032592200148381, -0.14857070561226135, 0.4344658141708778),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
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
            pos=(-2.7759612492221355, -0.14857075847228968, 0.43446581417087776),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
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
            pos=(-6.564789311941147, -0.17600517864387114, 0.41228807980087784),
            rot=(-0.34202015414019793, 0.0, 0.0, 0.9396926168497416),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
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
            pos=(-7.24477743524403, -0.19535009675890386, 0.43446581417087776),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
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
            pos=(-7.781008046915444, -2.0738352899358077, 0.4344658141708779),
            rot=(-0.34202015414019793, 0.0, 0.0, 0.9396926168497416),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
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
            pos=(-7.784058711670798, -3.7000748282014015, 0.43446581417087776),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.786850106668137, -4.924107795233378, 0.4344658141708779),
            rot=(0.7372774422875599, 0.0, 0.0, -0.6755900925072198),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.784058764528662, -6.163948699053896, 0.4344658141708778),
            rot=(-0.49999998092101927, 0.0, 0.0, 0.8660254147996931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushKnspbi8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushKnspbi8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.786850064273521, -7.8027508579293166, 0.4344658141708778),
            rot=(0.7372774422875599, 0.0, 0.0, -0.6755900925072198),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/knspbi/usd/knspbi.usd"),
            visual_material_path="materials",
            scale=(0.6547477262910592, 0.6547394651731294, 0.6547659374022776),
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
            pos=(-5.1722059246022125, -0.19135174402604221, 0.26333747262657087),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.3939591545418051, 0.39396373781333316, 0.3939478875314064),
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
            pos=(-7.706454577845238, -2.7015075089618192, 0.2633374726265709),
            rot=(0.7372773853937731, 0.0, 0.0, 0.6755901545959072),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.3939591545418051, 0.39396373781333316, 0.3939478875314064),
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
            pos=(-7.753403796595239, -4.307787660326819, 0.26333747262657087),
            rot=(0.7372773853937731, 0.0, 0.0, 0.6755901545959072),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/kyghri/usd/kyghri.usd"),
            visual_material_path="materials",
            scale=(0.3939591545418051, 0.39396373781333316, 0.3939478875314064),
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
            pos=(-1.8920144440935265, 1.1910357726955125, 0.4314935199132135),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(0.6445817212937108, 0.644536728728282, 0.6445283766941753),
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
            pos=(-1.904563840750588, 0.3472480974327627, 0.4314935199132135),
            rot=(0.8433914979594475, 0.0, 0.0, -0.5372995264931092),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/lfyqkj/usd/lfyqkj.usd"),
            visual_material_path="materials",
            scale=(0.6445817212937108, 0.644536728728282, 0.6445283766941753),
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
            pos=(1.8640695080717011, 2.0681779573409957, 0.7763235117393469),
            rot=(0.6899669835574462, 0.7238408399645869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.3063841700721517, 0.3063763923268903, 0.30637996874322676),
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
            pos=(-1.9858211045714282, 2.056963667011764, 0.7763234371215394),
            rot=(0.58191227861118, 0.6104811424544704, 0.3889193829413277, 0.3707190152683916),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/pjhpwk/usd/pjhpwk.usd"),
            visual_material_path="materials",
            scale=(0.3063841700721517, 0.3063763923268903, 0.30637996874322676),
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
            pos=(-1.786370605465, 8.357517089845, 0.0023729740949999995),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
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
            pos=(-7.021195312502497, 6.371994384764632, 0.0023729740950000004),
            rot=(0.9999999112960265, 0.0, 0.0, 0.0004211982183381278),
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
            pos=(-7.251796630860001, 3.153099609375, 0.002372974095),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-0.6167932009636277, 5.433181852684895, 0.86036413574),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-1.5368719100952148, 4.4944047927856445, 1.2662105560302734),
            rot=(0.7071067690849304, 2.9103830456733704e-11, 9.841016890277388e-12, 0.7071067690849304),
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
            pos=(-5.271219253540039, 4.732454776763916, 1.2662105560302734),
            rot=(1.6292324289679527e-07, 0.0, 4.440892098500626e-13, 1.0),
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
            pos=(-6.361223220825195, 4.732454299926758, 1.2662105560302734),
            rot=(1.6292324289679527e-07, 0.0, 4.440892098500626e-13, 1.0),
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
            pos=(-5.26235818862915, 3.742565155029297, 1.2662105560302734),
            rot=(1.0, 1.4921397450962104e-13, -1.338318345034395e-12, -2.3841860752327193e-07),
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
            pos=(-6.392362117767334, 3.7425649166107178, 1.2662105560302734),
            rot=(1.0, 1.4921397450962104e-13, -1.338318345034395e-12, -2.3841860752327193e-07),
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
            pos=(-7.725917339324951, 5.547470569610596, 1.1510998010635376),
            rot=(1.6291960491798818e-07, 0.0, 9.947598300641403e-14, 1.0000001192092896),
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
            pos=(-3.985975503921509, 5.592474460601807, 1.1510998010635376),
            rot=(1.6291960491798818e-07, 0.0, -2.8421709430404007e-13, 1.0000001192092896),
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

    electricSwitchWseglt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.825666555273782, 3.785652254427968, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-4.686928977046318, 4.9046067045303365, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-0.9683151141527214, 9.332105257291772, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-1.6069292211863164, 4.025118423280356, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-5.876928977046315, 4.908387954530337, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-6.956932883296316, 5.412427017030336, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-5.886928977046318, 3.5986887357803363, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-5.77665602776013, 3.6074270177213172, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-3.372104055807041, 5.555375032712452, 1.200281898479443),
            rot=(1.1924880699735396e-08, 0.0, 0.0, 1.0),
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
            pos=(-1.4666560277601295, 4.002473892721298, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-2.7966519994401295, 5.308282486471318, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(4.951064401227965, 9.332103304197451, 1.200281898479443),
            rot=(1.1924880699735396e-08, 0.0, 0.0, 1.0),
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

    lowResolutionTreeClcozg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeClcozg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2555732488822104, -12.468781470888668, 3.4140493529448355),
            rot=(-0.42261825552267474, 0.0, 0.0, 0.9063077899361625),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/clcozg/usd/clcozg.usd"),
            visual_material_path="materials",
            scale=(1.0000090892753792, 1.000006716184508, 1.0000028997706294),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeClcozg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeClcozg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.237297815237222, 21.82870122833561, 3.414049352944835),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/clcozg/usd/clcozg.usd"),
            visual_material_path="materials",
            scale=(1.0000090892753792, 1.000006716184508, 1.0000028997706294),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeClcozg2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeClcozg2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.473387885088044, -3.2127056481284137, 3.4140493529448346),
            rot=(3.1391647332140566e-07, 0.0, 0.0, 0.9999999999999507),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/clcozg/usd/clcozg.usd"),
            visual_material_path="materials",
            scale=(1.0000090892753792, 1.000006716184508, 1.0000028997706294),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeClcozg3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeClcozg3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.982968543796727, 28.88993532112661, 3.739901739419834),
            rot=(0.04361921903467527, 0.0, 0.0, 0.999048228931319),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/clcozg/usd/clcozg.usd"),
            visual_material_path="materials",
            scale=(1.0000090892753792, 1.000006716184508, 1.0000028997706294),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeClcozg4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeClcozg4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.388832874477266, 8.591087718635324, 3.739901739419834),
            rot=(-0.5372995688904416, 0.0, 0.0, 0.8433914709493721),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/clcozg/usd/clcozg.usd"),
            visual_material_path="materials",
            scale=(1.0000090892753792, 1.000006716184508, 1.0000028997706294),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeClcozg5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeClcozg5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.0907154007243305, -11.95691658580261, 3.414049352944835),
            rot=(0.6087613733975067, 0.0, 0.0, 0.7933533829632173),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/clcozg/usd/clcozg.usd"),
            visual_material_path="materials",
            scale=(1.0000090892753792, 1.000006716184508, 1.0000028997706294),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.61310646037133, -0.8887282390099152, 3.3788430687794526),
            rot=(0.42261825552267446, 0.0, 0.0, 0.9063077899361626),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.59388413067309, -8.342308695054276, 3.349283742604452),
            rot=(0.34202004887573995, 0.0, 0.0, 0.9396926551628657),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.373141568838216, -9.581157939360851, 3.3997220970994526),
            rot=(0.42261825552267446, 0.0, 0.0, 0.9063077899361626),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.884044811800736, 9.117426485650928, 3.399722097099453),
            rot=(-0.6087613358817694, 0.0, 0.0, 0.7933534117500497),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.692971877785222, 28.37182790110278, 3.536522023854452),
            rot=(-0.6087613358817694, 0.0, 0.0, 0.7933534117500497),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7732224963449069, 27.585339712513342, 3.399722097099453),
            rot=(0.999048219141985, 0.0, 0.0, 0.04361944324757271),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeDjpxqx6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeDjpxqx6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.526411338287318, 24.852175985756837, 3.399722097099453),
            rot=(0.46174858677709474, 0.0, 0.0, 0.8870108469513527),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/djpxqx/usd/djpxqx.usd"),
            visual_material_path="materials",
            scale=(0.8115622396339975, 0.8115530613676584, 0.8115577982551186),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeWcadtc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeWcadtc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.871038315039668, 2.946076666691482, 3.441463827848669),
            rot=(0.2588194235049121, 0.0, 0.0, 0.9659257248963736),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/wcadtc/usd/wcadtc.usd"),
            visual_material_path="materials",
            scale=(0.6102868871853669, 0.610300684408431, 0.6102963922938734),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeWcadtc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeWcadtc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.488494195407401, -12.329258041035203, 3.7343070895686687),
            rot=(-0.6087614021843396, 0.0, 0.0, 0.793353360874306),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/wcadtc/usd/wcadtc.usd"),
            visual_material_path="materials",
            scale=(0.6102868871853669, 0.610300684408431, 0.6102963922938734),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeWcadtc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeWcadtc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.051550905229275, -12.386692705176849, 3.7343070895686683),
            rot=(-0.46174889449612977, 0.0, 0.0, 0.887010686762906),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/wcadtc/usd/wcadtc.usd"),
            visual_material_path="materials",
            scale=(0.6102868871853669, 0.610300684408431, 0.6102963922938734),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeWcadtc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeWcadtc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.535035379157364, 16.674343995086815, 3.441463827848669),
            rot=(0.17364811027380397, 0.0, 0.0, 0.9848077648954323),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/wcadtc/usd/wcadtc.usd"),
            visual_material_path="materials",
            scale=(0.6102868871853669, 0.610300684408431, 0.6102963922938734),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeWcadtc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeWcadtc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.816519014051144, 29.026311416951422, 3.7343070895686687),
            rot=(0.7660447275646701, 0.0, 0.0, -0.6427872706972115),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/wcadtc/usd/wcadtc.usd"),
            visual_material_path="materials",
            scale=(0.6102868871853669, 0.610300684408431, 0.6102963922938734),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lowResolutionTreeWcadtc5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lowResolutionTreeWcadtc5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.007892532230724, 16.005206328037424, 3.7343070895686696),
            rot=(0.9999999999999962, 0.0, 0.0, 8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/low_resolution_tree/wcadtc/usd/wcadtc.usd"),
            visual_material_path="materials",
            scale=(0.6102868871853669, 0.610300684408431, 0.6102963922938734),
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
            pos=(-7.241796803081008, 5.604236366078178, 2.2001228026437705),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-7.851796805124643, 5.604281050935389, 2.2001228082189392),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-6.769345527142287, 4.252014169367889, 1.0941618753066547),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
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
            pos=(5.273228466577405, 3.9741021939844297, 1.1936310559874135),
            rot=(0.7086903385473923, 0.0, 0.0, -0.7055196694987196),
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
            pos=(2.595853055812443, 9.210839897571761, 1.0941618753066544),
            rot=(0.9999999999999716, 0.0, 0.0, -2.3841857910156083e-07),
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
            pos=(-2.6840728513532546, 6.886585955856126, 0.9946926283552342),
            rot=(0.7058696196683109, 0.0, 0.0, 0.7083417819310917),
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
            pos=(-2.684072852418218, 8.646585528043664, 0.9946926283552344),
            rot=(0.7058696196683109, 0.0, 0.0, 0.7083417819310917),
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
            pos=(1.6510059240231665, 8.665648434011635, 0.36864791353024073),
            rot=(0.9650643545679205, 0.0, 0.0, 0.2620129606382154),
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
            pos=(0.36129528341747313, 8.692262093882457, 0.3589458519746342),
            rot=(-0.7065682271120347, 0.0, 0.0, 0.7076449253939127),
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
            pos=(0.4540788548946768, 6.23806742591947, 0.5335676694329708),
            rot=(0.7097207214281124, 0.0, 0.0, -0.7044831421514355),
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

    shelfVgzdul1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9615273544879434, 6.53997079899667, 1.2335468728870773),
            rot=(0.7068464398076056, 0.0, 0.0, 0.707367026748712),
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
            pos=(5.206193162657196, 7.05530360361916, 0.3854828114223254),
            rot=(0.7072060159565797, 0.0, 0.0, -0.7070075324880365),
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
            pos=(-0.621324197947979, 5.301981596243062, 1.450843003333787),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-8.967365593197563, 6.507693657759108, 1.130750128235951),
            rot=(0.7074249983542708, 0.0, 0.0, 0.7067884207480057),
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
            pos=(-7.084245204925537, 2.3931591510772705, 0.4498513340950012),
            rot=(1.6291960491798818e-07, 2.3283064365386963e-10, -3.0880187296133954e-11, 1.0),
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
            pos=(3.0532362517926117, 4.536575573216514, 0.32944487410709217),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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

    toiletWusctd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletWusctd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.498641014099121, 2.454629421234131, 0.3653491139411926),
            rot=(1.6298145055770874e-07, 0.0, 9.54355527937878e-09, 1.0),
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

    treeDyymaq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeDyymaq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.51283587634626, -3.972433536948336, 3.748855834960658),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.7110538523396942, 0.7110590264318605, 0.7110548345458616),
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
            pos=(4.575306133725397, -4.376684594600513, 3.7488558349606578),
            rot=(0.8191519943362758, 0.0, 0.0, 0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/dyymaq/usd/dyymaq.usd"),
            visual_material_path="materials",
            scale=(0.7110538523396942, 0.7110590264318605, 0.7110548345458616),
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
            pos=(-2.022873328047042, -0.2360834337704122, 1.4656092882176976),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/flkzbo/usd/flkzbo.usd"),
            visual_material_path="materials",
            scale=(0.2735872463647102, 0.2735731758303083, 0.27357563130795426),
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
            pos=(-9.042328643526908, -7.887374772749829, 1.1044155039197496),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.26264630526856364, 0.26266043183127263, 0.2626491977474279),
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
            pos=(7.654330553396426, 24.00889838694791, 1.5312911713134258),
            rot=(-0.6427875979601523, 0.0, 0.0, 0.7660444529585849),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.409628905932553, 24.029706536391114, 1.5149849579334258),
            rot=(0.3826835598862554, 0.0, 0.0, 0.9238794796902803),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.695523390422976, 23.927028446064913, 1.529957125903426),
            rot=(0.7372773853937731, 0.0, 0.0, 0.6755901545959072),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.838612433955343, 23.98108154150926, 1.5282581512934261),
            rot=(0.7071063043492206, 0.0, 0.0, 0.707107258023553),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.583427606581337, -7.753800443219075, 1.550864352463426),
            rot=(0.2588194235049121, 0.0, 0.0, 0.9659257248963736),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.616260630340492, -6.346814841098878, 1.532631869553426),
            rot=(-0.21643978811295536, 0.0, 0.0, 0.9762959685062821),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.6531469839657555, -4.594727959862961, 1.5282579681884259),
            rot=(0.30070631833590694, 0.0, 0.0, 0.953716787161086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.686912141003825, -3.173068768394398, 1.528257968188426),
            rot=(0.9848077317681942, 0.0, 0.0, -0.17364829814767654),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.721530064164605, -1.82206367839904, 1.5282579681884259),
            rot=(-1.192488079931532e-08, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.723115648074304, -0.40775989796518575, 1.5380162079334259),
            rot=(0.04361957970030058, 0.0, 0.0, 0.9990482131843134),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.717789416309976, 0.8966902326269556, 1.542237948658426),
            rot=(0.13052648266526534, 0.0, 0.0, 0.9914448231359295),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(6.364385878819244, 24.01869045994272, 1.5163189423084262),
            rot=(0.9063077671062576, 0.0, 0.0, -0.4226183044815612),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.68505705419258, 2.3631958160586124, 1.528257968188426),
            rot=(0.9961947201080615, 0.0, 0.0, -0.08715549109964865),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.630972514612378, 3.6123234907610913, 1.5282579681884259),
            rot=(-0.34202008235140974, 0.0, 0.0, 0.9396926429787215),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.669370154563315, 4.868477550007006, 1.5557725555884259),
            rot=(-0.2588190044193875, 0.0, 0.0, 0.9659258371900801),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.609350474094323, 6.15734433858291, 1.530141452073426),
            rot=(-0.21643978811295536, 0.0, 0.0, 0.9762959685062821),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.664598155844109, 7.355481024514689, 1.528257968188426),
            rot=(0.30070631833590694, 0.0, 0.0, 0.953716787161086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.635634839527954, 8.56955919598835, 1.528257968188426),
            rot=(0.7660442417738453, 0.0, 0.0, -0.6427878496402483),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.670550399181425, 9.658874680615618, 1.5438809540284257),
            rot=(-0.34202008235140974, 0.0, 0.0, 0.9396926429787215),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.609581902390055, 10.832696725002812, 1.5289085419184258),
            rot=(0.9762961374691818, 0.0, 0.0, -0.21643902596980186),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.605547183273948, 12.003302224984957, 1.5282581512934261),
            rot=(-0.6427875979601523, 0.0, 0.0, 0.7660444529585849),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.496847103150206, 12.224753148303437, 1.5282581512934261),
            rot=(0.9396926621352807, 0.0, 0.0, -0.34202002971918066),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(5.20484781918932, 24.053738104635215, 1.539061129808426),
            rot=(0.8191522408036777, 0.0, 0.0, 0.5735761556988869),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.487525379115954, 11.060923849109166, 1.535551852463426),
            rot=(0.7372772716061827, 0.0, 0.0, -0.6755902787732688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.428754145056311, 9.883363082081097, 1.5400523407484261),
            rot=(-0.34202008235140974, 0.0, 0.0, 0.9396926429787215),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.465533394294036, 8.79013453732635, 1.499922396898426),
            rot=(0.9848077317681942, 0.0, 0.0, -0.17364829814767654),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.434708812426187, 7.579971488306425, 1.5323805267834258),
            rot=(0.30070631833590694, 0.0, 0.0, 0.953716787161086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.4899563670685, 6.381834479452831, 1.500299960373426),
            rot=(-0.21643978811295536, 0.0, 0.0, 0.9762959685062821),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.429934716042956, 5.092961819293461, 1.522003512618426),
            rot=(-0.2588190044193875, 0.0, 0.0, 0.9659258371900801),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.465872803341364, 3.833242527296415, 1.528257968188426),
            rot=(0.17364822588849677, 0.0, 0.0, 0.9848077445094437),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.478172220017624, 2.5960832077992455, 1.528257968188426),
            rot=(-0.34202008235140974, 0.0, 0.0, 0.9396926429787215),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.55037612739404, 1.2163776715930812, 1.5196763641834257),
            rot=(0.13052648266526534, 0.0, 0.0, 0.9914448231359295),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.450456622050151, -0.06616812205610997, 1.5407399017834258),
            rot=(0.04361957970030058, 0.0, 0.0, 0.9990482131843134),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(4.142806615941318, 24.01609377379679, 1.528257968188426),
            rot=(-0.5735765076909113, 0.0, 0.0, 0.8191519943362758),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.504513392870393, -1.2092667728790574, 1.5282579681884259),
            rot=(-1.192488079931532e-08, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.463670830688987, -2.398049899982138, 1.5282579681884259),
            rot=(0.7660442417738453, 0.0, 0.0, -0.6427878496402483),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.434708812426189, -3.8098506552485727, 1.5340597259984259),
            rot=(0.30070631833590694, 0.0, 0.0, 0.953716787161086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.489956367068501, -5.245653801797169, 1.547709567308426),
            rot=(-0.21643978811295536, 0.0, 0.0, 0.9762959685062821),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.428136785506332, -6.547689985939507, 1.516315524338426),
            rot=(0.2588194235049121, 0.0, 0.0, 0.9659257248963736),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.30183593735608, -7.873429592242861, 1.527751986743426),
            rot=(-0.5735763596999339, 0.0, 0.0, 0.819152097960673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.479233787501387, -7.936854233225471, 1.512779635668426),
            rot=(0.8433912130494966, 0.0, 0.0, 0.5372999737119841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.468332029625357, -7.908512936878433, 1.5282579681884259),
            rot=(-0.34202008235140974, 0.0, 0.0, 0.9396926429787215),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(3.0318581652748695, 23.985303858470253, 1.528257968188426),
            rot=(0.8870108220366241, 0.0, 0.0, 0.4617486346378432),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(1.8344504089014388, 24.04048634844158, 1.512553256273426),
            rot=(0.5372992758735288, 0.0, 0.0, 0.8433916576216426),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(0.4642743093107949, 24.021568698391548, 1.5473882782484258),
            rot=(0.5000007238392059, 0.0, 0.0, 0.8660249858752749),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
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
            pos=(-0.7925356732643809, 23.944900036565368, 1.5282579681884259),
            rot=(0.42261779701135616, 0.0, 0.0, 0.9063080037433566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    treeWtyipq9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/treeWtyipq9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.0368340817629216, 23.9522773199588, 1.5282581512934261),
            rot=(0.8191519943362758, 0.0, 0.0, 0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tree/wtyipq/usd/wtyipq.usd"),
            visual_material_path="materials",
            scale=(0.36219249751232796, 0.3622175945983129, 0.3622056882550165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableYtelxk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableYtelxk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.019369125366211, 15.707921981811523, 0.6765556335449219),
            rot=(1.0000001192092896, 3.3269316190853715e-09, -1.0310304787708446e-07, -1.1387510312488303e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/ytelxk/usd/ytelxk.usd"),
            visual_material_path="materials",
            scale=(0.999997377402508, 1.0000000207320507, 0.9999995231630692),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableEjlbho0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableEjlbho0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.138490676879883, 18.901262283325195, 0.34949541091918945),
            rot=(0.999999463558197, -0.000981797929853201, -0.00020894408226013184, -0.00019268604228273034),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/ejlbho/usd/ejlbho.usd"),
            visual_material_path="materials",
            scale=(0.9999935633294538, 0.9999858050594398, 0.9999450250824002),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampChjeoy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampChjeoy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.647038459777832, 20.354387283325195, 0.9660980701446533),
            rot=(0.9860491752624512, 0.0009176400490105152, -0.003794626332819462, -0.1664082258939743),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/chjeoy/usd/chjeoy.usd"),
            visual_material_path="materials",
            scale=(0.9999824738272258, 1.0001862037063143, 1.0000189221247733),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    flowerMylblj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/flowerMylblj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.99473762512207, 15.700148582458496, 1.0883270502090454),
            rot=(0.9134439826011658, -9.313225746154785e-10, -1.862645149230957e-09, -0.406964510679245),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/flower/mylblj/usd/mylblj.usd"),
            visual_material_path="materials",
            scale=(0.9999607440954029, 0.999913942313288, 1.000026828778443),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    grillCgobyh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/grillCgobyh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.402883529663086, 14.894882202148438, 0.538658857345581),
            rot=(0.9999996423721313, -0.00033371231984347105, -0.000877890270203352, 5.550682544708252e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grill/cgobyh/usd/cgobyh.usd"),
            visual_material_path="materials",
            scale=(1.000045073331792, 0.9999936570374536, 1.0000409736808313),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaRdvxkm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaRdvxkm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.71617603302002, 19.47946548461914, 0.4749751091003418),
            rot=(0.9999993443489075, 0.0008265441283583641, 0.0007666274905204773, 2.398155629634857e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/rdvxkm/usd/rdvxkm.usd"),
            visual_material_path="materials",
            scale=(1.0000038068432109, 0.9999857627331225, 1.0000335193515213),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.960047721862793, 14.519254684448242, 0.45946797728538513),
            rot=(0.6360777616500854, -6.370246410369873e-05, 2.5146640837192535e-05, 0.7716249823570251),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.483168601989746, 15.075031280517578, 0.4594597816467285),
            rot=(0.9990482926368713, -3.742985427379608e-05, 6.836903048679233e-05, -0.043619561940431595),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.502808570861816, 15.674799919128418, 0.4594603180885315),
            rot=(1.0, -3.5431236028671265e-05, 6.092467810958624e-05, 1.193024218082428e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.517955780029297, 16.291988372802734, 0.4594602882862091),
            rot=(0.9990482926368713, -4.0568149415776134e-05, 6.465730257332325e-05, 0.04361862689256668),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.063843727111816, 16.85793685913086, 0.45946797728538513),
            rot=(0.8241250514984131, -9.194016456604004e-06, 9.239558130502701e-05, -0.5664079189300537),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.570015907287598, 16.340482711791992, 0.4594603478908539),
            rot=(0.043618783354759216, -6.824731826782227e-05, -3.712344914674759e-05, 0.9990482330322266),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.550375938415527, 15.740707397460938, 0.4594614505767822),
            rot=(6.556510925292969e-07, -5.805492401123047e-05, -3.114156424999237e-05, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairDgqubu7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairDgqubu7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.535222053527832, 15.12351131439209, 0.45946118235588074),
            rot=(-0.04362010955810547, -5.7369470596313477e-05, -3.576651215553284e-05, 0.9990482330322266),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/dgqubu/usd/dgqubu.usd"),
            visual_material_path="materials",
            scale=(1.0000039235644567, 1.0000052205171823, 0.9999863000977712),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    backgroundZqogsh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/backgroundZqogsh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2401405754089363, 7.914317254123574, -0.309636841741523),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/background/zqogsh/usd/zqogsh.usd"),
            visual_material_path="materials",
            scale=(1.0000005436217958, 1.000000109095131, 1.0000416632746845),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushJivsft0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushJivsft0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9771339500505274, -4.871417152110211, 0.43260657046818785),
            rot=(8.781764223087535e-07, 0.0, 0.0, 0.9999999999996144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/jivsft/usd/jivsft.usd"),
            visual_material_path="materials",
            scale=(0.9999671097396253, 0.9999995089414919, 1.0000164629002541),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushJonbyb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushJonbyb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7855981676042039, -7.189032708324533, 0.5125084055694967),
            rot=(0.9961947071702905, 0.0, 0.0, 0.08715563897935256),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/jonbyb/usd/jonbyb.usd"),
            visual_material_path="materials",
            scale=(1.0000348408505693, 1.0000000772972013, 1.0000006731823234),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushJylruu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushJylruu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.8234702909395915, -3.144851497466197, 0.34061136483787235),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/jylruu/usd/jylruu.usd"),
            visual_material_path="materials",
            scale=(0.9999705176885562, 1.0000166574726377, 1.0000161503181875),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushLlcsvc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushLlcsvc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.8691516703546855, -4.0495057423598695, 0.4463418657185454),
            rot=(0.08715670445061788, 0.0, 0.0, 0.9961946139531711),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/llcsvc/usd/llcsvc.usd"),
            visual_material_path="materials",
            scale=(0.9999821461025821, 0.9999723378135836, 1.000010590035505),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushNhorlu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushNhorlu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9481772765353846, -1.4032541788128685, 0.40889644117486385),
            rot=(8.781764223087535e-07, 0.0, 0.0, 0.9999999999996144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/nhorlu/usd/nhorlu.usd"),
            visual_material_path="materials",
            scale=(1.0000288070553185, 0.9999784978818461, 1.0000199956524458),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushRkxgdi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushRkxgdi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.0516021739348758, 0.4482627469522482, 0.4266582048219746),
            rot=(8.781764223087535e-07, 0.0, 0.0, 0.9999999999996144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/rkxgdi/usd/rkxgdi.usd"),
            visual_material_path="materials",
            scale=(0.9999816040990656, 1.0000181578391263, 0.999964891811902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushUjrbvp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushUjrbvp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9297999271698392, -0.4798352266982872, 0.418510756852142),
            rot=(0.4617488944961297, 0.0, 0.0, 0.887010686762906),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/ujrbvp/usd/ujrbvp.usd"),
            visual_material_path="materials",
            scale=(1.0000006151050223, 1.0000369053094893, 0.9999823727383569),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushWaafqw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushWaafqw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9773456315845521, -2.198003740373471, 0.4320394747271391),
            rot=(0.13052688585544897, 0.0, 0.0, 0.9914447700547311),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/waafqw/usd/waafqw.usd"),
            visual_material_path="materials",
            scale=(1.0000068150638912, 0.9999770485570035, 1.000003467737001),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushWaafqw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushWaafqw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.827726043061538, -5.495032764587814, 0.43203944420713924),
            rot=(-0.08715579942815933, 0.0, 0.0, 0.9961946931328426),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/waafqw/usd/waafqw.usd"),
            visual_material_path="materials",
            scale=(1.0000068150638912, 0.9999770485570035, 1.000003467737001),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bushZwhhlc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bushZwhhlc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.875250053663479, -6.419035699032085, 0.4265574877257405),
            rot=(0.6755901869956753, 0.0, 0.0, 0.7372773557048585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bush/zwhhlc/usd/zwhhlc.usd"),
            visual_material_path="materials",
            scale=(1.0000388434649254, 0.9999769235440833, 0.9999542095987851),
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
            pos=(-5.385941432083964, -5.236967645986383, 0.6484541136663834),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/car/supuws/usd/supuws.usd"),
            visual_material_path="materials",
            scale=(0.9999993577900183, 1.000019860433339, 0.9999902140319837),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorMfocvp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorMfocvp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.07021039724349976, 2.8847146034240723, 1.2726844549179077),
            rot=(-0.7071067094802856, 7.275957614183426e-11, -2.0403945200087037e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/mfocvp/usd/mfocvp.usd"),
            visual_material_path="materials",
            scale=(1.0000780327798484, 1.0000168999373316, 1.0000169085774515),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorMfocvp1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorMfocvp1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.864053964614868, 9.497942924499512, 1.2551825046539307),
            rot=(0.7071068286895752, -2.1973391994833946e-09, 9.953282642527483e-11, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/mfocvp/usd/mfocvp.usd"),
            visual_material_path="materials",
            scale=(0.9185499322814911, 1.0000168999373316, 1.0000169085774515),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorOfgpit0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorOfgpit0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.02515983581543, 21.665742874145508, 0.985720157623291),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ofgpit/usd/ofgpit.usd"),
            visual_material_path="materials",
            scale=(1.0000116929874352, 1.0000109598695572, 1.0000105985293717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorPoafwh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorPoafwh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5690796375274658, 9.490585327148438, 1.1969422101974487),
            rot=(0.7071068286895752, 9.458744898438454e-11, -3.0240698833949864e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/poafwh/usd/poafwh.usd"),
            visual_material_path="materials",
            scale=(1.0000649721501271, 1.000025469263781, 1.0000085688342626),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    drivewayAipswu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/drivewayAipswu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6706480045318606, -3.274310606757525, -0.30963682070240983),
            rot=(1.6292068456008897e-07, 0.9999999999999869, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/driveway/aipswu/usd/aipswu.usd"),
            visual_material_path="materials",
            scale=(0.9999956894254739, 1.0000010950220408, 1.0000378131611993),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceCzawic0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceCzawic0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9474198654200903, -8.471825202267159, 1.1381292830361431),
            rot=(1.685874083169919e-07, 0.7071069003958149, 0.7071066619772319, 1.0677012532177061e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/czawic/usd/czawic.usd"),
            visual_material_path="materials",
            scale=(0.9998945704999439, 1.0000133151451693, 0.9999836280015909),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceJayfuh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceJayfuh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.026104466231198, 8.055189003677903, 1.1381293952437512),
            rot=(1.685874083169919e-07, 0.7071069003958149, 0.7071066619772318, 1.0677012532177064e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/jayfuh/usd/jayfuh.usd"),
            visual_material_path="materials",
            scale=(0.999999157631206, 1.0004769098654012, 0.9999825824789705),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceNmmzqh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceNmmzqh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.210032359959936, 8.054218182929528, 1.1381377740084306),
            rot=(1.685874083169919e-07, 0.7071069003958149, 0.7071066619772319, 1.067701253217706e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/nmmzqh/usd/nmmzqh.usd"),
            visual_material_path="materials",
            scale=(1.0000004889309422, 0.999933604834331, 0.9999824779268287),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceNrcmie0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceNrcmie0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.994979170747435, -8.472377345666189, 1.1381317438965843),
            rot=(1.685874083169919e-07, 0.7071069003958149, 0.7071066619772319, 1.0677012532177064e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/nrcmie/usd/nrcmie.usd"),
            visual_material_path="materials",
            scale=(0.9999392665557492, 1.0000044996580182, 0.9999835234492305),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceVjfdnl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceVjfdnl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.644774903069075, -8.472542427337684, 1.1381375347000777),
            rot=(1.685874083169919e-07, 0.7071069003958149, 0.7071066619772318, 1.0677012532177065e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/vjfdnl/usd/vjfdnl.usd"),
            visual_material_path="materials",
            scale=(0.9999327853799634, 1.0000035911341185, 0.9999839416588033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceWcocar0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceWcocar0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.4074146445749616, 24.583634450064974, 1.1381302132005426),
            rot=(1.9949601776664493e-07, 0.70710684079117, 0.7071067215818785, 1.37678756078359e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/wcocar/usd/wcocar.usd"),
            visual_material_path="materials",
            scale=(0.9999815825039748, 0.999999009484618, 0.9999835234492305),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gateFlveay0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gateFlveay0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5671402812004089, -8.470063209533691, 1.1418095827102661),
            rot=(0.7071068286895752, 0.0, 0.0, -0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/gate/flveay/usd/flveay.usd"),
            visual_material_path="materials",
            scale=(1.0000693665063984, 1.0000003400972066, 1.0000215023987125),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    gateRhnrfc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/gateRhnrfc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.46584235236405, -8.469704548001944, 1.1635884826921727),
            rot=(-2.61313236987575e-07, -0.7071067215818612, 0.7071068407911526, 1.9949601775853196e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/gate/rhnrfc/usd/rhnrfc.usd"),
            visual_material_path="materials",
            scale=(0.9999905229512961, 0.9999883081654397, 1.000020977918494),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    greeneryCcisua0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/greeneryCcisua0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.914549772245111, 17.119762422422586, 1.3822596883448761),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/greenery/ccisua/usd/ccisua.usd"),
            visual_material_path="materials",
            scale=(1.0000000223517422, 1.000005825683553, 0.9999935838244002),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lawnGoumgk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lawnGoumgk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.961052451666535, -5.454128480589076, -0.3096379852330011),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/lawn/goumgk/usd/goumgk.usd"),
            visual_material_path="materials",
            scale=(1.0000030237184567, 1.0000043596730246, 1.0000402194786535),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lawnUcjwnm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lawnUcjwnm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5501553764337013, 11.616511505126955, -0.30963603064799605),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/lawn/ucjwnm/usd/ucjwnm.usd"),
            visual_material_path="materials",
            scale=(0.9999967333243737, 0.9999986225749078, 1.0000402194786535),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    lawnUinmme0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/lawnUinmme0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.590114744188744, 1.948030992984771, -0.30963798338357024),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/lawn/uinmme/usd/uinmme.usd"),
            visual_material_path="materials",
            scale=(1.0000014793100458, 1.0000007423384565, 1.0000402194786535),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarNecxcp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarNecxcp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.630286385765697, 13.807097659341052, 1.4586915696741412),
            rot=(-0.7071067215819004, 0.0, 0.0, 0.7071068407911898),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/necxcp/usd/necxcp.usd"),
            visual_material_path="materials",
            scale=(0.9997996791230815, 0.9997535197009126, 1.0000082086814075),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarNecxcp1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarNecxcp1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.625739510765696, 20.587012210126048, 1.4586691087341412),
            rot=(-0.7071067215819004, 0.0, 0.0, 0.7071068407911898),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/necxcp/usd/necxcp.usd"),
            visual_material_path="materials",
            scale=(0.9997996791230815, 0.9997535197009126, 1.0000082086814075),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarNecxcp2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarNecxcp2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.625739510765696, 24.405355960126048, 1.4586691087341412),
            rot=(-0.7071067215819004, 0.0, 0.0, 0.7071068407911898),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/necxcp/usd/necxcp.usd"),
            visual_material_path="materials",
            scale=(0.9997996791230815, 0.9997535197009126, 1.0000082086814075),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarYrbqij0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarYrbqij0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.230462811101095, 13.809479552721513, 1.1502282078489845),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/yrbqij/usd/yrbqij.usd"),
            visual_material_path="materials",
            scale=(1.0000511520227335, 0.9998814407082052, 1.0000121753488975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarYrbqij1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarYrbqij1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.230072186101095, 24.40565582225151, 1.1500065281589846),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/yrbqij/usd/yrbqij.usd"),
            visual_material_path="materials",
            scale=(1.0000511520227335, 0.9998814407082052, 1.0000121753488975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarYrbqij2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarYrbqij2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.230072186101095, 20.587315978501515, 1.1500075047189848),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/yrbqij/usd/yrbqij.usd"),
            visual_material_path="materials",
            scale=(1.0000511520227335, 0.9998814407082052, 1.0000121753488975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    playgroundVojjkc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/playgroundVojjkc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.735372374730809, 19.95113817134877, 1.2399802037485306),
            rot=(5.205485536564991e-07, 0.0, 0.0, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/playground/vojjkc/usd/vojjkc.usd"),
            visual_material_path="materials",
            scale=(0.9999995596228485, 0.9999958539182351, 0.9999850424114143),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swimmingPoolSbvksi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swimmingPoolSbvksi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.369640674890172, 20.952331119168658, 0.16190548086189815),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swimming_pool/sbvksi/usd/sbvksi.usd"),
            visual_material_path="materials",
            scale=(0.9999900996478556, 0.9999907304144635, 1.000046284888198),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roofAcfbve0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roofAcfbve0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9912637287378305, 5.755102269889174, 5.535223141671165),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/roof/acfbve/usd/acfbve.usd"),
            visual_material_path="materials",
            scale=(1.000000692710624, 0.9999972797813114, 1.0000058920003139),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roofHbnfbg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roofHbnfbg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.142976794822754, 18.695211355134845, 2.9259588526493605),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/roof/hbnfbg/usd/hbnfbg.usd"),
            visual_material_path="materials",
            scale=(1.0000029596152173, 1.0000005302358, 1.0000368153142032),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightDdvvuq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightDdvvuq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.020926690514486, 15.710395616048947, 1.9694410068954427),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ddvvuq/usd/ddvvuq.usd"),
            visual_material_path="materials",
            scale=(1.0000601694954923, 1.0000601694954923, 1.0000083842028151),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sandboxDcqptj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sandboxDcqptj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.3424432972224776, 16.63960209882755, 0.13754530641561577),
            rot=(0.9999999999999962, 0.0, 0.0, 8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sandbox/dcqptj/usd/dcqptj.usd"),
            visual_material_path="materials",
            scale=(1.0000093277928797, 0.999990461464285, 1.0001287623966983),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toyBoxQgfbdj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toyBoxQgfbdj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.435535225117336, 16.865854155901165, 0.21868191599818543),
            rot=(0.9998476968953101, 0.0, 0.0, -0.017452306814406775),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toy_box/qgfbdj/usd/qgfbdj.usd"),
            visual_material_path="materials",
            scale=(0.9999773725565978, 0.9999949382157886, 0.9999484467327855),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallClockJerval0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallClockJerval0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.666242309486917, 20.46617337730341, 1.6339375026565823),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_clock/jerval/usd/jerval.usd"),
            visual_material_path="materials",
            scale=(1.0004247805277058, 1.000074197712395, 1.000053953966988),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXezdng0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXezdng0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.409096289175116, 20.417179904524648, 1.3251990466262655),
            rot=(-0.7071067215818991, -1.4614422852813105e-08, -1.461441930009936e-08, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xezdng/usd/xezdng.usd"),
            visual_material_path="materials",
            scale=(1.0001584581544003, 1.0000107738593604, 1.000567882328892),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowAgoayg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowAgoayg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.5969367027282715, 9.414531707763672, 1.7867637872695923),
            rot=(0.70710688829422, -5.238689482212067e-10, 5.602487362921238e-09, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/agoayg/usd/agoayg.usd"),
            visual_material_path="materials",
            scale=(0.9997730856863017, 1.000011546842584, 1.0000048031640285),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowJdxnzi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowJdxnzi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.242993354797363, 8.146360397338867, 1.6850382089614868),
            rot=(-7.587950676679611e-07, -2.9103830456733704e-11, -5.937295100011397e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/jdxnzi/usd/jdxnzi.usd"),
            visual_material_path="materials",
            scale=(0.9997733671110269, 0.9999859220181686, 1.0000015873230566),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUzxlbr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUzxlbr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.5057783126831055, 6.35849142074585, 1.6861679553985596),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/uzxlbr/usd/uzxlbr.usd"),
            visual_material_path="materials",
            scale=(0.9997777292145272, 1.0000228269883449, 1.0000018813594456),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYorgot0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYorgot0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.033881187438965, 23.4528865814209, 1.2108509540557861),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/yorgot/usd/yorgot.usd"),
            visual_material_path="materials",
            scale=(0.9999450318234895, 0.9999868516564177, 1.0000164309500923),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYsgkig0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYsgkig0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.568208288377121, 2.1280398730287025, 1.7573800895963951),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ysgkig/usd/ysgkig.usd"),
            visual_material_path="materials",
            scale=(0.9997760406538181, 0.999950667215703, 0.9999699731046304),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYsgkig1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYsgkig1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.665005650479757, 2.128039873028702, 1.7573800895963951),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ysgkig/usd/ysgkig.usd"),
            visual_material_path="materials",
            scale=(0.9997760406538181, 0.999950667215703, 0.9999699731046304),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
