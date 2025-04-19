#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
import cv2.aruco as aruco
import numpy as np

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        
        # Subscriber and publisher
        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # ArUco parameters
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters()
        self.detector = aruco.ArucoDetector(self.aruco_dict, self.parameters)
        
        # Camera calibration parameters (replace with actual calibrated values)
        self.camera_matrix = np.array([[500, 0, 320], [0, 500, 240], [0, 0, 1]])
        self.dist_coeffs = np.zeros((4, 1))
        
        # Control parameters
        self.target_distance = 0.5  # meters
        self.Kp_dist = 0.5
        self.Kp_angle = 1.0
        self.last_error = 0.0
        
        self.bridge = CvBridge()
        self.twist_msg = Twist()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error(f'Image conversion error: {str(e)}')
            return

        # Detect ArUco markers
        detection_result = self.detector.detectMarkers(cv_image)
        corners = detection_result.corners
        ids = detection_result.ids
        
        if ids is not None:
            # Estimate pose for each detected marker
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(
                corners, 0.05, self.camera_matrix, self.dist_coeffs)
            
            # Process first detected marker
            distance = np.linalg.norm(tvecs[0][0])
            rotation_matrix, _ = cv2.Rodrigues(rvecs[0])
            euler_angles = self.rotation_matrix_to_euler_angles(rotation_matrix)
            angle = np.degrees(euler_angles[2])  # Yaw angle
            
            # Calculate errors
            error_dist = distance - self.target_distance
            error_angle = -angle  # Adjust direction
            
            # Proportional control
            linear_speed = self.Kp_dist * error_dist
            angular_speed = self.Kp_angle * error_angle
            
            # Publish control command
            self.twist_msg.linear.x = np.clip(linear_speed, -0.2, 0.2)
            self.twist_msg.angular.z = np.clip(angular_speed, -0.5, 0.5)
            self.cmd_pub.publish(self.twist_msg)
            
            # Logging
            self.get_logger().info(
                f'Distance: {distance:.2f}m | Angle: {angle:.1f}° | '
                f'Linear: {self.twist_msg.linear.x:.2f} | Angular: {self.twist_msg.angular.z:.2f}',
                throttle_duration_sec=1.0)
        else:
            # Stop if no marker detected
            self.twist_msg.linear.x = 0.0
            self.twist_msg.angular.z = 0.0
            self.cmd_pub.publish(self.twist_msg)
            self.get_logger().warn('No ArUco marker detected!', throttle_duration_sec=1.0)

    @staticmethod
    def rotation_matrix_to_euler_angles(R):
        # Convert rotation matrix to Euler angles (roll, pitch, yaw)
        sy = np.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
        singular = sy < 1e-6
        if not singular:
            x = np.arctan2(R[2,1], R[2,2])
            y = np.arctan2(-R[2,0], sy)
            z = np.arctan2(R[1,0], R[0,0])
        else:
            x = np.arctan2(-R[1,2], R[1,1])
            y = np.arctan2(-R[2,0], sy)
            z = 0
        return np.array([x, y, z])

def main(args=None):
    rclpy.init(args=args)
    follower_node = FollowerNode()
    rclpy.spin(follower_node)
    follower_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
