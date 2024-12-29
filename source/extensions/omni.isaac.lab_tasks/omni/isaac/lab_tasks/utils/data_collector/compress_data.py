import h5py
import fnmatch
import os
import cv2
import numpy as np
import argparse
import os


def compress_single_hdf5(dataset_dir, output_dir, filename, args):
    base_action_t265 = None
    # for root, dirs, files in os.walk(dataset_dir):
        # for filename in fnmatch.filter(files, '*.hdf5'):
    print(f"Processing {filename}...")
    with h5py.File(os.path.join(dataset_dir, filename), 'a') as f:
        action = f['action'][:]
        base_action = f['base_action'][:]
        if 'base_action_t265' in f:
            base_action_t265 = f['base_action_t265'][:]
        else:
            base_action_t265 = None
        qpos = f['observations']['qpos'][:]
        qvel = f['observations']['qvel'][:]
        effort = f['observations']['effort'][:]
        cam_high = [cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() for img in f['observations']['images']['cam_high'][:]]
        cam_left_wrist = [cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() for img in f['observations']['images']['cam_left_wrist'][:]]
        cam_right_wrist = [cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() for img in f['observations']['images']['cam_right_wrist'][:]]
        if args.use_depth_image:
            try:
                cam_high_depth = [cv2.imencode('.tif', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() for img in f['observations']['images_depth']['cam_high'][:]]
                cam_left_wrist_depth = [cv2.imencode('.tif', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() for img in f['observations']['images_depth']['cam_left_wrist'][:]]
                cam_right_wrist_depth = [cv2.imencode('.tif', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes() for img in f['observations']['images_depth']['cam_right_wrist'][:]]
            except KeyError:
                cam_high_depth = None
                cam_left_wrist_depth = None
                cam_right_wrist_depth = None
                print("No depth images found in the dataset")
        else:
            cam_high_depth = None
            cam_left_wrist_depth = None
            cam_right_wrist_depth = None
            print("Depth images not saved")

    # if new file already exists, delete the old one
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    new_file_path = os.path.join(output_dir, filename)
    if os.path.exists(new_file_path):
        os.remove(new_file_path)

    with h5py.File(new_file_path, 'a') as f_new:
        f_new.attrs['sim'] = False
        f_new.attrs['compress'] = True
        
        f_new.create_dataset('action', data=action)
        f_new.create_dataset('base_action', data=base_action)
        if base_action_t265 is not None:
            f_new.create_dataset('base_action_t265', data=base_action_t265)
        f_new.create_dataset('observations/qpos', data=qpos)
        f_new.create_dataset('observations/qvel', data=qvel)
        f_new.create_dataset('observations/effort', data=effort)
        f_new.create_dataset('observations/images/cam_high', data=np.bytes_(cam_high))
        f_new.create_dataset('observations/images/cam_left_wrist', data=np.bytes_(cam_left_wrist))
        f_new.create_dataset('observations/images/cam_right_wrist', data=np.bytes_(cam_right_wrist))
        if cam_high_depth is not None:
            f_new.create_dataset('observations/images_depth/cam_high', data=np.bytes_(cam_high_depth))
            f_new.create_dataset('observations/images_depth/cam_left_wrist', data=np.bytes_(cam_left_wrist_depth))
            f_new.create_dataset('observations/images_depth/cam_right_wrist', data=np.bytes_(cam_right_wrist_depth))
        
    print(f"Processed {filename}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress the images in the collected urdf5.')
    parser.add_argument('--input_dir', type=str, help='The directory of the input raw dataset', required=True)
    parser.add_argument('--output_dir', type=str, help='The directory of the output dataset', required=True)
    parser.add_argument('--annotation_file', type=str, help='The annotation file for the dataset, whose format is "<task_name> <num_episodes> <instr>\\n"', required=True)

    # Whether to save depth
    parser.add_argument('--depth', action='store_true', help='Whether to save depth images', default=False)
    
    args = parser.parse_args()

    # Split annotation file content to get (task_name, instr)
    pairs = []
    with open(args.annotation_file, "r") as file:
        for line in file.readlines():
            split_result = line.split(maxsplit=2)
            if len(split_result) < 3:
                continue
            task_name, _, instr = split_result
            pairs.append((task_name, instr.strip()))

    for task_name, instr in pairs:
        print(f'Processing {task_name} with instruction "{instr}"')
        input_dir = os.path.join(args.input_dir, task_name)
        output_dir = os.path.join(args.output_dir, task_name)
        # convert instruction to bytes
        instruction = instr.encode()
        
        find_all_hdf5(input_dir, output_dir, instruction)
        print(f"Processed {task_name}")
