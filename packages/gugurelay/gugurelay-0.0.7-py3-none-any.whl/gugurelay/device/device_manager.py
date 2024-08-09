#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/7/30 14:48
# @File    : device_manager.py
# @Description: 
"""
import json

import can
from usb.core import USBError, USBTimeoutError
from .device_can import CanDevice
from ..utils.error import ServiceException, ServerError


class DeviceManager(object):

    # canalystii
    def __init__(self, logger):
        self.logger = logger
        self.usb_status = None
        # 根据usb状态拿设备信息
        self.can_list: list = []

    def getStatus(self, device_type: str):
        return json.dumps(self.can_list)


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
        except ServiceException as ex:
            raise ex
        except Exception as ex:
            raise ServiceException(ServerError.ERROR.code, str(ex))

    def stopCanDevice(self, device_type: str, channel: int) -> bool:
        try:
            self.logger.info('关闭can设备:: 设备类型 - ' + device_type + ' | channel - ' + str(channel))
            devicecan = self.findCanDevice(device_type, channel)
            return devicecan.stopCan()
        except ServiceException as ex:
            raise ex
        except Exception as ex:
            raise ServiceException(ServerError.ERROR.code, str(ex))

    def sendCanMessage(self, device_type: str, channel: int, arbitration_id: int, data, is_extended_id=False, is_remote_frame=False):
        try:
            self.logger.info('发送can消息:: 设备类型 - ' + device_type + ' | channel - ' + str(channel))
            self.logger.info('arbitration_id: ' + str(arbitration_id) + ' data: ' + str(data) + ' is_extended_id: ' + str(is_extended_id) + ' is_remote_frame: ' + str(is_remote_frame))
            devicecan = self.findCanDevice(device_type, channel)
            return devicecan.sendCan(arbitration_id, data, is_extended_id, is_remote_frame)
        except ServiceException as ex:
            raise ex
        except Exception as ex:
            raise ServiceException(ServerError.ERROR.code, str(ex))

    def recvCanMessage(self, device_type: str, channel: int, num: int) -> str:
        try:
            devicecan = self.findCanDevice(device_type, channel)
            return devicecan.recvCan(num)

        except ServiceException as ex:
            raise ex
        except (USBError, USBTimeoutError) as ex:
            if devicecan is not None:
                devicecan.running = False
            raise ServiceException(ServerError.CAN_DEVICE_USB_DOWN.code,
                                   ServerError.CAN_DEVICE_USB_DOWN.msg)
        except Exception as ex:
            raise ServiceException(ServerError.ERROR.code, str(ex))

