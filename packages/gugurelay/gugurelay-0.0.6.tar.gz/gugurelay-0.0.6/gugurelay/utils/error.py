from enum import Enum


class ServerError(Enum):

    # 通用错误
    EXAMPLE_ERROR = (20000, "ERROR")

    # CAN
    CAN_DEVICE_NO_FOUND = (20500, "can设备不存在")
    IMPOSSIBLE_DBC_UUID = (20501, "该DBC文件不能删除，请联系管理员")
    # Hardware


    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


class ServiceException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
