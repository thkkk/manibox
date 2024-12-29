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
class officeLargequickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/office_large/usd/office_large_quick.usd"),
        )
    )
@configclass
class officeLargefullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/office_large/usd/office_large_quick.usd"),
        )
    )
    bottomCabinetBamfsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.326410174369812, 8.308073043823242, 0.2652606964111328),
            rot=(-8.791685104370117e-07, -1.7033889889717102e-06, 3.650828148238361e-06, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
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
            pos=(1.2026448249816895, -15.646201133728027, 0.26541388034820557),
            rot=(0.9999574422836304, 0.00034708602470345795, 8.71645170263946e-06, -0.009224955923855305),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21063858270645142, -7.234973430633545, 0.2652603089809418),
            rot=(-5.736947059631348e-07, -2.248212695121765e-06, 4.148008883930743e-06, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.72467565536499, -12.474238395690918, 0.2652594745159149),
            rot=(1.0000001192092896, 3.8103607948869467e-06, 1.343603798886761e-06, 3.02025000564754e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.731008529663086, -12.594537734985352, 0.26526105403900146),
            rot=(-3.2782554626464844e-07, -1.4705583453178406e-06, 7.189970347099006e-06, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.73099422454834, -11.006278038024902, 0.26526159048080444),
            rot=(-5.5847689509391785e-05, -5.827285349369049e-06, -7.508788257837296e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.724674224853516, -10.885994911193848, 0.2652614116668701),
            rot=(1.0000001192092896, 6.524860509671271e-06, 6.719346856698394e-09, 3.2896423363126814e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.721181392669678, -9.284927368164062, 0.26559194922447205),
            rot=(0.9998383522033691, -0.0011288027744740248, -2.3433458409272134e-05, 0.01794891245663166),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.732466697692871, -9.406604766845703, 0.26526039838790894),
            rot=(0.01706460304558277, -3.4458935260772705e-08, -2.38200300373137e-07, 0.9998544454574585),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.735811233520508, -7.799017906188965, 0.26525938510894775),
            rot=(0.045603927224874496, -6.817281246185303e-07, -1.2098171282559633e-06, 0.9989596009254456),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.7131195068359375, -7.677432537078857, 0.2661586403846741),
            rot=(0.9990108013153076, -0.0032143094576895237, -0.00013475981540977955, 0.044354021549224854),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.217477560043335, -2.902317762374878, 0.2652651369571686),
            rot=(0.7071064710617065, 1.1469237506389618e-05, 1.234395313076675e-05, 0.7071072459220886),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
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
            pos=(0.2153564989566803, -15.7597074508667, 0.2657261788845062),
            rot=(-0.02016260102391243, 3.32854688167572e-05, -0.0016414506826549768, 0.9997953772544861),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0971779823303223, -3.895979404449463, 0.2652719020843506),
            rot=(0.7070938348770142, 2.119317650794983e-05, -2.1191517589613795e-05, -0.7071198225021362),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5087758302688599, -3.8959882259368896, 0.2652595639228821),
            rot=(0.7071179151535034, 1.9194558262825012e-06, -1.9649305613711476e-06, -0.707095742225647),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6290268898010254, -2.9024524688720703, 0.26526114344596863),
            rot=(0.7072258591651917, 2.8703361749649048e-06, 4.9466179916635156e-06, 0.7069878578186035),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.08331962674856186, -3.895315408706665, 0.26525798439979553),
            rot=(0.7110896706581116, 4.842877388000488e-08, 7.153721526265144e-08, -0.703101396560669),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.03626903146505356, -2.9032862186431885, 0.2652583122253418),
            rot=(0.7117789387702942, 1.5832483768463135e-08, 4.598405212163925e-09, 0.7024036645889282),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.687861442565918, -3.8904407024383545, 0.26696035265922546),
            rot=(0.7276142239570618, -0.004418076016008854, 0.004175086505711079, -0.6859596967697144),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5677688121795654, -2.9053096771240234, 0.26405858993530273),
            rot=(0.727977454662323, -0.0028505176305770874, -0.0019413249101489782, 0.6855924129486084),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.554970741271973, 3.5152196884155273, 0.26583951711654663),
            rot=(-0.0435725562274456, 8.215382695198059e-05, -0.0020251062233000994, 0.9990482926368713),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.575594425201416, 3.6327767372131348, 0.2652597725391388),
            rot=(0.9992116093635559, 2.450542524456978e-07, -5.668953235726804e-07, -0.03970126435160637),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.574305772781372, 5.2436370849609375, 0.2652580142021179),
            rot=(0.9998326301574707, -1.0937219485640526e-07, -1.5034311218187213e-07, -0.018306227400898933),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21090230345726013, -14.157544136047363, 0.2652595341205597),
            rot=(-0.0010149776935577393, -6.891787052154541e-07, 2.101471181958914e-06, 0.9999995231628418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.562554359436035, 5.123103618621826, 0.26525628566741943),
            rot=(-0.016505444422364235, 9.406358003616333e-08, 3.832847869489342e-05, 0.9998639225959778),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.5726470947265625, 6.8439459800720215, 0.2652622163295746),
            rot=(1.0000001192092896, 6.987189408391714e-06, 1.2052114470861852e-06, -0.000253072299528867),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.566228866577148, 6.723575592041016, 0.2652612328529358),
            rot=(-9.882263839244843e-05, -7.264316082000732e-08, 6.0492311604321e-06, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.572589635848999, 8.432358741760254, 0.2652619183063507),
            rot=(1.0, 7.819733582437038e-06, 7.312155503313988e-07, 5.012952897232026e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.566254138946533, 8.312067031860352, 0.2652639150619507),
            rot=(-7.934868335723877e-07, -3.259629011154175e-08, 1.2223070370964706e-05, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.320076823234558, 8.432361602783203, 0.2652604281902313),
            rot=(1.0000001192092896, 2.4985347408801317e-06, 3.130840923404321e-06, 4.1934981709346175e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3200749158859253, 6.844110012054443, 0.26526105403900146),
            rot=(1.0000001192092896, 6.587099051102996e-06, 1.5723344404250383e-08, 3.170098352711648e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3264102339744568, 6.723814964294434, 0.2652592957019806),
            rot=(-7.245689630508423e-07, -1.8849968910217285e-06, 1.8424761947244406e-06, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3191008567810059, 5.251955986022949, 0.2652583122253418),
            rot=(0.9999849796295166, 4.1385646909475327e-08, 2.6033740141429007e-07, -0.005474461242556572),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3268794119358063, 5.13224983215332, 0.2652578353881836),
            rot=(-0.004939449951052666, -4.284083843231201e-07, -3.92465153709054e-07, 0.9999878406524658),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2040554285049438, -14.037320137023926, 0.265261173248291),
            rot=(0.9999985098838806, -1.3271346688270569e-08, 4.868084943154827e-06, -0.0017899598460644484),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3166874647140503, 3.647451639175415, 0.265156090259552),
            rot=(0.999547004699707, -0.0009207929251715541, 0.0006007762858644128, -0.030079428106546402),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.33272096514701843, 3.5265893936157227, 0.26620933413505554),
            rot=(-0.028672387823462486, 8.98558646440506e-05, -0.003349900711327791, 0.9995833039283752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.076026916503906, 5.89500617980957, 0.2652595639228821),
            rot=(0.6986278295516968, -3.650784492492676e-07, 1.4312536222860217e-06, -0.7154854536056519),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.954448223114014, 6.885532379150391, 0.2653559744358063),
            rot=(0.6993345618247986, -0.00022227410227060318, -0.00021675953757949173, 0.7147944569587708),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.550195693969727, 6.887580871582031, 0.2652604281902313),
            rot=(0.7063239812850952, 1.816079020500183e-07, 3.606328391470015e-06, 0.7078888416290283),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.670454978942871, 5.894545555114746, 0.26526057720184326),
            rot=(0.7061885595321655, 2.9187649488449097e-06, 2.9848888516426086e-06, -0.7080239057540894),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.466280937194824, -2.194871664047241, 0.2698943614959717),
            rot=(1.0, 5.123671144247055e-06, 7.904927770141512e-07, 6.287846190389246e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.46260929107666, -4.8890380859375, 0.2698911130428314),
            rot=(0.99998539686203, 4.3542240746319294e-07, 1.3877797755412757e-07, -0.005410181824117899),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz48 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz48",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.101372718811035, -3.6839828491210938, 0.2652587890625),
            rot=(0.003048280254006386, -1.4472752809524536e-06, 1.2113014236092567e-07, 0.9999953508377075),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz49 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz49",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.100116729736328, -2.2245326042175293, 0.26525846123695374),
            rot=(0.00985717959702015, -3.073364496231079e-08, 5.369656719267368e-09, 0.9999514222145081),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2031371593475342, -10.319452285766602, 0.26532959938049316),
            rot=(0.9996752738952637, 0.00015420443378388882, -4.1262210288550705e-06, -0.02548382245004177),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz50 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz50",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.100116729736328, -0.6877884864807129, 0.26525843143463135),
            rot=(0.009856797754764557, -6.426125764846802e-08, 2.278829924762249e-08, 0.9999515414237976),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz51 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz51",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.537036418914795, 2.338028907775879, 0.26525840163230896),
            rot=(0.835283100605011, 9.313225746154785e-10, -3.5288394428789616e-09, -0.5498200058937073),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21861127018928528, -10.43547534942627, 0.2660275101661682),
            rot=(-0.0326632522046566, 9.010452777147293e-05, -0.0027115363627672195, 0.9994627833366394),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21168260276317596, -8.827430725097656, 0.265259325504303),
            rot=(-0.005539225414395332, -1.2153759598731995e-06, -1.4073302736505866e-06, 0.9999847412109375),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2037558555603027, -8.707472801208496, 0.2652592360973358),
            rot=(0.9999767541885376, 3.605964593589306e-08, 3.6900019040331244e-08, -0.006839990150183439),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2043043375015259, -7.114680767059326, 0.2652597725391388),
            rot=(1.0, 4.7674402594566345e-06, 1.2364434951450676e-06, 6.951995601411909e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.5626442762396122, 0.8967337959921297, 0.9564465783156997),
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
            pos=(5.23659610748291, -14.41171646118164, 0.4866344630718231),
            rot=(-0.00014972873032093048, -3.7993304431438446e-06, -0.002583651803433895, 0.9999966621398926),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/immwzb/usd/immwzb.usd"),
            visual_material_path="materials",
            scale=(1.0776845142144862, 2.206954150303624, 1.8325128949645366),
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
            pos=(5.236603260040283, -15.416367530822754, 0.48634499311447144),
            rot=(-0.0001497473567724228, -3.8065481930971146e-06, -0.002842468675225973, 0.9999959468841553),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/immwzb/usd/immwzb.usd"),
            visual_material_path="materials",
            scale=(1.0776845142144862, 2.206954150303624, 1.8325128949645366),
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
            pos=(-12.910027503967285, -8.61928939819336, 0.4572509825229645),
            rot=(-0.7109615802764893, -0.00209216121584177, -0.001471411669626832, 0.7032265067100525),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(0.878616861371198, 6.1529058220225, 2.432547059157785),
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
            pos=(-18.847225189208984, 0.8079901933670044, 0.4541342854499817),
            rot=(8.009374141693115e-08, -6.51925802230835e-09, -1.3540557119995356e-08, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(0.878616861371198, 6.1529058220225, 2.432547059157785),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetKubcdk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetKubcdk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.4099907875061035, -4.315474033355713, 1.3703789710998535),
            rot=(-0.706521213054657, -0.004018005449324846, 0.011661187745630741, 0.70758455991745),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/kubcdk/usd/kubcdk.usd"),
            visual_material_path="materials",
            scale=(2.4853926953553325, 2.1965473899942687, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetOjceew0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetOjceew0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.909998893737793, -10.22398853302002, 0.3712292015552521),
            rot=(0.7061352729797363, -0.014810055494308472, -0.008238323032855988, -0.7078741192817688),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ojceew/usd/ojceew.usd"),
            visual_material_path="materials",
            scale=(0.7452097111247481, 2.5822415943420625, 1.0375940293952577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetOjceew1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetOjceew1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.868946075439453, 1.0535082817077637, 0.36447611451148987),
            rot=(0.00029774289578199387, 1.2367963790893555e-06, -0.0030062359292060137, 0.9999955296516418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ojceew/usd/ojceew.usd"),
            visual_material_path="materials",
            scale=(0.7452097111247481, 2.5822415943420625, 1.0375940293952577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetOjceew2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetOjceew2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.637877464294434, 0.5703771710395813, 0.3644830584526062),
            rot=(0.9999957084655762, -0.0029803412035107613, -1.1082738637924194e-06, -5.7658879086375237e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ojceew/usd/ojceew.usd"),
            visual_material_path="materials",
            scale=(0.7452097111247481, 2.5822415943420625, 1.0375940293952577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetOjceew3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetOjceew3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.329833030700684, -13.182331085205078, 0.36737358570098877),
            rot=(0.7069308161735535, -0.0037112832069396973, 0.0037209438160061836, -0.7072632908821106),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ojceew/usd/ojceew.usd"),
            visual_material_path="materials",
            scale=(0.7452097111247481, 2.5822415943420625, 1.0375940293952577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetOjceew4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetOjceew4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.536983489990234, -9.331184387207031, 0.3689613342285156),
            rot=(0.70710688829422, 8.381903171539307e-09, -9.546056389808655e-09, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ojceew/usd/ojceew.usd"),
            visual_material_path="materials",
            scale=(0.7452097111247481, 2.5822415943420625, 1.0375940293952577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetOjceew5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetOjceew5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.659090042114258, -10.020477294921875, 0.3644624650478363),
            rot=(0.00030085258185863495, 1.2479722499847412e-06, -0.0029935957863926888, 0.9999955296516418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ojceew/usd/ojceew.usd"),
            visual_material_path="materials",
            scale=(0.7452097111247481, 2.5822415943420625, 1.0375940293952577),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.330262184143066, -8.633561134338379, 1.2877223491668701),
            rot=(-0.7088610529899597, -0.0070768785662949085, 0.013482047244906425, 0.7051839232444763),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.247658729553223, -4.308233737945557, 1.2614467144012451),
            rot=(-0.70644611120224, 0.00433688797056675, -0.0013471113052219152, 0.7077522277832031),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.307663917541504, -8.624345779418945, 1.264901041984558),
            rot=(-0.7130428552627563, 0.004879811313003302, 0.0023866361007094383, 0.7010995149612427),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.256614685058594, -4.30508279800415, 1.2697972059249878),
            rot=(-0.7071691751480103, -0.0021560087334364653, 0.0012625849340111017, 0.7070400714874268),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.239161014556885, -4.305365562438965, 1.277817726135254),
            rot=(-0.7076733708381653, -0.005693133920431137, 0.006762031931430101, 0.7064844369888306),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.78653335571289, 4.525447845458984, 1.2754361629486084),
            rot=(-0.707064151763916, -0.003424082649871707, 0.0033107406925410032, 0.7071334719657898),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.783882141113281, 4.524544715881348, 1.2734392881393433),
            rot=(-0.7071628570556641, -0.0032479362562298775, 0.0030998880974948406, 0.7070364356040955),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.781709671020508, 4.524530410766602, 1.273602843284607),
            rot=(-0.7071688771247864, -0.003349351231008768, 0.003204307984560728, 0.7070295214653015),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.784784317016602, 4.524921417236328, 1.2734100818634033),
            rot=(-0.7072870135307312, -0.003214827971532941, 0.002950521884486079, 0.7069131731987),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.790260314941406, 4.524694442749023, 1.2626194953918457),
            rot=(-0.7072873711585999, 0.0008985919994302094, 0.00010252615174977109, 0.7069257497787476),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvunhj9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvunhj9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.580077171325684, -9.739907264709473, 1.2772256135940552),
            rot=(0.0012466823682188988, -0.0016624133568257093, 0.005024358164519072, 0.9999852776527405),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvunhj/usd/rvunhj.usd"),
            visual_material_path="materials",
            scale=(1.1391291158965362, 3.581164610418463, 2.948818765084899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetZuwvdo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetZuwvdo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.29500675201416, -13.957640647888184, 0.37263786792755127),
            rot=(0.9999270439147949, -0.0007666407618671656, -1.3135606423020363e-05, 0.012062961235642433),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/zuwvdo/usd/zuwvdo.usd"),
            visual_material_path="materials",
            scale=(1.2209680577973676, 4.343490370353489, 1.46797540804427),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetZuwvdo1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetZuwvdo1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.3325834274292, -14.933734893798828, 0.3700558841228485),
            rot=(0.9999939799308777, -0.0034962892532348633, -1.6100239008665085e-07, 4.461035132408142e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/zuwvdo/usd/zuwvdo.usd"),
            visual_material_path="materials",
            scale=(1.2209680577973676, 4.343490370353489, 1.46797540804427),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetZuwvdo2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetZuwvdo2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.063436508178711, -11.130890846252441, 0.3699153959751129),
            rot=(0.9999930262565613, -0.0037277520168572664, 2.3757340386509895e-05, -0.0002043906133621931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/zuwvdo/usd/zuwvdo.usd"),
            visual_material_path="materials",
            scale=(1.0475251324017865, 4.269194396228207, 1.46797540804427),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetZuwvdo3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetZuwvdo3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(15.063436508178711, -10.143941879272461, 0.3699168562889099),
            rot=(0.999993085861206, -0.003726271213963628, 2.3815198801457882e-05, -0.0002032257616519928),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/zuwvdo/usd/zuwvdo.usd"),
            visual_material_path="materials",
            scale=(1.0475251324017865, 4.269194396228207, 1.46797540804427),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    fridgeJuwaoh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeJuwaoh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.959928512573242, -14.293412208557129, 0.9953969120979309),
            rot=(0.7066477537155151, 0.7075418829917908, -0.0036389026790857315, 0.004518989473581314),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/juwaoh/usd/juwaoh.usd"),
            visual_material_path="materials",
            scale=(1.7966346319193618, 2.6105277900609387, 0.3963410287550783),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    fridgeJuwaoh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeJuwaoh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-21.9888916015625, -14.305756568908691, 1.004380464553833),
            rot=(0.7075921297073364, 0.706591010093689, -0.005122419446706772, 0.004040273372083902),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/juwaoh/usd/juwaoh.usd"),
            visual_material_path="materials",
            scale=(1.7966346319193618, 2.6105277900609387, 0.3963410287550783),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanGlzckq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanGlzckq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.720727920532227, 4.460785388946533, 0.40588143467903137),
            rot=(1.0000001192092896, 1.3190772733651102e-05, 3.992111305706203e-05, 2.287561073899269e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/glzckq/usd/glzckq.usd"),
            visual_material_path="materials",
            scale=(1.0631162120770548, 1.0636773577784944, 1.3696587213218103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanGlzckq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanGlzckq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.84346580505371, 0.2558392286300659, 0.40589264035224915),
            rot=(1.0000001192092896, 3.277423093095422e-05, 1.7754282453097403e-05, 5.564652383327484e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/glzckq/usd/glzckq.usd"),
            visual_material_path="materials",
            scale=(1.0631162120770548, 1.0636773577784944, 1.3696587213218103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanGlzckq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanGlzckq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.75703239440918, 0.672167956829071, 0.40589118003845215),
            rot=(1.0000001192092896, 2.0505234715528786e-05, 3.5121964174322784e-05, -5.2721588872373104e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/glzckq/usd/glzckq.usd"),
            visual_material_path="materials",
            scale=(1.0628283387458668, 1.0636773577784944, 1.3696587213218103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanGlzckq3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanGlzckq3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.83010482788086, -11.820531845092773, 0.40588071942329407),
            rot=(1.0000001192092896, 1.5263474779203534e-05, -4.678367986343801e-06, -4.545290721580386e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/glzckq/usd/glzckq.usd"),
            visual_material_path="materials",
            scale=(1.0628283387458668, 1.0636773577784944, 1.3696587213218103),
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
            pos=(-12.575140953063965, -11.464221000671387, 1.323404312133789),
            rot=(-1.1932570487260818e-08, -1.1368683772161603e-13, 1.9166296327810528e-10, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/dajebq/usd/dajebq.usd"),
            visual_material_path="materials",
            scale=(1.1391313025731498, 7.194377215467296, 2.94881895730198),
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
            pos=(-26.009414672851562, -16.074443817138672, 0.39739102125167847),
            rot=(-0.7071067094802856, 2.9103830456733704e-10, -1.127773430198431e-10, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(6.90016874269832, 1.3777734172296605, 1.4719086216719937),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPniubv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPniubv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.10027259375876, -16.72973731262031, 0.7128246903419495),
            rot=(0.9999999999999998, 0.0, 0.0, 2.1073424255447017e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/pniubv/usd/pniubv.usd"),
            visual_material_path="materials",
            scale=(1.0000140407196096, 0.9999999602635717, 0.9999999719507562),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkYyntym0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkYyntym0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.809179785377317, -14.268009425893421, 0.506292494635145),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/yyntym/usd/yyntym.usd"),
            visual_material_path="materials",
            scale=(0.9999992072968176, 1.0000094950797103, 0.9999889188479479),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairCcpgpe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairCcpgpe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.93003273010254, -15.839860916137695, 0.4793848991394043),
            rot=(0.6484619975090027, 0.6484377384185791, -0.2819911539554596, -0.28196898102760315),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ccpgpe/usd/ccpgpe.usd"),
            visual_material_path="materials",
            scale=(0.9999986605078237, 0.9999564643375376, 0.9999221480587827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairCcpgpe1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairCcpgpe1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.930850982666016, -16.799928665161133, 0.47938528656959534),
            rot=(0.6576253175735474, 0.6576220393180847, 0.2598543167114258, 0.25988075137138367),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ccpgpe/usd/ccpgpe.usd"),
            visual_material_path="materials",
            scale=(0.9999986605078237, 0.9999564643375376, 0.9999221480587827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairCcpgpe2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairCcpgpe2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.479856491088867, -16.831132888793945, 0.4793867766857147),
            rot=(0.6576260924339294, 0.6576212644577026, 0.2598634958267212, 0.2598714828491211),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ccpgpe/usd/ccpgpe.usd"),
            visual_material_path="materials",
            scale=(0.9999986605078237, 0.9999564643375376, 0.9999221480587827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairCcpgpe3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairCcpgpe3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.479013442993164, -15.871088027954102, 0.47938671708106995),
            rot=(0.6484649777412415, 0.6484369039535522, -0.2819821238517761, -0.2819731533527374),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ccpgpe/usd/ccpgpe.usd"),
            visual_material_path="materials",
            scale=(0.9999986605078237, 0.9999564643375376, 0.9999221480587827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairCcpgpe4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairCcpgpe4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.48863983154297, -14.890190124511719, 0.47938770055770874),
            rot=(0.6576265096664429, 0.6576219201087952, 0.25986024737358093, 0.25987210869789124),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ccpgpe/usd/ccpgpe.usd"),
            visual_material_path="materials",
            scale=(0.9999986605078237, 0.9999564643375376, 0.9999221480587827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairCcpgpe5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairCcpgpe5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.4877986907959, -13.930136680603027, 0.4793868064880371),
            rot=(0.6484648585319519, 0.6484370827674866, -0.2819819450378418, -0.28197336196899414),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ccpgpe/usd/ccpgpe.usd"),
            visual_material_path="materials",
            scale=(0.9999986605078237, 0.9999564643375376, 0.9999221480587827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairPfntgd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairPfntgd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.51348876953125, -15.900510787963867, 0.4793808162212372),
            rot=(-0.26812681555747986, -0.26813551783561707, 0.6542932987213135, 0.6543024778366089),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/pfntgd/usd/pfntgd.usd"),
            visual_material_path="materials",
            scale=(0.9999984635008056, 0.9999563946387294, 0.9999236207635331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairPfntgd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairPfntgd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.551374435424805, -16.852428436279297, 0.47937652468681335),
            rot=(0.28576821088790894, 0.28576579689979553, 0.6467812061309814, 0.6467987895011902),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/pfntgd/usd/pfntgd.usd"),
            visual_material_path="materials",
            scale=(0.9999984635008056, 0.9999563946387294, 0.9999236207635331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairPfntgd2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairPfntgd2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.560161590576172, -14.911417007446289, 0.47937875986099243),
            rot=(0.285788357257843, 0.2857447564601898, 0.6468152403831482, 0.6467651724815369),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/pfntgd/usd/pfntgd.usd"),
            visual_material_path="materials",
            scale=(0.9999984635008056, 0.9999563946387294, 0.9999236207635331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairPfntgd3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairPfntgd3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.522499084472656, -13.959601402282715, 0.47939515113830566),
            rot=(-0.26794180274009705, -0.2683197259902954, 0.6543407440185547, 0.6542553305625916),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/pfntgd/usd/pfntgd.usd"),
            visual_material_path="materials",
            scale=(0.9999984635008056, 0.9999563946387294, 0.9999236207635331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairPfntgd4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairPfntgd4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.964509963989258, -15.869303703308105, 0.47937852144241333),
            rot=(-0.2681007385253906, -0.26816070079803467, 0.6542949676513672, 0.6543012261390686),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/pfntgd/usd/pfntgd.usd"),
            visual_material_path="materials",
            scale=(0.9999984635008056, 0.9999563946387294, 0.9999236207635331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairPfntgd5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairPfntgd5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.002370834350586, -16.8211612701416, 0.4793761372566223),
            rot=(0.2857842445373535, 0.285748690366745, 0.6468045115470886, 0.6467759013175964),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/pfntgd/usd/pfntgd.usd"),
            visual_material_path="materials",
            scale=(0.9999984635008056, 0.9999563946387294, 0.9999236207635331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.87608528137207, 1.0247465372085571, 0.5174773931503296),
            rot=(-9.834766387939453e-07, -0.0002602040767669678, -9.123235940933228e-05, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.718781471252441, 1.9036688804626465, 0.5175241827964783),
            rot=(0.7071070075035095, 0.00017555058002471924, 0.00031262263655662537, -0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.986937522888184, -15.591198921203613, 0.5174718499183655),
            rot=(0.9209568500518799, -0.0002750605344772339, 0.00024954043328762054, 0.3896644115447998),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.938157081604004, -15.57127571105957, 0.5175251364707947),
            rot=(0.9342123866081238, 1.8775463104248047e-05, 0.00039877742528915405, -0.3567175269126892),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.934736251831055, -16.533004760742188, 0.5174725651741028),
            rot=(-0.3719385862350464, -0.00026926398277282715, -0.00030441582202911377, 0.9282572865486145),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.901516914367676, -16.5216121673584, 0.5174770355224609),
            rot=(0.38152602314949036, -0.00027877092361450195, 2.6125460863113403e-05, 0.9243581295013428),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.87197494506836, 3.6264572143554688, 0.5175129771232605),
            rot=(0.9999998807907104, -0.00017989054322242737, 0.0004323124885559082, 2.9280781745910645e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.718133926391602, 2.741050958633423, 0.5174885988235474),
            rot=(0.7071062922477722, 0.000140264630317688, 0.00023514404892921448, -0.7071073055267334),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.530611753463745, -9.791327476501465, 0.5174699425697327),
            rot=(-0.7071059346199036, -0.00015369057655334473, -0.0002299770712852478, 0.7071076035499573),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.4246625900268555, -8.757328033447266, 0.5174590349197388),
            rot=(1.0, -0.00019907578825950623, 0.00036529824137687683, -5.21540641784668e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.063713550567627, -13.715167999267578, 0.5175079703330994),
            rot=(0.9209492206573486, -0.00016267597675323486, 0.00014653056859970093, 0.38968273997306824),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.978286266326904, -14.645038604736328, 0.5174980163574219),
            rot=(0.3811415433883667, -0.0004458427429199219, -1.2341886758804321e-05, 0.9245167970657349),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.015082359313965, -13.695094108581543, 0.5175190567970276),
            rot=(0.9342118501663208, -2.3849308490753174e-05, 0.00047602877020835876, -0.3567183017730713),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQerjol9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQerjol9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.045148849487305, -14.694236755371094, 0.5174721479415894),
            rot=(-0.36533123254776, -0.00025691092014312744, -0.00026872754096984863, 0.930877685546875),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qerjol/usd/qerjol.usd"),
            visual_material_path="materials",
            scale=(0.9999558318303111, 0.9999640372497417, 0.9999443966454031),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.671451568603516, 3.858687400817871, 0.2839440107345581),
            rot=(-0.0022119281347841024, -0.00024472555378451943, 0.00012179256009403616, 0.999997615814209),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.579203605651855, 3.858994245529175, 0.283871054649353),
            rot=(0.001706441049464047, 3.622582880780101e-06, -7.384161290246993e-05, 0.9999986290931702),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.560916423797607, 4.940418720245361, 0.28389570116996765),
            rot=(-0.7101919054985046, -0.00024151959223672748, -1.9335828255861998e-05, 0.7040082216262817),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.564281463623047, 6.033720970153809, 0.2839343547821045),
            rot=(-0.7081571221351624, 0.00010564032709226012, 5.648250589729287e-05, 0.7060549855232239),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.564825057983398, 7.1270318031311035, 0.28393107652664185),
            rot=(-0.7060880661010742, 0.00011729390826076269, -0.00010302323789801449, 0.708124041557312),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.560603618621826, 8.220256805419922, 0.28393134474754333),
            rot=(-0.7041540741920471, 0.00012027748744003475, -0.0001047016994562, 0.7100473046302795),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.766141891479492, 8.222516059875488, 0.2839052379131317),
            rot=(0.7052374482154846, 1.526111736893654e-05, 0.00025144487153738737, 0.7089712619781494),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.76423168182373, 7.1289544105529785, 0.2839219570159912),
            rot=(0.7069446444511414, 3.559175820555538e-05, 0.00026506202993914485, 0.707269012928009),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairWkmkvd8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairWkmkvd8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.766519546508789, 6.036034107208252, 0.28392690420150757),
            rot=(0.7090864181518555, -0.00010033682337962091, -0.00011465321586001664, 0.705121636390686),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/wkmkvd/usd/wkmkvd.usd"),
            visual_material_path="materials",
            scale=(1.0000356755870146, 0.9999833114366199, 0.9999483136077827),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.57994270324707, 5.10917329788208, 0.5177554488182068),
            rot=(0.5000084638595581, 0.499991238117218, -0.5000414252281189, -0.4999591112136841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.20497703552246, 5.109208583831787, 0.5177581906318665),
            rot=(0.500034749507904, 0.4999639391899109, -0.5000534057617188, -0.4999481439590454),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815324783325195, 6.120232105255127, 0.5177580118179321),
            rot=(0.5000349283218384, 0.4999636709690094, -0.5000530481338501, -0.4999484717845917),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.425670623779297, 6.120232105255127, 0.5177580118179321),
            rot=(0.5000349283218384, 0.4999634921550751, -0.5000530481338501, -0.4999487102031708),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.256715774536133, 6.120232582092285, 0.5177573561668396),
            rot=(0.5000356435775757, 0.49996301531791687, -0.5000523328781128, -0.49994921684265137),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.867061614990234, 6.120232582092285, 0.51775723695755),
            rot=(0.5000357031822205, 0.49996283650398254, -0.5000522136688232, -0.4999493360519409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.45146369934082, 6.120232582092285, 0.5177571773529053),
            rot=(0.50003582239151, 0.49996277689933777, -0.5000521540641785, -0.4999493956565857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.035865783691406, 6.120232582092285, 0.5177570581436157),
            rot=(0.5000360608100891, 0.49996259808540344, -0.5000519156455994, -0.4999496340751648),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.035865783691406, 7.131256580352783, 0.5177568197250366),
            rot=(0.5000362992286682, 0.4999622404575348, -0.5000516176223755, -0.49994996190071106),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.45146369934082, 7.131257057189941, 0.5177570581436157),
            rot=(0.5000361800193787, 0.4999624788761139, -0.5000517964363098, -0.49994969367980957),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.8670597076416, 7.131257057189941, 0.5177570581436157),
            rot=(0.5000360608100891, 0.49996259808540344, -0.5000519156455994, -0.4999496340751648),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.2567138671875, 7.131257057189941, 0.5177571177482605),
            rot=(0.5000359416007996, 0.499962717294693, -0.5000520348548889, -0.49994945526123047),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.81532859802246, 5.109208583831787, 0.5177581906318665),
            rot=(0.500034749507904, 0.4999639391899109, -0.5000534057617188, -0.4999481439590454),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.42567253112793, 7.131257057189941, 0.517757773399353),
            rot=(0.5000351667404175, 0.4999634325504303, -0.5000527501106262, -0.49994876980781555),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815324783325195, 7.131257057189941, 0.517757773399353),
            rot=(0.5000351071357727, 0.49996355175971985, -0.5000529289245605, -0.4999487102031708),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204973220825195, 7.131256580352783, 0.5177580118179321),
            rot=(0.5000349283218384, 0.4999636709690094, -0.5000530481338501, -0.4999484717845917),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.57994270324707, 7.131221771240234, 0.517755389213562),
            rot=(0.5000085234642029, 0.499991238117218, -0.5000414252281189, -0.4999591112136841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.57994270324707, 8.142248153686523, 0.5177544355392456),
            rot=(0.5000086426734924, 0.49999094009399414, -0.5000414252281189, -0.4999592900276184),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204973220825195, 8.14228343963623, 0.5177574157714844),
            rot=(0.5000357627868652, 0.4999634325504303, -0.500052273273468, -0.49994874000549316),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815324783325195, 8.14228343963623, 0.5177572965621948),
            rot=(0.5000357031822205, 0.4999633729457855, -0.5000521540641785, -0.49994879961013794),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.42567253112793, 8.14228343963623, 0.5177572965621948),
            rot=(0.50003582239151, 0.49996331334114075, -0.5000520944595337, -0.4999488592147827),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.2567138671875, 8.142284393310547, 0.5177568793296814),
            rot=(0.5000364184379578, 0.49996283650398254, -0.5000515580177307, -0.4999493956565857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.8670597076416, 8.14228343963623, 0.5177568793296814),
            rot=(0.5000365376472473, 0.499962717294693, -0.5000513792037964, -0.49994951486587524),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.425676345825195, 5.109208106994629, 0.5177581310272217),
            rot=(0.500034749507904, 0.4999638795852661, -0.5000534057617188, -0.4999482035636902),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.45146369934082, 8.142282485961914, 0.5177568197250366),
            rot=(0.5000365972518921, 0.4999626576900482, -0.5000514388084412, -0.4999496042728424),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.035863876342773, 8.142282485961914, 0.5177563428878784),
            rot=(0.5000370144844055, 0.4999622404575348, -0.5000510215759277, -0.4999499022960663),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.57994270324707, 9.15327262878418, 0.5177538990974426),
            rot=(0.5000087022781372, 0.4999907612800598, -0.5000413656234741, -0.4999592900276184),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204973220825195, 9.153307914733887, 0.5177572965621948),
            rot=(0.50003582239151, 0.49996331334114075, -0.5000520944595337, -0.4999488592147827),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815324783325195, 9.153307914733887, 0.5177571177482605),
            rot=(0.5000360012054443, 0.4999631941318512, -0.5000519752502441, -0.49994903802871704),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.425670623779297, 9.153307914733887, 0.517756998538971),
            rot=(0.5000361204147339, 0.49996307492256165, -0.5000519156455994, -0.4999490976333618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.2567138671875, 9.15330696105957, 0.5177567601203918),
            rot=(0.5000364184379578, 0.499962717294693, -0.5000514984130859, -0.49994945526123047),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.8670597076416, 9.15330696105957, 0.5177565813064575),
            rot=(0.5000367760658264, 0.4999624788761139, -0.5000512599945068, -0.4999496638774872),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.451461791992188, 9.15330696105957, 0.5177562236785889),
            rot=(0.5000370144844055, 0.4999622404575348, -0.5000509023666382, -0.4999500811100006),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.03586196899414, 9.15330696105957, 0.5177561640739441),
            rot=(0.5000371336936951, 0.49996212124824524, -0.5000508427619934, -0.4999501407146454),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.2567138671875, 5.109207630157471, 0.5177578330039978),
            rot=(0.5000351071357727, 0.49996355175971985, -0.5000529289245605, -0.499948650598526),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.969593048095703, 10.138352394104004, 0.5177537798881531),
            rot=(0.5000087022781372, 0.4999907612800598, -0.5000413656234741, -0.4999593496322632),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.57994270324707, 10.138352394104004, 0.5177534222602844),
            rot=(0.500008761882782, 0.4999905228614807, -0.5000414252281189, -0.49995946884155273),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204971313476562, 10.138387680053711, 0.5177571177482605),
            rot=(0.5000360608100891, 0.4999631345272064, -0.5000518560409546, -0.4999490976333618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815322875976562, 10.138386726379395, 0.5177568793296814),
            rot=(0.5000362992286682, 0.4999629557132721, -0.5000516176223755, -0.4999493360519409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.425670623779297, 10.138388633728027, 0.5177568793296814),
            rot=(0.5000364184379578, 0.49996283650398254, -0.5000515580177307, -0.4999493956565857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.2567138671875, 10.138386726379395, 0.5177564024925232),
            rot=(0.5000368356704712, 0.4999624192714691, -0.5000512003898621, -0.49994978308677673),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.867055892944336, 10.138386726379395, 0.5177562236785889),
            rot=(0.5000371336936951, 0.49996212124824524, -0.5000507831573486, -0.49995020031929016),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.451461791992188, 10.138386726379395, 0.5177562236785889),
            rot=(0.5000370144844055, 0.4999622404575348, -0.5000509023666382, -0.4999500811100006),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz48 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz48",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.035860061645508, 10.138387680053711, 0.5177557468414307),
            rot=(0.500037670135498, 0.4999615252017975, -0.5000501275062561, -0.4999508261680603),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz49 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz49",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.620264053344727, 10.138386726379395, 0.5177559852600098),
            rot=(0.5000373125076294, 0.49996188282966614, -0.5000505447387695, -0.49995046854019165),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.867061614990234, 5.109208106994629, 0.5177573561668396),
            rot=(0.5000355839729309, 0.49996307492256165, -0.5000523328781128, -0.4999490976333618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz50 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz50",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.96959114074707, 11.123431205749512, 0.5177532434463501),
            rot=(0.5000088214874268, 0.49999046325683594, -0.5000413656234741, -0.49995946884155273),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz51 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz51",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.579936981201172, 11.123431205749512, 0.517753005027771),
            rot=(0.5000088810920715, 0.4999902844429016, -0.5000414252281189, -0.4999595880508423),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz52 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz52",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204971313476562, 11.123466491699219, 0.5177568793296814),
            rot=(0.5000364184379578, 0.49996277689933777, -0.5000516176223755, -0.49994927644729614),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz53 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz53",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815322875976562, 11.123466491699219, 0.5177568793296814),
            rot=(0.5000365376472473, 0.49996259808540344, -0.5000513792037964, -0.49994951486587524),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz54 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz54",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.425670623779297, 11.123467445373535, 0.5177568793296814),
            rot=(0.5000364184379578, 0.49996277689933777, -0.5000515580177307, -0.4999493956565857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz55 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz55",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.256711959838867, 11.123465538024902, 0.5177562832832336),
            rot=(0.5000370144844055, 0.49996206164360046, -0.5000510215759277, -0.4999501407146454),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz56 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz56",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.867055892944336, 11.123465538024902, 0.5177561044692993),
            rot=(0.5000372529029846, 0.4999617636203766, -0.5000507235527039, -0.4999504089355469),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz57 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz57",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.451457977294922, 11.123465538024902, 0.5177556872367859),
            rot=(0.5000377297401428, 0.4999612867832184, -0.5000501871109009, -0.4999508857727051),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz58 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz58",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.03586196899414, 11.123465538024902, 0.5177558064460754),
            rot=(0.5000377297401428, 0.4999615252017975, -0.5000502467155457, -0.49995070695877075),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz59 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz59",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.620264053344727, 11.123465538024902, 0.5177558064460754),
            rot=(0.5000377297401428, 0.49996158480644226, -0.5000502467155457, -0.4999507665634155),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.451467514038086, 5.109208583831787, 0.5177575349807739),
            rot=(0.5000354051589966, 0.49996307492256165, -0.5000525712966919, -0.4999491274356842),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz60 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz60",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.96955108642578, 12.425915718078613, 0.6660940647125244),
            rot=(0.5000258088111877, 0.4999735951423645, -0.5000160336494446, -0.49998483061790466),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz61 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz61",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.57990074157715, 12.425915718078613, 0.6660943627357483),
            rot=(0.5000259280204773, 0.4999738335609436, -0.5000159740447998, -0.4999845325946808),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz62 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz62",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204944610595703, 12.425915718078613, 0.6660938858985901),
            rot=(0.5000253915786743, 0.49997323751449585, -0.5000162124633789, -0.4999852478504181),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz63 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz63",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.815296173095703, 12.42591381072998, 0.6660937666893005),
            rot=(0.5000253319740295, 0.4999728202819824, -0.5000162720680237, -0.4999857246875763),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz64 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz64",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.425643920898438, 12.42591381072998, 0.6660935878753662),
            rot=(0.5000252723693848, 0.49997255206108093, -0.5000163316726685, -0.49998602271080017),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz65 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz65",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.035991668701172, 12.42591381072998, 0.6660935878753662),
            rot=(0.5000252723693848, 0.49997255206108093, -0.5000163316726685, -0.49998602271080017),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz66 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz66",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.646339416503906, 12.42591381072998, 0.6660932898521423),
            rot=(0.5000247955322266, 0.4999715983867645, -0.5000163912773132, -0.49998754262924194),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz67 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz67",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.25668716430664, 12.42591381072998, 0.6660933494567871),
            rot=(0.5000247359275818, 0.499971479177475, -0.5000166296958923, -0.49998748302459717),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz68 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz68",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.867033004760742, 12.42591381072998, 0.6660933494567871),
            rot=(0.5000247359275818, 0.499971479177475, -0.5000166296958923, -0.49998748302459717),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz69 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz69",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-28.45143699645996, 12.42591381072998, 0.6660933494567871),
            rot=(0.5000247359275818, 0.499971479177475, -0.5000166296958923, -0.49998748302459717),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.035865783691406, 5.109208106994629, 0.5177571773529053),
            rot=(0.50003582239151, 0.49996277689933777, -0.5000521540641785, -0.4999493956565857),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz70 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz70",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.03584098815918, 12.425911903381348, 0.6660928726196289),
            rot=(0.5000243782997131, 0.4999704360961914, -0.5000165104866028, -0.4999887943267822),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz71 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz71",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.620241165161133, 12.42591381072998, 0.6660929918289185),
            rot=(0.5000246167182922, 0.4999710023403168, -0.5000165104866028, -0.4999880790710449),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz72 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz72",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.896530151367188, 2.830855369567871, 0.5177438855171204),
            rot=(0.4999812841415405, 0.5000207424163818, 0.4999736547470093, 0.5000245571136475),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.579944610595703, 6.1201982498168945, 0.5177552700042725),
            rot=(0.5000085830688477, 0.4999910593032837, -0.5000414252281189, -0.4999591112136841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZrgdsz9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZrgdsz9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.204973220825195, 6.120232582092285, 0.5177581906318665),
            rot=(0.5000348687171936, 0.4999636709690094, -0.5000531077384949, -0.4999484717845917),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zrgdsz/usd/zrgdsz.usd"),
            visual_material_path="materials",
            scale=(0.9999531623832181, 1.0000370846772997, 1.0000549363098414),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZxhcxt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZxhcxt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.58014678955078, -1.1567721366882324, 0.377410352230072),
            rot=(0.6736086010932922, 0.6730745434761047, 0.21624499559402466, 0.21554656326770782),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zxhcxt/usd/zxhcxt.usd"),
            visual_material_path="materials",
            scale=(1.0000380368757855, 0.9999971711397806, 1.0000533913875052),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZxhcxt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZxhcxt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.397621154785156, -0.7623906135559082, 0.3774113357067108),
            rot=(0.7072466611862183, 0.7069666385650635, 0.00040686875581741333, -0.00040650367736816406),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zxhcxt/usd/zxhcxt.usd"),
            visual_material_path="materials",
            scale=(1.0000380368757855, 0.9999971711397806, 1.0000533913875052),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZxhcxt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZxhcxt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.22120475769043, -1.13755202293396, 0.37741148471832275),
            rot=(0.6700379252433777, 0.6700478196144104, -0.22551178932189941, -0.2263394594192505),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zxhcxt/usd/zxhcxt.usd"),
            visual_material_path="materials",
            scale=(1.0000380368757855, 0.9999971711397806, 1.0000533913875052),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZxhcxt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZxhcxt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.461055755615234, -5.918481349945068, 0.3774091303348541),
            rot=(0.22031421959400177, 0.21939516067504883, 0.6720373630523682, 0.6720811128616333),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zxhcxt/usd/zxhcxt.usd"),
            visual_material_path="materials",
            scale=(1.0000380368757855, 0.9999971711397806, 1.0000533913875052),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZxhcxt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZxhcxt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.38149642944336, -6.259430408477783, 0.3774109482765198),
            rot=(0.00040332600474357605, -0.00040416419506073, 0.706968367099762, 0.7072448134422302),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zxhcxt/usd/zxhcxt.usd"),
            visual_material_path="materials",
            scale=(1.0000380368757855, 0.9999971711397806, 1.0000533913875052),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairZxhcxt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairZxhcxt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.30917739868164, -5.948235511779785, 0.3774135410785675),
            rot=(-0.1667940318584442, -0.1674649715423584, 0.6868820190429688, 0.6872615814208984),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/zxhcxt/usd/zxhcxt.usd"),
            visual_material_path="materials",
            scale=(1.0000380368757855, 0.9999971711397806, 1.0000533913875052),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.41732290387153625, 1.9112987518310547, 0.35912415385246277),
            rot=(0.7036884427070618, 0.011983796954154968, -0.016772018745541573, 0.7102097272872925),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2226580381393433, 1.8955796957015991, 0.3612464964389801),
            rot=(0.705824613571167, 0.0056848712265491486, -0.005058850161731243, 0.7083460092544556),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa310 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa310",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.35750961303711, 12.274031639099121, 0.3541111946105957),
            rot=(0.7071067094802856, -1.1641532182693481e-10, -6.093614501878619e-11, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa311 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa311",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.549570083618164, 12.274031639099121, 0.3541111946105957),
            rot=(0.7071067094802856, -1.1641532182693481e-10, -6.093614501878619e-11, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa312 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa312",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.474798202514648, 12.274031639099121, 0.3541111946105957),
            rot=(0.7071067094802856, -1.1641532182693481e-10, -6.093614501878619e-11, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa313 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa313",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.666857719421387, 12.274031639099121, 0.3541111946105957),
            rot=(0.7071067094802856, -1.1641532182693481e-10, -6.093614501878619e-11, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa314 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa314",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.696503639221191, 0.9554834365844727, 0.3541111946105957),
            rot=(0.7071071267127991, 0.0, -1.0436451702844352e-10, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa315 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa315",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.862835884094238, 0.9554834365844727, 0.3541111946105957),
            rot=(0.7071071267127991, 0.0, -1.0436451702844352e-10, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa316 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa316",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.668691635131836, 1.0547336339950562, 0.3541111946105957),
            rot=(0.7071071267127991, 0.0, -1.0436451702844352e-10, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa317 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa317",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.4437894821167, 0.4016125500202179, 0.3541111946105957),
            rot=(0.7071071267127991, 0.0, -1.0436451702844352e-10, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa318 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa318",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.710674285888672, 4.440584182739258, 0.3541111946105957),
            rot=(0.70710688829422, 0.0, -1.77351466845721e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.472500801086426, 1.8977227210998535, 0.35314804315567017),
            rot=(0.6932678818702698, 0.006136985030025244, -0.004436943680047989, 0.720640242099762),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6766934394836426, 1.883089303970337, 0.35218822956085205),
            rot=(0.709429144859314, 0.007798192091286182, -0.006979500874876976, 0.7046992778778076),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.3188014030456543, -2.999454975128174, 0.36088791489601135),
            rot=(-0.0002649291418492794, 0.007781111169606447, -0.0005652901018038392, 0.9999696612358093),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.302330732345581, -3.8047845363616943, 0.3592374324798584),
            rot=(-0.004978868179023266, 0.021636229008436203, -0.0037293958012014627, 0.9997466206550598),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.336616039276123, 5.994422435760498, 0.3571415841579437),
            rot=(0.9999465942382812, 0.0004122577083762735, -0.01008041575551033, -0.0023128397297114134),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.340556621551514, 6.800720691680908, 0.3583976626396179),
            rot=(0.9999030828475952, -0.0017932902555912733, -0.012838744558393955, 0.005090789403766394),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.739951133728027, 4.572044849395752, 0.3541111946105957),
            rot=(1.000000238418579, -2.381430022069253e-07, -8.185452315956354e-12, 1.5086061466718093e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.739951133728027, 5.379985332489014, 0.3541111946105957),
            rot=(1.000000238418579, -2.381430022069253e-07, -8.185452315956354e-12, 1.5086061466718093e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa3/usd/todoa3.usd"),
            visual_material_path="materials",
            scale=(0.9999310690583232, 1.0000041153547952, 0.9999300071384596),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.762598037719727, 6.892089366912842, 0.40785670280456543),
            rot=(0.9999817609786987, -1.1012889444828033e-06, 0.0016956882318481803, 0.005811343435198069),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa4/usd/todoa4.usd"),
            visual_material_path="materials",
            scale=(1.0000769739875877, 1.000034219736151, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.76875114440918, 7.928515911102295, 0.4218443036079407),
            rot=(0.9998515248298645, 0.006553267128765583, -0.01138091180473566, 0.011164659634232521),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa4/usd/todoa4.usd"),
            visual_material_path="materials",
            scale=(1.0000769739875877, 1.000034219736151, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetTodoa42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetTodoa42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.7789306640625, 5.8618693351745605, 0.414265900850296),
            rot=(0.9999646544456482, -0.001353247556835413, -0.004117685370147228, -0.007205468602478504),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/todoa4/usd/todoa4.usd"),
            visual_material_path="materials",
            scale=(1.0000769739875877, 1.000034219736151, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableYclkbw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableYclkbw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.4642333984375, -10.083569526672363, 0.7308448553085327),
            rot=(0.9999998211860657, 0.0006847030017524958, 6.000202847644687e-05, 7.310768523893785e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/yclkbw/usd/yclkbw.usd"),
            visual_material_path="materials",
            scale=(0.9999999783255843, 1.0, 1.000000006146129),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -14.636799812316895, 0.6720735430717468),
            rot=(0.9999967217445374, -0.0025882243644446135, 2.5358167476952076e-07, -3.3032847568392754e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -15.34217357635498, 0.6720735430717468),
            rot=(0.9999967217445374, -0.002588162897154689, 2.5419285520911217e-07, -1.8641003407537937e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -13.931407928466797, 0.6720737218856812),
            rot=(0.9999967217445374, -0.0025882867630571127, 2.236192813143134e-07, 1.4565011952072382e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -13.222841262817383, 0.6720737218856812),
            rot=(0.9999967217445374, -0.0025882830377668142, 2.2364838514477015e-07, 1.4567922335118055e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -10.397120475769043, 0.6720737218856812),
            rot=(0.9999967217445374, -0.0025882923509925604, 2.221786417067051e-07, 1.4557735994458199e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -11.105687141418457, 0.6720737218856812),
            rot=(0.9999967217445374, -0.0025882830377668142, 2.2225140128284693e-07, 1.4565011952072382e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -11.811079025268555, 0.6720737218856812),
            rot=(0.9999967217445374, -0.0025882867630571127, 2.2408494260162115e-07, 1.4566467143595219e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    conferenceTableQzmjrj7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/conferenceTableQzmjrj7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.202340126037598, -12.517623901367188, 0.6720737218856812),
            rot=(0.9999967217445374, -0.002588296076282859, 2.2308086045086384e-07, 1.4557735994458199e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/conference_table/qzmjrj/usd/qzmjrj.usd"),
            visual_material_path="materials",
            scale=(1.0000204728968742, 0.9999304500015077, 0.9999487130319005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskGhtnfq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskGhtnfq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.592656135559082, 10.761143684387207, 0.6726502776145935),
            rot=(0.9999992847442627, -0.001186687033623457, -0.0003788108006119728, 4.1678595152916387e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/ghtnfq/usd/ghtnfq.usd"),
            visual_material_path="materials",
            scale=(1.000011675562587, 0.9999750717788667, 1.0000047598263277),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskGhtnfq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskGhtnfq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.780871391296387, 2.4193785190582275, 0.6726611256599426),
            rot=(-1.773238182067871e-06, 0.00035982756526209414, -0.0011534815421327949, 0.9999994039535522),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/ghtnfq/usd/ghtnfq.usd"),
            visual_material_path="materials",
            scale=(1.000011675562587, 1.0000250655330805, 1.0000047598263277),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8230782747268677, 7.9029107093811035, 0.7173399925231934),
            rot=(0.9999927878379822, -0.0033950333017855883, 0.001788532012142241, 0.00016789801884442568),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.0707502365112305, 7.882200717926025, 0.7262017726898193),
            rot=(0.9999749064445496, -0.0070616318844258785, -0.00021608246606774628, -0.0007665916346013546),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6894919872283936, -3.3984718322753906, 0.7148340344429016),
            rot=(0.7079196572303772, -1.023290678858757e-07, 1.9400067685637623e-07, 0.7062931060791016),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0649561882019043, -3.4006264209747314, 0.715302586555481),
            rot=(0.7074998617172241, -0.00021364283747971058, -0.00021201555500738323, 0.7067136168479919),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5595146417617798, -3.401569128036499, 0.7157862186431885),
            rot=(0.7071226835250854, -0.00030020682606846094, 0.00040409850771538913, 0.7070908546447754),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.1838536262512207, -3.4015867710113525, 0.7246576547622681),
            rot=(0.7069422602653503, -0.005007730331271887, -0.002921035513281822, 0.7072476744651794),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7082307934761047, -7.689947605133057, 0.7148337364196777),
            rot=(1.0000001192092896, 1.04919308796525e-08, 4.096364136785269e-08, -6.657196536252741e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7079907655715942, -9.314090728759766, 0.7148430943489075),
            rot=(1.0000001192092896, -6.103291525505483e-06, -9.127688826993108e-08, -0.00012375930964481086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7074374556541443, -10.938233375549316, 0.714833676815033),
            rot=(1.0000001192092896, -2.6222551241517067e-08, 1.126027200371027e-07, -0.00024873221991583705),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7070378661155701, -16.255741119384766, 0.714834988117218),
            rot=(0.9999998807907104, -7.275230018422008e-08, -9.576615411788225e-07, -0.000607072317507118),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7087416648864746, -14.631608009338379, 0.714834451675415),
            rot=(1.0, -1.249114575330168e-06, 1.3664830476045609e-06, -0.0004849555261898786),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.227762699127197, -12.041327476501465, 0.7173720598220825),
            rot=(-6.062537431716919e-05, -8.452706970274448e-05, -0.0015423597069457173, 0.9999988675117493),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.071384906768799, 6.256612777709961, 0.726055383682251),
            rot=(0.9999744296073914, 0.00713755376636982, 3.4264521673321724e-06, 0.0004223573487251997),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.228139400482178, -10.417173385620117, 0.7172249555587769),
            rot=(5.955249071121216e-05, 0.00011503323912620544, 0.0014076479710638523, 0.9999991059303284),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.22744607925415, -8.792705535888672, 0.7171790599822998),
            rot=(-0.0004893168807029724, 1.0409858077764511e-06, -0.0015029682544991374, 0.9999988675117493),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.225862979888916, -7.168518543243408, 0.7168572545051575),
            rot=(-0.00046978890895843506, -3.916211426258087e-07, 0.0012885464821010828, 0.9999991655349731),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.984524250030518, -11.280726432800293, 0.7148107886314392),
            rot=(0.9999992251396179, -8.94651748239994e-08, -2.735760062932968e-09, -0.0013544324319809675),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.070436000823975, 4.632153511047363, 0.7185208797454834),
            rot=(0.9999973177909851, -0.002360446145758033, -1.7598940758034587e-06, 6.894749822095037e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.070844650268555, 3.0075314044952393, 0.7185856103897095),
            rot=(0.9999977350234985, 0.0021716393530368805, 0.00021827095770277083, -0.00028177094645798206),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8234078288078308, 6.2786784172058105, 0.7170453071594238),
            rot=(0.9999911785125732, 0.003616096219047904, 0.002214238280430436, 3.608409679145552e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8233853578567505, 4.654597759246826, 0.7163764834403992),
            rot=(0.9999916553497314, -0.003357498673722148, 0.002363207982853055, -8.249090024037287e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8227384686470032, 3.030388593673706, 0.7281607985496521),
            rot=(0.9999900460243225, -0.003904151963070035, 0.002154012443497777, -0.0003153473953716457),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.465457439422607, 6.391139984130859, 0.719576358795166),
            rot=(-0.70726078748703, -0.002028937917202711, 0.0021018858533352613, 0.7069469094276428),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPuapey9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPuapey9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.08961296081543, 6.392022132873535, 0.7195174694061279),
            rot=(-0.7073382139205933, 0.0021248143166303635, -0.0021223954390734434, 0.7068691849708557),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/puapey/usd/puapey.usd"),
            visual_material_path="materials",
            scale=(0.9999700498803183, 1.0000166444172562, 0.9999931063920582),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskQpuflh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskQpuflh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.146737098693848, 10.761113166809082, 0.672652542591095),
            rot=(0.9999993443489075, -0.0011656918795779347, 0.0003728121519088745, 7.660673873033375e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/qpuflh/usd/qpuflh.usd"),
            visual_material_path="materials",
            scale=(1.0000119316206606, 0.999975429353276, 1.0000059132111696),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskQpuflh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskQpuflh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.246849060058594, 6.656641006469727, 0.6726396083831787),
            rot=(-0.7071061134338379, 0.0005695761647075415, -0.0011043120175600052, 0.7071064114570618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/qpuflh/usd/qpuflh.usd"),
            visual_material_path="materials",
            scale=(1.0000119316206606, 1.0000254231253665, 1.0000059132111696),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskQpuflh2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskQpuflh2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.035945892333984, 2.4193131923675537, 0.672646164894104),
            rot=(-5.811452865600586e-07, -0.0003928834921680391, -0.0011961290147155523, 0.9999992847442627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/qpuflh/usd/qpuflh.usd"),
            visual_material_path="materials",
            scale=(1.0000119316206606, 0.999975429353276, 1.0000059132111696),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskWtlxfr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskWtlxfr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.88169288635254, 3.477935791015625, 0.6623764038085938),
            rot=(-0.7071071863174438, -6.613176083192229e-05, -2.228384983027354e-05, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/wtlxfr/usd/wtlxfr.usd"),
            visual_material_path="materials",
            scale=(0.9999601742081329, 0.9999996736943136, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskWtlxfr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskWtlxfr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.014623641967773, 2.245223045349121, 0.6615728735923767),
            rot=(0.83941251039505, -0.0005953720537945628, -0.0009121051407419145, -0.5434938669204712),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/wtlxfr/usd/wtlxfr.usd"),
            visual_material_path="materials",
            scale=(0.9999601742081329, 0.9999996736943136, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskWtlxfr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskWtlxfr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.178749084472656, -0.21190515160560608, 0.6607041954994202),
            rot=(-2.0524021238088608e-06, -3.219244536012411e-05, 2.93103585136123e-05, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/wtlxfr/usd/wtlxfr.usd"),
            visual_material_path="materials",
            scale=(0.9999601742081329, 0.9999996736943136, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskWtlxfr3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskWtlxfr3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.178749084472656, -1.7486506700515747, 0.6607041954994202),
            rot=(-2.055894583463669e-06, -3.219640348106623e-05, 2.931910421466455e-05, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/wtlxfr/usd/wtlxfr.usd"),
            visual_material_path="materials",
            scale=(0.9999601742081329, 0.9999996736943136, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskWtlxfr4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskWtlxfr4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.178805351257324, -3.211923122406006, 0.6610347032546997),
            rot=(-4.3227337300777435e-06, -0.0004772792453877628, 2.9136523153283633e-05, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/wtlxfr/usd/wtlxfr.usd"),
            visual_material_path="materials",
            scale=(0.9999601742081329, 0.9999996736943136, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableAympln0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableAympln0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.50493860244751, -14.15097427368164, 0.6079347133636475),
            rot=(1.0, 0.00025315769016742706, -9.623938240110874e-05, -8.005008567124605e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/aympln/usd/aympln.usd"),
            visual_material_path="materials",
            scale=(1.0000000264909539, 1.0000000264909539, 1.0000439555688292),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableAympln1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableAympln1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.427181243896484, -16.114540100097656, 0.6101239919662476),
            rot=(0.9999900460243225, -0.003767000511288643, -0.00014398200437426567, -0.0024134234990924597),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/aympln/usd/aympln.usd"),
            visual_material_path="materials",
            scale=(1.0000000264909539, 1.0000000264909539, 1.0000439555688292),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableAympln2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableAympln2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.00886344909668, -12.310159683227539, 0.607925534248352),
            rot=(0.9999848008155823, 0.00022307690232992172, -0.00011072808410972357, 0.005514953751116991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/aympln/usd/aympln.usd"),
            visual_material_path="materials",
            scale=(1.0000000264909539, 1.0000000264909539, 1.0000439555688292),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableAympln3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableAympln3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.03034782409668, -10.141480445861816, 0.6079110503196716),
            rot=(0.9999991059303284, 0.00041546206921339035, 7.542152889072895e-05, 0.0012589066755026579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/aympln/usd/aympln.usd"),
            visual_material_path="materials",
            scale=(1.0000000264909539, 1.0000000264909539, 1.0000439555688292),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableDmghrm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableDmghrm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.974260330200195, -14.393668174743652, 0.5297175645828247),
            rot=(-0.13159799575805664, -0.13692834973335266, 0.6894717812538147, 0.6989715695381165),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/dmghrm/usd/dmghrm.usd"),
            visual_material_path="materials",
            scale=(0.999964916004216, 1.0000702657778313, 0.9999660072891662),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableDmghrm1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableDmghrm1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.142900466918945, 1.2445068359375, 0.5263927578926086),
            rot=(-0.1338343322277069, -0.13383446633815765, 0.6943262219429016, 0.6943255662918091),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/dmghrm/usd/dmghrm.usd"),
            visual_material_path="materials",
            scale=(0.999964916004216, 1.0000702657778313, 0.9999660072891662),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableDmghrm2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableDmghrm2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.109434127807617, 1.0814082622528076, 0.5263927578926086),
            rot=(-0.1338343322277069, -0.13383446633815765, 0.6943262219429016, 0.6943255662918091),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/dmghrm/usd/dmghrm.usd"),
            visual_material_path="materials",
            scale=(0.999964916004216, 1.0000702657778313, 0.9999660072891662),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableDmghrm3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableDmghrm3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.004371643066406, -16.34829330444336, 0.5263927578926086),
            rot=(-0.1338343322277069, -0.13383446633815765, 0.6943262219429016, 0.6943255662918091),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/dmghrm/usd/dmghrm.usd"),
            visual_material_path="materials",
            scale=(0.999964916004216, 1.0000702657778313, 0.9999660072891662),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableDmghrm4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableDmghrm4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.48244285583496, -16.336328506469727, 0.527399480342865),
            rot=(-0.13519400358200073, -0.1320018470287323, 0.6946501731872559, 0.6940889358520508),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/dmghrm/usd/dmghrm.usd"),
            visual_material_path="materials",
            scale=(0.999964916004216, 1.0000702657778313, 0.9999660072891662),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableGikdir0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableGikdir0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.33725929260254, -1.7493077516555786, 0.26594677567481995),
            rot=(-0.13393092155456543, -0.13373813033103943, 0.6944054961204529, 0.6942461729049683),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/gikdir/usd/gikdir.usd"),
            visual_material_path="materials",
            scale=(1.000028021448628, 1.0000213829021067, 0.9999455868590589),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableGikdir1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableGikdir1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.312150955200195, -5.2573418617248535, 0.2659485340118408),
            rot=(-0.13393110036849976, -0.1337376832962036, 0.6944059133529663, 0.6942458748817444),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/gikdir/usd/gikdir.usd"),
            visual_material_path="materials",
            scale=(1.000028021448628, 1.0000213829021067, 0.9999455868590589),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTablePljlcn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTablePljlcn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.228062629699707, 8.066157341003418, 0.2879383862018585),
            rot=(0.9999995231628418, -7.095886394381523e-05, -1.1794210877269506e-05, 0.0010408463422209024),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/pljlcn/usd/pljlcn.usd"),
            visual_material_path="materials",
            scale=(1.0000762135125507, 1.0000770241707702, 0.9999079699096842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTablePljlcn1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTablePljlcn1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.218865394592285, 7.240221977233887, 0.2879384458065033),
            rot=(0.9999995231628418, -7.215887308120728e-05, -1.2801086995750666e-05, 0.0010410654358565807),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/pljlcn/usd/pljlcn.usd"),
            visual_material_path="materials",
            scale=(1.0000762135125507, 1.0000770241707702, 0.9999079699096842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTablePljlcn2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTablePljlcn2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.206188201904297, 6.331261157989502, 0.28793978691101074),
            rot=(0.7063703536987305, -3.866571933031082e-05, -7.210229523479939e-05, 0.7078424692153931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/pljlcn/usd/pljlcn.usd"),
            visual_material_path="materials",
            scale=(1.0000762135125507, 1.0000770241707702, 0.9999079699096842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableSsnzie0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableSsnzie0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.678894996643066, 1.100476861000061, 0.227134570479393),
            rot=(-0.13383419811725616, -0.1338343471288681, 0.6943261623382568, 0.6943257451057434),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/ssnzie/usd/ssnzie.usd"),
            visual_material_path="materials",
            scale=(0.9999964079633376, 1.0000214658280928, 1.0000738760278671),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableSsnzie1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableSsnzie1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.691383361816406, 3.540310859680176, 0.22713272273540497),
            rot=(-0.13383419811725616, -0.1338343471288681, 0.6943261623382568, 0.6943257451057434),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/ssnzie/usd/ssnzie.usd"),
            visual_material_path="materials",
            scale=(0.9999964079633376, 1.0000214658280928, 1.0000738760278671),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableSsnzie2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableSsnzie2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.7044947147369385, -9.019243240356445, 0.2271340936422348),
            rot=(-0.13383419811725616, -0.1338343471288681, 0.6943261623382568, 0.6943257451057434),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/ssnzie/usd/ssnzie.usd"),
            visual_material_path="materials",
            scale=(0.9999964079633376, 1.0000214658280928, 1.0000738760278671),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    photocopierTlbmhm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/photocopierTlbmhm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.395956039428711, -9.114351272583008, 0.5373477339744568),
            rot=(1.0, -7.176915823947638e-05, -4.871783676207997e-05, 4.5425258576869965e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/photocopier/tlbmhm/usd/tlbmhm.usd"),
            visual_material_path="materials",
            scale=(1.00003520056254, 1.000008914464223, 0.9999638062207087),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    photocopierTlbmhm1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/photocopierTlbmhm1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.39593505859375, -11.35080337524414, 0.5373313426971436),
            rot=(1.0000001192092896, -1.322705065831542e-05, -2.7816462534246966e-05, 9.582145139575005e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/photocopier/tlbmhm/usd/tlbmhm.usd"),
            visual_material_path="materials",
            scale=(1.00003520056254, 1.000008914464223, 0.9999638062207087),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    photocopierTlbmhm2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/photocopierTlbmhm2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.606830596923828, 4.5093536376953125, 0.5373306274414062),
            rot=(1.0, -2.18274217331782e-05, -3.698328146128915e-05, 9.130453690886497e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/photocopier/tlbmhm/usd/tlbmhm.usd"),
            visual_material_path="materials",
            scale=(1.00003520056254, 1.000008914464223, 0.9999638062207087),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    standWaxtja0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/standWaxtja0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.890223503112793, 5.194461822509766, 0.30780017375946045),
            rot=(1.0, -7.223852094284666e-08, 1.465341483708471e-07, 1.093685941810918e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stand/waxtja/usd/waxtja.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9999999602635717, 0.9999999980563703),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    standWaxtja1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/standWaxtja1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.630105495452881, 4.023699760437012, 0.30780014395713806),
            rot=(1.0, -6.971981036940633e-08, 1.501530277892016e-07, 1.0509891623655676e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stand/waxtja/usd/waxtja.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9999999602635717, 0.9999999980563703),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-21.84544563293457, -16.22935676574707, 0.5457768440246582),
            rot=(0.9845353960990906, 1.4133111108094454e-05, 8.341623470187187e-06, 0.17518632113933563),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.920183181762695, -16.206298828125, 0.5411719083786011),
            rot=(0.9845353364944458, 8.32056684885174e-06, 8.668925147503614e-06, 0.17518575489521027),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.29134178161621, -9.752389907836914, 0.5411263704299927),
            rot=(0.9845352172851562, -6.31164584774524e-06, 6.813439540565014e-06, 0.17518654465675354),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.65955924987793, -9.67191219329834, 0.5411262512207031),
            rot=(1.0, 1.6286394384223968e-06, -4.772329702973366e-06, 3.043533070012927e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.65955924987793, -9.118103981018066, 0.5411262512207031),
            rot=(1.0, 1.8600967450765893e-06, -4.541361704468727e-06, 2.874439815059304e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.291349411010742, -9.198599815368652, 0.5411273837089539),
            rot=(0.9845354557037354, 8.186354534700513e-06, 4.948058631271124e-06, 0.17518582940101624),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.291349411010742, -8.705655097961426, 0.5411272644996643),
            rot=(0.9845353364944458, 8.377130143344402e-06, 4.582689143717289e-06, 0.17518575489521027),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.65955924987793, -8.62515926361084, 0.5411262512207031),
            rot=(1.0, 1.9008057279279456e-06, -4.556437488645315e-06, 2.8294743970036507e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.40084457397461, -16.239309310913086, 0.5411606431007385),
            rot=(0.9845348000526428, 2.9728587833233178e-05, 7.70187471061945e-05, 0.17518900334835052),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.5057430267334, -16.21625328063965, 0.5411720871925354),
            rot=(0.9845353364944458, 8.34587262943387e-06, 8.61630542203784e-06, 0.17518582940101624),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.65955924987793, -11.333328247070312, 0.5411264300346375),
            rot=(1.0, 1.5479363355552778e-06, -4.701199941337109e-06, 3.022578312084079e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.291351318359375, -11.413824081420898, 0.5411271452903748),
            rot=(0.9845353960990906, 7.947019184939563e-06, 4.495028406381607e-06, 0.17518576979637146),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.291351318359375, -10.860017776489258, 0.5411271452903748),
            rot=(0.9845354557037354, 7.976472261361778e-06, 4.473025910556316e-06, 0.17518579959869385),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.659557342529297, -10.779521942138672, 0.5411261916160583),
            rot=(1.0, 1.5898222045507282e-06, -4.647183232009411e-06, 2.675296855159104e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.65955924987793, -10.225716590881348, 0.5411262512207031),
            rot=(1.0, 1.6067369870143011e-06, -4.740431904792786e-06, 2.5363988243043423e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretStnoqf9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretStnoqf9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.291353225708008, -10.3062105178833, 0.5411270260810852),
            rot=(0.9845353364944458, 8.050992619246244e-06, 4.460976924747229e-06, 0.17518587410449982),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/stnoqf/usd/stnoqf.usd"),
            visual_material_path="materials",
            scale=(0.9998816624880309, 0.9999564136028066, 1.000034275160184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairJhipgz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairJhipgz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.809602737426758, -4.174584865570068, 0.5520002245903015),
            rot=(-0.49841609597206116, -0.4333314299583435, 0.4912759065628052, 0.5678497552871704),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/jhipgz/usd/jhipgz.usd"),
            visual_material_path="materials",
            scale=(0.9999486746169255, 0.9999649775169095, 0.999966782060857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairJhipgz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairJhipgz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.804959297180176, -3.1054775714874268, 0.5520244240760803),
            rot=(-0.5000180602073669, -0.43466320633888245, 0.48985928297042847, 0.5666462182998657),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/jhipgz/usd/jhipgz.usd"),
            visual_material_path="materials",
            scale=(0.9999486746169255, 0.9999649775169095, 0.999966782060857),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.455595970153809, -10.44815444946289, 0.4819768965244293),
            rot=(0.7071034908294678, -3.451691009104252e-05, -3.918493166565895e-05, -0.7071100473403931),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.455595016479492, -11.125082969665527, 0.48197612166404724),
            rot=(0.7071064710617065, -3.4193508327007294e-05, -3.778224345296621e-05, -0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.648489952087402, -16.098602294921875, 0.4819668233394623),
            rot=(-7.89714977145195e-06, -2.8357375413179398e-05, 5.882066034246236e-07, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866140365600586, -14.583124160766602, 0.481967955827713),
            rot=(0.7071051597595215, -9.116611909121275e-05, -1.2108299415558577e-05, 0.7071084380149841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866135597229004, -13.868660926818848, 0.4819679260253906),
            rot=(0.7071051597595215, -9.0943300165236e-05, -1.2243050150573254e-05, 0.7071083784103394),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.86613941192627, -13.204882621765137, 0.48197081685066223),
            rot=(0.707105278968811, -9.485066402703524e-05, -1.7059675883501768e-05, 0.7071084380149841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866165161132812, -12.525303840637207, 0.4819645881652832),
            rot=(0.7071042656898499, -6.602494977414608e-05, 3.806606400758028e-06, 0.7071093320846558),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866143226623535, -11.862552642822266, 0.4819689095020294),
            rot=(0.7071051597595215, -9.197869803756475e-05, -1.4117569662630558e-05, 0.7071083784103394),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866135597229004, -11.109245300292969, 0.48196786642074585),
            rot=(0.7071051597595215, -9.077973663806915e-05, -1.237762626260519e-05, 0.7071083784103394),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866140365600586, -10.432316780090332, 0.4819680154323578),
            rot=(0.7071051597595215, -9.116611909121275e-05, -1.2108299415558577e-05, 0.7071084380149841),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.824783325195312, -9.725897789001465, 0.4819616675376892),
            rot=(1.0, -2.066099114017561e-05, -3.2732728868722916e-05, -1.2392993085086346e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.637295722961426, -9.725898742675781, 0.48196154832839966),
            rot=(0.9999999403953552, -2.0809817215194926e-05, -3.2650772482156754e-05, -1.31258275359869e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.45559310913086, -11.853718757629395, 0.481979101896286),
            rot=(0.707102358341217, -2.5550369173288345e-05, -3.582966746762395e-05, -0.7071111798286438),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.545660018920898, 9.650310516357422, 0.481984406709671),
            rot=(-0.28955408930778503, 2.0673731341958046e-05, 2.148249768652022e-05, 0.9571616649627686),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.0376615524292, 10.806099891662598, 0.4819786548614502),
            rot=(0.7829296588897705, -2.7373083867132664e-05, -3.463157918304205e-05, -0.6221101880073547),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.673686027526855, 10.813963890075684, 0.48197123408317566),
            rot=(0.7832708358764648, -9.083363693207502e-05, -8.155417162925005e-06, 0.6216806769371033),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.106521606445312, 9.6346435546875, 0.48196449875831604),
            rot=(0.2900714874267578, -4.11283690482378e-05, -4.563710535876453e-05, 0.9570050239562988),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.05106258392334, 5.187558174133301, 0.4819622337818146),
            rot=(0.43022090196609497, -3.9744190871715546e-05, -3.451513475738466e-05, 0.9027236700057983),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.247859954833984, 4.805933475494385, 0.48196184635162354),
            rot=(-0.16017839312553406, -3.3870572224259377e-05, -3.02107073366642e-05, 0.987088143825531),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.109601974487305, 2.419311046600342, 0.48198434710502625),
            rot=(0.6320929527282715, 1.4611287042498589e-05, -7.346540223807096e-05, 0.7748926281929016),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.631109714508057, 3.56215500831604, 0.48196616768836975),
            rot=(0.9607934355735779, -2.4130626115947962e-05, -2.3048429284244776e-05, 0.2772653102874756),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.551874160766602, 2.3418996334075928, 0.48197874426841736),
            rot=(-0.5985329747200012, -6.052805110812187e-05, -4.3274194467812777e-05, 0.801098108291626),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.188645362854004, 3.5444765090942383, 0.4819695055484772),
            rot=(0.948123037815094, -1.677684485912323e-05, -2.527091419324279e-05, -0.3179035186767578),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.455589294433594, -12.516457557678223, 0.48198384046554565),
            rot=(0.7071020603179932, -3.185763489454985e-05, -4.460330819711089e-05, -0.7071114778518677),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.637273788452148, 0.39738377928733826, 0.48197272419929504),
            rot=(-0.3191852867603302, -2.140807919204235e-05, -7.02559482306242e-05, 0.9476924538612366),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.89500617980957, 1.4194093942642212, 0.48197290301322937),
            rot=(0.8406729698181152, -6.89973821863532e-05, 1.1862837709486485e-05, 0.5415432453155518),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.13969898223877, 1.8605396747589111, 0.4819689989089966),
            rot=(0.9997816681861877, -4.5961067371536046e-05, 4.558335058391094e-05, -0.02089831791818142),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.339064598083496, 1.3920146226882935, 0.4819648265838623),
            rot=(0.8294153809547424, -2.0307721570134163e-05, 5.337601760402322e-05, -0.5586323738098145),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.592869758605957, 0.3928208351135254, 0.48196667432785034),
            rot=(0.28416574001312256, -5.7877739891409874e-05, -2.574946847744286e-05, 0.9587751626968384),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.670738220214844, 0.5397951006889343, 0.4819523096084595),
            rot=(-0.31918349862098694, -3.055785782635212e-05, -5.100484122522175e-05, 0.9476929903030396),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.626315116882324, 0.535207211971283, 0.4819522500038147),
            rot=(0.2841661870479584, -5.0518661737442017e-05, -3.2148294849321246e-05, 0.958774983882904),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.928462982177734, 1.5617989301681519, 0.4819525480270386),
            rot=(0.8406728506088257, -5.962641444057226e-05, 1.5247846022248268e-05, 0.5415432453155518),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.173133850097656, 2.0029306411743164, 0.4819592833518982),
            rot=(0.9997817277908325, -4.3036812712671235e-05, 6.124179344624281e-05, -0.02089623734354973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.372522354125977, 1.5343942642211914, 0.48195260763168335),
            rot=(0.8294153213500977, -7.767695933580399e-06, 5.937443347647786e-05, -0.5586324334144592),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.455642700195312, -13.168547630310059, 0.48196661472320557),
            rot=(0.707107663154602, 4.922039806842804e-06, 6.715895142406225e-05, -0.7071059942245483),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.515593528747559, -10.62060546875, 0.4844871163368225),
            rot=(-0.37417587637901306, -0.004039364401251078, -0.003537924727424979, 0.9273422956466675),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.515729904174805, -10.640740394592285, 0.4819394052028656),
            rot=(0.4290471076965332, 4.1353050619363785e-05, -3.056044806726277e-05, 0.9032822251319885),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.527877807617188, -9.705503463745117, 0.48194175958633423),
            rot=(0.927915632724762, -5.4899370297789574e-05, 2.5137909688055515e-05, 0.37279048562049866),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.526599884033203, -9.696983337402344, 0.4838535189628601),
            rot=(0.9225847125053406, -0.002590866293758154, -0.002923372434452176, -0.38577497005462646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.507611274719238, -12.829163551330566, 0.4861206114292145),
            rot=(0.42211800813674927, -0.0006426789332181215, 0.0034261085093021393, 0.9065342545509338),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.51416015625, -12.820185661315918, 0.48557576537132263),
            rot=(-0.4009671211242676, 0.0015199334593489766, 0.00644288444891572, 0.9160684943199158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.5194730758667, -11.900467872619629, 0.48196497559547424),
            rot=(0.9279156923294067, -5.945854354649782e-05, 1.7693149857223034e-05, 0.37279003858566284),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.519728660583496, -11.889603614807129, 0.48226431012153625),
            rot=(0.9194920063018799, -0.0004730375949293375, -0.00047239684499800205, -0.39310798048973083),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.407031059265137, -13.884578704833984, 0.48196783661842346),
            rot=(0.707107663154602, -1.5182537026703358e-05, 6.64278632029891e-05, -0.7071059346199036),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.407015800476074, -14.599053382873535, 0.48196303844451904),
            rot=(0.7071061134338379, 4.789908416569233e-06, 6.051186937838793e-05, -0.7071074843406677),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.40701675415039, -15.339110374450684, 0.4819619357585907),
            rot=(0.707106351852417, 3.8135331124067307e-06, 5.8384030126035213e-05, -0.7071072459220886),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.866162300109863, -15.323193550109863, 0.4819628894329071),
            rot=(0.7071054577827454, -6.174109876155853e-05, 2.2604363039135933e-06, 0.7071081399917603),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairSrucpc9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairSrucpc9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.83596134185791, -16.098648071289062, 0.48196032643318176),
            rot=(-8.945353329181671e-07, -4.1048042476177216e-05, -3.7157627957640216e-05, 0.9999999403953552),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/srucpc/usd/srucpc.usd"),
            visual_material_path="materials",
            scale=(1.0000305045359357, 0.9999739487793364, 0.9999418046433775),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7693382501602173, -14.759261131286621, 0.48677965998649597),
            rot=(-0.7071060538291931, -0.0003055129200220108, -0.00048512278590351343, 0.7071073651313782),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7693383693695068, -16.49375343322754, 0.48677971959114075),
            rot=(-0.7071062326431274, -0.00030560046434402466, -0.00048521277494728565, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.529863119125366, -2.3204166889190674, 0.4867807626724243),
            rot=(0.9999998807907104, -0.00012865511234849691, 0.000558329513296485, -3.2654497772455215e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1221120357513428, -2.3204169273376465, 0.4867807626724243),
            rot=(0.9999998807907104, -0.0001286552578676492, 0.0005583094898611307, -2.735760062932968e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6147231459617615, -2.3204169273376465, 0.48678064346313477),
            rot=(0.9999998807907104, -0.0001285815378651023, 0.0005583929596468806, -3.0011869966983795e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.170192241668701, -2.3204166889190674, 0.48678094148635864),
            rot=(1.0, -0.00012884597526863217, 0.0005580710712820292, -3.0011869966983795e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.0691072940826416, -4.535468101501465, 0.48677965998649597),
            rot=(3.3155083656311035e-07, -0.0005569830536842346, -0.00012609889381565154, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5136390924453735, -4.535467147827148, 0.48677971959114075),
            rot=(2.5704503059387207e-07, -0.0005569932982325554, -0.00012609886471182108, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.020896315574646, -4.535468101501465, 0.48677971959114075),
            rot=(2.6263296604156494e-07, -0.00055699422955513, -0.0001260988792637363, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6309494972229004, -4.535468101501465, 0.48677971959114075),
            rot=(3.46451997756958e-07, -0.0005569718778133392, -0.0001260988210560754, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.10624361038208, -7.1646904945373535, 0.48677998781204224),
            rot=(0.7071071267127991, -0.0004825280047953129, 0.0003109424142166972, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.321287631988525, -7.2657790184021, 0.48677965998649597),
            rot=(-0.7071062922477722, -0.00030554039403796196, -0.0004852120764553547, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.44570568203926086, -16.392669677734375, 0.4867797791957855),
            rot=(0.7071070075035095, -0.00048254290595650673, 0.00031085312366485596, 0.7071065306663513),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.106243133544922, -8.77474594116211, 0.4867797791957855),
            rot=(0.7071071267127991, -0.0004825941286981106, 0.00031149317510426044, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.321287155151367, -8.673528671264648, 0.48677971959114075),
            rot=(-0.7071059346199036, -0.0003053499385714531, -0.00048512150533497334, 0.707107424736023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.10624361038208, -10.309280395507812, 0.4867798388004303),
            rot=(0.7071070671081543, -0.0004825275391340256, 0.00031085312366485596, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.321287155151367, -10.41036319732666, 0.48677971959114075),
            rot=(-0.7071060538291931, -0.0003053504042327404, -0.00048507656902074814, 0.707107424736023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.321287631988525, -11.965834617614746, 0.48677971959114075),
            rot=(-0.7071059346199036, -0.0003052009269595146, -0.00048510509077459574, 0.707107424736023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.106243133544922, -11.86474895477295, 0.4867798388004303),
            rot=(0.7071070671081543, -0.00048248283565044403, 0.00031082378700375557, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9573801755905151, 2.9558749198913574, 0.48677971959114075),
            rot=(-0.7071061134338379, -0.00030551105737686157, -0.00048522709403187037, 0.7071073055267334),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2576635777950287, 3.0569651126861572, 0.4867797791957855),
            rot=(0.7071071267127991, -0.00048261042684316635, 0.00031164195388555527, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9573801755905151, 4.51134729385376, 0.48677971959114075),
            rot=(-0.7071062326431274, -0.0003053918480873108, -0.00048519589472562075, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2576639652252197, 4.612433910369873, 0.4867798984050751),
            rot=(0.7071071267127991, -0.0004825596697628498, 0.0003110910765826702, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.44570550322532654, -14.658174514770508, 0.4867798686027527),
            rot=(0.7071070075035095, -0.00048249727115035057, 0.0003107939846813679, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9573801755905151, 6.248180866241455, 0.48677965998649597),
            rot=(-0.7071062326431274, -0.00030554039403796196, -0.0004852121928706765, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.25766393542289734, 6.146968841552734, 0.4867798686027527),
            rot=(0.7071070075035095, -0.0004825899377465248, 0.00031110597774386406, 0.7071064114570618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9573805332183838, 7.655932903289795, 0.48677965998649597),
            rot=(-0.7071062922477722, -0.000305703841149807, -0.00048524350859224796, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.25766393542289734, 7.757020950317383, 0.4867798984050751),
            rot=(0.7071071267127991, -0.0004825596697628498, 0.0003110910765826702, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.959672451019287, 3.0060179233551025, 0.4867797791957855),
            rot=(-0.7071061730384827, -0.0003055254928767681, -0.00048522709403187037, 0.7071072459220886),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.174715518951416, 3.107107639312744, 0.4867798984050751),
            rot=(0.7071071863174438, -0.0004826257936656475, 0.0003117311280220747, 0.7071061730384827),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.174716472625732, 4.662576675415039, 0.48677998781204224),
            rot=(0.7071071267127991, -0.00048254290595650673, 0.0003109422978013754, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.9596729278564453, 4.561489582061768, 0.4867797791957855),
            rot=(-0.7071062326431274, -0.0003053918480873108, -0.00048519589472562075, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.9596734046936035, 6.2983245849609375, 0.48677971959114075),
            rot=(-0.7071062326431274, -0.00030554039403796196, -0.0004852121928706765, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.174716472625732, 6.197110652923584, 0.4867798984050751),
            rot=(0.7071071863174438, -0.0004825284704566002, 0.0003109721001237631, 0.707106351852417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7693381309509277, -11.011273384094238, 0.48677965998649597),
            rot=(-0.7071059346199036, -0.00030533550307154655, -0.00048507668543606997, 0.707107424736023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.174716472625732, 7.807163238525391, 0.48677995800971985),
            rot=(0.7071070671081543, -0.00048254523426294327, 0.0003111212281510234, 0.7071064114570618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.959672689437866, 7.7060747146606445, 0.48677965998649597),
            rot=(-0.7071062326431274, -0.0003053918480873108, -0.00048519589472562075, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.788060665130615, 1.651087760925293, 0.4867774248123169),
            rot=(-0.3115489184856415, -0.0004922011867165565, -0.0002926079323515296, 0.9502300024032593),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.885877847671509, -11.353480339050293, 0.48675647377967834),
            rot=(-0.7071059346199036, -0.00030533596873283386, -0.00048504688311368227, 0.707107424736023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.100921154022217, -11.252395629882812, 0.48675665259361267),
            rot=(0.7071070075035095, -0.0004827468656003475, 0.00031240086536854506, 0.7071064114570618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.415782928466797, -3.1191246509552, 0.4867800772190094),
            rot=(0.640364944934845, -0.0005090469494462013, 0.00026727269869297743, 0.768070638179779),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.4168853759765625, -1.6737239360809326, 0.4867800772190094),
            rot=(0.6403650045394897, -0.0005090394988656044, 0.00026727269869297743, 0.768070638179779),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.416884422302246, -0.058189909905195236, 0.4867800772190094),
            rot=(0.6403650045394897, -0.0005090702325105667, 0.0002673171693459153, 0.7680705785751343),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf48 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf48",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.11304759979248, 1.5989190340042114, 0.4867786467075348),
            rot=(0.23262017965316772, -0.0005714632570743561, 9.124138159677386e-06, 0.9725674986839294),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf49 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf49",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.646462440490723, 1.5802810192108154, 0.4867793321609497),
            rot=(-0.1918737143278122, -0.0005242479965090752, -0.00023091718321666121, 0.981419563293457),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.4457055628299713, -10.910188674926758, 0.4867798686027527),
            rot=(0.7071070075035095, -0.0004825121723115444, 0.0003108087694272399, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf50 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf50",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(14.06378173828125, 6.760971546173096, 0.48677965998649597),
            rot=(-0.5333603620529175, -0.00040590669959783554, -0.0004064204404130578, 0.8458881378173828),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf51 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf51",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.753154754638672, 11.58499526977539, 0.48678073287010193),
            rot=(0.9480018019676208, -0.00029304996132850647, 0.0004962175153195858, 0.3182646930217743),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf52 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf52",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.052277565002441, 11.567203521728516, 0.4867795407772064),
            rot=(0.9667193293571472, 2.0408770069479942e-05, 0.000572454184293747, -0.25583910942077637),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf53 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf53",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.945013523101807, 7.505934715270996, 0.48678094148635864),
            rot=(0.9999999403953552, -0.00012877240078523755, 0.0005580410361289978, -1.1187512427568436e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf54 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf54",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.046229362487793, 5.290884494781494, 0.4867796301841736),
            rot=(4.209578037261963e-07, -0.0005569392815232277, -0.00012606880045495927, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf55 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf55",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.436173915863037, 5.290883541107178, 0.4867798984050751),
            rot=(1.5273690223693848e-07, -0.00055694580078125, -0.0001261428842553869, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf56 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf56",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.537262439727783, 7.505934715270996, 0.48678094148635864),
            rot=(1.0, -0.00012878705456387252, 0.0005580642027780414, -1.869630068540573e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7693380117416382, -9.274438858032227, 0.48677971959114075),
            rot=(-0.7071059346199036, -0.0003052013926208019, -0.0004850603872910142, 0.707107424736023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.44570550322532654, -9.375654220581055, 0.4867798686027527),
            rot=(0.7071070075035095, -0.00048249727115035057, 0.0003107939846813679, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.44570550322532654, -7.765600204467773, 0.4867797791957855),
            rot=(0.7071071267127991, -0.0004824982024729252, 0.00031092786230146885, 0.7071064114570618),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairWksozf9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairWksozf9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7693382501602173, -7.866687297821045, 0.48677965998649597),
            rot=(-0.7071062326431274, -0.0003054961562156677, -0.0004851819248870015, 0.7071071267127991),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/wksozf/usd/wksozf.usd"),
            visual_material_path="materials",
            scale=(1.0000066346372878, 0.9999354332815711, 1.0000229776133955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskPfsjbc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskPfsjbc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.873546113008926, -3.264669069010134, 0.580703147316541),
            rot=(-0.4999999180436094, -0.5000000074505778, 0.5000000074505778, 0.5000000670552236),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/pfsjbc/usd/pfsjbc.usd"),
            visual_material_path="materials",
            scale=(0.9999880605270121, 0.9999961020987767, 0.9999612290060589),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.520915985107422, -13.244119644165039, 1.5355417728424072),
            rot=(0.5000006556510925, 0.5000006556510925, -0.49999934434890747, -0.4999995529651642),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.0618577003479, -3.3857500553131104, 1.5355409383773804),
            rot=(0.5000004768371582, 0.5000009536743164, -0.49999934434890747, -0.4999992847442627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9905766448937036),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.863365173339844, 4.062570095062256, 1.53554105758667),
            rot=(0.7071067690849304, 0.7071068286895752, 4.656612873077393e-10, 1.376321279167314e-10),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.95918083190918, 7.43586540222168, 1.5355397462844849),
            rot=(0.4999999403953552, 0.4999992549419403, 0.500000536441803, 0.5000004768371582),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.267742156982422, 9.094651222229004, 1.53554105758667),
            rot=(-1.125037670135498e-06, -1.555909875605721e-06, 0.7071070075035095, 0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.028026103973389, 0.5810582637786865, 1.535539984703064),
            rot=(0.5000005960464478, 0.5000008344650269, -0.49999934434890747, -0.49999943375587463),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.39512825012207, 3.295689582824707, 1.5355403423309326),
            rot=(0.5000005960464478, 0.5000008344650269, -0.49999934434890747, -0.49999943375587463),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.84206771850586, 2.7070512771606445, 1.53554105758667),
            rot=(0.7071067690849304, 0.7071068286895752, 2.0954757928848267e-09, 1.7674750552032492e-09),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.229411125183105, -12.131876945495605, 1.5355414152145386),
            rot=(0.4999997019767761, 0.4999997913837433, 0.5000003576278687, 0.5000001788139343),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.437644958496094, 2.8513336181640625, 1.5355409383773804),
            rot=(0.500000536441803, 0.5000007748603821, -0.4999995231628418, -0.49999937415122986),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.941983222961426, -11.8155517578125, 1.5355398654937744),
            rot=(0.49999892711639404, 0.49999913573265076, 0.5000008940696716, 0.500001072883606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.064062118530273, -1.887682318687439, 1.5355405807495117),
            rot=(0.5000005960464478, 0.5000008344650269, -0.49999934434890747, -0.49999943375587463),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.967622756958008, 4.06151008605957, 1.53554105758667),
            rot=(-1.564621925354004e-07, -5.009542292100377e-07, 0.7071070075035095, 0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.960241317749023, 8.540131568908691, 1.5355418920516968),
            rot=(0.5000005960464478, 0.5000008344650269, -0.49999934434890747, -0.49999943375587463),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.943865776062012, -10.714859008789062, 1.5355393886566162),
            rot=(0.5000005960464478, 0.5000008344650269, -0.49999934434890747, -0.49999943375587463),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.530411720275879, -8.373661041259766, 1.5355406999588013),
            rot=(-1.564621925354004e-07, -5.009542292100377e-07, 0.7071070075035095, 0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.412603378295898, -8.37366008758545, 1.5355411767959595),
            rot=(-1.564621925354004e-07, -5.009542292100377e-07, 0.7071070075035095, 0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.641200065612793, 2.704540252685547, 1.5355408191680908),
            rot=(-1.125037670135498e-06, -1.555909875605721e-06, 0.7071070075035095, 0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDqnbsj9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDqnbsj9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.0629096031188965, -0.004930893890559673, 1.5355408191680908),
            rot=(0.5, 0.4999995529651642, 0.5000003576278687, 0.5000002980232239),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dqnbsj/usd/dqnbsj.usd"),
            visual_material_path="materials",
            scale=(0.9999860719153563, 1.000007372724646, 0.9998997191985856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorJsoewn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorJsoewn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.025835037231445, 2.1621861457824707, 1.5413918495178223),
            rot=(0.7071067094802856, 0.7071068286895752, 9.883660823106766e-08, -2.2248727304940985e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/jsoewn/usd/jsoewn.usd"),
            visual_material_path="materials",
            scale=(0.9999857173117075, 0.999995044329781, 0.9999002979935104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorStvajh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorStvajh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-20.18523406982422, 0.3616958260536194, 1.6714472770690918),
            rot=(-8.866190910339355e-07, -9.171581609734858e-07, 0.7071067690849304, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/stvajh/usd/stvajh.usd"),
            visual_material_path="materials",
            scale=(0.9999832510961851, 0.9999947789019196, 0.9998880276845772),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6939482305025177, -7.6665962016107825, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.581710918672485, -7.666596201610782, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-13.126818340542481, -7.6665962016107825, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.750028301482482, -7.666596201610782, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.234417949917483, -7.6665962016107825, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.972230449922485, -7.6665962016107825, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightGhdczp6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightGhdczp6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.7496161921024824, -7.6665962016107825, 2.480659263302241),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/ghdczp/usd/ghdczp.usd"),
            visual_material_path="materials",
            scale=(0.9999644993731479, 0.9999640656454123, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightTghdrr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightTghdrr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.750054663574026, -3.539682629995285, 2.60774462891),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/tghdrr/usd/tghdrr.usd"),
            visual_material_path="materials",
            scale=(0.999999769614044, 1.0000000340607427, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightTyfhjt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightTyfhjt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.670090403020192, -1.2994112571142344, 2.5183055024444814),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/tyfhjt/usd/tyfhjt.usd"),
            visual_material_path="materials",
            scale=(0.9999779579516913, 0.9999791270021039, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightTyfhjt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightTyfhjt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.670090403020192, -3.1349796164942347, 2.5183055024444814),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/tyfhjt/usd/tyfhjt.usd"),
            visual_material_path="materials",
            scale=(0.9999779579516913, 0.9999791270021039, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightTyfhjt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightTyfhjt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.67009040302019, -5.066575197544235, 2.5183055024444814),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/tyfhjt/usd/tyfhjt.usd"),
            visual_material_path="materials",
            scale=(0.9999779579516913, 0.9999791270021039, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    elevatorDoorZlmfwf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/elevatorDoorZlmfwf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-21.238550269767643, -2.6537209502742876, 1.1339965687391018),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/elevator_door/zlmfwf/usd/zlmfwf.usd"),
            visual_material_path="materials",
            scale=(1.0000239925523224, 1.0000201352232498, 0.9999823751022362),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    elevatorDoorZlmfwf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/elevatorDoorZlmfwf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-21.238550269767643, -5.171617434644287, 1.1339965687391018),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/elevator_door/zlmfwf/usd/zlmfwf.usd"),
            visual_material_path="materials",
            scale=(1.0000239925523224, 1.0000201352232498, 0.9999823751022362),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    elevatorDoorZlmfwf2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/elevatorDoorZlmfwf2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-21.238550269767643, -7.689616458084288, 1.1339965687391018),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/elevator_door/zlmfwf/usd/zlmfwf.usd"),
            visual_material_path="materials",
            scale=(1.0000239925523224, 1.0000201352232498, 0.9999823751022362),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightLmicjz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightLmicjz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.19502850447287, -14.69481579315715, 1.9998663868905675),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/lmicjz/usd/lmicjz.usd"),
            visual_material_path="materials",
            scale=(1.0, 1.0, 0.9999845198887872),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightLmicjz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightLmicjz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.19502850447287, -11.078836300977152, 1.999866203785568),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/lmicjz/usd/lmicjz.usd"),
            visual_material_path="materials",
            scale=(1.0, 1.0, 0.9999845198887872),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightLmicjz2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightLmicjz2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.19502850447287, -12.848699582227152, 1.999866203785568),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/lmicjz/usd/lmicjz.usd"),
            visual_material_path="materials",
            scale=(1.0, 1.0, 0.9999845198887872),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.526383925553876, -16.73047886823717, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.654544081803877, -16.73047886823717, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.471647597433876, -16.37333970807717, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.016817519303878, -16.35646861432717, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-16.994040175553877, -14.418605333077169, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.443368300553878, -11.453226426827172, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.443368300553878, -10.52213072370717, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.443368300553878, -9.59103404401717, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightRueuqi8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightRueuqi8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.443368300553878, -8.719750840892171, 1.6802025301487702),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/rueuqi/usd/rueuqi.usd"),
            visual_material_path="materials",
            scale=(0.9999184346484024, 0.9999779687762196, 0.9999754975573127),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.27225338629706, 10.842217769621683, 2.6981899764296737),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.87225338629706, 10.842217769621682, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.87225338629706, 3.642215328211683, 2.6981902205697232),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm100 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm100",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.527745739053595, -13.157782230383964, 2.6981902205698),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm101 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm101",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.527745739053595, -14.957782230383962, 2.6981902205698),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm102 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm102",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.527745739053595, -11.357782230383963, 2.6981902205697996),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm103 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm103",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.527745739053595, -9.557782230383962, 2.6981902205697996),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm104 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm104",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.927745898780488, -13.157782230384106, 2.698190220569875),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm105 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm105",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.927745898780487, -14.957782230384103, 2.698190220569875),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm106 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm106",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.927745898780486, -11.357782230384101, 2.698190220569875),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm107 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm107",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.327745774092664, -13.157782230383907, 2.698190220569987),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm108 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm108",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.327745774092666, -14.957782230383904, 2.698190220569987),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm109 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm109",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.327745774092664, -11.357782230383904, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.27225338629706, 3.642215328211683, 2.698189976429724),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm110 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm110",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092664, -13.157782230383905, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm111 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm111",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092664, -14.957782230383904, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm112 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm112",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092662, -11.357782230383904, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm113 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm113",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.072254286492952, -11.357782230384004, 2.6981902205698227),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm114 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm114",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.072254286492951, -9.557782230384007, 2.6981902205698223),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm115 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm115",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.872254736046886, -9.55778223038394, 2.698190220569788),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm116 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm116",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.872254260946406, -11.357782230383963, 2.6981902205697996),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm117 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm117",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277477201796655, -7.757781253818712, 2.698189244009877),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm118 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm118",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.527745739053187, -5.357782718663963, 2.6981902205699018),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm119 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm119",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.27225340907423, -9.557782230383761, 2.698190220569911),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.47225533942716, 0.6422175254766825, 2.698190220569711),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm120 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm120",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.27225536219923, -11.357781253818763, 2.698190220569911),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm121 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm121",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.527747692173188, -7.7577812538189646, 2.6981892440099022),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm122 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm122",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.327747692173187, -7.757781742098964, 2.698189244009902),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm123 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm123",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.072253306947822, -9.557782230383184, 2.698190220569602),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm124 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm124",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.072253306947822, -11.357782230383185, 2.698190220569602),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm125 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm125",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.327745739053187, -5.357782718663962, 2.6981902205699018),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm126 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm126",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.327745739053262, -0.5577823371939623, 2.698190220569844),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm127 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm127",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.872253306947822, -9.557782230383186, 2.698190220569602),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm128 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm128",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.872255260077822, -11.357781253818185, 2.6981902205696016),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm129 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm129",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.327745739053288, -1.7577823524539622, 2.6981902205698507),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.27225533942716, 0.6422172813366825, 2.698190464709711),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm130 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm130",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.327745739053186, -2.9577827186639625, 2.6981904647098505),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm131 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm131",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.272257292547064, -14.957781253818318, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm132 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm132",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.672257292547062, -14.957781253818318, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm133 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm133",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-22.07225533942706, -14.957782230383318, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm134 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm134",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-23.872257292547065, -14.957782230383318, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm135 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm135",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.672257292547062, -14.957782230383318, 2.6981904647096733),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm136 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm136",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.1277457390531875, -2.9577822303839625, 2.6981902205698507),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm137 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm137",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.127745739053289, -1.7577823524539624, 2.698190220569851),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm138 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm138",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.127745739053264, -0.5577823371939623, 2.698190220569844),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm139 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm139",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.472253306947824, -12.557782230383182, 2.698189976429602),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.639880260077927, 1.8422166099468151, 2.6981902205696526),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm140 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm140",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.272253306947825, -12.557782230383186, 2.698189732289602),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm141 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm141",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.272255260077824, -10.157782230383187, 2.698190464709602),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm142 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm142",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.472255260077825, -10.157782230383186, 2.6981902205696016),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm143 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm143",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.272255339427062, -10.157782230383319, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm144 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm144",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.672257292547066, -13.757781253818317, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm145 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm145",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.272257292547064, -13.757781253818317, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm146 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm146",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.672257292547062, -11.957781253818318, 2.698190464709673),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm147 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm147",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.27225729254706, -11.957781253818318, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm148 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm148",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-19.672255339427064, -10.157782230383319, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm149 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm149",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.272253306947926, 1.8422163658068147, 2.6981902205696526),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.639882213197977, 0.642217525476815, 2.6981902205696398),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm150 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm150",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.272255260077976, 0.642217281336815, 2.69819022056964),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm151 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm151",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.472255260077976, 0.642217525476815, 2.6981902205696398),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm152 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm152",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.472253306947927, 1.842216609946815, 2.6981902205696526),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.47225338629706, 3.642215328211683, 2.6981902205697237),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-20.27225338629706, 3.642214839931683, 2.6981904647097235),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-17.272253386297063, 3.642215328211683, 2.6981902205697232),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-14.272253306947823, 3.6422158164918144, 2.6981902205696526),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.47225338629706, 10.842217769621683, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.472253306947824, 3.642215816491815, 2.698190220569652),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.072253306947822, 3.642215328211815, 2.698190220569652),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.272253409074638, 3.642215328211237, 2.698190220569962),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.872254736046886, 3.64221532821106, 2.698190220569839),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.072254286492951, 3.6422167930559954, 2.698190220569874),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722537582893902, 3.6422163047711638, 2.698190220569892),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277472416937678, 3.6422167930562286, 2.6981897322898716),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596656, 3.6422167930562876, 2.698190220569826),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.1277457390531875, 3.642216304771038, 2.698190220569851),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.52774577409246, 3.642216304771096, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.47225338629706, 8.442217769621685, 2.698190220569672),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.327745774092461, 3.042217281336096, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.12774577409246, 3.042217769621096, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.92774577409246, 3.042217769621096, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.127745774092256, 1.8422175865110961, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092255, 1.8422175865110961, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.127745774092256, 4.842216793056097, 2.6981902205700887),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092255, 4.842216793056096, 2.6981902205700887),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.127745774092256, 7.242217769621097, 2.6981902205700887),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092255, 7.242217769621098, 2.6981902205700887),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.127745774092665, 9.042217769621097, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.87225338629706, 8.442217769621683, 2.6981902205696726),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092664, 9.042217769621095, 2.698190464709987),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.127745774092665, 10.842217769621096, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(13.927745774092664, 10.842217769621096, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.52774473993218, 10.842218746181816, 2.698190220569601),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.727743820967662, 10.842218746181095, 2.6981902205699866),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(9.727743820967664, 9.642218746181095, 2.698190464709987),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.52774473993218, 9.642218746181813, 2.6981902205696016),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.439882213197974, 0.642217281336815, 2.6981902205696398),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm48 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm48",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.072253306947822, 5.442216304771815, 2.6981902205697037),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm49 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm49",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.272253409074638, 5.442215816491236, 2.6981902205700132),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.27225338629706, 8.442217769621687, 2.6981899764296733),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm50 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm50",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.872254260946813, 5.442216304771037, 2.6981904647099015),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm51 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm51",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.072254286492952, 5.442217769620996, 2.6981902205699244),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm52 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm52",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722527817295938, 5.4422177696211635, 2.6981897322899435),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm53 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm53",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.727746265133564, 5.442217281336228, 2.6981902205699226),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm54 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm54",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.127745767059665, 5.442217281336288, 2.6981904647098762),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm55 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm55",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.1277457390531875, 5.442217281336037, 2.6981902205699013),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm56 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm56",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.527745774092258, 5.442217281336096, 2.6981902205700887),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm57 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm57",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(10.327745774092255, 1.8422175865110963, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm58 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm58",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.072253306947822, 7.242217769621815, 2.6981902205697037),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm59 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm59",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.272255362199639, 7.242218746181237, 2.698190220570013),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.47225338629706, 6.042216793056683, 2.6981902205697743),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm60 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm60",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.872254736046886, 7.2422177696210595, 2.6981902205698898),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm61 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm61",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.072254286492952, 7.242218746180995, 2.698190220569924),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm62 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm62",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722552231295937, 7.242219722741162, 2.698190220569943),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm63 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm63",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277448002935641, 7.242219722741228, 2.6981902205699226),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm64 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm64",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596656, 7.242218746181289, 2.6981902205698765),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm65 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm65",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.127744762493188, 7.242219722741037, 2.6981902205699018),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm66 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm66",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.52774473993218, 7.2422197227418135, 2.6981904647097035),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm67 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm67",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.439880260077924, 1.842216365806815, 2.6981902205696526),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm68 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm68",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.1277457390531875, 1.8422175865110375, 2.6981902205698507),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm69 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm69",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.527745774092255, 1.8422175865110961, 2.6981902205700377),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.872253386297064, 6.042216304771683, 2.6981902205697743),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm70 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm70",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.127745767059564, 1.8422175865112878, 2.6981902205698254),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm71 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm71",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277457768536659, 1.8422175865112276, 2.6981902205698716),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm72 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm72",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722542465694918, 1.8422175865111632, 2.6981902205698924),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm73 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm73",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.072254286493053, 1.8422175865109949, 2.6981902205698733),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm74 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm74",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.872254736047091, 1.8422166099460597, 2.698190220569839),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm75 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm75",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.272254385634639, 1.842216609946237, 2.698190220569962),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm76 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm76",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596145, 0.042217662806288206, 2.698190220569819),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm77 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm77",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277448002936405, 0.04221717452622819, 2.6981907088498653),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm78 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm78",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722542465695174, 0.042217662806163535, 2.698190220569886),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm79 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm79",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596656, -1.7577823524537117, 2.698190220569826),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-29.272253386297063, 6.042216304771683, 2.6981899764297754),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm80 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm80",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277457768536659, -1.757782352453772, 2.698190220569872),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm81 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm81",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722542465694918, -1.7577823524538363, 2.6981902205698924),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm82 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm82",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596656, -3.5577822303837117, 2.6981902205698254),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm83 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm83",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277457768537678, -3.5577822303837716, 2.6981902205698716),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm84 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm84",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6722532700093902, -3.557782230383836, 2.6981899764298927),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm85 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm85",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596656, -5.357782718663712, 2.6981902205698765),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm86 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm86",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277467534135641, -5.357781742098773, 2.698189732289923),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm87 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm87",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.672254246569594, -5.357782718663836, 2.6981902205699435),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm88 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm88",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596656, -9.557782230383712, 2.6981902205697748),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm89 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm89",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277462651335639, -9.557782230383772, 2.6981902205698205),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-24.47225338629706, 3.642215328211683, 2.698190464709724),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm90 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm90",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.672253758289594, -9.557782230383838, 2.6981902205698414),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm91 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm91",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.127745767059665, -11.357782230383712, 2.6981902205697748),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm92 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm92",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277438237285639, -11.357782230383773, 2.6981907088498205),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm93 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm93",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.672255223129594, -11.357781253818837, 2.6981904647098416),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm94 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm94",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.127745767059665, -13.157782230383715, 2.6981902205697743),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm95 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm95",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.727745776853564, -13.157781253818774, 2.698189732289821),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm96 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm96",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.672255223129594, -13.15778125381884, 2.6981902205698414),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm97 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm97",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1277457670596647, -14.957782230383712, 2.6981902205697743),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm98 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm98",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7277448002935639, -14.957781253818771, 2.6981902205698205),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    squareLightZljdtm99 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/squareLightZljdtm99",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.672255223129594, -14.957781253818837, 2.6981902205698414),
            rot=(0.4999992549417051, 0.4999999105927979, 0.5000005364415683, 0.5000002980229891),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/square_light/zljdtm/usd/zljdtm.usd"),
            visual_material_path="materials",
            scale=(0.9999999602635717, 0.9998347836947269, 0.9999993642175266),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvCwdngq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvCwdngq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.928750468503408, -1.6642954446570695, 0.9083829400323703),
            rot=(-0.49999976158137643, -0.49999982118602126, 0.5000002384185347, 0.50000017881389),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/cwdngq/usd/cwdngq.usd"),
            visual_material_path="materials",
            scale=(0.999998386987122, 0.9999890406416795, 0.9992154629745718),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvCwdngq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvCwdngq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-12.928750468503429, -6.16019659822707, 0.9083829400323855),
            rot=(-0.49999976158137643, -0.49999982118602126, 0.5000002384185347, 0.50000017881389),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/cwdngq/usd/cwdngq.usd"),
            visual_material_path="materials",
            scale=(0.999998386987122, 0.9999890406416795, 0.9992154629745718),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-27.664552688598633, 2.334538459777832, 1.660489559173584),
            rot=(2.77668732451275e-07, 2.843612492142711e-07, 0.7071067094802856, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-25.35612678527832, 2.334538459777832, 1.6604893207550049),
            rot=(2.77668732451275e-07, 2.843612492142711e-07, 0.7071067094802856, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.094820022583008, -16.96242904663086, 1.542090654373169),
            rot=(-0.004356973804533482, -0.004357022233307362, 0.7070932388305664, 0.7070934772491455),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(12.643917083740234, -16.942581176757812, 1.5420905351638794),
            rot=(-0.004356973804533482, -0.004357022233307362, 0.7070932388305664, 0.7070934772491455),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.949132442474365, 3.8982346057891846, 1.6604893207550049),
            rot=(0.5000001192092896, 0.5000001192092896, 0.49999988079071045, 0.49999988079071045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.949132442474365, 2.3491370677948, 1.6604893207550049),
            rot=(0.5000001192092896, 0.5000001192092896, 0.49999988079071045, 0.49999988079071045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.949132442474365, 7.482461452484131, 1.6604893207550049),
            rot=(0.5000001192092896, 0.5000001192092896, 0.49999988079071045, 0.49999988079071045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvPghmyr7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvPghmyr7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.949132442474365, 5.933363437652588, 1.6604893207550049),
            rot=(0.5000001192092896, 0.5000001192092896, 0.49999988079071045, 0.49999988079071045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/pghmyr/usd/pghmyr.usd"),
            visual_material_path="materials",
            scale=(1.0000066593684747, 0.9999595760407067, 1.0011553437595984),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvZesqym0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvZesqym0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-15.999748229980469, -15.512624740600586, 1.5664883852005005),
            rot=(-0.4999997615814209, -0.4999998211860657, 0.5000001788139343, 0.5000002384185791),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/zesqym/usd/zesqym.usd"),
            visual_material_path="materials",
            scale=(0.9999711496415906, 1.0000493723229151, 1.001136416020629),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    webcamHqyxlb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/webcamHqyxlb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-26.49364187364853, 2.318884284763217, 1.2257417021384402),
            rot=(-5.3385080295117214e-08, -5.338508034759387e-08, 0.7071067811865455, 0.7071067811865456),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/webcam/hqyxlb/usd/hqyxlb.usd"),
            visual_material_path="materials",
            scale=(1.0002634161092379, 0.9997881592061306, 1.0004931000709907),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowBlindLcollf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowBlindLcollf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-20.40522199806191, -17.28606069751585, 1.3946859175718043),
            rot=(0.7026496403594907, -0.12075555853099201, 0.11876775856453499, -0.6910830612249896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window_blind/lcollf/usd/lcollf.usd"),
            visual_material_path="materials",
            scale=(1.0000319961133965, 0.9999843387388238, 0.9999849705213654),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowBlindLcollf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowBlindLcollf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.614658101989741, -16.788265794429137, 1.3946855966148797),
            rot=(0.7026494630404277, -0.1207555289855744, 0.11876778861953223, -0.6910832415091824),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window_blind/lcollf/usd/lcollf.usd"),
            visual_material_path="materials",
            scale=(1.0000319961133965, 0.9999843387388238, 0.9999849705213654),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowBlindQnasqy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowBlindQnasqy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-18.23670230102593, -17.567485173936806, 1.394685083742399),
            rot=(0.9855178451906138, -0.169368562630435, -0.001405570984957244, 0.008178702437185732),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window_blind/qnasqy/usd/qnasqy.usd"),
            visual_material_path="materials",
            scale=(0.9999913239022773, 0.9999840916807383, 0.9999852499753146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowBlindQnasqy1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowBlindQnasqy1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.766187593726004, -17.010110170622504, 1.394685691120028),
            rot=(0.9855178452216081, -0.16936856263576178, -0.0014055702865095555, 0.00817869871215271),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window_blind/qnasqy/usd/qnasqy.usd"),
            visual_material_path="materials",
            scale=(0.9999913239022773, 0.9999840916807383, 0.9999852499753146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowBlindRfijuh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowBlindRfijuh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.054498465832776, -17.074271073452692, 1.3946853614979582),
            rot=(0.9855178449617034, -0.1693685625910956, -0.0014055736621831144, 0.008178730374962888),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window_blind/rfijuh/usd/rfijuh.usd"),
            visual_material_path="materials",
            scale=(1.0000030578643164, 0.9999842769742909, 0.9999853431266656),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
