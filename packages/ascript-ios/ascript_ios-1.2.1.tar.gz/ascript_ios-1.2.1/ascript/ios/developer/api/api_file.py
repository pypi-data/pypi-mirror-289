import io
import json
import mimetypes
import os
import shutil
import sys
import time

from PIL import Image
from flask import request, send_file, Response, jsonify

from ascript.ios.developer.api import dao
from ascript.ios.developer.api.utils import module_space, cache, home_dir, path_home_filter
from ascript.ios.developer.utils import file_utils

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

def api(app):
    @app.route("/api/file/get", methods=['GET'])
    def api_file_get():
        if "path" in request.args:
            file_path = os.path.join(module_space, path_home_filter(request.args["path"]))
            if not os.path.exists(file_path):
                return "File does not exist", 404

            mine_type, _ = mimetypes.guess_type(file_path)
            if not mine_type:
                mine_type = "application/octet-stream"

            return send_file(file_path, mimetype=mine_type)

        else:
            return "path缺少参数", 404

    @app.route("/api/file/copy", methods=['POST'])
    def api_file_copy():
        source_path = request.form.get("source")
        target_path = request.form.get("target")
        source_path = path_home_filter(source_path)
        target_path = path_home_filter(target_path)

        if not os.path.exists(os.path.dirname(target_path)):
            os.makedirs(os.path.dirname(target_path))

        print(source_path,target_path)
        shutil.copy(source_path,target_path)
        return dao.api_result()

    @app.route("/api/file/get/image", methods=['GET'])
    def api_file_get_image():
        if "path" in request.args:
            file_path = os.path.join(module_space, request.args["path"])
            if not os.path.exists(file_path):
                return "File does not exist", 404
            max_height = -1
            if 'maxheight' in request.args:
                max_height = int(request.args['maxheight'])

            if max_height < 0:
                return api_file_get()
            else:
                with Image.open(file_path) as img:
                    width, height = img.size
                    target_width = int(width * (max_height / height))
                    resized_img = img.resize((target_width, max_height))
                    byte_arr = io.BytesIO()
                    resized_img.save(byte_arr, format='PNG')
                    byte_arr = byte_arr.getvalue()
                    return Response(byte_arr, mimetype='image/png')
        else:
            return "path缺少参数", 404

    @app.route("/api/file/save", methods=['POST'])
    def api_file_save():
        file_path = request.form.get("path")
        content = request.form.get("content")
        print(content)
        if file_path and content:
            if not os.path.exists(file_path):
                return "File does not exist", 404

            with open(file_path, "w", newline='\n', encoding="utf-8") as f:
                f.write(content)

            return dao.api_result()

        else:
            return "缺少参数[path,content]", 404

    @app.route("/api/file/create", methods=['POST'])
    def api_file_create():
        file_path = request.form.get("path")
        file_name = request.form.get("name")
        file_type = request.form.get("type")
        if file_path and file_name and file_type:

            if file_path.startswith("~/"):
                file_path = os.path.join(home_dir, file_path.replace("~/", ""))

            new_file = os.path.join(file_path, file_name)
            print(new_file, file_type)

            if file_type == "file":

                if not os.path.exists(os.path.dirname(new_file)):
                    os.makedirs(os.path.dirname(new_file))

                with open(new_file, "w") as f:
                    pass
            else:
                os.makedirs(new_file)

            return dao.api_result()

        else:
            return "缺少参数 path,name,type", 404

    @app.route("/api/file/remove", methods=['POST'])
    def api_file_remove():
        file_path = request.form.get("path")
        file_path = path_home_filter(file_path)
        print("删除", file_path)
        if file_path:
            if os.path.exists(file_path):
                if os.path.isfile(file_path):
                    os.remove(file_path)
                else:
                    shutil.rmtree(file_path)
            return dao.api_result()

        else:
            return "缺少参数 path", 404

    @app.route("/api/file/finder", methods=['POST'])
    def api_file_finder():
        file_path = request.form.get("path")
        if file_path:
            if os.path.isfile(file_path):
                os.startfile(os.path.dirname(file_path))
            else:
                os.startfile(file_path)

            return dao.api_result()

        else:
            return "缺少参数 path", 404

    @app.route("/api/file/rename", methods=['POST'])
    def api_file_rename():
        src_file = request.form.get("path")
        file_rname = request.form.get("name")
        new_file = os.path.join(os.path.dirname(src_file), file_rname)
        if src_file and file_rname:
            os.rename(src_file, new_file)
            return dao.api_result()
        else:
            return "缺少参数 path", 404

    @app.route("/api/file/image/crop", methods=['POST'])
    def api_file_image_crop():
        img_path = request.form.get("image")
        rect = json.loads(request.form.get("rect"))
        target_path = request.form.get("target")
        if target_path is None:
            target_path = os.path.join(cache,f"{time.time()}.png")
        with Image.open(img_path) as img:
            cropped_img = img.crop(rect)
            # 保存裁剪后的图像

            if not os.path.exists(os.path.dirname(target_path)):
                os.makedirs(os.path.dirname(target_path))

            cropped_img.save(target_path)

        return dao.api_result(data=target_path)

    @app.route("/api/files", methods=['POST'])
    def api_files():
        path = request.form.get("path")
        return jsonify(dao.api_result(data=file_utils.get_module_files({}, path)))