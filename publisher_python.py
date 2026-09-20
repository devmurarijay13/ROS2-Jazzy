import rclpy

#### Node class --- parent class for bulding Nodes
from rclpy.node import Node

## we will send flaots and strings
from std_msgs.msg import Float32
from std_msgs.msg import String

### topic for float message
topic1 = 'float_topic'

### topic for string message
topic2 = 'string_topic'

class PublisherNode(Node):

    def __init__(self):

        super().__init__('publisher_node')

        ### publisher for float
        self.pub_float = self.create_publisher(Float32,topic1,10)

        ### publisher for strings
        self.pub_string = self.create_publisher(String,topic2,10)

        ## period for publishing messages
        self.period = 1

        self.timer = self.create_timer(self.period,self.callback_func)
        #### a callback func is a func thats automatically being called by the time decide by timer

        ### message counter
        self.counter = 0

        ##flaot val
        self.value = 0

    def callback_func(self):
        message1 = Float32()
        message2 = String()

        self.value = self.value + 0.01
        message1.data = self.value  ### msg1 is a Data structure
        message2.data = "Message Number : %d" % self.counter  

        self.pub_string.publish(message2)
        self.pub_float.publish(message1)

        self.get_logger().info('Publishing : "%s" and value %s' %(message2.data,message1.data))

        self.counter += 1

def main(args=None):
    """
    before using rclpy API, we must initialize it. this should be done once per process. This function will initialize any global resources that are neccessory for middleware and client libraries.
    """
    rclpy.init(args=args)

    ### create node
    publisher_node = PublisherNode()

    ### spin node
    rclpy.spin(publisher_node)
 
    ## destroy the node explicitely (optional, otherwise it will be done automatically)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

