#!/usr/bin/python3

"""class student"""


class Student:
    """define and retrive instance as a object"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive any instance from the class as a dict object"""
        return self.__dict__
