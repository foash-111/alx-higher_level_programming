#!/usr/bin/python3
""""my rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")

        if type(height) is int:
            self.__height = height
        else:
            raise TypeError(" must be an integer")
        if height < 0:
            raise ValueError(" must be > 0")

        if type(x) is int:
            self.__x = x
        else:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")

        if type(y) is int:
            self.__y = y
        else:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__ = value
        else:
            raise TypeError(" must be an integer")
        if value < 0:
            raise ValueError(" must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int:
            self.__x = value
        else:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int:
            self.__y = value
        else:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
