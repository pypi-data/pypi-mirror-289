#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/5 14:04
# @Author  : 曹智辉
# @File    : save_data_tool.py
# @Description : 保存数据工具
import json
import os

class SaveData:
    def __init__(self, functionality, feature_branch, analysis_functionality, analysis_data=None, id=None, type=None,
                 content=None, comments_example=None, start_time=None, end_time=None):
        self.functionality = functionality
        self.feature_branch = feature_branch
        self.analysis_functionality = analysis_functionality
        self.analysis_data = analysis_data
        self.id = id
        self.type = type
        self.content = content
        self.comments_example = comments_example
        self.start_time = start_time
        self.end_time = end_time

    def to_json(self):
        data = {
            "功能模块": self.functionality,
            "功能分支": self.feature_branch,
            "具体功能": self.analysis_functionality,
            "分析数据": {
                self.id: {
                    "type": self.type,
                    "data": self.analysis_data,
                    "content": self.content,
                    "comments_example": self.comments_example,
                    "start_time": self.start_time,
                    "end_time": self.end_time
                }
            }
        }
        return json.dumps(data)

def save_data_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2,ensure_ascii=False)


def load_data_from_file(file_path):
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        if data:
            return json.loads(data)
        else:
            return []

def add_data(data, file_path):
    existing_data = load_data_from_file(file_path)

    new_data = {
        "type": data.type,
        "data": data.analysis_data,
        "content": data.content,
        "comments_example": data.comments_example,
        "start_time": data.start_time,
        "end_time": data.end_time
    }

    found = False
    for item in existing_data:
        if item["功能模块"] == data.functionality and item["功能分支"] == data.feature_branch and item["具体功能"] == data.analysis_functionality:
            item["分析数据"].update({data.id: new_data})
            found = True
            break

    if not found:
        new_item = {
            "功能模块": data.functionality,
            "功能分支": data.feature_branch,
            "具体功能": data.analysis_functionality,
            "分析数据": {data.id: new_data}
        }
        existing_data.append(new_item)

    save_data_to_file(existing_data, file_path)


def delete_data(data, id, file_path):
    existing_data = data.load_data_from_file(file_path)
    if id in existing_data["分析数据"]:
        del existing_data["分析数据"][id]
        save_data_to_file(existing_data, file_path)


def update_data(data, id, updated_data, file_path):
    existing_data = load_data_from_file(file_path)

    for item in existing_data:
        if item["功能模块"] == data.functionality and item["功能分支"] == data.feature_branch and item["具体功能"] == data.analysis_functionality:
            if id in item["分析数据"]:
                item["分析数据"][id].update(updated_data)
                save_data_to_file(existing_data, file_path)
                return True

    return False


def get_data(data, file_path, data_id = None, get_data_type = None):
    existing_data = load_data_from_file(file_path)

    for item in existing_data:
        if item["功能模块"] == data.functionality and item["功能分支"] == data.feature_branch and item["具体功能"] == data.analysis_functionality:
            if get_data_type == "all":
                return item["分析数据"]
            if data_id in item["分析数据"]:
                return item["分析数据"][data_id]

    return None
