#!/usr/bin/python3
"""base class"""

from json import dumps, dump


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
        if list_dictionaries:
            return dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def to_dictionary(self):
        """retrun dict representation"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    @classmethod
    def save_to_file(cls, list_objs):
        """itrate over list, convert to dict, append and dump into a file"""
        my_list = []
        for i in list_objs:
            my_dict = i.to_dictionary()
            my_list.append(my_dict)

        my_string = cls.to_json_string(my_list)

        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs:
                dump(my_string, file)
            else:
                dump("[]", file)
