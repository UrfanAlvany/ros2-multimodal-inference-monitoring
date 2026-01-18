import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#Creating Talker Node

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "/chat2", 10)
        self.timer = self.create_timer(1.0, self.tick)
        self.i = 0

    def tick(self):
        msg = String()
        msg.data = f"hello {self.i}"
        self.pub.publish(msg)
        self.get_logger().info(f"published: {msg.data}")
        self.i += 1

def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
