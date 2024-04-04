from index import app
import webbrowser
import os

if __name__ == '__main__':
    from group import *
    if not os.environ.get("FLASK_RUN_FROM_RELOADER"):
        # 设置环境变量，表明此后的运行是由重载器触发的
        os.environ["FLASK_RUN_FROM_RELOADER"] = "1"
        # 打开默认浏览器并跳转到指定URL
        webbrowser.open("http://127.0.0.1:5022/")
    app.run(debug=True, port=5022)