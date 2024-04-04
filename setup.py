from distutils.core import setup
import py2exe

setup(
    console=['main.py'],  # 如果您的程序是GUI应用，请使用windows=[...]代替console=[...]
    options={
        "py2exe": {
            "includes": ["flask", "pandas", "numpy", "jinja2", "werkzeug"],  # 添加您的应用依赖的包
            "packages": ["flask", "pandas", "numpy"],
        }
    }
)