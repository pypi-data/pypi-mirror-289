from enum import Enum


class ServerError(Enum):

    # 通用错误
    ERROR = (20000, "")

    # CAN
    CAN_DEVICE_NO_FOUND = (20500, "can设备不存在")
    CAN_DEVICE_USB_DOWN = (20501, "can设备usb连接异常")
    CAN_DEVICE_NOT_RUNNING = (20502, "can设备未启动或已异常")
    # util
    WIN32_GUI_ERROR = (20602, "usb检测功能异常: ")


    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


class ServiceException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
