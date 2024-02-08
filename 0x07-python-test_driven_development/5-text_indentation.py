#!/usr/bin/python3
"""
print strings till . or ? or :

return Nothing
"""

#hello.
def text_indentation(text):
    """print \n\n after . , ?"""
    length = 0
    current = 0
    if type(text) is str:
        for value in (text):
            print(value, end="")
            if value in {'.', '?', ':'}:
                print()
                print()
    else:
        raise TypeError("text must be a string")
