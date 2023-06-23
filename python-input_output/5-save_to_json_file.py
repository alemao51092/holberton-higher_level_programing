#!/usr/bin/python3
"""shebang"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object"""

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
