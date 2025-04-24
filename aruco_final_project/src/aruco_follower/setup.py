from setuptools import setup

package_name = 'aruco_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yahboom',
    maintainer_email='',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts':[
            'follower_node = aruco_follower.aruco_follower:main',
            'tag_distance_service = aruco_follower.tag_distance_service:main',
            'webcam_pub = webcam.cam_pub:main',
            'webcam_sub = webcam.cam_sub:main'

        ],
    },
)
