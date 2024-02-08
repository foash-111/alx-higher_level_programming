#!/usr/bin/python3
"""
check  if the object is
an instance of a class that inherited
(directly or indirectly) from the specified class

return true if it is, false otherwise
"""


def inherits_from(obj, a_class):
    """check if the object is an instance of it's classess or not """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
