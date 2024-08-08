import os
import shutil
import sys
import time
from flask import request, jsonify
from . import dao
from ascript.ios.developer.utils import worker, file_utils
from ascript.ios.developer.utils.env import get_asenv
from .utils import module_space, venv_space

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
developer_dir = os.path.dirname(os.path.dirname(__file__))
# print(current_dir)

run_process = None


def api(app):
    @app.route("/api/module/list", methods=['GET'])
    def api_module_list():
        modules = []
        for m in os.listdir(module_space):

            m_path = os.path.join(module_space, m)
            m_mime = os.path.getmtime(m_path)
            m_format_mime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(m_mime))
            m_length = file_utils.convert_bytes(file_utils.get_folder_size(m_path))
            ico_path = os.path.join(m_path, "res/img/logo.png")
            # print(ico_path)
            if os.path.isdir(m_path):
                m_dir = {
                    "name": m,
                    "lastModified": m_mime,
                    "lastModified_format": m_format_mime,
                    "length_format": m_length,
                    "ico": ico_path
                }
                modules.append(m_dir)

        return jsonify(dao.api_result(data=modules))

    @app.route("/api/module/rname", methods=['GET'])
    def api_module_rname():
        if "name" in request.args and "rename" in request.args:
            src_dir = os.path.join(module_space, request.args["name"])
            new_dir = os.path.join(module_space, request.args["rename"])
            try:
                os.rename(src_dir, new_dir)
            except Exception as e:
                return jsonify(dao.api_result_error(e))
            return jsonify(dao.api_result())
        else:
            return jsonify(dao.api_result(code=-1, msg="缺少参数name或rename"))

    @app.route("/api/module/remove", methods=['GET'])
    def api_module_remove():
        if "name" in request.args:
            src_dir = os.path.join(module_space, request.args["name"])
            try:
                shutil.rmtree(src_dir)
            except Exception as e:
                return jsonify(dao.api_result_error(e))
            return jsonify(dao.api_result())
        else:
            return jsonify(dao.api_result(code=-1, msg="缺少参数name"))

    @app.route("/api/module/create", methods=['GET'])
    def api_module_create():
        if "name" in request.args:
            module_dir = os.path.join(module_space, request.args["name"])
            try:
                os.makedirs(module_dir)
                # 创建 目录结构
                _init_file_ = os.path.join(module_dir, "main.py")
                with open(_init_file_, "w") as f:
                    f.write('print("Hello AS")')

                # 创建 res/ui 和 res/img/ 并拷贝logo
                img_dir = os.path.join(module_dir, "res/img/")
                os.makedirs(img_dir)
                ui_dir = os.path.join(module_dir, "res/ui/")
                os.makedirs(ui_dir)
                logo_img = os.path.join(img_dir, "logo.png")

                src_img = os.path.join(developer_dir, "assets/templates/static/img/ico/ico_testing.png")
                print("路径", src_img, logo_img)
                shutil.copy(src_img, logo_img)

            except Exception as e:
                return jsonify(dao.api_result_error(e))
            return jsonify(dao.api_result())
        else:
            return jsonify(dao.api_result(code=-1, msg="缺少参数name"))

    @app.route("/api/module/files", methods=['GET'])
    def api_module_files():
        if "name" in request.args:
            module_dir = os.path.join(module_space, request.args["name"])
            if not os.path.exists(module_dir):
                return dao.api_result_error(Exception("工程不存在"))
            return jsonify(dao.api_result(data=file_utils.get_module_files({}, module_dir)))
        else:
            return jsonify(dao.api_result(code=-1, msg="缺少参数name"))

    @app.route("/api/module/run", methods=['GET'])
    def api_module_run():
        api_module_stop()
        if "name" in request.args and "device" in request.args and "venv" in request.args:
            module_dir = os.path.join(module_space, request.args["name"])
            src_dir = os.path.join(venv_space, request.args["venv"])
            if sys.platform == 'win32':
                python_path = os.path.join(src_dir, "Scripts/python.exe")
            else:
                python_path = os.path.join(src_dir, "bin/python")
            module_name = request.args["name"]
            cmds = [python_path, "-m", f"{module_name}.main", "-d", request.args["device"], "-r", module_dir]

            print(cmds)

            if os.path.exists(python_path):
                worker.run_script(cmds, module_space)
                # global run_process
                # run_process = subprocess.Popen(cmds, cwd=module_space, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            return jsonify(dao.api_result(data={}))
        else:
            return jsonify(dao.api_result(code=-1, msg="缺少参数name"))

    @app.route("/api/module/stop", methods=['GET'])
    def api_module_stop():
        if worker.run_process:
            worker.run_process.kill()
            # worker.run_process = None
        return jsonify(dao.api_result(data={}))
