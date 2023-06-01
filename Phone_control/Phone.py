import os
import time
from ppadb.client import Client as AdbClient

class Phone:
    """Super Class"""
    def __init__(self):
        self.client = AdbClient(host='127.0.0.1', port=5037)
        self.devices = self.client.devices()
        self.mydevice = self.devices[0] # 목록 중 첫번 째
        self.mydevice.shell("input keyevent KEYCODE_WAKEUP")


    def clear_gallery(self, path):
        self.mydevice.shell(f"rm -rf {path}")
        time.sleep(2)

    def take_picture(self):
        self.mydevice.shell(f"input keyevent KEYCODE_CAMERA")  # 촬영
        time.sleep(8)

    def pull_image(self, rm_dir, dest_path, img_format=".jpg"):
        rm_image_dir = self.mydevice.shell(f"ls {rm_dir}").split()
        image_list = [s for s in rm_image_dir if img_format in s]
        if len(image_list) == 1:
            self.mydevice.pull(f'{rm_dir}/{image_list[0]}',
                          f'{dest_path}_{image_list[0]}')
        else:
            print(f"{img_format} image 파일 개수를 확인하세요 ")
        time.sleep(2)

    def mirroring(self):
        os.system("scrcpy -m 1080") # mirroring

    def load_camera(self):
        self.mydevice.shell('am start -a android.media.action.STILL_IMAGE_CAMERA')


class Mate50Pro(Phone):
    """Sub Class"""

    jpg_folder = "/sdcard/DCIM/Camera"
    dng_folder = f"{jpg_folder}/RAW"
    savedir = "D:/Result/MF/DOF/Mate 50 Pro"

    def __init__(self):
        super().__init__()

    def setting_pro_mode(self):
        for _ in range(3):
            self.mydevice.shell("input tap 925 1754") # up
            time.sleep(1)
        self.mydevice.shell("input tap 167 1762") # down
        time.sleep(1)

    def f_num_setting(self, f_num):
        f_num_pos = {  # F number Touch UI position
            1.4: {"x": 244,
                  "y": 1474},
            2.0: {"x": 479,
                  "y": 1474},
            2.8: {"x": 725,
                  "y": 1474},
            4.0: {"x": 969,
                  "y": 1474}
        }
        self.mydevice.shell("input tap 400 1627")  # F# 버튼 클릭
        time.sleep(2)
        self.mydevice.shell(f"input tap {f_num_pos[f_num]['x']} {f_num_pos[f_num]['y']}") # 원하는  F# 터치
        time.sleep(2)
        self.mydevice.shell("input tap 533 928")  # 화면 중앙 Touch
        time.sleep(1)

    def best_mf_setting(self, f_num):
        best_mf_pos = {  # Best Focus Touch UI position @ 30cm
            1.4: {"x": 682,
                  "y": 1298},
            2.0: {"x": 682,
                  "y": 1298},
            2.8: {"x": 674,
                  "y": 1298},
            4.0: {"x": 672,
                  "y": 1298}
        }
        self.mf_setting(x=best_mf_pos[f_num]['x'], y=best_mf_pos[f_num]['y'])

    def mf_setting(self, x, y):
        self.mydevice.shell("input tap 819 1625")  # MF 버튼 클릭
        time.sleep(2)
        self.mydevice.shell("input tap 777 1458")  # AF/MF 선택
        time.sleep(2)
        self.mydevice.shell(f"input tap 974 1298") # Dac 초기화 ( INF )
        time.sleep(2)
        self.mydevice.shell(f"input tap {x} {y}") # 원하는  Dac 터치
        time.sleep(3)

