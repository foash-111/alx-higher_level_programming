#!/usr/bin/python3
"""
this is a 0-square module that that defines a square class
"""


class Square:
    """ a class Square that defines a square:"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if isinstance(position, tuple) and\
                len(position) == 2 and\
                isinstance(position[0], int) and\
                isinstance(position[1], int) and\
                position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.my_print()

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        return self.__size * self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
