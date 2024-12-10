from setuptools import find_packages
from distutils.core import setup

install_requires = [
    'torch>=2.0.0', 
    'torchvision>=0.15.1', 
    'torchaudio>=2.0.1', 
    'h5py==3.8.0',
    'opencv-python==4.9.0.80',
    'matplotlib==3.7.5',
    'tqdm',
    'ipython==8.12.3',
    'accelerate==0.30.1',
    'transformers==4.40.1',
    'pdbpp',
    'lap==0.4.0',
    'ultralytics',  
    'numpy==1.22.4',
    'clip @ git+https://github.com/openai/CLIP',
]

setup(
    name='ManiBox',
    version='1.0.0',
    author=' ',
    license="Apache 2.0 License",
    packages=find_packages(),
    author_email=' ',
    description=' ',
    install_requires=install_requires,
    # dependency_links=[
    #     'git+https://github.com/openai/CLIP.git#egg=clip'
    # ]
)