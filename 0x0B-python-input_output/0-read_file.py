#!/usr/bin/python3

"""function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:"""
    with open(str(filename), "r") as file:
        for line in file:
            print(line, end="")
