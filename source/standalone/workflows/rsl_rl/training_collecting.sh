# tmux new -s exp
# conda activate Orbit
# ./source/standalone/workflows/rsl_rl/training_collecting.sh > training_collecting.log 2>&1
# ps: 记得检查play, 检查生成数据和qpos差值，改回一倍速，
python source/standalone/workflows/rsl_rl/train.py --task Isaac-Lift-Cube-MobileAloha-IK-Abs-v0 --headless --num_envs 4096
python source/standalone/workflows/rsl_rl/play.py --task Isaac-Lift-Cube-MobileAloha-IK-Abs-Play-v0  --num_envs 6
conda deactivate 
conda activate act
cd $HOME/RL/0projects/low-level-ACT
python aloha-devel/act/train.py --batch_size 32 --num_epochs 2000 --lr 7e-5  --enc_layers 2 --dec_layers 4 --hidden_dim 256 --dim_feedforward 1024  --chunk_size 30
python source/standalone/workflows/rsl_rl/student_inference_orbit.py --task Isaac-Lift-Cube-MobileAloha-Room-v0 --ckpt_dir /home/thk/RL/0projects/low-level-thk/ckpt/2024-08-07_15-13-32RNN --policy_class RNN --ckpt_name policy_best.ckpt 
python source/standalone/workflows/rsl_rl/student_inference_orbit.py --task Isaac-Lift-Cube-MobileAloha-Room-v0 --ckpt_dir /home/thk/RL/0projects/low-level-thk/ckpt/2024-07-08_12-24-14FCNet --policy_class FCNet --ckpt_name policy_best.ckpt 