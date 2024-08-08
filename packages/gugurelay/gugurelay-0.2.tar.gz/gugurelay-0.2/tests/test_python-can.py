#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/8/1 16:27
# @File    : test_python-can.py
# @Description:
"""

import can

if __name__ == "__main__":


    bus = can.interface.Bus(interface='canalystii', channel=0, bitrate=500000)
    msg = can.Message(
        arbitration_id=0x123, data=[0x01,0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08], is_extended_id=False
    )
    try:
        bus.send(msg)
        print(f"Message sent on {bus.channel_info}")
        print(msg)
    except can.CanError:
        print("Message NOT sent")

    """Receives messages."""


    while True:
        msg = bus.recv(1)
        print(msg)

    bus.shutdown()


