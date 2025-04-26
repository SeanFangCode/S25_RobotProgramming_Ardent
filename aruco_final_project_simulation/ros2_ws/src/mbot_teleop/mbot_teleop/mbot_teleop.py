#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import select
import termios
import tty

msg = """
Control mbot!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly

CTRL-C to quit
"""

moveBindings = {
    'i': (1, 0),
    'o': (1, -1),
    'j': (0, 1),
    'l': (0, -1),
    'u': (1, 1),
    ',': (-1, 0),
    '.': (-1, 1),
    'm': (-1, -1),
}

speedBindings = {
    'q': (1.1, 1.1),
    'z': (.9, .9),
    'w': (1.1, 1),
    'x': (.9, 1),
    'e': (1, 1.1),
    'c': (1, .9),
}

class MbotTeleop(Node):

    def __init__(self):
        super().__init__('mbot_teleop')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.settings = termios.tcgetattr(sys.stdin)
        self.speed = 1.0
        self.turn = 2.5

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def run(self):
        try:
            print(msg)
            print(self.vels(self.speed, self.turn))
            while True:
                key = self.getKey()

                if key in moveBindings:
                    x = moveBindings[key][0]
                    th = moveBindings[key][1]
                elif key in speedBindings:
                    self.speed = self.speed * speedBindings[key][0]
                    self.turn = self.turn * speedBindings[key][1]
                    print(self.vels(self.speed, self.turn))
                elif key == ' ' or key == 'k':
                    x = 0
                    th = 0
                elif key == '\x03':
                    break
                else:
                    x = 0
                    th = 0

                twist = Twist()
                twist.linear.x = x * self.speed
                twist.angular.z = th * self.turn
                self.pub.publish(twist)

        except Exception as e:
            self.get_logger().error(f'Encountered an error: {e}')

        finally:
            twist = Twist()
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
            self.pub.publish(twist)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)

    def vels(self, speed, turn):
        return "currently:\tspeed %s\tturn %s " % (speed, turn)

def main(args=None):
    rclpy.init(args=args)
    mbot_teleop = MbotTeleop()
    try:
        mbot_teleop.run()
    except Exception as e:
        mbot_teleop.get_logger().error(f'Unhandled exception: {e}')
    finally:
        mbot_teleop.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

