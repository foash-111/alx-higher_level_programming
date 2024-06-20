#!/usr/bin/python3
""""my rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)

        self.__width = width
        if type(self.__width) is not int:
            raise TypeError('width must be an integer')
        if self.__width <= 0:
            raise ValueError("width must be > 0")

        self.__height = height
        if type(self.__height) is not int:
            raise TypeError('height must be an integer')
        if self.__height <= 0:
            raise ValueError("height must be > 0")

        self.__x = x
        if type(self.__x) is not int:
            raise TypeError('x must be an integer')
        if self.__x < 0:
            raise ValueError("x must be >= 0")

        self.__y = y
        if type(self.__y) is not int:
            raise TypeError('y must be an integer')
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(self.__width) is not int:
            raise TypeError('width must be an integer')
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(self.__height) is not int:
            raise TypeError('height must be an integer')
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(self.__x) is not int:
            raise TypeError('x must be an integer')
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(self.__y) is not int:
            raise TypeError('y must be an integer')
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """compute area and return it"""
        return self.__width * self.__height

    def display(self):
        """display rectangle using #"""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """consider *args as incoming tuple and **kwargs as a dictionary"""
        if args:
            defualt_arguments = ("id", "width", "height", "x", "y")
            for key, value in zip(defualt_arguments, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
