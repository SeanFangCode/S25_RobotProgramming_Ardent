#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SetEntityState
from gazebo_msgs.msg import EntityState
import math
import sys
import tty
import termios

class CarController(Node):
    def __init__(self):
        super().__init__('car_tty_controller')
        self.cli = self.create_client(SetEntityState, '/gazebo/set_entity_state')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /gazebo/set_entity_state service...')

        self.model_name = 'marker_CAR11'
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.speed = 0.02
        self.angular_speed = math.radians(10)

    def send_state(self):
        request = SetEntityState.Request()
        state = EntityState()
        state.name = self.model_name
        state.pose.position.x = self.x
        state.pose.position.y = self.y
        state.pose.position.z = 0.175
        qz = math.sin(self.yaw / 2.0)
        qw = math.cos(self.yaw / 2.0)
        state.pose.orientation.z = qz
        state.pose.orientation.w = qw
        state.twist.linear.x = 0.0
        state.twist.angular.z = 0.0
        request.state = state
        self.cli.call_async(request)

    def handle_key(self, ch):
        if ch == 'w':
            self.x += self.speed * math.cos(self.yaw)
            self.y += self.speed * math.sin(self.yaw)
        elif ch == 's':
            self.x -= self.speed * math.cos(self.yaw)
            self.y -= self.speed * math.sin(self.yaw)
        elif ch == 'a':
            self.yaw += self.angular_speed
        elif ch == 'd':
            self.yaw -= self.angular_speed
        elif ch == 'q':
            print("退出控制")
            return False
        else:
            print("输入 w/s/a/d 控制移动，q 退出")
            return True

        self.send_state()
        return True

def get_key():
    """从终端读取一个字符（非阻塞、不需要回车）"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    rclpy.init()
    node = CarController()
    print("控制指令：按 w(前进), s(后退), a(左转), d(右转), q(退出)")

    try:
        while True:
            key = get_key()
            if not node.handle_key(key):
                break
            rclpy.spin_once(node, timeout_sec=0.01)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
