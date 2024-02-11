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
        """creat an instant like r1 = rectangle(10,,,etc)"""
        dummy = cls(**dictionary)
        """validate it's attributes by update"""
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """print instances that exist in a file"""
        # open a file
        my_list = []
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                my_string = file.read()
        except FileNotFoundError:
            return []
        # load the list of dicts from the file
        list_of_dicts = cls.from_json_string(my_string)
        # for each dict creat an instance with it's attributes
        # and append each instance for a list
        for dic in list_of_dicts:
            my_list.append(cls.create(**dic))
        # return list
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save each objects' dict to a file """
        if list_objs is None:
            my_string = "[]"
        else:
            my_list = []
            for i in list_objs:
                my_list.append(i.to_dictionary())
            my_string = cls.to_json_string(my_list)

        with open(f"{cls.__name__}.csv", "w") as file:
            file.write(my_string)

    @classmethod
    def load_from_file_csv(cls):
        """print instances that exist in a file"""
        # open a file
        my_list = []
        try:
            with open(f"{cls.__name__}.csv", "r") as file:
                my_string = file.read()
        except FileNotFoundError:
            return []
        # load the list of dicts from the file
        list_of_dicts = cls.from_json_string(my_string)
        # for each dict creat an instance with it's attributes
        # and append each instance for a list
        for dic in list_of_dicts:
            my_list.append(cls.create(**dic))
        # return list
        return my_list
