#!/usr/bin/python3
"""
BaseGeometry class

return nothing
"""


class BaseGeometry:
    """area nothing"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

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
