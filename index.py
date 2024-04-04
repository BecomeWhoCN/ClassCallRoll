from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import os
import sys

# 使用getattr安全地获取sys._MEIPASS，如果不存在则回退到当前文件的目录
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder=os.path.join(base_path, 'templates'), static_folder=os.path.join(base_path, 'static'))

class CallTheRoll:
    def __init__(self):
        # 尝试使用GBK编码读取，如果失败则尝试UTF-8
        try:
            self.data = pd.read_csv('名单.csv', encoding='gbk')
        except UnicodeDecodeError:
            self.data = pd.read_csv('名单.csv', encoding='utf-8')
        self.called_names = []

    # 在服务器端加载CSV文件并计算数量
    @staticmethod
    def load_csv_and_get_count():
        # 尝试使用GBK编码读取，如果失败则尝试UTF-8
        try:
            data = pd.read_csv('名单.csv', encoding='gbk')
        except UnicodeDecodeError:
            data = pd.read_csv('名单.csv', encoding='utf-8')
        count = len(data)
        return count

    def weighted_random_choice(self):
        if len(self.data) == 0:
            return "所有人都已被点过名了!"
        probabilities = self.data['chance'] / sum(self.data['chance'])
        selected = np.random.choice(self.data['name'], p=probabilities)
        self.called_names.append(selected)
        self.data = self.data[self.data['name'] != selected]
        return selected

    def reset(self):
        try:
            self.data = pd.read_csv('名单.csv', encoding='gbk')
        except UnicodeDecodeError:
            self.data = pd.read_csv('名单.csv', encoding='utf-8')
        self.called_names = []

    def weighted_random_choice(self, n=1):
        if len(self.data) < n:
            return ["名单中的人数不足"]
        selected_names = self.data.sample(n=n, weights=self.data['chance']).to_dict(orient='records')
        for name_record in selected_names:
            self.called_names.append(name_record['name'])
            self.data = self.data[self.data['name'] != name_record['name']]
        return selected_names

call_the_roll = CallTheRoll()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_total_count')
def get_total_count():
    total_count = load_csv_and_get_count()
    return jsonify({"total_count": total_count})

@app.route('/call_name')
def call_name():
    selected_names = call_the_roll.weighted_random_choice(1)
    if selected_names:
        selected_name = selected_names[0]['name']
        selected_id = selected_names[0]['id']
        return jsonify({"id": selected_id, "name": selected_name})
    else:
        return jsonify({"id": None, "name": "所有人都已被点过名了!"})


@app.route('/reset')
def reset():
    call_the_roll.reset()
    return "Reset successful!"

@app.route('/call_names/<int:n>')
def call_names(n):
    selected_names = call_the_roll.weighted_random_choice(n)
    return jsonify(selected_names)

@app.route('/exit')
def exit_app():
    os.kill(os.getpid(), signal.SIGINT)
    return "Exiting..."

@app.route('/get_called_names')
def get_called_names():
    return jsonify(call_the_roll.called_names)

@app.route('/readme')
def readme_page():
    return render_template('readme.html')

@app.route('/group')
def group_page():
    return render_template('group.html')

@app.route('/update_csv', methods=['POST'])
def update_csv():
    action = request.form.get('action')

    if action == "delete_and_update":
        call_the_roll.reset()
        return "记录已删除，CSV已更新！"
    
    elif action == "directly_update":
        return "CSV更新！"
    
    else:
        return "操作已取消！"  # 默认返回

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
    if action == "delete_and_update":
        call_the_roll.reset()
        return "记录已删除，CSV已更新！"
    
    elif action == "directly_update":
        return "CSV更新！"
    
    else:
        return "操作已取消！"
