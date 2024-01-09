#!/usr/bin/python3
"""
BaseGeometry class

return nothing
"""


class BaseGeometry:
    """area nothing"""

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
class Rectangle that inherits from BaseGeometry

with method init for width, height
"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area implemented """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""
class Square that inherits from Rectangle

with method init for size
inhert area method from rectangle
"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """initiation method , validate size, get area"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
