#!/usr/bin/python3

"""class student"""


class Student:
    """define and retrive instance as a object"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrive any instance from the class as a dict object"""
        my_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for key in attrs:
                if key in self.__dict__:
                    value = self.__dict__.get(key)
                    my_dict[key] = value
        return my_dict



        
