#!/usr/bin/python3

"""
print full name

return nothing
"""


def say_my_name(first_name, last_name=""):
    """
    print full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
