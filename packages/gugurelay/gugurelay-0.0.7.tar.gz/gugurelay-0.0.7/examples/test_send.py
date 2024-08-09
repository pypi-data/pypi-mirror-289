#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Author  : wangzc
# @Date    : 2024/8/1 16:26
# @File    : test_send.py
# @Description:
"""

from gugurelay.gugu_relay import GuGuRelay


def main():
    gugurelay = GuGuRelay()

    type = "canalystii"
    channel  = 0
    bitrate = 500000
    arbitration_id = 0x07FF
    data = [0x11, 0x22, 0x33, 0x44, 0xAA, 0xBB, 0xCC, 0xDD],
    is_extended_id = False
    is_remote_id = True

    gugurelay.startCanDevice(type, channel, bitrate)

    gugurelay.sendCanMessage(
        type,
        channel,
        arbitration_id,
        data,
        is_extended_id,
        is_remote_id,
        )

    gugurelay.stopCanDevice(type, channel)


if __name__ == "__main__":
    main()