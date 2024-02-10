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
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is int:
            self.__x = x
        else:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is int:
            self.__y = y
        else:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

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
            raise ValueError("x must be >= 0")

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
            raise ValueError("y must be >= 0")

    def area(self):
        """get rectangle area"""
        return self.__width * self.__height

    def display(self):
        """display rectangle with #"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method
        return information about the instance when we print it"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update my arguments in order considered
        the number of arguments passed"""
        attributes = ("id", "width", "height", "x", "y")

        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

        for key,cntt in kwargs.items():
            self.__dict__[key] = cntt
