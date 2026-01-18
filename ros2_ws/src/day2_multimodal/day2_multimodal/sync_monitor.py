import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, JointState

def stamp_to_sec(stamp):
    return stamp.sec + stamp.nanosec * 1e-9

class SyncMonitor(Node):
    def __init__(self):
        super().__init__("sync_monitor")
        self.last_js_t = None
        self.create_subscription(Image, "/camera/image", self.on_img, 10)
        self.create_subscription(JointState, "/robot/joint_states", self.on_js, 10)

    def on_js(self, msg: JointState):
        self.last_js_t = stamp_to_sec(msg.header.stamp)

    def on_img(self, msg: Image):
        now = self.get_clock().now().nanoseconds * 1e-9
        t_img = stamp_to_sec(msg.header.stamp)
        age_ms = (now - t_img) * 1000.0
        dt_ms = None if self.last_js_t is None else (t_img - self.last_js_t) * 1000.0
        self.get_logger().info(f"IMG age_ms={age_ms:.1f} dt_img_minus_js_ms={dt_ms}")

def main():
    rclpy.init()
    node = SyncMonitor()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
