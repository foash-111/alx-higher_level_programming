#!/usr/bin/python3
""" Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """call rectangle constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return information about the instance when we print it"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter method"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.width = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def update(self, *args, **kwargs):
        """update args--> tuple"""
        """update kwargs --> dictionary if args doesn't found"""

        if args:
            attributes = ("id", "size", "x", "y")
            for key, value in zip(attributes, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.width,
                "y": self.y}

