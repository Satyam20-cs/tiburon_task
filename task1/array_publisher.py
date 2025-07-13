import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random

class ArrayPublisher(Node):
    def __init__(self):
        super().__init__('array_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'array_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_array)

    def publish_array(self):
        msg = Int32MultiArray()
        msg.data = [random.randint(1100, 1900) for _ in range(8)]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published data: {msg.data}')

def main():
    rclpy.init()
    rclpy.spin(ArrayPublisher())
    ArrayPublisher().destroy_node()
    rclpy.shutdown()
