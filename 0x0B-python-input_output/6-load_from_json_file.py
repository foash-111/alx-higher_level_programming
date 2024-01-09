#!/usr/bin/python3
""" impor (json) java script object notation module"""


import json

"""a function that comeback the JSON representation as object from file"""


def load_from_json_file(filename):
    """function that comebacks the JSON representation as object from file"""
    with open(filename, "r") as file:
        my_object = json.load(file)
        return my_object
