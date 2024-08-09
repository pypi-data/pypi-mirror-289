import os.path
import threading

from flask import Flask, render_template, request
from gevent import pywsgi

from ascript.ios.developer.api import api_module, api_file, api_screen, api_node

current_dir = os.path.dirname(__file__)
print("当前目录",current_dir)
template_folder = os.path.join(current_dir, 'assets/templates')
static_folder = os.path.join(current_dir, 'assets/templates/static')
print(template_folder, static_folder)
static_url_path = '../../assets'

app = Flask(__name__, template_folder=template_folder,
            static_folder=static_folder)

api_module.api(app)
api_file.api(app)
api_screen.api(app)
api_node.api(app)


@app.route("/")
def page_home():
    return render_template("index.html")


@app.route("/modules.html")
def modules():
    return render_template("modules.html")


@app.route("/editor.html")
def editor():
    return render_template("editor.html")


@app.route("/vtree.html")
def vtree():
    return render_template("vtree.html")

@app.route("/screen.html")
def screen():
    return render_template("screen.html")


@app.route("/api/<string:m>")
def page_hwnd():
    return render_template("hwnd.html")


@app.route("/colors")
def page_colors():
    return render_template("colors.html")


@app.route("/api/tool/capture")
def api_tool_capture():
    pass


@app.route("/api/stop")
def api_stop():
    close()

web_server = None
web_server_thread = None
stop = False


def run_worker():
    # webbrowser.open("http://127.0.0.1:9096", new=2, autoraise=True)
    # app.run(host='0.0.0.0', port=9096)
    global web_server
    web_server = pywsgi.WSGIServer(('0.0.0.0', 9096), app)

    # app.debug = True
    web_server.serve_forever()


def run():
    global web_server_thread
    web_server_thread = threading.Thread(target=run_worker, daemon=True)
    web_server_thread.start()


def close():
    print("close")
    global stop
    stop = True
