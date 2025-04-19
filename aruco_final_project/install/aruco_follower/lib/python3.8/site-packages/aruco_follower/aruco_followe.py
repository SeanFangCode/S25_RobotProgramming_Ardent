#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
import cv2.aruco as aruco
import numpy as np

class ArucoTracker(Node):
    def __init__(self):
        super().__init__('aruco_tracker')
        
        # Subscriber and publisher
        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # ArUco parameters
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters()
        self.detector = aruco.ArucoDetector(self.aruco_dict, self.parameters)
        
        # Camera calibration parameters (you need to calibrate your camera!)
        self.camera_matrix = np.array([[500, 0, 320], [0, 500, 240], [0, 0, 1]])  # Replace with actual values
        self.dist_coeffs = np.zeros((4, 1))  # Replace with actual values
        
        # Control parameters
        self.target_distance = 0.5  # meters
        self.Kp_dist = 0.5         # Proportional gain for distance
        self.Kp_angle = 1.0        # Proportional gain for angle
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
        corners, ids, _ = self.detector.detectMarkers(cv_image)
        
        if ids is not None:
            # Estimate pose (distance/orientation)
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(
                corners, 0.05, self.camera_matrix, self.dist_coeffs)
            
            # Process first detected marker
            distance = np.linalg.norm(tvecs[0])
            angle = np.degrees(rvecs[0][0][2])  # Simplified angle calculation
            
            # Calculate control outputs
            error_dist = distance - self.target_distance
            error_angle = -angle  # Negative sign for correction direction
            
            # Simple proportional control
            linear_speed = self.Kp_dist * error_dist
            angular_speed = self.Kp_angle * error_angle
            
            # Publish control command
            self.twist_msg.linear.x = np.clip(linear_speed, -0.2, 0.2)
            self.twist_msg.angular.z = np.clip(angular_speed, -0.5, 0.5)
            self.cmd_pub.publish(self.twist_msg)
            
            # Debug logging
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

def main(args=None):
    rclpy.init(args=args)
    tracker = ArucoTracker()
    rclpy.spin(tracker)
    tracker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
