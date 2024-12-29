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
class wainscott0IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Wainscott_0_int/usd/Wainscott_0_int_quick.usd"),
        )
    )
@configclass
class wainscott0IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Wainscott_0_int/usd/Wainscott_0_int_quick.usd"),
        )
    )
    armchairBslhmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.4167613983154297, 4.771460056304932, 0.3226168751716614),
            rot=(0.2694556713104248, 6.51925802230835e-09, 1.1408701539039612e-08, 0.9630129933357239),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(0.8631481651065848, 0.8654905569684882, 1.0322162861207331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairXpcheg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairXpcheg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5866771340370178, 11.154885292053223, 0.28721216320991516),
            rot=(-0.7061046957969666, 1.3969838619232178e-09, 6.9267116487026215e-09, 0.7081074714660645),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/xpcheg/usd/xpcheg.usd"),
            visual_material_path="materials",
            scale=(1.3950983213570456, 1.262788293675437, 0.9758380546083039),
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
            pos=(-2.54056715965271, 4.393309593200684, 0.3552984893321991),
            rot=(-1.694541424512863e-05, 5.1371753215789795e-06, -0.006242190953344107, 0.9999805092811584),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.1078784372054589, 1.2505751839916852, 1.0117323012103638),
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
            pos=(-4.090001583099365, -2.8049871921539307, 0.2982258200645447),
            rot=(0.7089084386825562, -1.30385160446167e-08, -1.4086253941059113e-08, 0.7053005695343018),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/dnsjnv/usd/dnsjnv.usd"),
            visual_material_path="materials",
            scale=(0.6651568925463738, 0.651674842077137, 1.1644640369811154),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableDnsjnv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableDnsjnv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.1200289726257324, 10.8149995803833, 0.5570352077484131),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/dnsjnv/usd/dnsjnv.usd"),
            visual_material_path="materials",
            scale=(1.5166217750595892, 1.3965032864008113, 2.1834070411467095),
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
            pos=(-4.310818195343018, -5.934988021850586, 0.6374865770339966),
            rot=(0.7083161473274231, -4.1155144572257996e-06, 6.728841981384903e-06, 0.7058954834938049),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.0629111439308652, 1.1539626712783047, 1.6386046200435262),
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
            pos=(-4.235006332397461, -0.5840968489646912, 0.5577901601791382),
            rot=(1.0, -3.9383594412356615e-06, -4.829096724279225e-06, -6.659829523414373e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.5264714744743862, 1.2629256970331553, 1.4337530461454588),
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
            pos=(-3.150698184967041, -1.744996190071106, 0.39066609740257263),
            rot=(0.7089084386825562, 0.0, 9.778887033462524e-09, 0.7053005695343018),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.41782652580401575, 0.9822755421368985, 0.9830795835697105),
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
            pos=(-2.349997043609619, 8.225692749023438, 0.5737265348434448),
            rot=(1.000000238418579, 1.2027876437059604e-06, 2.714859647312551e-06, 4.514495230978355e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.019520177538227, 0.9822755421368985, 1.4747233609250723),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableZypvuv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableZypvuv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.659743309020996, 6.6007537841796875, 0.6391333341598511),
            rot=(0.9999336004257202, -2.4556356947869062e-11, 4.320099833421409e-12, -0.01153634488582611),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/zypvuv/usd/zypvuv.usd"),
            visual_material_path="materials",
            scale=(1.578097814869874, 1.4880553940528523, 1.8003179618549163),
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
            pos=(-0.005793584510684013, 13.166942596435547, 0.120510995388031),
            rot=(0.9999999403953552, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.6213208071551322, 1.3538792705418952, 1.5342496749964756),
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
            pos=(-2.4144692420959473, 6.267605304718018, 0.32586994767189026),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/gpkbiw/usd/gpkbiw.usd"),
            visual_material_path="materials",
            scale=(1.1522445532107692, 1.6657481737804072, 1.8186539403152462),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableGpkbiw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableGpkbiw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3119094371795654, 11.23257064819336, 0.3331214189529419),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/gpkbiw/usd/gpkbiw.usd"),
            visual_material_path="materials",
            scale=(1.491920067154858, 1.3913387015220893, 1.770678681593606),
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
            pos=(-3.988447427749634, 12.6199312210083, 0.27403244376182556),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qlmqyy/usd/qlmqyy.usd"),
            visual_material_path="materials",
            scale=(1.1192411012128654, 1.2962598011504634, 0.9271366083197401),
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
            pos=(-3.423689603805542, 9.75578498840332, 0.2736169099807739),
            rot=(0.0017712172120809555, 6.232503801584244e-05, 2.2320920834317803e-05, 0.9999984502792358),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qlmqyy/usd/qlmqyy.usd"),
            visual_material_path="materials",
            scale=(0.8939220482635396, 1.4669290870422556, 1.0021386405861088),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableEmeeke0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableEmeeke0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3995935916900635, -6.419454574584961, 0.5614084005355835),
            rot=(0.0028251081239432096, -3.5762786865234375e-07, 2.9597722459584475e-06, 0.9999960660934448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/emeeke/usd/emeeke.usd"),
            visual_material_path="materials",
            scale=(0.6251667753961789, 0.9835957883687052, 1.314191632863149),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableEmeeke1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableEmeeke1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6106789112091064, -0.2846922278404236, 0.6415635943412781),
            rot=(1.0, -7.336655471590348e-06, -1.4058302895136876e-06, 2.9918510335846804e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/emeeke/usd/emeeke.usd"),
            visual_material_path="materials",
            scale=(0.5397987266271265, 1.0108267591607674, 1.501824663621999),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableEmeeke2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableEmeeke2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5182888507843018, 6.32808780670166, 0.5614094138145447),
            rot=(0.7023763656616211, -3.805849701166153e-06, -3.6423311939870473e-06, 0.7118058800697327),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/emeeke/usd/emeeke.usd"),
            visual_material_path="materials",
            scale=(0.7327153691559231, 0.7995406725332003, 1.314191632863149),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableEmeeke3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableEmeeke3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1904395818710327, 9.81531047821045, 0.5614093542098999),
            rot=(1.0000001192092896, 1.3660610420629382e-06, -3.1251402106136084e-06, -1.8177506717620417e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/emeeke/usd/emeeke.usd"),
            visual_material_path="materials",
            scale=(0.3454755129525786, 1.0761154722646276, 1.314191632863149),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampJqsuky0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampJqsuky0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.129539966583252, 4.598179340362549, 0.49716508388519287),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/jqsuky/usd/jqsuky.usd"),
            visual_material_path="materials",
            scale=(1.8973669273357454, 1.9730624615016272, 1.7933751232819173),
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
            pos=(-4.1423797607421875, -2.8623862266540527, 0.4497299790382385),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/jatssq/usd/jatssq.usd"),
            visual_material_path="materials",
            scale=(1.0240157153507534, 1.0768909162020281, 0.7275057982202585),
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
            pos=(-1.2130963802337646, 9.811403274536133, 0.7415556907653809),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/jatssq/usd/jatssq.usd"),
            visual_material_path="materials",
            scale=(0.6696850179975515, 0.6540602206300279, 0.6231735713437099),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantKxmvco0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantKxmvco0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.64718770980835, 6.593664646148682, 0.988669753074646),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/kxmvco/usd/kxmvco.usd"),
            visual_material_path="materials",
            scale=(1.3779527119291182, 1.5793068887521666, 1.7756507342078314),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantKxmvco1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantKxmvco1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.982823610305786, 9.777109146118164, 0.220580592751503),
            rot=(1.0, -6.878748536109924e-06, -1.3511627912521362e-05, 6.3783954828977585e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/kxmvco/usd/kxmvco.usd"),
            visual_material_path="materials",
            scale=(1.3779527119291182, 1.2958415497453675, 1.6202076640366703),
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
            pos=(6.400440692901611, 5.0626540184021, 0.5919111371040344),
            rot=(0.9999999403953552, -0.00034038617741316557, 0.0004962707753293216, 1.8399623513687402e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(2.2437007157954416, 2.076268123430433, 1.9168469115558702),
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
            pos=(-4.270036697387695, 8.128983497619629, 0.8197285532951355),
            rot=(1.0000001192092896, -0.0002903129789046943, 6.359865074045956e-05, 5.493902790476568e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(2.2437007157954416, 1.8727922195270195, 2.6542103100794603),
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
            pos=(0.8287560343742371, 13.161136627197266, 0.6830391883850098),
            rot=(0.9999999403953552, -0.0002883285051211715, 0.00033856695517897606, 1.911321305669844e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(2.007480250893307, 2.32043920811453, 2.211792270965306),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.082291126251221, 9.318840980529785, 0.6375027894973755),
            rot=(0.9999998807907104, -0.0002744188532233238, 0.0003553399001248181, 1.7068032320821658e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.8503936417333875, 1.8727922195270195, 2.0643195912605883),
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
            pos=(-2.244974136352539, 9.762255668640137, 0.3371507525444031),
            rot=(1.9471190171316266e-07, 7.275957614183426e-12, 2.559946032931748e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/mnfbbh/usd/mnfbbh.usd"),
            visual_material_path="materials",
            scale=(1.015268552917792, 1.2087934541059275, 1.001961926243301),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaUixwiv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaUixwiv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0177737474441528, 6.695276260375977, 0.24671293795108795),
            rot=(-0.7043925523757935, -2.7939677238464355e-09, 1.1641532182693481e-09, 0.7098106741905212),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/uixwiv/usd/uixwiv.usd"),
            visual_material_path="materials",
            scale=(1.2639288264136455, 1.1664666218808433, 1.5272225850617833),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaUixwiv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaUixwiv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.2451910972595215, 12.777111053466797, 0.2532612681388855),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/uixwiv/usd/uixwiv.usd"),
            visual_material_path="materials",
            scale=(1.2792873461156733, 1.1924450190431832, 1.504644237519172),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    loudspeakerSnbvop0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/loudspeakerSnbvop0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.466705799102783, 9.126625061035156, 0.2011372148990631),
            rot=(-0.005276843905448914, -5.913898348808289e-07, -1.9964886632806156e-08, 0.9999862313270569),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/loudspeaker/snbvop/usd/snbvop.usd"),
            visual_material_path="materials",
            scale=(1.8065521532120772, 5.855177966847914, 0.899822524376567),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    loudspeakerSnbvop1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/loudspeakerSnbvop1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.482282638549805, 9.994827270507812, 0.35201534628868103),
            rot=(0.7098636627197266, -9.577488526701927e-07, -4.5374872570391744e-07, 0.7043392062187195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/loudspeaker/snbvop/usd/snbvop.usd"),
            visual_material_path="materials",
            scale=(1.7000177100490061, 2.475762353846898, 1.574803204017664),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    loudspeakerSnbvop2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/loudspeakerSnbvop2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.492283344268799, 12.314827919006348, 0.35201534628868103),
            rot=(0.7098636627197266, -9.578652679920197e-07, -4.530520527623594e-07, 0.7043392062187195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/loudspeaker/snbvop/usd/snbvop.usd"),
            visual_material_path="materials",
            scale=(1.7000177100490061, 2.475762353846898, 1.574803204017664),
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
            pos=(-2.007308006286621, -6.179296493530273, 0.5299682021141052),
            rot=(0.14995789527893066, -4.7501176595687866e-05, 8.024199632927775e-05, 0.9886924028396606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(1.1995731048362237, 1.2220379784337254, 1.2667396457758693),
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
            pos=(4.968170642852783, 5.753507614135742, 0.5448533296585083),
            rot=(-0.022371411323547363, 1.862645149230957e-09, 0.0, 0.9997498393058777),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.5978462355066425, 1.4668649150951656, 1.3731451582969099),
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
            pos=(4.344651222229004, 7.368102550506592, 0.5448530316352844),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.5978462355066425, 1.4668649150951656, 1.3731451582969099),
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
            pos=(5.0646514892578125, 7.368102550506592, 0.5448530316352844),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.5978462355066425, 1.4668649150951656, 1.3731451582969099),
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
            pos=(5.808023452758789, 6.5481696128845215, 0.5448530316352844),
            rot=(0.7227487564086914, 2.7939677238464355e-09, 2.60770320892334e-08, -0.6911109685897827),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.5978462355066425, 1.4668649150951656, 1.3731451582969099),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.5118966102600098, 6.624989032745361, 0.5448530316352844),
            rot=(0.7089948058128357, 1.955777406692505e-08, 6.984919309616089e-09, 0.7052137851715088),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.5978462355066425, 1.4668649150951656, 1.3731451582969099),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.266189098358154, 5.783994197845459, 0.5448533296585083),
            rot=(-0.0066663287580013275, 0.0, -1.0302755981683731e-08, 0.9999778866767883),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.5978462355066425, 1.4668649150951656, 1.3731451582969099),
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
            pos=(2.851747512817383, 10.814560890197754, 0.43336305022239685),
            rot=(0.711353063583374, -0.0007402617484331131, 0.00036851782351732254, -0.70283442735672),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.1557544709013692, 1.1757083002829676, 1.1407194988476557),
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
            pos=(2.1653926372528076, 11.541752815246582, 0.4333648979663849),
            rot=(0.9999998211860657, -0.0007935817120596766, -0.00026869215071201324, 2.9001384973526e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.1557544709013692, 1.1757083002829676, 1.1407194988476557),
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
            pos=(1.3882070779800415, 10.815618515014648, 0.4333652853965759),
            rot=(0.6822708249092102, -0.0003528906963765621, -0.0007646158337593079, 0.731099009513855),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.1557544709013692, 1.1757083002829676, 1.1407194988476557),
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
            pos=(2.1150197982788086, 10.138264656066895, 0.4333653450012207),
            rot=(0.06337594985961914, 0.00021258369088172913, -0.0008155786199495196, 0.9979894161224365),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/psoizi/usd/psoizi.usd"),
            visual_material_path="materials",
            scale=(1.1557544709013692, 1.1757083002829676, 1.1407194988476557),
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
            pos=(-3.845784902572632, -5.937966346740723, 0.44241446256637573),
            rot=(-0.6633721590042114, 0.0022365739569067955, -0.0016850181855261326, 0.7482845187187195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/qtqitn/usd/qtqitn.usd"),
            visual_material_path="materials",
            scale=(0.8136931204085672, 0.7968671882775256, 0.8498210481907039),
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
            pos=(-1.3738200664520264, -6.44369649887085, 0.8758530616760254),
            rot=(-0.01041509211063385, 0.0, 2.9103830456733704e-11, 0.9999457597732544),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.5499653796762862, 1.575859757301767, 1.644819105388792),
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
            pos=(-4.429662704467773, -5.504913330078125, 0.9917618632316589),
            rot=(0.9999999403953552, 0.00020947329176124185, 0.00027337754727341235, -0.0003508083173073828),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.9025091989867307, 1.8342980299185432, 1.644819105388792),
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
            pos=(-4.269992351531982, -0.6297195553779602, 0.89057457447052),
            rot=(0.9999997019767761, 0.0001481162034906447, 0.0002188230282627046, -0.0008772657020017505),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.3102871563322736, 2.4459580049508602, 1.644819105388792),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedSmmmaf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedSmmmaf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2248273121586254, -5.487498520949624, 0.18813612174575556),
            rot=(-0.7033641878989774, 0.0, 0.0, 0.7108296695982885),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/smmmaf/usd/smmmaf.usd"),
            visual_material_path="materials",
            scale=(1.0033682994109099, 0.6585675038174735, 0.7763779279783489),
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
            pos=(6.1494245529174805, 8.5556001663208, 0.6068630218505859),
            rot=(1.9371509552001953e-07, 0.0, -1.1641532182693481e-10, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.9925572600861525, 1.6524009017727945, 2.183714286844538),
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
            pos=(-2.8200631141662598, -4.386989593505859, 0.9713040590286255),
            rot=(0.7071069478988647, 2.2737367544323206e-12, -1.0504663805477321e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/dajebq/usd/dajebq.usd"),
            visual_material_path="materials",
            scale=(1.9177492393061693, 1.4542171094787475, 2.139217016161698),
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
            pos=(-1.0674058198928833, -2.2499802112579346, 0.37272006273269653),
            rot=(-0.7069947719573975, -4.656612873077393e-10, 1.2350938050076365e-09, 0.7072187066078186),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(2.333383113127667, 1.9647934557718905, 1.9741444725877089),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetLwjdmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetLwjdmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.724429130554199, 4.956909656524658, 1.1803405284881592),
            rot=(0.001519635901786387, 0.0, -1.4406396076083183e-09, 0.9999989867210388),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/lwjdmj/usd/lwjdmj.usd"),
            visual_material_path="materials",
            scale=(2.8684402480243234, 1.9334808537250916, 2.2699036599948883),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetLwjdmj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetLwjdmj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.5186381340026855, 11.14521312713623, 1.1803406476974487),
            rot=(0.705676257610321, 0.0, 4.4065018300898373e-10, 0.7085344791412354),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/lwjdmj/usd/lwjdmj.usd"),
            visual_material_path="materials",
            scale=(3.2946216368134804, 0.7382766060722724, 2.2699036599948883),
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
            pos=(6.695128917694092, 8.58330249786377, 0.47712892293930054),
            rot=(1.9418075680732727e-07, 0.0, 3.205059329047799e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/bmsclc/usd/bmsclc.usd"),
            visual_material_path="materials",
            scale=(1.2117964417340539, 1.5623300484262697, 1.4873191692003036),
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
            pos=(6.564576625823975, 12.528535842895508, 0.47521352767944336),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.2004758273642693, 1.6060407453033003, 1.44663790212104),
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
            pos=(4.419398307800293, 12.522662162780762, 0.47521352767944336),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.7072187389152302, 1.5839645838558323, 1.44663790212104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQohxjq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQohxjq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.319511413574219, 10.38654899597168, 0.47521352767944336),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.3871987030490989, 0.9238873565765376, 1.44663790212104),
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
            pos=(4.52999316406, 6.60332250977, 0.0023727299550000006),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.540420227489384, 3.0365863025849826, 0.24480330607770978),
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
            pos=(-3.163034423830473, -1.6912098999025114, 0.0023727299550000006),
            rot=(0.7050837151982163, 0.0, 0.0, 0.7091240755765387),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.9434330517061315, 0.8375323337647924, 0.24480330607770978),
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
            pos=(-2.470004089355, 6.198726074214998, 0.002372729955),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.4656396132501415, 2.306274603024269, 0.24480330607770978),
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
            pos=(-2.1650069274950003, 11.293436523439999, 0.002372729955),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.516011948311385, 2.8316814848151686, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeMakerPyttso0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeMakerPyttso0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.330059051513672, 12.628690719604492, 1.0708982944488525),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_maker/pyttso/usd/pyttso.usd"),
            visual_material_path="materials",
            scale=(1.7316389585835168, 2.445385446680932, 1.2223324079135705),
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
            pos=(4.424998291015, 12.464222656255, 0.910315490725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.6344737205800696, 1.3005092855973577, 0.5858268216935112),
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
            pos=(6.584995117189999, 12.459234375000001, 0.910315490725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.5714507271642146, 1.2825588468727565, 0.5858268216935112),
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
            pos=(7.094392578130001, 11.58000195312992, 0.9103154907250001),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.9956176112172977, 1.0154563186506904, 0.5858268216935112),
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
            pos=(7.1094133751238, 9.18000325351292, 0.9103154907250001),
            rot=(0.7079857008022238, 0.0, 0.0, -0.7062267677308642),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.7204507275843453, 0.9824275113974242, 0.5858268216935112),
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
            pos=(6.734999267579999, 8.65424462891, 0.910315490725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.22447897566580766, 1.2647879125354013, 0.5858268216935112),
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
            pos=(5.34999829102, 10.599020996095, 0.9103154907250001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5661412630943592, 1.6388750555560905, 0.5858268216935112),
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
            pos=(4.19499829102, 10.599020996095, 0.910315490725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5563515127382402, 1.6388750555560905, 0.5858268216935112),
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
            pos=(4.77999829102, 10.814479003905001, 0.910315490725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5661412630943592, 0.8729298351773569, 0.5858268216935112),
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
            pos=(6.052809715270996, 12.517958641052246, 0.4602763056755066),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/dngvvi/usd/dngvvi.usd"),
            visual_material_path="materials",
            scale=(1.0858215253991117, 1.2417255872159843, 1.2446790448194136),
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
            pos=(0.04448249936103821, -0.7569488883018494, 1.1368623971939087),
            rot=(0.0010226527228951454, 0.0, -2.1373125491663814e-11, 0.9999995231628418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(6.450810465151496, 9.64065783503957, 5.30375420379901),
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
            pos=(1.2803436517715454, 1.9944159984588623, 1.1368625164031982),
            rot=(0.7075935006141663, 0.0, 4.347384674474597e-10, -0.7066197395324707),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(6.143482374440153, 5.654974524562862, 5.30375420379901),
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
            pos=(-3.615593671798706, -3.499911069869995, 1.1510995626449585),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.9640048045046745, 4.575518627975419, 4.527199682615753),
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
            pos=(1.8844537734985352, 9.120067596435547, 1.1510995626449585),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6468206645382772, 3.4302073318614217, 4.527199682615753),
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
            pos=(-1.655593752861023, -0.049933310598134995, 1.1510995626449585),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.9640048045046745, 3.4302073318614217, 4.527199682615753),
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
            pos=(-3.509342670440674, -0.05006822571158409, 1.1510995626449585),
            rot=(0.0013926781248301268, 0.0, 1.5774048733874224e-12, 0.9999991655349731),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.698887742790718, 3.4302073318614217, 4.527199682615753),
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
            pos=(-2.155052423477173, 0.5539240837097168, 1.1510995626449585),
            rot=(0.7086573243141174, 0.0, 1.212363542890671e-11, 0.7055529356002808),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.698887742790718, 2.5740871380162087, 4.527199682615753),
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
            pos=(-1.6993422508239746, 1.159942865371704, 1.1510995626449585),
            rot=(0.001392678008414805, -2.9103830456733704e-11, -1.4210854715202004e-14, 0.9999991059303284),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.698887742790718, 2.860414962044708, 4.527199682615753),
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
            pos=(2.9793148040771484, 12.970986366271973, 0.9860121011734009),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.2092265801656117, 5.100339025608655, 2.8287788690487865),
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
            pos=(6.894611835479736, 6.435593128204346, 1.0846130847930908),
            rot=(-0.7066790461540222, 0.0, 0.0, 0.7075343132019043),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.0271314259696025, 3.684699420422759, 3.111699687792625),
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
            pos=(1.4025909750485082, 8.956246635007258, 1.200281898479443),
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

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1968631264651255, 2.5773622526908206, 1.200281898479443),
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

    electricSwitchWseglt10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1968670327664916, 8.944669380622742, 1.200281898479443),
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

    electricSwitchWseglt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.4594413534978408, 9.193132601035325, 1.200281898479443),
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

    electricSwitchWseglt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1781677946808207, -3.5831329709314503, 1.2002818990966122),
            rot=(0.9999999999999869, -1.6186804311275753e-07, 0.0, 0.0),
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
            pos=(-4.074628365970821, -3.583132974996026, 1.200281899856334),
            rot=(0.9999999999999378, -3.5262583393451713e-07, 0.0, 0.0),
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
            pos=(-2.121624215580821, -0.11313295583987439, 1.200281898479443),
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
            pos=(-3.0431346762698746, 0.1311874518158206, 1.200281898479443),
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

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.284107717844936, 0.013127087413753284, 1.200281898479443),
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
            pos=(-1.1531329672848745, 1.2993511442908205, 1.200281898479443),
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

    electricSwitchWseglt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.533133704125401, 7.316985404537291, 1.3803873680385639),
            rot=(0.7071066023725722, -1.475139325138769e-07, -1.4751400350965183e-07, 0.7071069600004469),
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
            pos=(1.1968670327664914, 5.473797798587742, 1.200281898479443),
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

    fridgeDszchb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeDszchb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.140077114105225, 8.594399452209473, 1.0103967189788818),
            rot=(0.0010572236496955156, 1.1641532182693481e-10, 1.4640590961789712e-09, 0.9999995231628418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/dszchb/usd/dszchb.usd"),
            visual_material_path="materials",
            scale=(1.839193585670747, 1.2707085691305042, 1.1809830968276134),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    grandfatherClockVeyqcp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/grandfatherClockVeyqcp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.8518180146478331, 1.5880838826626082, 0.9487561260466251),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grandfather_clock/veyqcp/usd/veyqcp.usd"),
            visual_material_path="materials",
            scale=(2.15902423622259, 1.276887495270831, 2.173943088912519),
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
            pos=(6.149538993835449, 8.469914436340332, 1.4111589193344116),
            rot=(-0.002747371792793274, -7.450580596923828e-09, -1.3969838619232178e-09, 0.9999964237213135),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/microwave/bfbeeb/usd/bfbeeb.usd"),
            visual_material_path="materials",
            scale=(1.7324747673716263, 1.6119675235197675, 1.319281416095561),
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
            pos=(4.844999755859037, 8.06987768555, 1.749999778780986),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.9137783584360184, 3.5164131688274387, 1.9000151504591616),
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
            pos=(-4.567683658865295, 0.5422518089176575, 1.5999998377330262),
            rot=(0.7041910745772442, 0.0, 0.0, 0.7100105143487287),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.6657659419445106, 4.349490110656976, 1.7273501146886807),
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
            pos=(-1.5850001831053055, 2.61087805176, 1.5499998356479583),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(0.9247257686535058, 3.5164131688274387, 1.5545101396722316),
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
            pos=(1.1696583862300005, 0.5400001200374992, 1.4999997461830266),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.4133294523177589, 2.637309876620579, 1.7273501146886807),
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
            pos=(-4.718611816409997, 6.322308105469058, 1.7499997787809858),
            rot=(0.7057244824942753, 0.0, 0.0, 0.7084863829377297),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.852025010661768, 8.758814476804472, 1.9000151504591616),
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
            pos=(4.1019110679626465, 8.657806396484375, 0.3769833445549011),
            rot=(1.9470462575554848e-07, 2.3283064365386963e-10, 3.3032847568392754e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/fexqbj/usd/fexqbj.usd"),
            visual_material_path="materials",
            scale=(1.6319631159552745, 1.4243321811828336, 1.3815278544094567),
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
            pos=(4.089991569519043, 8.657806396484375, 1.1279778480529785),
            rot=(1.94646418094635e-07, 0.0, -5.1513779908418655e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/fexqbj/usd/fexqbj.usd"),
            visual_material_path="materials",
            scale=(1.6319631159552745, 1.4243321811828336, 1.377792985919569),
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
            pos=(1.1882843402211245, 3.4499999943802178, 1.5004088066927728),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fanvpf/usd/fanvpf.usd"),
            visual_material_path="materials",
            scale=(1.178483091445834, 1.1028412941285772, 2.158137953769703),
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
            pos=(-4.611903431033805, 9.400090930283856, 1.600163357807165),
            rot=(0.7119662827190048, 0.0, 0.0, 0.7022136514418402),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/gwricv/usd/gwricv.usd"),
            visual_material_path="materials",
            scale=(1.0039416090824753, 1.1028412941285772, 0.8633980072832057),
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
            pos=(3.2350045740063997, 4.772827262671024, 1.7001633958491043),
            rot=(0.001250223015479598, 0.0, 0.0, 0.9999992184709006),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/lucjyq/usd/lucjyq.usd"),
            visual_material_path="materials",
            scale=(1.2658267405148829, 1.1028412941285772, 0.5763012290232217),
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
            pos=(-2.490000698750804, 2.6408246774838897, 1.520097992529417),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qjkajj/usd/qjkajj.usd"),
            visual_material_path="materials",
            scale=(0.4655897687436955, 1.1028412941285772, 0.5179513495198568),
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
            pos=(-2.5800000832878847, -0.12271082104118305, 1.6001633999170788),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qtvjzk/usd/qtvjzk.usd"),
            visual_material_path="materials",
            scale=(0.843835888418342, 1.1028412941285772, 0.92208183810604),
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
            pos=(1.1882969571475341, 4.789999625150099, 1.5004083107968182),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/szpupz/usd/szpupz.usd"),
            visual_material_path="materials",
            scale=(1.178483091445834, 1.1028412941285772, 2.5609485439513815),
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
            pos=(-3.40999988877437, 4.251702375205235, 1.6001634514459673),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/weqggl/usd/weqggl.usd"),
            visual_material_path="materials",
            scale=(1.134884174798679, 1.1028412941285772, 1.0244782873598215),
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
            pos=(-3.0517151493001746, 0.9325000286863829, 1.4901306817011797),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/wfdvzv/usd/wfdvzv.usd"),
            visual_material_path="materials",
            scale=(0.6038231231968817, 1.1028412941285772, 0.6915177692197941),
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
            pos=(7.08039665222168, 10.559223175048828, 1.8353886604309082),
            rot=(0.7088465094566345, -3.725290298461914e-09, 1.6370904631912708e-09, -0.7053629159927368),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/range_hood/iqbpie/usd/iqbpie.usd"),
            visual_material_path="materials",
            scale=(1.4462622669733212, 1.330792717788517, 0.6387391789323882),
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
            pos=(4.215027709964972, 10.343265818854158, 0.43655594484039595),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(0.9746481357216122, 1.7826937885383547, 2.036814882126215),
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
            pos=(-3.826922063873549, 2.3672236399631825, 1.2098174125871806),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.8540123634642, 0.8547716426760182, 1.1653542935171972),
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
            pos=(5.246823787689209, 12.472125053405762, 0.4877564311027527),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/czyfhq/usd/czyfhq.usd"),
            visual_material_path="materials",
            scale=(6.9999016509029035, 5.173165477303487, 4.931451850023588),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkCzyfhq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkCzyfhq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.762884140014648, 10.357072830200195, 0.4877564311027527),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/czyfhq/usd/czyfhq.usd"),
            visual_material_path="materials",
            scale=(3.7801149899862887, 3.0177996442341404, 4.931451850023588),
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
            pos=(-1.5849945545196533, 2.3858706951141357, 0.4614204466342926),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.160535853317268, 3.446624811473869, 4.481572962832644),
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
            pos=(-4.284749507904053, 0.5530683398246765, 0.49483248591423035),
            rot=(0.7085028290748596, 0.0, -1.074795363820158e-09, 0.7057080864906311),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(3.6297822254040324, 4.284218091536991, 4.9205786442908765),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaQnnwfx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaQnnwfx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.1864834942866365, -1.7510816735113688, 0.34907350546353655),
            rot=(0.7050837151982163, 0.0, 0.0, 0.7091240755765387),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/qnnwfx/usd/qnnwfx.usd"),
            visual_material_path="materials",
            scale=(0.836833385060868, 1.132560544833282, 1.0061117499547307),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    stoveIgwqpj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/stoveIgwqpj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.110574245452881, 10.571812629699707, 0.47597044706344604),
            rot=(0.7078554630279541, 0.0, 5.762558430433273e-09, -0.706357479095459),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stove/igwqpj/usd/igwqpj.usd"),
            visual_material_path="materials",
            scale=(1.2937007461140237, 1.4798230606690974, 1.516788059799252),
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
            pos=(-4.293049335479736, 1.5119010210037231, 0.3086572587490082),
            rot=(0.7048937678337097, -2.0256265997886658e-08, -1.6996636986732483e-08, 0.7093130946159363),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.2238775864957843, 1.195473507603933, 1.1551359314283232),
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
            pos=(-2.4943623542785645, 2.334923267364502, 0.3086572587490082),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.2178965109356341, 1.1669033086027447, 1.1551359314283232),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetEobsmt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetEobsmt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.877038955688477, 8.424910545349121, 1.8518542051315308),
            rot=(1.94646418094635e-07, 2.3283064365386963e-10, 2.9103830456733704e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/eobsmt/usd/eobsmt.usd"),
            visual_material_path="materials",
            scale=(1.6842915301356605, 1.2408137542813953, 1.4256870684209964),
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
            pos=(6.406895160675049, 12.707901954650879, 1.8488599061965942),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.3165916383992973, 1.5782400299911667, 2.2084445086090536),
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
            pos=(7.293971538543701, 11.78067398071289, 1.8488599061965942),
            rot=(0.7071069478988647, 1.0186340659856796e-10, 5.093170329928398e-11, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.3254389941829796, 1.2666794321044328, 2.2084445086090536),
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
            pos=(7.293971538543701, 9.380674362182617, 1.8488599061965942),
            rot=(0.7071069478988647, 1.0186340659856796e-10, 5.093170329928398e-11, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(2.3254389941829796, 1.2666794321044328, 2.2084445086090536),
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
            pos=(4.102437973022461, 8.553910255432129, 1.8999888896942139),
            rot=(1.9371509552001953e-07, 0.0, -5.238689482212067e-10, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/jvdbxh/usd/jvdbxh.usd"),
            visual_material_path="materials",
            scale=(1.5915953252501542, 3.033518557795917, 1.9579831599878172),
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
            pos=(7.281961917877197, 10.561826705932617, 2.1999270915985107),
            rot=(-0.7052923440933228, -1.1459633242338896e-10, -1.000444171950221e-10, 0.7089166045188904),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.8359525397215788, 1.3718645678645218, 0.9789973896575583),
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
            pos=(5.13069486618042, 8.561745643615723, 2.149890661239624),
            rot=(0.0010572238825261593, 0.0, -1.0371081771154422e-10, 0.9999995231628418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.940702337670227, 3.3363122518763966, 1.4684960844863375),
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
            pos=(6.15111780166626, 8.552891731262207, 1.949744701385498),
            rot=(1.94646418094635e-07, 0.0, -1.0186340659856796e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.588941191856185, 3.244479195865257, 3.426490863801454),
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
            pos=(-3.072041899519665, 0.9499990207306087, 1.3150314907033125),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.8756511072355757, 1.0325864343157334, 0.4668082200873506),
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
            pos=(-1.1881506630162508, 1.7875128827231934, 1.3150314907033123),
            rot=(-0.7028343649539913, 0.0, 0.0, 0.7113535375885325),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.2327817119884668, 1.1193584035859632, 0.4668082200873506),
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
            pos=(-3.287278413772583, -6.699953556060791, 1.4718577861785889),
            rot=(-0.002915335353463888, 0.0, -8.128608897095546e-11, 0.9999958872795105),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.748343787279471, 2.278619110582054, 1.6189770615270167),
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
            pos=(-0.7272784113883972, -6.699953556060791, 1.4718577861785889),
            rot=(-0.002915335353463888, 0.0, -8.128608897095546e-11, 0.9999958872795105),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.748343787279471, 2.278619110582054, 1.6189770615270167),
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
            pos=(0.9385398626327515, -0.7993060350418091, 1.0718578100204468),
            rot=(1.9470462575554848e-07, 0.0, 7.401013135677204e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.6736841968902277, 4.076317547638816, 1.6189770615270167),
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
            pos=(-3.6296651363372803, 13.727662086486816, 1.374772548675537),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.4840778444095883, 3.356753617981325, 1.8348697755902836),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.24033498764038086, 13.727662086486816, 1.374772548675537),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.4840778444095883, 3.356753617981325, 1.8348697755902836),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.749415636062622, 13.727662086486816, 1.374772548675537),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.619078406664788, 3.356753617981325, 1.8348697755902836),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.157429218292236, 12.934928894042969, 1.7145724296569824),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.2720845593244126, 2.1586917889724724, 1.079354423342592),
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
            pos=(-2.037278175354004, -6.699953079223633, 1.4718577861785889),
            rot=(-0.002915335353463888, 0.0, -8.128608897095546e-11, 0.9999958872795105),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.748343787279471, 2.278619110582054, 1.6189770615270167),
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
            pos=(0.35455700755119324, -5.618524074554443, 1.4718577861785889),
            rot=(-0.7059988379478455, 0.0, 2.3936763682286255e-10, 0.708213210105896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.9850571374099143, 1.9188371457533089, 1.6189770615270167),
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
            pos=(-4.709654331207275, 12.92101001739502, 1.374772548675537),
            rot=(0.7071069478988647, 0.0, 6.292566467891447e-11, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.340751406672379, 2.0387644673628906, 1.8348697755902836),
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
            pos=(-4.709654808044434, 7.731010913848877, 1.374772548675537),
            rot=(0.7071069478988647, 0.0, 6.292566467891447e-11, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.340751406672379, 2.0387644673628906, 1.8348697755902836),
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
            pos=(-4.709654331207275, 4.801011085510254, 1.374772548675537),
            rot=(0.7071069478988647, 0.0, 6.292566467891447e-11, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.340751406672379, 2.0387644673628906, 1.8348697755902836),
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
            pos=(-4.709532737731934, 1.3941045999526978, 1.8145723342895508),
            rot=(0.7061959505081177, 1.862645149230957e-09, -5.451283868751489e-10, 0.7080166935920715),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.8271233885095921, 2.0387644673628906, 1.079354423342592),
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
            pos=(-4.709810733795166, -1.9151115417480469, 1.4718577861785889),
            rot=(0.7075098752975464, 0.0, -1.022669948724797e-09, 0.7067035436630249),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.399219646337937, 2.0387644673628906, 1.6189770615270167),
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
            pos=(-0.7890772819519043, -2.1985280513763428, 1.4718577861785889),
            rot=(-0.7059987783432007, 0.0, 1.4568968254025094e-10, 0.7082130908966064),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.9850571374099143, 2.5172623667142524, 1.6189770615270167),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
