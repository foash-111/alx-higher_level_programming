#!/usr/bin/python3

"""function that appends a text into a file"""


def append_write(filename="", text=""):
    """function that appends a text into a file"""
    with open(filename, "a") as file:
        n_chars_read = file.write(text)
        return n_chars_read
