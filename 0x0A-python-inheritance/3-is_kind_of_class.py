#!/usr/bin/python3
"""
check if the object is an instance of, or
if the object is an instance of a class that inherited from

return true if it is, false otherwise
"""


def is_kind_of_class(obj, a_class):
    """check if the object is an instance of it's classess or not """
    return isinstance(obj, a_class)
