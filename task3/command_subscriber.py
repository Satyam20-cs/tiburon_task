import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandSubscriber(Node):
    def __init__(self):
        super().__init__('command_subscriber')
        self.subscription = self.create_subscription(String, 'command_topic', self.callback, 10)

    def callback(self, msg):
        command = msg.data.lower()
        if command == 'start':
            self.get_logger().info('System starting')
        elif command == 'stop':
            self.get_logger().info('System stopping')
        elif command == 'pause':
            self.get_logger().info('System paused')
        elif command == 'resume':
            self.get_logger().info('System resuming')
        else:
            self.get_logger().warn(f'Unknown command: "{command}"')

def main():
    rclpy.init()
    rclpy.spin(CommandSubscriber())
    CommandSubscriber().destroy_node()
    rclpy.shutdown()
