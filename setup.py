import atexit
import subprocess
import os
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# in the setup function:

setup(
    name="datatotext",
    version="0.1.0",
    python_requires='>=3.6',
    install_requires=[
        "bert-score==0.3.5",
        "configargparse",
        "dataclasses",
        "datasets==1.1.2",
        "h5py>=2.10.0",
        "fire",
        "pandas==1.1.3",
        "pyarrow==1.0.1",
        "pytorch-lightning==1.2.10",
        "sentencepiece==0.1.91",
        "tensorboard",
        "tensorflow==2.5.0",
        "torchvision==0.8.2+cu110",
        "typing==3.7.4.3",
        "gitpython",
        "rouge_score",
        "sacrebleu",
        "wandb",
        "transformers @ git+https://github.com/m-chanakya/transformers.git@controlprefixes",
        "torchtext==0.8.1",
        "torch==1.7.1+cu110"
    ],
    packages=['datatotext'],
    package_dir={'datatotext': 'src/datatotext'},
    description="Code for Control Prefixes for Parameter-Efficient Text Generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jordan Clive",
    author_email="jordan.clive19@imperial.ac.uk",
    url="https://github.com/m-chanakya/ControlPrefixes",
    download_url="https://github.com/m-chanakya/ControlPrefixes.git",
    license="MIT License",
)
