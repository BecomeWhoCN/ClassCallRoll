import csv
from collections import defaultdict
import random
from index import app
from flask import jsonify,request

def read_csv(filename="名单.csv"):
    data = defaultdict(list)  # 使用字典存储每个小组的名字列表

    with open(filename, "r", encoding="gbk") as file:
        reader = csv.DictReader(file)
        for row in reader:
            group_id = row["group"]
            data[group_id].append(row["name"])  # 将名字添加到对应的小组

    return data

@app.route('/api/groups', methods=['GET'])
def get_groups():
    data = read_csv()
    return jsonify(list(data.keys()))  # 返回所有小组的ID

@app.route('/api/draw', methods=['POST'])
def draw_people():
    data = request.json
    group_ids = data['group']  # 这里改为group_ids，因为现在可以有多个组ID
    num_people = int(data['numPeople'])
    save_history = data['history']  # 注意，你还没有实现这部分

    all_people = read_csv()

    if "all" in group_ids:
        winners = []
        for group, members in all_people.items():
            sampled_members = random.sample(members, min(num_people, len(members)))
            for member in sampled_members:
                winners.append({"name": member, "group": group})
    else:
        winners = []
        for group_id in group_ids:
            selected_group = all_people.get(group_id, [])
            if not selected_group or num_people > len(selected_group):
                continue  # 或者可以返回错误
            sampled_members = random.sample(selected_group, num_people)
            for member in sampled_members:
                winners.append({"name": member, "group": group_id})

    return jsonify(winners)
