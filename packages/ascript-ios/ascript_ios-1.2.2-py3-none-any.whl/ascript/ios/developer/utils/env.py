import requests

from ascript.ios import wdapy

host = "http://127.0.0.1"

def get_asenv():
    response = requests.get("http://127.0.0.1:9097/env")
    if response.status_code == 200:
        env = response.json()["data"]
        return env


def get_devices():
    response = requests.get("http://127.0.0.1:9097/api/device")
    if response.status_code == 200:
        devices = response.json()["data"]
        return devices


def get_client(device_id: str) -> wdapy.AppiumUSBClient:
    for device in get_devices():
        if device["udid"] == device_id:
            return wdapy.AppiumUSBClient(device['udid'])
