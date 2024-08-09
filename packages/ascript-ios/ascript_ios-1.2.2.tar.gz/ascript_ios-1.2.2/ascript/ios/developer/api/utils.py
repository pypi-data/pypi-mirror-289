import os
import shutil
import sys

from ascript.ios.developer.utils.env import get_asenv
home_dir = get_asenv()["home"]
module_space = os.path.join(home_dir, 'modules')
venv_space = os.path.join(home_dir, 'envs')
cache = os.path.join(home_dir, 'data', "cache")
data_space = os.path.join(home_dir, 'data')
screen_shot_dir = os.path.join(data_space, 'screenshot')
gp_home_dir = os.path.join(data_space, 'gp')

if not os.path.exists(screen_shot_dir):
    os.makedirs(screen_shot_dir)

if not os.path.exists(gp_home_dir):
    os.makedirs(gp_home_dir)

sys.path.append(gp_home_dir)

if not os.path.exists(module_space):
    os.makedirs(module_space)

if not os.path.exists(cache):
    os.makedirs(cache)
else:
    # 删除文件夹及其内容
    shutil.rmtree(cache, ignore_errors=True)
    # 重新创建文件夹
    os.makedirs(cache, exist_ok=True)


def path_home_filter(path):
    if path.startswith("~/"):
        path = os.path.join(home_dir, path.replace("~/", ""))
    elif path.startswith("/~/"):
        path = os.path.join(home_dir, path.replace("/~/", ""))


    return path