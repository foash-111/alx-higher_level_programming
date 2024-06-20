#!/usr/bin/python3
"""base class"""

from json import dumps


class Base:
    """my base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            # == self.__class__.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list into json string representation"""
        return dumps(list_dictionaries)
