#!/usr/bin/python3
"""base class"""

from json import dumps, loads, load


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

    # @staticmethod
    # def to_dictionary(self):
    #     """retrun dict representation"""
    #     return {"id": self.id, "width": self.width,
    #             "height": self.height, "x": self.x, "y": self.y}

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

    # def update(self, *args, **kwargs):
    #     """consider *args as an incoming tuple, **kwargs as a dictionary"""
    #     if args:
    #         defualt_arguments = ("id", "width", "height", "x", "y")
    #         for key, value in zip(defualt_arguments, args):
    #             setattr(self, key, value)
    #     else:
    #         for key, value in kwargs.items():
    #             setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """load a json string from a file and return it as an objects"""

        with open('{}.json'.format(cls.__name__)) as file:
            my_string = file.read()
            my_objects = cls.from_json_string(my_string)
            mylist = []
            for i in my_objects:
                mylist.append(cls.create(**i))
            return mylist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """itrate over list, convert to dict, append and dump into a file"""
        my_list = []

        with open("{}.csv".format(cls.__name__), "w") as file:
            if list_objs:
                for i in list_objs:
                    my_dict = i.to_dictionary()
                    my_list.append(my_dict)

                file.write(cls.to_json_string(my_list))
            else:
                file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """load a json string from a file and return it as an objects"""

        with open('{}.csv'.format(cls.__name__)) as file:
            my_string = file.read()
            my_objects = cls.from_json_string(my_string)
            mylist = []
            for i in my_objects:
                mylist.append(cls.create(**i))
            return mylist
