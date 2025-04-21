#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
import cv2.aruco as aruco
import numpy as np
import yaml
import os
from rclpy.duration import Duration


class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        
        # Load action configuration
        self.actions_config = self.load_actions_config()
        self.commands = {k: v for k, v in self.actions_config.items() if k.startswith('tag_')}
        self.settings = self.actions_config.get('settings', {})
        
        # Subscriber and publisher
        self.img_subscription = self.create_subscription(
            Image, 
            'image_raw', 
            self.image_callback, 
            1
        )
        self.cmd_pub = self.create_publisher(
            Twist, 
            self.settings.get('cmd_vel_topic', '/cmd_vel'), 
            10
        )
        
        # ArUco parameters
        self.setup_aruco_detector()
        
        # Timing and state management
        self.last_detection_time = self.get_clock().now()
        self.current_command_timer = None
        self.active_command = None
        
        self.bridge = CvBridge()
        self.twist_msg = Twist()

        # Create OpenCV window
        cv2.namedWindow('Robot View', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Robot View', 640, 480)

    def load_actions_config(self):
        config_path = os.path.join(os.getcwd(), 'actions.yaml')
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.get_logger().error(f'Failed to load actions config: {str(e)}')
            return {}

    def setup_aruco_detector(self):
        tag_family = self.settings.get('tag_family', '36h11')
        try:
            if tag_family == '36h11':
                self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_APRILTAG_36h11)
            elif tag_family == '16h5':
                self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_APRILTAG_16h5)
            else:
                raise ValueError(f"Unsupported tag family: {tag_family}")
                
            self.parameters = aruco.DetectorParameters()
            self.detector = aruco.ArucoDetector(self.aruco_dict, self.parameters)
        except Exception as e:
            self.get_logger().error(f'ArUco setup failed: {str(e)}')
            raise

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error(f'Image conversion error: {str(e)}')
            return

        processed_image = cv_image.copy()
        corners, ids, _ = self.detector.detectMarkers(cv_image)
        command_executed = False

        if ids is not None:
            self.last_detection_time = self.get_clock().now()
            aruco.drawDetectedMarkers(processed_image, corners, ids)
            
            # Process first detected tag
            first_id = ids[0][0]
            command_key = f"tag_{first_id}"
            command = self.commands.get(command_key)

            if command:
                self.execute_command(command)
                command_executed = True
                cv2.putText(processed_image, f"Executing: {command_key}", (10, 150),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Handle command timeout
        if not command_executed:
            self.check_detection_timeout()

        cv2.imshow('Robot View', processed_image)
        cv2.waitKey(1)

    def execute_command(self, command):
        # Cancel any previous command timer
        if self.current_command_timer:
            self.current_command_timer.cancel()

        # Set velocities from command
        linear = command.get('linear', {'x': 0.0, 'y': 0.0, 'z': 0.0})
        angular = command.get('angular', {'x': 0.0, 'y': 0.0, 'z': 0.0})
        duration = command.get('duration', 0.0)

        # Apply velocity limits
        max_linear = self.settings.get('max_linear_speed', 0.5)
        max_angular = self.settings.get('max_angular_speed', 1.0)
        
        self.twist_msg.linear.x = np.clip(linear.get('x', 0.0), -max_linear, max_linear)
        self.twist_msg.angular.z = np.clip(angular.get('z', 0.0), -max_angular, max_angular)
        self.cmd_pub.publish(self.twist_msg)

        # Set command timeout timer
        if duration > 0:
            self.current_command_timer = self.create_timer(
                duration, 
                self.stop_robot,
                oneshot=True
            )

    def check_detection_timeout(self):
        timeout = self.settings.get('detection_timeout', 1.0)
        elapsed = self.get_clock().now() - self.last_detection_time
        if elapsed > Duration(seconds=timeout):
            self.stop_robot()

    def stop_robot(self):
        self.twist_msg.linear.x = 0.0
        self.twist_msg.angular.z = 0.0
        self.cmd_pub.publish(self.twist_msg)
        if self.current_command_timer:
            self.current_command_timer.cancel()
            self.current_command_timer = None

    def __del__(self):
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    follower_node = FollowerNode()
    try:
        rclpy.spin(follower_node)
    except KeyboardInterrupt:
        pass
    finally:
        follower_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()