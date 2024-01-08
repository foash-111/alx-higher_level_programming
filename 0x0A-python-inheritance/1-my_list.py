#!/usr/bin/python3
"""
class MyList that inherits from list

has a method print a sorted list
"""


class MyList(list):
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        if not all(isinstance(i, int) for i in self):
            raise TypeError("all elements must be integers")
        else:
            print(sorted(self))
