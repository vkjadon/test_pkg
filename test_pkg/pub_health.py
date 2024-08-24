import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.executors import ExternalShutdownException

class RobotHealth(Node):
    def __init__(self):
        super().__init__('pub_RoboHealth')
        self.publisher= self.create_publisher(String, 'robot_health', 10)
        self.timer = self.create_timer(1.0, self.callback_health)  # 1 Hz

    def callback_health(self):
        status = String()
        # Perform health checks and populate status
        status.data = 'All systems operational'
        self.publisher.publish(status)
        self.get_logger().info('Publishing robot status')

def main(args=None):
    rclpy.init(args=args)

    try:
        node = RobotHealth()
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)

if __name__ == '__main__':
    main()