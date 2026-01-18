import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.subscriber = self.create_subscription(String,"/chat2",
        self.callback,10)


    def callback(self, msg):
        # TODO: Print the message data using self.get_logger().info()
        # Hint: The data is in 'msg.data'
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


    

if __name__ == "__main__":
    main()
