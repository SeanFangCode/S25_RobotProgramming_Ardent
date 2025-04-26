#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Attach ArUco tag to a model in Gazebo using ROS 2 services.

This script:
1. Sets the pose of the standalone "aruco" model using `/gazebo/set_entity_state`.
2. Attaches the tag to another model using the `gazebo_ros_link_attacher` `/attach` service.
"""

import rclpy
from rclpy.node import Node

from gazebo_msgs.srv import SetEntityState
from gazebo_msgs.msg import EntityState
from geometry_msgs.msg import Pose, Twist
from tf_transformations import quaternion_from_euler
from gazebo_ros_link_attacher.srv import Attach


class AttachArucoNode(Node):
    """Node that positions an ArUco marker in Gazebo and attaches it to another link."""

    def __init__(self):
        super().__init__('attach_aruco_node')
        # Create service clients
        self.set_cli = self.create_client(SetEntityState, '/gazebo/set_entity_state')
        self.attach_cli = self.create_client(Attach, '/attach')
        self.get_logger().info('Waiting for /gazebo/set_entity_state and /attach services…')
        self.set_cli.wait_for_service()
        self.attach_cli.wait_for_service()
        self.get_logger().info('Services are available.')

    def set_aruco_pose(self, x, y, z, roll, pitch, yaw, reference_frame='world'):
        """Call `/gazebo/set_entity_state` to set the ArUco pose."""
        req = SetEntityState.Request()
        state = EntityState()
        state.name = 'aruco'

        # Fill in pose
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        q = quaternion_from_euler(roll, pitch, yaw)
        pose.orientation.x = q[0]
        pose.orientation.y = q[1]
        pose.orientation.z = q[2]
        pose.orientation.w = q[3]
        state.pose = pose

        # Zero velocity
        state.twist = Twist()
        state.reference_frame = reference_frame
        req.state = state

        self.get_logger().info(f'Setting ArUco to ({x}, {y}, {z}), rpy=({roll}, {pitch}, {yaw}) …')
        future = self.set_cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        res = future.result()
        if res.success:
            self.get_logger().info('ArUco pose successfully set.')
        else:
            self.get_logger().error(f'Pose set failed: {res.status_message}')

    def attach_links(self, model1, link1, model2, link2):
        """Call `/attach` to rigidly connect two links."""
        req = Attach.Request()
        req.model_name_1 = model1
        req.link_name_1 = link1
        req.model_name_2 = model2
        req.link_name_2 = link2

        self.get_logger().info(f'Attaching {model1}::{link1} ↔ {model2}::{link2} …')
        future = self.attach_cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        res = future.result()
        # Print result if the Attach.srv defines a success field
        if hasattr(res, 'success'):
            if res.success:
                self.get_logger().info('Attach succeeded.')
            else:
                self.get_logger().error(f'Attach failed: {res.status_message}')
        else:
            self.get_logger().info('Attach service call completed (no return fields).')


def main(args=None):
    rclpy.init(args=args)
    node = AttachArucoNode()

    # 1. Set ArUco pose
    node.set_aruco_pose(
        x=1.867, y=0.084, z=0.15,
        roll=-2.17, pitch=-1.57, yaw=2.17,
        reference_frame='world'
    )

    # 2. Attach the two model/link pairs
    node.attach_links(
        model1='marker_CAR11', link1='base_link',
        model2='aruco',       link2='link'
    )

    # Shutdown
    rclpy.spin_once(node, timeout_sec=1.0)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

