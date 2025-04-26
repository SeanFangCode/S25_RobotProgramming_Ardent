from setuptools import find_packages
from setuptools import setup

setup(
    name='gazebo_ros_link_attacher',
    version='0.0.0',
    packages=find_packages(
        include=('gazebo_ros_link_attacher', 'gazebo_ros_link_attacher.*')),
)
