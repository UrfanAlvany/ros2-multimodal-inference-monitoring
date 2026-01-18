import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraPub(Node):
    def __init__(self):
        super().__init__("camera_pub")
        self.pub = self.create_publisher(Image, "/camera/image", 10)
        self.timer = self.create_timer(0.1, self.tick)  # 10 Hz
        self.frame_id = 0

    def tick(self):
        h, w = 240, 320
        img = (np.random.rand(h, w, 3) * 255).astype(np.uint8)

        msg = Image()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "camera"
        msg.height = h
        msg.width = w
        msg.encoding = "rgb8"
        msg.is_bigendian = False
        msg.step = w * 3
        msg.data = img.tobytes()

        self.pub.publish(msg)
        self.get_logger().info(f"published frame={self.frame_id}")
        self.frame_id += 1

def main():
    rclpy.init()
    node = CameraPub()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
