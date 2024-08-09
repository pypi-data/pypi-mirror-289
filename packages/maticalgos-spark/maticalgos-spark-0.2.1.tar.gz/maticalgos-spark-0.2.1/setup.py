from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
    
setup(
name='maticalgos-spark',
version='0.2.1',
author='Niraj Munot',
author_email='nirajmunot28@gmail.com',
description='SparkLib is a Python client library for interacting with https://spark.maticalgos.com . It provides functionalities to manage accounts, strategies, place orders, and much more.',
long_description=long_description,
long_description_content_type='text/markdown',
packages=find_packages(),
install_requires=['websocket-client==1.7.0', 'numpy==1.26.4', 'requests==2.31.0'],
extras_require={"dataws" : ['python-engineio==3.13.0', 'python-socketio==4.6.0']},
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)