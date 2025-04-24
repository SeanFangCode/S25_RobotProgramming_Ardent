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
from ament_index_python.packages import get_package_share_directory

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        print("[INIT] Starting FollowerNode")

        # Load action configuration
        self.actions_config = self.load_actions_config()
        print(f"[INIT] actions_config: {self.actions_config}")
        self.commands = {k: v for k, v in self.actions_config.items() if k.startswith('tag_')}
        print(f"[INIT] Available commands keys: {list(self.commands.keys())}")
        self.settings = self.actions_config.get('settings', {})
        print(f"[INIT] Settings: {self.settings}")

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
        print(f"[INIT] Subscribed to image_raw, publishing to {self.settings.get('cmd_vel_topic', '/cmd_vel')}")

        # ArUco parameters
        self.setup_aruco_detector()
        print("[INIT] ArUco detector set up")

        # Timing and state management
        self.last_detection_time = self.get_clock().now()
        self.current_command_timer = None
        self.active_command = None

        self.bridge = CvBridge()
        self.twist_msg = Twist()

        # Create OpenCV window
        cv2.namedWindow('Robot View', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Robot View', 640, 480)
        print("[INIT] OpenCV window created")

    def send_distance_request(self):
        # Helper method to send distance request for tag ID 3
        if not self.distance_client.service_is_ready():
            print("[DISTANCE] Service not available, skipping request")
            return

        request = ArUcoDistance.Request()
        request.tag_id = 3  # We're specifically checking for tag ID 3
        
        print("[DISTANCE] Sending request for tag 3 distance...")
        future = self.distance_client.call_async(request)
        future.add_done_callback(self.distance_response_callback)

    def distance_response_callback(self, future):
        # Handle the service response
        try:
            response = future.result()
            if response.success:
                print(f"[DISTANCE] Distance to tag 3: {response.distance:.2f} meters")
            else:
                print("[DISTANCE] Failed to get distance measurement")
        except Exception as e:
            print(f"[DISTANCE] Service call failed: {str(e)}")

    def image_callback(self, msg):
        print("[CALLBACK] Received image")
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            print(f"[CALLBACK] Image conversion error: {e}")
            self.get_logger().error(f'Image conversion error: {str(e)}')
            return

        corners, ids, _ = self.detector.detectMarkers(cv_image)
        print(f"[CALLBACK] detectMarkers → ids: {ids}, number of corners sets: {len(corners) if corners is not None else 0}")

        processed_image = cv_image.copy()
        command_executed = False

        if ids is not None and len(ids) > 0:
            self.last_detection_time = self.get_clock().now()
            aruco.drawDetectedMarkers(processed_image, corners, ids)

            # Check if tag ID 3 is present
            if 3 in ids:
                print("[CALLBACK] Detected tag ID 3, requesting distance...")
                self.send_distance_request()

            # Original command processing remains
            first_id = int(ids[0][0])
            command_key = f"tag_{first_id}"
            command = self.commands.get(command_key)
            print(f"[CALLBACK] First detected ID: {first_id} → looking for key '{command_key}' → command: {command}")

            if command:
                print(f"[CALLBACK] Executing command for {command_key}: {command}")
                self.execute_command(command)
                command_executed = True
                cv2.putText(processed_image, f"Executing: {command_key}", (10, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                print(f"[CALLBACK] No command found for {command_key}")

        # Handle command timeout
        if not command_executed:
            self.check_detection_timeout()

        cv2.imshow('Robot View', processed_image)
        cv2.waitKey(1)
        
    def load_actions_config(self):
        from ament_index_python.packages import get_package_share_directory
        pkg_share = get_package_share_directory('aruco_follower')

        # Possible locations for actions.yaml
        candidate_paths = [
            os.path.join(pkg_share, 'config', 'actions.yaml'),
            os.path.join(pkg_share, 'actions.yaml'),
        ]

        config_path = None
        for p in candidate_paths:
            exists = os.path.exists(p)
            print(f"[LOAD_CONFIG] Checking {p} → exists={exists}")
            if exists:
                config_path = p
                break
            
        if config_path is None:
            print("[LOAD_CONFIG] No actions.yaml found in any expected location!")
            self.get_logger().error("actions.yaml not found; please install it under share/aruco_follower/(config/)")
            return {}

        print(f"[LOAD_CONFIG] Loading YAML from: {config_path}")
        try:
            with open(config_path, 'r') as f:
                cfg = yaml.safe_load(f)
            print(f"[LOAD_CONFIG] YAML contents: {cfg}")
            return cfg or {}
        except Exception as e:
            print(f"[LOAD_CONFIG] Failed to parse YAML: {e}")
            self.get_logger().error(f'Failed to load actions config: {str(e)}')
            return {}

    def setup_aruco_detector(self):
        try:
            self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
            self.parameters = aruco.DetectorParameters()
            self.detector = aruco.ArucoDetector(self.aruco_dict, self.parameters)
        except Exception as e:
            print(f"[ARUCO_SETUP] ArUco setup failed: {e}")
            self.get_logger().error(f'ArUco setup failed: {str(e)}')
            raise

    def image_callback(self, msg):
        print("[CALLBACK] Received image")
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            print(f"[CALLBACK] Image conversion error: {e}")
            self.get_logger().error(f'Image conversion error: {str(e)}')
            return

        corners, ids, _ = self.detector.detectMarkers(cv_image)
        print(f"[CALLBACK] detectMarkers → ids: {ids}, number of corners sets: {len(corners) if corners is not None else 0}")

        processed_image = cv_image.copy()
        command_executed = False

        if ids is not None and len(ids) > 0:
            self.last_detection_time = self.get_clock().now()
            aruco.drawDetectedMarkers(processed_image, corners, ids)

            first_id = int(ids[0][0])
            command_key = f"tag_{first_id}"
            command = self.commands.get(command_key)
            print(f"[CALLBACK] First detected ID: {first_id} → looking for key '{command_key}' → command: {command}")

            if command:
                print(f"[CALLBACK] Executing command for {command_key}: {command}")
                self.execute_command(command)
                command_executed = True
                cv2.putText(processed_image, f"Executing: {command_key}", (10, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                print(f"[CALLBACK] No command found for {command_key}")

        # Handle command timeout
        if not command_executed:
            self.check_detection_timeout()

        cv2.imshow('Robot View', processed_image)
        cv2.waitKey(1)

    def execute_command(self, command):
        print(f"[EXECUTE] Received command: {command}")
        if self.current_command_timer:
            print("[EXECUTE] Cancelling previous timer")
            self.current_command_timer.cancel()

        linear = command.get('linear', {'x': 0.0})
        angular = command.get('angular', {'z': 0.0})
        duration = command.get('duration', 0.0)
        print(f"[EXECUTE] linear={linear}, angular={angular}, duration={duration}")

        max_linear = self.settings.get('max_linear_speed', 0.5)
        max_angular = self.settings.get('max_angular_speed', 1.0)

        self.twist_msg.linear.x = np.clip(linear.get('x', 0.0), -max_linear, max_linear)
        self.twist_msg.angular.z = np.clip(angular.get('z', 0.0), -max_angular, max_angular)
        print(f"[EXECUTE] Publishing Twist → linear.x={self.twist_msg.linear.x}, angular.z={self.twist_msg.angular.z}")
        self.cmd_pub.publish(self.twist_msg)

        if duration > 0:
            print(f"[EXECUTE] Setting up stop timer for {duration}s")
            self.current_command_timer = self.create_timer(
                duration,
                self.stop_robot
            )

    def check_detection_timeout(self):
        timeout = self.settings.get('detection_timeout', 1.0)
        elapsed = (self.get_clock().now() - self.last_detection_time).nanoseconds * 1e-9
        print(f"[TIMEOUT] elapsed since last detection: {elapsed:.2f}s (timeout={timeout}s)")
        if elapsed > timeout:
            print("[TIMEOUT] Timeout exceeded, stopping robot")
            self.stop_robot()

    def stop_robot(self):
        print("[STOP] Stopping robot (publishing zero velocities)")
        self.twist_msg.linear.x = 0.0
        self.twist_msg.angular.z = 0.0
        self.cmd_pub.publish(self.twist_msg)
        if self.current_command_timer:
            print("[STOP] Cancelling timer")
            self.current_command_timer.cancel()
            self.current_command_timer = None

    def __del__(self):
        print("[CLEANUP] Destroying OpenCV windows")
        cv2.destroyAllWindows()

def main(args=None):
    print("[MAIN] Initializing rclpy")
    rclpy.init(args=args)
    node = FollowerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("[MAIN] KeyboardInterrupt, shutting down")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        print("[MAIN] rclpy shutdown")

if __name__ == '__main__':
    main()
