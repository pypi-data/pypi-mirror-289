#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/7/30 13:42
# @File    : gugu_relay.py
# @Description: pip install pyudev
"""
import logging

from gugurelay.device.device_manager import DeviceManager
from gugurelay.usbtool.usb_manager import UsbManager
from gugurelay.utils.error import ServiceException, ServerError


class GuGuRelay(object):

    def __init__(self, logging_enabled=True):
        self.configure_logger(logging_enabled)
        self.usb_manager = UsbManager(self.logger)
        self.device_manager = DeviceManager(self.logger)


    def startCanDevice(self, device_type: str, channel: int, bitrate: int) -> int:
        '''
        启动can设备 X设备的Y号
        :return: 设备状态 0 成功
        '''
        if not self.usb_manager.getDevice(device_type, channel):
            raise ServiceException(ServerError.CAN_DEVICE_NO_FOUND.code,
                                   ServerError.CAN_DEVICE_NO_FOUND.msg)
        return self.device_manager.startCanDevice(device_type, channel, bitrate)

    def stopCanDevice(self, device_type: str, channel: int) -> int:
        '''
        启动can设备 X设备的Y号
        :return: 设备状态 0 成功
        '''
        if not self.usb_manager.getDevice(device_type,channel):
            raise ServiceException(ServerError.CAN_DEVICE_NO_FOUND.code,
                                   ServerError.CAN_DEVICE_NO_FOUND.msg)
        return self.device_manager.stopCanDevice(device_type, channel)

    def sendCanMessage(self, device_type: str, channel: int, arbitration_id:int, data, is_extended_id=False, is_remote_frame=False):
        if not self.usb_manager.getDevice(device_type, channel):
            raise ServiceException(ServerError.CAN_DEVICE_NO_FOUND.code,
                                   ServerError.CAN_DEVICE_NO_FOUND.msg)
        return self.device_manager.sendCanMessage(device_type, channel, arbitration_id, data, is_extended_id, is_remote_frame)

    def recvCanMessage(self, device_type: str, channel: int, num: int) -> str:
        if not self.usb_manager.getDevice(device_type, channel):
            raise ServiceException(ServerError.CAN_DEVICE_NO_FOUND.code,
                                   ServerError.CAN_DEVICE_NO_FOUND.msg)
        return self.device_manager.recvCanMessage(device_type, channel, num)

    def getCanDeviceList(self) -> str:
        return self.usb_manager.getList("can")

    def getCanDeviceStatus(self) -> str:

        return self.device_manager.getStatus("can")



    # no
    def startListen(self):
        self.usb_manager.startListen()

    # 启动can设备 停止 等等等
    # 获取输入输出流
    def configure_logger(self, logging_enabled):
        """
        Configures the logger based on the logging_enabled parameter.

        :param logging_enabled: If True, logs all levels. If False, logs only ERROR.
        """
        # create logger
        self.logger = logging.getLogger(__name__)

        # 根据logging_enabled参数设置logger的日志级别
        if logging_enabled:
            self.logger.setLevel(logging.DEBUG)  # 记录所有级别的日志
        else:
            self.logger.setLevel(logging.ERROR)  # 只记录ERROR级别的日志

        # 添加一个handler，比如StreamHandler
        handler = logging.StreamHandler()
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

