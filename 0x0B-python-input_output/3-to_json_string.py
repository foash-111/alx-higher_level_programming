#!/usr/bin/python3
""" impor (json) java script object notation module"""


import json

"""a function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """function that returns the JSON representation as str"""
    string = json.dumps(my_obj)
    return string
