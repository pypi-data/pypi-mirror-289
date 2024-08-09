#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/8/2 16:44
# @File    : device_base.py
# @Description: 
"""


class BaseDevice(object):

    def __init__(self, bustype: str, channel: int, bitrate: int):
        self.bustype = bustype
        self.channel = channel
        self.bitrate = bitrate
        self.running = False
        self.status = None

