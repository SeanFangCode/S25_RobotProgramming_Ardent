#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from aruco_follower_interfaces.srv import GetTagDistance
import cv2
import cv2.aruco as aruco
import numpy as np
import yaml
import os
from ament_index_python.packages import get_package_share_directory


class TagDistanceService(Node):
    def __init__(self):
        super().__init__('tag_distance_service')
        
        # Create the service
        self.srv = self.create_service(
            GetTagDistance, 
            'get_tag_distance', 
            self.handle_get_tag_distance
        )
        self.get_logger().info("Tag Distance Service created")
        
        # Image subscriber to get the latest frame
        self.latest_image = None
        self.image_subscription = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            10
        )
        self.get_logger().info("Subscribed to image_raw topic")
        
        # Load configuration
        self.config = self.load_config()
        self.settings = self.config.get('settings', {})
        self.get_logger().info(f"Loaded settings: {self.settings}")
        
        # Set up ArUco detector
        self.setup_aruco_detector()
        
        # Bridge for converting between ROS and OpenCV images
        self.bridge = CvBridge()
        
        self.get_logger().info("Tag Distance Service is ready")
    
    def load_config(self):
        try:
            pkg_share = get_package_share_directory('aruco_follower')
            config_path = os.path.join(pkg_share, 'config', 'actions.yaml')
            
            if not os.path.exists(config_path):
                config_path = os.path.join(pkg_share, 'actions.yaml')
            
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return yaml.safe_load(f) or {}
            else:
                self.get_logger().warn(f"Config file not found at {config_path}")
                return {}
        except Exception as e:
            self.get_logger().error(f"Failed to load config: {str(e)}")
            return {}
    
    def setup_aruco_detector(self):
        try:
            # Get tag family from settings or use default
            tag_family = self.settings.get('tag_family', 'DICT_4X4_250')
            
            # Map string to ArUco dictionary constant
            aruco_dict_map = {
                'DICT_4X4_50': aruco.DICT_4X4_50,
                'DICT_4X4_100': aruco.DICT_4X4_100,
                'DICT_4X4_250': aruco.DICT_4X4_250,
                'DICT_4X4_1000': aruco.DICT_4X4_1000,
                # Add other dictionaries as needed
            }
            
            dict_type = aruco_dict_map.get(tag_family, aruco.DICT_4X4_250)
            self.get_logger().info(f"Using ArUco dictionary: {tag_family}")
            
            self.aruco_dict = aruco.getPredefinedDictionary(dict_type)
            self.parameters = aruco.DetectorParameters()
            self.detector = aruco.ArucoDetector(self.aruco_dict, self.parameters)
            
            # Camera calibration parameters - ideally these would come from a calibration file
            self.camera_matrix = np.array([[520.19, 0.0, 346.28], [0.0, 520.23, 265.28], [0.0, 0.0, 1.0]])
            self.dist_coeffs = np.array([-0.1, -0.296, -0.004, 0.0016, 0.9144])
            
            # Get marker size from settings or use default
            self.marker_size = self.settings.get('marker_size', 0.1)  # Default to 10cm if not specified
            self.get_logger().info(f"Using marker size: {self.marker_size}m")
            
        except Exception as e:
            self.get_logger().error(f'ArUco setup failed: {str(e)}')
            raise
    
    def image_callback(self, msg):
        # Store the latest image
        self.latest_image = msg
    
    def handle_get_tag_distance(self, request, response):
        self.get_logger().info('Received request for tag distance')
        
        # Check if we have received any images
        if self.latest_image is None:
            self.get_logger().error('No image available')
            response.success = False
            response.distance = -1.0
            response.message = "No camera image available"
            return response
        
        # Convert ROS Image to OpenCV format
        try:
            cv_image = self.bridge.imgmsg_to_cv2(self.latest_image, "bgr8")
        except Exception as e:
            self.get_logger().error(f'Image conversion error: {str(e)}')
            response.success = False
            response.distance = -1.0
            response.message = f"Image conversion error: {str(e)}"
            return response
        
        # Detect ArUco markers
        detection_result = self.detector.detectMarkers(cv_image)
        corners = detection_result[0]
        ids = detection_result[1]
        
        # Check if tag ID 0 was detected
        tag_found = False
        distance = -1.0
        
        if ids is not None and len(ids) > 0:
            for i, tag_id in enumerate(ids):
                if tag_id[0] == 0:  # Looking specifically for tag ID 0
                    tag_found = True
                    # Calculate distance using solvePnP
                    distance = self.calculate_distance(corners[i])
                    break
        
        # Prepare response
        if tag_found:
            response.success = True
            response.distance = float(distance)
            response.message = f"Tag ID 0 detected at {distance:.3f} meters"
            self.get_logger().info(f"Tag ID 0 detected at {distance:.3f} meters")
        else:
            response.success = False
            response.distance = -1.0
            response.message = "Tag ID 0 not detected in current frame"
            self.get_logger().info("Tag ID 0 not detected in current frame")
        
        return response
    
    def calculate_distance(self, corners):
        # Define the 3D coordinates of the marker corners in the marker coordinate system
        # The marker is at the origin, with corners at known positions based on marker size
        half_size = self.marker_size / 2
        marker_points = np.array([
            [-half_size, half_size, 0],    # Top-left
            [half_size, half_size, 0],     # Top-right
            [half_size, -half_size, 0],    # Bottom-right
            [-half_size, -half_size, 0]    # Bottom-left
        ], dtype=np.float32)
        
        # Extract the 2D corner points from the detection
        image_points = corners.reshape((4, 2))
        
        # Solve for pose
        success, rvec, tvec = cv2.solvePnP(
            marker_points, 
            image_points, 
            self.camera_matrix, 
            self.dist_coeffs
        )
        
        if success:
            # The translation vector gives us the position of the marker relative to the camera
            # The Z component is the distance away from the camera
            distance = tvec[2][0]  # Z component is the depth/distance
            return distance
        else:
            self.get_logger().warn('Failed to calculate pose for marker')
            return -1.0


def main(args=None):
    rclpy.init(args=args)
    service = TagDistanceService()
    
    try:
        rclpy.spin(service)
    except KeyboardInterrupt:
        service.get_logger().info('Service stopped cleanly')
    except Exception as e:
        service.get_logger().error(f'Error in service: {str(e)}')
    finally:
        service.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()