#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
##from aruco_follower.srv import ArUcoDistance
from aruco_follower.srv import ArUcoDistance
import cv2.aruco as aruco
import numpy as np

class ArucoDistanceServer(Node):
    def __init__(self):
        super().__init__('aruco_distance_server')
        
        # Parameters
        self.declare_parameter('marker_size', 0.1)  # Default marker size: 0.1 meters
        self.declare_parameter('aruco_dictionary', 'DICT_4X4_250')
        self.declare_parameter('camera_info_topic', '/camera_info')
        
        self.marker_size = self.get_parameter('marker_size').value
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.__dict__[self.get_parameter('aruco_dictionary').value])
        self.detector = aruco.ArucoDetector(self.aruco_dict)
        
        # Service
        self.srv = self.create_service(ArUcoDistance, 'get_aruco_distance', self.handle_distance_request)
        
        # Subscriptions
        self.image_sub = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            10
        )
        self.camera_info_sub = self.create_subscription(
            CameraInfo,
            self.get_parameter('camera_info_topic').value,
            self.camera_info_callback,
            10
        )
        
        self.bridge = CvBridge()
        self.latest_image = None
        self.camera_matrix = None
        self.dist_coeffs = None

    def camera_info_callback(self, msg):
        self.camera_matrix = np.array(msg.k).reshape(3, 3)
        self.dist_coeffs = np.array(msg.d)
        self.get_logger().info("Camera calibration parameters received")

    def image_callback(self, msg):
        self.latest_image = msg
        self.get_logger().debug("New image received", throttle_duration_sec=1)

    def handle_distance_request(self, request, response):
        # Check if we have required data
        if self.latest_image is None:
            response.success = False
            response.distance = 0.0
            self.get_logger().warn("No image available")
            return response

        if self.camera_matrix is None or self.dist_coeffs is None:
            response.success = False
            response.distance = 0.0
            self.get_logger().warn("Camera calibration data missing")
            return response

        try:
            # Convert ROS Image to OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(self.latest_image, "bgr8")
            
            # Detect markers
            corners, ids, _ = self.detector.detectMarkers(cv_image)
            
            if ids is None or request.tag_id not in ids:
                response.success = False
                response.distance = 0.0
                self.get_logger().info(f"Tag {request.tag_id} not detected")
                return response

            # Find the requested tag
            idx = np.where(ids == request.tag_id)[0][0]
            marker_corners = corners[idx]

            # Calculate distance
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(
                marker_corners, self.marker_size, 
                self.camera_matrix, self.dist_coeffs
            )
            distance = np.linalg.norm(tvec[0][0])
            
            response.distance = float(distance)
            response.success = True
            self.get_logger().info(f"Distance to tag {request.tag_id}: {distance:.2f} meters")
            
        except Exception as e:
            self.get_logger().error(f"Processing failed: {str(e)}")
            response.success = False
            response.distance = 0.0

        return response

def main(args=None):
    rclpy.init(args=args)
    server = ArucoDistanceServer()
    try:
        rclpy.spin(server)
    except KeyboardInterrupt:
        server.get_logger().info("Server shutdown requested")
    finally:
        server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()