#!/usr/bin/python3

"""class student"""


class Student:
    """define and retrive"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive instance as a dict"""
        return self.__dict__
