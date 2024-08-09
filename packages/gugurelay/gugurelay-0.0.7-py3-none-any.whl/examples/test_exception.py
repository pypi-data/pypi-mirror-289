#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/8/1 16:26
# @File    : test_relay.py
# @Description:
"""
import time

from gugurelay.gugu_relay import GuGuRelay


def main():
    gugurelay = GuGuRelay()
    # gugurelay.getCanDeviceList()
    try:
        gugurelay.startCanDevice("canalystii", 0, 500000)
        print(gugurelay.getCanDeviceList())
        gugurelay.stopCanDevice("canalystii", 0)
        print(gugurelay.recvCanMessage("canalystii", 0, 1))
    except Exception as ex:
        print(f"接收到ServiceException: {ex}")



if __name__ == "__main__":
    main()