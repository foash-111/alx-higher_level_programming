#!/usr/bin/python3
"""
class MyList that inherits from list

has a method print a sorted list
"""


class MyList(list):
    """ prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        """print list"""
        print(sorted(self))
