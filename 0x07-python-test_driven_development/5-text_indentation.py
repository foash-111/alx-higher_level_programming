#!/usr/bin/python3
"""
print strings till . or ? or :

return Nothing
"""

#hello.
def text_indentation(text):
    length = 0
    current = 0
    for value in (text):
        print(value, end="")
        if value in {'.', ';', '?'}:
            print()
            print()
