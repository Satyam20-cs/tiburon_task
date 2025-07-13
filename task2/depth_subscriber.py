import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DepthSubscriber(Node):
    def __init__(self):
        super().__init__('depth_subscriber')
        self.subscription = self.create_subscription(Float32, 'depth_topic', self.callback, 10)

    def callback(self, msg):
        distance = msg.data
        if distance < 0.5:
            self.get_logger().warn(f'Warning: Object too close ({distance:.1f} m)')
        elif 0.5 <= distance <= 2.0:
            self.get_logger().info(f'Caution: Object nearby ({distance:.1f} m)')
        else:
            self.get_logger().info(f'All clear ({distance:.1f} m)')

def main():
    rclpy.init()
    rclpy.spin(DepthSubscriber())
    DepthSubscriber().destroy_node()
    rclpy.shutdown()
