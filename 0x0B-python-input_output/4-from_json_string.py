#!/usr/bin/python3
""" impor (json) java script object notation module"""


import json

"""a function returns JSON representation from string to its object"""


def from_json_string(my_str):
    """function that returns the JSON representation as object"""
    my_object = json.loads(my_str)
    return my_object
