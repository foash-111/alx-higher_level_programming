#!/usr/bin/python3
""" impor (json) java script object notation module"""


import json

"""a function that writes the JSON representation of an object as (string)"""


def save_to_json_file(my_obj, filename):
    """function that writes the JSON representation as str into file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
