#!/usr/bin/python3
def uppercase(str):
    x = 0
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            x = ord(i) - 32
        else:
            x = ord(i)
        print("{}".format(chr(x)), end="")
    print("")
