from typing import Union
from ascript.ios import system
from ascript.ios.screen.gp import Point

KEY_HOME = "home"
KEY_VOLUMEUP = "volumeup"
KEY_volumedown = "volumedown"
KEY_POWER = "power"
KEY_SNAPSHOT = "snapshot"
KEY_POWER_AND_HOME = "power+home"


def click(x, y: int = 0, duration: float = 20):
    if isinstance(x, Point):
        y = x.y
        x = x.x


    x = int(x / system.client.scale)
    y = int(y / system.client.scale)
    system.client.click(x, y, duration / 1000)


def slide(x1: int, y1: int, x2: int, y2: int, duration: float = 20):
    x1 = int(x1 / system.client.scale)
    y1 = int(y1 / system.client.scale)
    x2 = int(x2 / system.client.scale)
    y2 = int(y2 / system.client.scale)
    system.client.swipe(x1, y1, x2, y2, duration / 1000)


def slide_left():
    system.client.swipe_left()


def slide_up():
    system.client.swipe_up()


def slide_right():
    system.client.swipe_right()


def slide_down():
    system.client.swipe_down()


def double_tap(x: int, y: int):
    system.client.double_tap(x, y)


def input(value):
    keys(value)


def keys(value):
    system.client.send_keys(value)


def key_press(key):
    system.client.press(key)


def key_press_hid(key, duration: float):
    system.client.press_duration(key, duration / 1000)
