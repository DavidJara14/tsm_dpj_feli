#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from my_interface.msg import MyPosition, TargetPosition

class MySecNodo(Node):
    def __init__(self, node_name):
        super().__init__(node_name=node_name)
        self._topic_sub = self.create_subscription(MyPosition, '/mensaje', self._subs_callback, 10)
        self._target_pos_sub = self.create_subscription(TargetPosition, '/target_pos', self._tp_clbk, 10)

    def _tp_clbk(self, tpmsg : TargetPosition):
        self.get_logger().info(f"On [{tpmsg.header.stamp}]: To -> ({tpmsg.destino}), CurrPosXYZ ({tpmsg.target_point.x}, {tpmsg.target_point.y}, {tpmsg.target_point.z})")

    def _subs_callback(self, msg : MyPosition):
        #self.get_logger().info(f"Recibi ({msg.data})")
        self.get_logger().info(f"Recibi [{msg.etiqueta}]: Posx = {msg.pos_x}, Posy = {msg.pos_y}, Posz = {msg.pos_z}")


def main(args=None):
    rclpy.init(args=args)
    sub_nodo = MySecNodo('MySegNodo')
    rclpy.spin(sub_nodo)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
