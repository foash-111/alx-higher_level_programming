#!/usr/bin/python3
"""
this is a 0-square module that that defines a square class
"""


class Square:
    """ a class Square that defines a square:"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = value
            return self.__size

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
            return self.__size

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                if self.position[1] > 0:
                    pass
                else:
                    for k in range(0, self.position[0]):
                        print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
