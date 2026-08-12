import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotStatus

class StatusSubscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber')
        self.subscription = self.create_subscription(
            RobotStatus, 'robot_status', self.listener_callback, 10)

    def listener_callback(self, msg):
        if msg.battery_status < 20.0:
            self.get_logger().warn(f'LOW BATTERY: {msg.robot_name} ID: {msg.robot_id} at {msg.battery_status:.2f}%')
        else:
            self.get_logger().info(f'Received: {msg.robot_name} ID: {msg.robot_id} | Battery: {msg.battery_status:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
