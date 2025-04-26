#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, Twist

class ArucoFollower(Node):
    def __init__(self):
        super().__init__('aruco_follower')
        # Desired distance (meters) and control gains; can be adjusted based on performance
        self.desired_distance = 0.5
        self.kp_linear  = 0.8   # Linear velocity gain
        self.kp_angular = 15.0  # Angular velocity gain

        # Publisher for the cmd_vel control topic
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        # Subscriber for Aruco marker detection results
        self.create_subscription(
            PoseArray,
            'aruco_poses',
            self.aruco_callback,
            10
        )

    def aruco_callback(self, msg: PoseArray):
        twist = Twist()

        if msg.poses:
            # Use the first detected marker in the array
            pose = msg.poses[0]
            x = pose.position.x  # Horizontal deviation (camera coordinate system x-axis)
            z = pose.position.z  # Forward distance (camera coordinate system z-axis)

            # Linear velocity: difference between z and desired distance
            error_dist = z - self.desired_distance
            twist.linear.x = self.kp_linear * error_dist

            # Angular velocity: based on horizontal deviation x (positive means right);
            # use negative sign so the robot turns toward the marker
            twist.angular.z = - self.kp_angular * x
        else:
            # No marker detected; stop the robot
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        self.cmd_vel_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ArucoFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

