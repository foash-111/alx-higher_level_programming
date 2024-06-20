#!/usr/bin/python3
"""base class"""

from json import dumps, loads


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
    def to_dictionary(self):
        """retrun dict representation"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list into json string representation"""
        if list_dictionaries:
            return dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """itrate over list, convert to dict, append and dump into a file"""
        my_list = []

        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs:
                for i in list_objs:
                    my_dict = i.to_dictionary()
                    my_list.append(my_dict)

                file.write(cls.to_json_string(my_list))
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """return string as a object"""
        if json_string:
            return loads(json_string)
        else:
            return []
