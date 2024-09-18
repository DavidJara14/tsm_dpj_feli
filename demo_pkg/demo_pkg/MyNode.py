#l/usr/bin/env/ python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNodo(Node):
    def __init__(self):
        super().__init__('my_node')
        self._topic_pub = self.create_publisher(String, '/mesage', 10)
        self.timer = self.create_timer(1.0, self._timer_callback)
        self._count = 0
        self.get_logger().info("Nodo creado. ")

    def _timer_callback(self):
        self._count += 1
        mensaje = String()
        mensaje.data = f"{self._count} Repeticiones cada segundo"
        self._topic_pub.publish(mensaje)

def main(args = None):
    rclpy.init(args=args)
    myNodo = MyNodo
    rclpy.spin(myNodo)
    rclpy.shutdown()

if __name__ == '__main__':
    main()