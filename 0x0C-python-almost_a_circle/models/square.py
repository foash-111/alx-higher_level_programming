#!/usr/bin/python3
""" Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):

        if type(size) is not int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError("width must be > 0")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """consider *args as an incoming tuple and **kwargs as a dictionary"""
        if args:
            defualt_args = ("id", "size", "x", "y")

            for key, value in zip(defualt_args, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """retrun dict representation"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
