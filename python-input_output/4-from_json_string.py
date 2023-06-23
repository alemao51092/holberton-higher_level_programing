#!/usr/bin/python3
"""shebang"""


import json


def from_json_string(my_str):
    """return an obj"""
    return json.loads(my_str)
