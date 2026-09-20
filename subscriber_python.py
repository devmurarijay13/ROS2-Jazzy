import rclpy
from rclpy.node import Node

### will receive floats and strings
from std_msgs.msg import Float32
from std_msgs.msg import String

##topics
topic1 = 'float_topic'
topic2 = 'string_topic'

class SubscriberNode(Node):

    def __init__(self):

        super().__init__('subscriber_node')

        self.sub_float = self.create_subscription(
            Float32,
            topic1,
            self.callback_func1,
            10
        )

        self.sub_string = self.create_subscription(
            String,
            topic2,
            self.callback_func2,
            10
        )

        self.sub_float
        self.sub_string

    def callback_func1(self,msg):
        self.get_logger().info('Float Message : "%s"' % msg.data)

    def callback_func2(self,msg):
        self.get_logger().info('String Message : "%s"'% msg.data)

def main(args=None):
    rclpy.init(args=args)

    subscriber_node = SubscriberNode()

    rclpy.spin(subscriber_node)

    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


