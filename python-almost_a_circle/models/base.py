#!/usr/bin/python3
"""shebang"""


import json


class Base():
    """class"""

    __nb_objects = 0

    def __init__(self, id=None):
        "instantation"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "Returns the JSON representation of list_dictionaries"
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries is len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))