#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            output += chr(ord(i) - 32)
        else:
            output += chr(ord(i))

    print(output)
