import asyncio
import time
import win32gui, win32con, win32api
import win32gui_struct

GUID_DEVINTERFACE_USB_DEVICE = "{A5DCBF10-6530-11D2-901F-00C04FB951ED}"
class DeviceNotifier:

    # 供应商ID(VID)和产品识别码(PID)
    device_identifier = {
        "canalystii": "VID_04D8&PID_0053",
        "vector": "VID_1248&PID_1080",
        "neovi": "VID_093C&PID_1000",
    }

    def __init__(self, device_pool):
        self.device_pool: dict[str, int] = device_pool

    def compare_dicts(self,dict1: dict[str, int], dict2: dict[str, int]) -> bool:
        return dict1 == dict2

    def getListNow(self) -> dict[str, int]:
        device_now = {}
        import win32com.client
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("win32_usbcontrollerdevice"):
            for device_name, vid_pid in self.device_identifier.items():
                if vid_pid in usb.Dependent:
                    # Increment the count for the matched device in the device_pool
                    device_now[device_name] = device_now.get(device_name, 0) + 1
                    break
        if not self.compare_dicts(self.device_pool,device_now):
            # from copy import deepcopy
            # self.device_pool = deepcopy(device_now)
            self.copy_dict_contents(self.device_pool,device_now)
        return self.device_pool

    def copy_dict_contents(self, a, b):
        a.clear()  # 清空字典 a
        for key, value in b.items():
            a[key] = value  # 将 b 的内容复制到 a

    def OnDeviceChange(self, hwnd, msg, wp, lp):
        try:
            info = win32gui_struct.UnpackDEV_BROADCAST(lp)
            if info is None:
                return True
            if wp == win32con.DBT_DEVICEARRIVAL:
                # print("插入usb")
                for device_name, vid_pid in self.device_identifier.items():
                    if vid_pid in info.name:
                        # Increment the count for the matched device in the device_pool
                        self.device_pool[device_name] = self.device_pool.get(device_name, 0) + 1
                        # print("增添了：" + device_name)
                        break
                return True
            elif wp == win32con.DBT_DEVICEREMOVECOMPLETE:
                # print("拔出usb")
                for device_name, vid_pid in self.device_identifier.items():
                    if vid_pid in info.name:
                        # Decrement the count for the matched device in the device_pool
                        # print("移除了：" + device_name)
                        if device_name in self.device_pool:
                            self.device_pool[device_name] = max(0, self.device_pool[device_name] - 1)
                        break
            return True
        except Exception as e:
            print(f"Error processing device change: {e}")
            return True


    def register_and_wait(self):
        wc = win32gui.WNDCLASS()
        wc.lpszClassName = "test_devicenotify"
        wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
        wc.hbrBackground = win32con.COLOR_WINDOW + 1
        wc.lpfnWndProc = {
            win32con.WM_DEVICECHANGE: self.OnDeviceChange
        }
        class_atom = win32gui.RegisterClass(wc)
        hwnd = win32gui.CreateWindow(
            wc.lpszClassName,
            "Testing some devices",
            win32con.WS_CAPTION,
            100,
            100,
            900,
            900,
            0,
            0,
            0,
            None,
        )

        filter = win32gui_struct.PackDEV_BROADCAST_DEVICEINTERFACE(GUID_DEVINTERFACE_USB_DEVICE)
        hdev = win32gui.RegisterDeviceNotification(
            hwnd, filter, win32con.DEVICE_NOTIFY_WINDOW_HANDLE
        )

        while True:
            win32gui.PumpWaitingMessages()
            # await asyncio.sleep(0.01)
            time.sleep(0.01)

        win32gui.DestroyWindow(hwnd)
        win32gui.UnregisterClass(wc.lpszClassName, None)




