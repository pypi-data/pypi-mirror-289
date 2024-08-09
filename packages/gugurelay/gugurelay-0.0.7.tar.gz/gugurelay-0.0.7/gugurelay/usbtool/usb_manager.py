#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/7/30 14:48
# @File    : UsbManager.py
# @Description:
"""
import threading

from .usb_trigger import DeviceNotifier
import json
import asyncio


class UsbManager(object):

    # canalystii  VID_04D8&PID_0053
    # vector      VID_1248&PID_1080
    # neovi       VID_093C&PID_1000

    def __init__(self, logger):
        # 根据usb状态拿设备信息
        self.logger = logger
        self.device_pool: dict[str, int] = {}
        self.notifier = DeviceNotifier(self.device_pool)
        self.notifier.getListNow()
        self.startListen()
        # asyncio.run(self.notifier.register_and_wait())

    def getDevice(self, device_type: str, channel: int) -> bool:
        return device_type in self.device_pool and self.device_pool[device_type] - 1 >= channel

    def getList(self, device_type: str):
        return json.dumps(self.notifier.getListNow())

    def startListen(self):
        thread = threading.Thread(target=self.notifier.register_and_wait)
        thread.start()

