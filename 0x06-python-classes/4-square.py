#!/usr/bin/python3
"""
this is a 0-square module that that defines a square class
"""


class Square:
    """ a class Square that defines a square:"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    def size(self, value):
        self.__size = value
