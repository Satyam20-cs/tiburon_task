import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DepthPublisher(Node):
    def __init__(self):
        super().__init__('depth_publisher')
        self.publisher_ = self.create_publisher(Float32, 'depth_topic', 10)
        self.timer = self.create_timer(0.5, self.publish_depth)

    def publish_depth(self):
        msg = Float32()
        msg.data = round(random.uniform(0.1, 5.0), 1)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published depth: {msg.data:.1f} m')

def main():
    rclpy.init()
    rclpy.spin(DepthPublisher())
    DepthPublisher().destroy_node()
    rclpy.shutdown()
