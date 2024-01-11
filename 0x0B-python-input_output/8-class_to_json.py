#!/usr/bin/python3

"""convert any object from any class to dictionary"""


def class_to_json(obj):
    """return class' object as a dict object"""
    return obj.__dict__
