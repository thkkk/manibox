# ManiBox: Enhancing Spatial Grasping Generalization via Scalable Simulation Data Generation

- [Paper](https://arxiv.org/pdf/2411.01850)
- [Project Page](https://thkkk.github.io/manibox)
- Other Contributors: [Xuezhou Xu](https://github.com/xuxuezhou), [Chengyang Ying](https://github.com/yingchengyang), [Xinyi Mao](https://github.com/shhmxy2)

The code will be updated within a week. TODO:
- more policies
- data generation in simulator

## Installation Instructions

```bash
conda deactivate
conda create -n manibox python=3.9
conda activate manibox

pip install -e .

# for student inference code, you should install these in `isaac lab conda env`:
pip install einops
```

## Teacher Policy Training Instructions
```bash

# PPO Training
python source/standalone/workflows/rsl_rl/train.py --task Isaac-Lift-Cube-MobileAloha-v0  --num_envs 4096  --headless
```

## Data Collection Instructions
```bash

# Collect data in simulator
python source/standalone/workflows/rsl_rl/play_collect_data.py --task Isaac-Lift-Cube-MobileAloha-Play-v0 \
--num_envs 40  --load_run  2024-09-12_17-42-24 --headless --enable_cameras
```

## Simulator Inference Instruction
```bash

# Student policy inference in simulator
python source/standalone/workflows/rsl_rl/student_inference_orbit_multi_envs.py --task Isaac-Lift-Cube-MobileAloha-Play-v0 \
--ckpt_dir "\PATH\TO\Your\CKPT" --policy_class "RNN" --ckpt_name policy_best.ckpt --nheads 48 --num_train_step 38000 --seed 0
```

## Training Instructions
```bash

# BBOX RNN
python ManiBox/train.py --policy_class RNN --batch_size 128 --dataset ../ --num_episodes 38000  --loss_function l1  --rnn_layers 3 --rnn_hidden_dim 512 --actor_hidden_dim 512 --num_epochs 50 --lr 2e-3 --gradient_accumulation_steps 1 > train.log 2>&1
```

## Deployment Instructions

```bash
python VFCNet/inference_real_world.py  --ckpt_dir /PATH/TO/ManiBox/ckpt/2024-xx-xx_xx-xx-xxRNN --policy_class RNN --ckpt_name policy_best.ckpt
```

## Acknowledgement

- [cobot magic](https://github.com/agilexrobotics/cobot_magic)
- [mobile aloha](https://github.com/MarkFzp/mobile-aloha)

## BibTeX
If you find our work useful for your project, please consider citing the following paper.

```
@article{tan2024manibox,
  title={ManiBox: Enhancing Spatial Grasping Generalization via Scalable Simulation Data Generation},
  author={Tan, Hengkai and Xu, Xuezhou and Ying, Chengyang and Mao, Xinyi and Liu, Songming and Zhang, Xingxing and Su, Hang and Zhu, Jun},
  journal={arXiv preprint arXiv:2411.01850},
  year={2024}
}
```