#!/usr/bin/python3
"""
check if the object is from specific class

return true or false
"""


def is_same_class(obj, a_class):
    """
    check if the instance type is from specific class
    """

    if type(obj) is a_class:
        return True
    else:
        return False
