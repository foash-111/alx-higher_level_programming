#!/usr/bin/python3

"""function that writes a text into a file"""


def write_file(filename="", text=""):
    """function that writes a text into a file"""
    with open(filename, "w+") as file:
        n_chars_read = file.write(text)
        return n_chars_read
