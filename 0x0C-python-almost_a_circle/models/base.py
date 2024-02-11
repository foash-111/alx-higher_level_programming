#!/usr/bin/python3
"""base class"""

import json


class Base:
    """my base class"""
    __nb_objects = 0

    def __init__(self, id=None):

        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """accept an opject and return string representation of it"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save each objects' dict to a file """
        if list_objs is None:
            my_string = "[]"
        else:
            my_list = []
            for i in list_objs:
                my_list.append(i.to_dictionary())
            my_string = cls.to_json_string(my_list)

        with open(f"{cls.__name__}.json", "w") as file:
            file.write(my_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy
