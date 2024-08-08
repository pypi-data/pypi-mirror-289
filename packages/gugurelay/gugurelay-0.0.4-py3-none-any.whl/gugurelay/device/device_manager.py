#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/7/30 14:48
# @File    : device_manager.py
# @Description: 
"""
import can

from .device_can import CanDevice
from ..utils.error import ServiceException, ServerError


class DeviceManager(object):

    # canalystii
    def __init__(self, logger):
        self.logger = logger
        self.usb_status = None
        # 根据usb状态拿设备信息
        self.can_list: list = []

    def findCanDevice(self, device_type: str, channel: int) -> CanDevice:
        for device in self.can_list:
            if isinstance(device, CanDevice) and device.bustype == device_type and device.channel == channel:
                return device
        raise ServiceException(ServerError.CAN_DEVICE_NO_FOUND.code,
                               ServerError.CAN_DEVICE_NO_FOUND.msg)

    def startCanDevice(self, device_type: str, channel: int, bitrate: int) -> bool:
        try:
            self.logger.info('启动can设备:: 设备类型 - ' + device_type + ' | channel - ' + str(channel))
            tmp = CanDevice(device_type, channel, bitrate)
            tmp.startCan()
            self.can_list.append(tmp)
            return True
        except Exception as ex:
            # self.logging.exception(str(ex))
            print(str(ex))

    def stopCanDevice(self, device_type: str, channel: int) -> bool:
        try:
            self.logger.info('关闭can设备:: 设备类型 - ' + device_type + ' | channel - ' + str(channel))
            devicecan = self.findCanDevice(device_type, channel)
            return devicecan.stopCan()
        except Exception as ex:
            # self.logging.exception(str(ex))
            print(str(ex))

    def sendCanMessage(self, device_type: str, channel: int, arbitration_id: int, data, is_extended_id=False, is_remote_frame=False):
        try:
            self.logger.info('发送can消息:: 设备类型 - ' + device_type + ' | channel - ' + str(channel))
            self.logger.info('arbitration_id: ' + str(arbitration_id) + ' data: ' + str(data) + ' is_extended_id: ' + str(is_extended_id) + ' is_remote_frame: ' + str(is_remote_frame))
            devicecan = self.findCanDevice(device_type, channel)
            return devicecan.sendCan(arbitration_id, data, is_extended_id, is_remote_frame)
            # .sendCan(arbitration_id=0x123, data=[0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08], is_extended_id=False)
        except Exception as ex:
            # self.logging.exception(str(ex))
            print(str(ex))

    def recvCanMessage(self, device_type: str, channel: int, num: int) -> str:
        devicecan = self.findCanDevice(device_type, channel)
        return devicecan.recvCan(num)
