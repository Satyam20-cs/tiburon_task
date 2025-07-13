import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import time

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.publisher_ = self.create_publisher(String, 'command_topic', 10)
        self.timer = self.create_timer(1.0, self.send_command)
        self.command_list = ['start', 'stop', 'pause', 'resume', 'other_cmd']

    def send_command(self):
        delay = random.uniform(1.0, 3.0)
        time.sleep(delay)
        cmd = random.choice(self.command_list)
        msg = String()
        msg.data = cmd
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published command: "{cmd}"')

def main():
    rclpy.init()
    rclpy.spin(CommandPublisher())
    CommandPublisher().destroy_node()
    rclpy.shutdown()
