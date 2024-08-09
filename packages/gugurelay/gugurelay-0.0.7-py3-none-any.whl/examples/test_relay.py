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
    gugurelay.startCanDevice("canalystii", 0, 500000)
    print(gugurelay.getCanDeviceList())

    for i in range(15):
        while 1:
            print(gugurelay.recvCanMessage("canalystii", 0, 1))


    gugurelay.stopCanDevice("canalystii", 0)


if __name__ == "__main__":
    main()