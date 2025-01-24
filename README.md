# ManiBox

**Note**: The sim branch is developed based on Isaac lab, which is equivalent to another version of Isaac lab. Since the sim branch depends on `yolo_process_data`` in manibox, you should not switch the manibox repository to the sim branch directly, but **clone the sim branch to another folder and install the sim code separately**.
So in total there will be two conda environments:
- **Student policy environment**: containing the main branch of manibox repo (ManiBox package), used for student policy training and real robot deployment.
- **Simulator environment**: the sim branch of manibox repo (Isaac Lab replacement) with manibox main branch. It is used for reinforcement learning and simulator data generation.

The usd and urdf files required for the sim branch are shown in: [manibox-sim-usd-urdf.zip](manibox-sim-usd-urdf.zip).

## Installation
```bash
conda activate isaaclab
pip install dm_env
pip install einops
pip install -e .

```

## Code Position
```bash
# Lift Task Setting  
source/extensions/omni.isaac.lab_tasks/omni/isaac/lab_tasks/manager_based/manipulation/lift/config/mobile_aloha

# Data Collection Code  
source/extensions/omni.isaac.lab_tasks/omni/isaac/lab_tasks/utils/data_collector

# Auxiliary and Special Inference Code  
source/standalone/workflows/rsl_rl

# Robot-Related Code Definition
source/extensions/omni.isaac.lab_assets/omni/isaac/lab_assets/mobile_aloha.py

```
## Instructions

### Teacher Policy Training Instructions
```bash

# PPO Training
python source/standalone/workflows/rsl_rl/train.py --task Isaac-Lift-Cube-MobileAloha-v0  --num_envs 4096  --headless
```

### Data Collection Instructions 
```bash
# Collect data in simulator
python source/standalone/workflows/rsl_rl/play_collect_data.py --task Isaac-Lift-Cube-MobileAloha-Play-v0 \
--num_envs 40  --load_run  2024-09-12_17-42-24 --headless --enable_cameras
```

### Simulator Inference Instruction

```bash
# Student policy inference in simulator
python source/standalone/workflows/rsl_rl/student_inference_orbit_multi_envs.py --task Isaac-Lift-Cube-MobileAloha-Play-v0 \
--ckpt_dir "\PATH\TO\Your\CKPT" --policy_class "RNN" --ckpt_name policy_best.ckpt --nheads 48 --num_train_step 38000 --seed 0

```