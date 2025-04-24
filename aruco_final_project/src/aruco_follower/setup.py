from setuptools import setup
import os
from glob import glob

package_name = 'aruco_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/actions.yaml']),
        (os.path.join('share', package_name, 'srv'), 
         glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yahboom',
    maintainer_email='seanf0126@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'rosidl_generate_interfaces': [
            'aruco_follower/srv/ArUcoDistance.srv',
        ],
        'console_scripts':[
            'follower_node = aruco_follower.aruco_follower:main',
            'distance_server = aruco_follower.distance_server:main', 
            'webcam_pub = webcam.cam_pub:main',
            'webcam_sub = webcam.cam_sub:main'
        ]
    },
)
