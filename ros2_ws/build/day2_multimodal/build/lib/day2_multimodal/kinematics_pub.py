import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class KinematicsPub(Node):
    def __init__(self):
        super().__init__("kinematics_pub")
        self.pub = self.create_publisher(JointState, "/robot/joint_states", 10)
        self.timer = self.create_timer(0.02, self.tick)  # 50 Hz
        self.t = 0.0

    def tick(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ["joint1", "joint2", "joint3"]
        msg.position = [math.sin(self.t), math.cos(self.t), math.sin(2*self.t)]
        self.pub.publish(msg)
        self.t += 0.05

def main():
    rclpy.init()
    node = KinematicsPub()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
