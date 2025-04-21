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
        self.img_subscription = self.create_subscription(Image, 'image_raw', self.image_callback, 1)
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
        
        self.bridge = CvBridge()
        self.twist_msg = Twist()
        self.last_error = 0.0

        # Create OpenCV window
        cv2.namedWindow('Robot View', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Robot View', 640, 480)

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error(f'Image conversion error: {str(e)}')
            return

        # Detect ArUco markers
        corners, ids, _ = self.detector.detectMarkers(cv_image)

        processed_image = cv_image.copy()
        
        
        if ids is not None:
            # Draw detected markers
            aruco.drawDetectedMarkers(processed_image, corners, ids)
            
            # Estimate pose for each detected marker
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(
                corners, 0.05, self.camera_matrix, self.dist_coeffs)
            
            # Process first detected marker
            distance = np.linalg.norm(tvecs[0][0])
            rotation_matrix, _ = cv2.Rodrigues(rvecs[0])
            euler_angles = self.rotation_matrix_to_euler_angles(rotation_matrix)
            angle = np.degrees(euler_angles[2])  # Yaw angle
            
            # Draw axis and info
            cv2.drawFrameAxes(processed_image, self.camera_matrix, self.dist_coeffs,
                            rvecs[0], tvecs[0], 0.1)
            
            # Add text overlay
            cv2.putText(processed_image, f"Distance: {distance:.2f}m", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(processed_image, f"Angle: {angle:.1f}deg", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(processed_image, f"Linear: {self.twist_msg.linear.x:.2f}", (10, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(processed_image, f"Angular: {self.twist_msg.angular.z:.2f}", (10, 120),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Calculate control outputs
            error_dist = distance - self.target_distance
            error_angle = -angle  # Adjust direction
            
            # Proportional control
            linear_speed = self.Kp_dist * error_dist
            angular_speed = self.Kp_angle * error_angle
            
            # Publish control command
            self.twist_msg.linear.x = np.clip(linear_speed, -0.2, 0.2)
            self.twist_msg.angular.z = np.clip(angular_speed, -0.5, 0.5)
            self.cmd_pub.publish(self.twist_msg)
        else:
            # Add "No marker detected" text
            cv2.putText(processed_image, "No ArUco marker detected", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            # Stop robot
            self.twist_msg.linear.x = 0.0
            self.twist_msg.angular.z = 0.0
            self.cmd_pub.publish(self.twist_msg)

        # Display processed image
        cv2.imshow('Robot View', processed_image)
        cv2.waitKey(1)

    @staticmethod
    def rotation_matrix_to_euler_angles(R):
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
