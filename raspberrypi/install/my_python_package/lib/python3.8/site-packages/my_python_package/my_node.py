import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1.0 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, ROS 2 World!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
