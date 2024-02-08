#!/usr/bin/python3
"""
print square with #

return nothing
"""


def print_square(size):
    """print a square with #"""
    if size is None:
        raise TypeError("size isn't existed")
    if (isinstance(size, float) and size < 0) or not\
            isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
