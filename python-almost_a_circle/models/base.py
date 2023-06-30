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
        "hoy gana el bolso"
        filename = f"{cls.__name__}.json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        "returns the list of the JSON string"
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "Returns an instance with all attrs already set"
        if cls.__name__ == "Rectangle":
            newby = cls(5, 5)
        else:
            newby = cls(5)
        newby.update(**dictionary)
        return newby

    @classmethod
    def load_from_file(cls):
        "Returns a list of instances"
        file_to_load = "{}.json".format(cls.__name__)
        loaded_list = []
        if not os.path.isfile(file_to_load):
            return []
        with open(file_to_load, 'r') as f:
            json_readed = f.read()

        json_list = cls.from_json_string(json_readed)

        for i in range(len(json_list)):
            loaded_list.append(cls.create(**json_list[i]))
        return loaded_list
