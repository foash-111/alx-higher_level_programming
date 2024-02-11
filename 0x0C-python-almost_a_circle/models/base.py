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
