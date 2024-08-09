#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main():
    gugurelay = GuGuRelay()
    # gugurelay.getCanDeviceList()
    gugurelay.startCanDevice("canalystii", 0, 500000)

    print(gugurelay.getCanDeviceList())

    for i in range(15):
        print(gugurelay.recvCanMessage("canalystii", 0, 1))


    gugurelay.stopCanDevice("canalystii", 0)


if __name__ == "__main__":
    main()