#!/usr/bin/python3
"""shebang"""


import json


def load_from_json_file(filename):
    """creat an obj"""
    with open(filename, mode="r", encoding="utf-8") as file:
        json_str = file.read()
        python_obj = json.loads(json_str)
        return python_obj
