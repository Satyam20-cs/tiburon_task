import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ArraySubscriber(Node):
    def __init__(self):
        super().__init__('array_subscriber')
        self.subscription = self.create_subscription(Int32MultiArray,'array_topic',self.listener_callback,10)

    def listener_callback(self, msg):
        data = msg.data
        if len(data) == 8 and all(1100 <= val <= 1900 for val in data):
            self.get_logger().info(f'Received data: {data}')
        else:
            self.get_logger().error('ERROR Invalid data: incorrect array length or values out of range')

def main():
    rclpy.init()
    rclpy.spin(ArraySubscriber())
    ArraySubscriber().destroy_node()
    rclpy.shutdown()
