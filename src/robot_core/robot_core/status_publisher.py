import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotStatus

class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')
        self.publisher_ = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.battery = 100.0

    def timer_callback(self):
        msg = RobotStatus()
        msg.robot_name = "AlphaBot"
        msg.robot_id = 42
        msg.battery_status = self.battery
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.robot_name} ({msg.robot_id}) | Battery: {msg.battery_status:.2f}%')
        if self.battery > 0:
            self.battery -= 0.5

def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

