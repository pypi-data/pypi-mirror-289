import os.path

import requests

from ascript.ios import wdapy
import argparse

class AsR:
    def __init__(self, root_dir: str):
        self.name = os.path.basename(root_dir)
        self._root = root_dir
        self.id = None

    def root(self, child_path=None):
        return os.path.join(self._root, child_path)

    def res(self, child_path=None):
        return os.path.join(self._root, "res", child_path)

    def img(self, child_path=None):
        return os.path.join(self._root, "res", "img", child_path)

    def ui(self, child_path=None):
        return os.path.join(self._root, "res", "ui",child_path)

    @staticmethod
    def rel(path: str = __file__, rel_path: str = None):
        if not os.path.isdir(path):
            path = os.path.dirname(path)

        real_path = os.path.join(path, rel_path)
        real_path = os.path.normpath(real_path)

        return real_path

    def __repr__(self):
        return f"R({self._root})"


class Device:
    @staticmethod
    def display():
        return client.window_size()


def guess_client(device_id: str = None):
    if device_id:
        return wdapy.AppiumUSBClient(device_id)
    else:
        response = requests.get("http://127.0.0.1:9097/api/device")
        if response.status_code == 200:
            data = response.json()
            if data["data"] and len(data["data"]) > 0:
                for device in data["data"]:
                    if device["statue"] == 0:
                        print("猜测运行:", device)
                        return wdapy.AppiumUSBClient(device['udid'])

        return None


client = None
R = AsR("")


def parse_args_with_argparse():
    parser = argparse.ArgumentParser(description='Give a default device.')
    parser.add_argument('-d', '--device', type=str, help='运行设备')
    parser.add_argument('-r', '--root', type=str, help='工程根目录')
    args, unknown = parser.parse_known_args()
    return args


try:
    args = parse_args_with_argparse()
    if args.device:
        client = guess_client(args.device)
    else:
        client = guess_client()
    if not client.window_size():
        print("设备异常")
        client = None

    if args.root:
        R = AsR(args.root)

except Exception as e:
    print("设备异常:", str(e))
    client = None
