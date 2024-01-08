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
