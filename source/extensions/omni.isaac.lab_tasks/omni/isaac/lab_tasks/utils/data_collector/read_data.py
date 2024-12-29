import os
home_path = os.environ['HOME']
# file_path = 'real_robot_episode_0.hdf5'  # real-world
# 指定文件路径
# file_path = f'{home_path}/code/GES-low-level-Orbit/data/mobile_aloha/episode_1.hdf5'
file_path = f'{home_path}/RL/0projects/GES-low-level-IsaacLab/data/mobile_aloha/episode_10.hdf5'
# file_path = f'{home_path}/RL/0projects/GES-low-level-IsaacLab/data/mobile_aloha/episode_10.hdf5'
import h5py
import numpy as np
import torch
import matplotlib.pyplot as plt   
import imageio 
import os
import pandas as pd



# 指定hdf5文件路径
# file_path = '/home/xuxuezhou/Downloads/episode_0.hdf5'
# file_path = '/home/xuxuezhou/code/GES-low-level-Orbit/data/mobile_aloha/episode_0.hdf5'
# file_path = '/home/xuxuezhou/Downloads/episode_0(1).hdf5'
# file_path = '/home/xuxuezhou/Downloads/mobile_aloha.hdf5'

video_output_path = f'{home_path}/Videos/'

import cv2
import h5py
import numpy as np
import torch
from PIL import Image
import zlib
import sys


def check_image(observations, name, is_compress):
    print(f"Checking image data for '{name}'")
    output_path = video_output_path
    video_data = observations['images'][name]  
    height, width = 480, 640  # Make sure this matches the dimensions of video_data frames
    # read the first frame
    frame: np.ndarray = video_data[10]  # type: np.ndarray, shape: (480, 640, 3)
    # print(f"Data shape: {data.shape}, data: {data}")
    # if frame.shape[1:3] != (width, height):
    #     frame = cv2.resize(frame, (width, height))
    # if frame.shape[2] == 3:  # Assuming the frame is in RGB
    #     frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    img = frame

    # # 将numpy数组转换为PIL图像
    # img = Image.fromarray(frame, 'RGB')

    # # 保存原始图像
    Image.fromarray(frame, 'RGB').save(f'{output_path}original_image.jpg', 'JPEG')

    # # 保存压缩后的图像，质量为最低（1）
    # img.save(f'{output_path}compressed_image.jpg', 'JPEG', quality=1)
    print(f"原始图像shape: {img.shape}")
    print(f"原始图像占用内存: {sys.getsizeof(img)} bytes")

    cv_compress = cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))[1].tobytes()
    print("cv 压缩后的图像占用内存: {sys.getsizeof(cv_compress)} bytes")
    cv_reconstruction = cv2.imdecode(np.frombuffer(cv_compress, np.uint8), 1)
    print(f"cv原始图像和解压缩图像是否相同: {np.array_equal(img, cv_reconstruction)}")
    # save the cv_reconstruction image
    cv2.imwrite(f'{output_path}cv_reconstruction_image.jpg', cv_reconstruction)

    img_bytes = img.tobytes()

    # 使用zlib进行压缩
    compressed_bytes = zlib.compress(img_bytes)

    # 将压缩后的字节串转换为numpy.array
    compressed_array = np.frombuffer(compressed_bytes, dtype=np.uint8)

    print(f"压缩后的numpy.array占用内存: {compressed_array.nbytes} bytes")
    print(f"shape of compressed_array: {compressed_array.shape}, dtype: {compressed_array.dtype}")
    # 将压缩后的numpy.array保存到文件
    np.save('compressed_img.npy', compressed_array)

    # 从文件读取压缩后的numpy.array
    loaded_array = np.load('compressed_img.npy')

    # 将numpy.array转换回字节串
    loaded_bytes = loaded_array.tobytes()

    # 解压缩图像数据
    decompressed_bytes = zlib.decompress(loaded_bytes)

    # 将解压缩后的字节串转换回numpy数组
    decompressed_img = np.frombuffer(decompressed_bytes, dtype=np.uint8).reshape(480, 640, 3)

    print(f"解压缩后的图像shape: {decompressed_img.shape}")
    print(f"原始图像和解压缩图像是否相同: {np.array_equal(img, decompressed_img)}")
    

def output_RGB_image(img):
    plt.imshow(img)
    plt.show()

def output_BGR_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_video(observations, name, is_compress): 
    output_path = video_output_path + "output_video_" + name + ".mp4"
    video_data = observations['images'][name]
    fps = 15  # Frames per second
    height, width = 480, 640  # Make sure this matches the dimensions of video_data frames

    video_writer = cv2.VideoWriter(str(output_path), cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for i, frame in enumerate(video_data):
        if is_compress:
            frame = cv2.imdecode(np.frombuffer(frame, np.uint8), 1)
        
        if frame.shape[1:3] != (width, height):
            frame = cv2.resize(frame, (width, height))
        # if frame.shape[2] == 3:  # Assuming the frame is in RGB
        #     frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # render the first image at output_path
        indexes = [0, 1, 2, 3, 15, 20, 25, 30, 40, 45, 60, 89]  # from the 3rd image, robot can see the ob
        
        # output_RGB_image(frame)
        # frame here is in RGB format
        if i in indexes:
            Image.fromarray(frame, 'RGB').save(f'{video_output_path}/{name}_{i}th_image.jpg', 'JPEG')
            # Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR), 'RGB').save(f'{video_output_path}/{name}_first_image.jpg', 'JPEG')
        video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        # opencv VideoWriter needs BGR format, rather than RGB

    video_writer.release()
    print(f"Output video saved in {output_path}")


# 检查文件结构
def check_dataset_structure(file_path):
    with h5py.File(file_path, 'r') as file:
        # 打印顶层的keys
        print(list(file.keys()))  # 打印['action', 'base_action', 'observations']
        
        # 访问顶层数据
        observations = file["observations"]
        base_action = file["base_action"]
        action = file["action"]
        is_compress = file.attrs['compress']
        
        print(f"action Shape: {action.shape}")  # 打印形状
        print(f"action Dtype: {action.dtype}")  # 打印数据类型
        
        print(f"base_action Shape: {base_action.shape}")  # 打印形状
        print(f"base_action Dtype: {base_action.dtype}")  # 打印数据类型
        
        # 检查'observations'内部结构
        expected_obs_keys = ['images', 'images_depth', 'qpos', 'qvel', 'effort', 'base_vel']
        obs_keys = list(observations.keys())
        
        # save video of cam_high, cam_left_wrist, cam_right_wrist
        for name in ['cam_high', 'cam_left_wrist', 'cam_right_wrist']:
            save_video(observations, name, is_compress)
        # check_image(observations, 'cam_high', is_compress)

        print(f"--------------------------------episode length: {len(observations['qpos'])}")
        
        for key in expected_obs_keys:
            if key not in obs_keys:
                print(f"Missing '{key}' in observations.")
            else:
                try:
                    if key == "qpos":
                        print(f"qpos:", observations[key][30])
                        finger_qpos_list = []
                        for i in range(len(observations[key])):
                            finger_qpos = observations[key][i][6]
                            finger_qpos_list.append(finger_qpos)
                        print(f"finger_qpos_list: {finger_qpos_list} \n")
                        
                        qpos_0_list = []
                        for i in range(len(observations[key])):
                            qpos_0 = observations[key][i][0]
                            qpos_0_list.append(qpos_0)
                        qpos_4_list = []
                        for i in range(len(observations[key])):
                            qpos_4 = observations[key][i][4]
                            qpos_4_list.append(qpos_4)
                        print(f"qpos_0_list: {qpos_0_list} \n")
                        # print(f"qpos_4_list: {qpos_4_list} \n")
                        
                        print(f"[3] qpos: {observations[key][3]} \n")
                        
                        qpos_0_6_list = []
                        for i in range(len(observations[key])):
                            qpos_0_6 = observations[key][i][:6]
                            qpos_0_6_list.append(qpos_0_6)
                        # export qpos_0_6_list to path "~/RL/0projects/mobile_aloha_sim(info_see_here/aloha真机信息/qpos_data.txt"
                        with open(f'{home_path}/RL/0projects/mobile_aloha_sim(info_see_here/aloha真机信息/qpos_data.txt', 'w') as f:
                            for item in qpos_0_6_list:
                                f.write("%s\n" % item)
                        
                    elif key == "effort":
                        print(f"effort:", observations[key][0])
                        
                        
                    # 尝试直接访问
                    print(observations[key])
                    data_as_array = observations[key][:]
                    
                    print(f"{observations[key]}: {observations[key].shape}")  # 打印形状
                    print(f"{observations[key]}: {observations[key].dtype}")  # 打印数据类型
                    print(f"'{observations[key]}' is accessible as a numpy array.")
                    
                except Exception as e:
                    print(f"Error accessing '{key}' as a numpy array: {e}")
                    # 如果是组结构，进一步检查其内部结构
                    if isinstance(observations[key], h5py.Group):
                        nested_keys = list(observations[key].keys())
                        print(f"Nested keys in '{key}': {nested_keys}")
                        for nested_key in nested_keys:
                            try:
                                nested_data_as_array = observations[key][nested_key][:]
                                
                                print(f"'{nested_key}': {observations[key][nested_key].shape}")  # 打印形状
                                print(f"'{nested_key}': {observations[key][nested_key].dtype}")  # 打印数据类型
                                print(f"'{key}/{nested_key}' is accessible as a numpy array.")
                            except Exception as nested_e:
                                print(f"Error accessing '{key}/{nested_key}' as a numpy array: {nested_e}")


# 检查文件内容数据格式
def check_if_dataset(file_path):
    with h5py.File(file_path, 'r') as file:
        # 遍历文件中的所有items（包括组和数据集）
        def visit_items(name, item):
            if isinstance(item, h5py.Dataset):
                # 如果是数据集，尝试读取为numpy数组
                try:
                    data_as_array = item[:]
                    print(f"'{name}' is a Dataset and accessible as a numpy array.")
                except Exception as e:
                    print(f"Error accessing '{name}' as a numpy array: {e}")
            elif isinstance(item, h5py.Group):
                # 如果是组，打印其包含的keys
                print(f"'{name}' is a Group with keys: {list(item.keys())}")

        file.visititems(visit_items)
        
 

def visualize_images(file_path):
    with h5py.File(file_path, 'r') as file:
        # 循环遍历所有像素索引
        for i in range(10): 
            # 读取不同相机视角的图片数据
            cam_high_data = np.array(file['observations']['images']["cam_high"][i])
            cam_left_wrist_data = np.array(file['observations']['images']["cam_left_wrist"][i])
            cam_right_wrist_data = np.array(file['observations']['images']["cam_right_wrist"][i])

            # # 读取并打印 'qpos' 和 'effort' 数据
            # print(f"Pixel: {i}")
            # print(f"qpos data:", file['observations']['qpos'][i])
            # print(f"effort data:", file['observations']['effort'][i])

            # 设置画布大小
            plt.figure(figsize=(15, 5))

            # 显示 cam_high 视角的图片
            plt.subplot(1, 3, 1)
            plt.imshow(cam_high_data)
            plt.title(f'Camera High - Pixel {i}')

            # 显示 cam_left_wrist 视角的图片
            plt.subplot(1, 3, 2)
            plt.imshow(cam_left_wrist_data)
            plt.title(f'Camera Left Wrist - Pixel {i}')

            # 显示 cam_right_wrist 视角的图片
            plt.subplot(1, 3, 3)
            plt.imshow(cam_right_wrist_data)
            plt.title(f'Camera Right Wrist - Pixel {i}')

            # 显示所有图片
            plt.show()

        
# visualize_images(file_path)
            
def save_videos(file_path):
    images_dict = {}
    with h5py.File(file_path, 'r') as file:
        for key in file['observations']['images'].keys():
            dataset = file['observations']['images'][key]
            
            key_images = []
            for i in range(len(dataset)):
                frame = np.array(dataset[i])
                # frame = ((frame - frame.min()) / (frame.max() - frame.min()) * 255).astype(np.uint8)
                # print(frame)
                key_images.append(frame)
                
            images_dict[key] = key_images  
            
    fps = 30  # 每秒帧数
    base_video_path = os.path.expanduser('~/Downloads/demos')
    
    if not os.path.exists(base_video_path):
        os.makedirs(base_video_path)
    for key, key_images in images_dict.items():
        video_file_name = f'{key}_mobile_aloha_demo.mp4'
        video_path = os.path.join(base_video_path, video_file_name)
        writer = imageio.get_writer(video_path, fps=fps, codec='libx264')

        for img in key_images:
            writer.append_data(img)

#     writer.close()   

     
        

# 使用此函数并传入你的文件路径
# check_if_dataset(file_path)

# 使用实际的HDF5文件路径替换'<your_file_path>'
check_dataset_structure(file_path)


# check relationship with action and next qpos
def error_between_action_next_qpos(file_path):
    with h5py.File(file_path, 'r') as file:
        action = file["action"]
        qpos = file['observations']['qpos']
        
        for i in range(len(action)-1):
            error = abs(action[i] - qpos[i+1])
            if torch.any(torch.from_numpy(error) > 1.75): # Error between 1.75 - 2.0
                print(f"The error is too large!")
                break
                
                
# error_between_action_next_qpos(file_path)

# file_path = '/home/xuxuezhou/Downloads/episode_0.hdf5' # real machine
# file_path = '/home/xuxuezhou/code/GES-low-level-Orbit/data/mobile_aloha/episode_0.hdf5' # simulator
    
def calculate_range_of_qpos(file_path):
    # Open the HDF5 file
    with h5py.File(file_path, 'r') as file:
        # Access the 'qpos' dataset
        qpos = file['observations']['qpos']
        
        # Compute min, max, and mean for each dimension
        qpos_min = np.min(qpos, axis=0)
        qpos_max = np.max(qpos, axis=0)
        qpos_mean = np.mean(qpos, axis=0)
        
        # create a DataFrame
        df = pd.DataFrame({
            'Dimension': range(len(qpos_min)),  # Assuming you want to label dimensions starting at 0
            'Min': qpos_min,
            'Max': qpos_max,
            'Mean': qpos_mean
        })
    
    print(df)
    return qpos_min, qpos_max, qpos_mean


image_output_path = f'{home_path}/Pictures/'
def plot_qpos_ranges(file_path, image_output_path=None, name=None):
    # Get the min, max, and mean values
    qpos_min, qpos_max, qpos_mean = calculate_range_of_qpos(file_path)
    
    # Create an index array for the x-axis
    x = np.arange(len(qpos_min))
    
    # Plotting the data
    plt.figure(figsize=(10, 5))
    plt.plot(x, qpos_max, label='Max', marker='o', linestyle='-', color='r')
    plt.plot(x, qpos_min, label='Min', marker='o', linestyle='-', color='b')
    plt.plot(x, qpos_mean, label='Mean', marker='o', linestyle='-', color='g')
    
    # Adding labels and title
    plt.xlabel('Dimension Index')
    plt.ylabel('Value')
    plt.title('QPos Statistics: Max, Min, Mean')
    plt.legend()
    
    # Show the plot
    plt.grid(True)
    
    # check if save path is provided
    if image_output_path:
        save_path = image_output_path + "qpos_ranges_" + name + ".png"
        
        plt.savefig(save_path, format='png', dpi=300)  # Save the figure to the specified path
        print(f"Saved plot to {save_path}")
    plt.show()
    
# calculate_range_of_qpos(file_path)
# plot_qpos_ranges(file_path, image_output_path, name="fake")