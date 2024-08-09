#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/8/2 16:43
# @File    : device_can.py
# @Description: 
"""
import can
from can import Message

from .device_base import BaseDevice
from ..utils.error import ServiceException, ServerError


class CanDevice(BaseDevice):

    # canalystii
    def __init__(self, bustype: str, channel: int, bitrate: int):
        super().__init__(bustype, channel, bitrate)  # 调用基类的初始化方法
        self.bus = None

    def getBusByType(self,bustype: str):
        pass

    # no init
    def startCan(self):
        self.bus = can.interface.Bus(
            bustype=self.bustype,
            channel=self.channel,
            bitrate=self.bitrate
        )  # 初始化CAN1通道用来发送
        self.running = True
        return True

    def stopCan(self):
        self.bus.shutdown()
        self.running = False
        return True

    def sendCan(self, arbitration_id: int, data, is_extended_id=True, is_remote_frame=False):
        msg = can.Message(
            arbitration_id=arbitration_id,
            is_extended_id=is_extended_id,
            is_remote_frame=is_remote_frame,
            data=data,
            check=True
        )
        self.bus.send(msg)
        return True

    def recvCan(self, num=0):
        if self.bus is None or self.running is False:
            raise ServiceException(ServerError.CAN_DEVICE_USB_DOWN.code,
                                   ServerError.CAN_DEVICE_USB_DOWN.msg)
        return self.bus.recv(num)