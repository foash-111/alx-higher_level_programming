#!/usr/bin/python3

"""
class MyInt that inherits from int

MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __init__(self, num):
        self.num = num
        super().__init__()

    def __str__(self):
        return "{}".format(self.num)

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
