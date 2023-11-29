#!/usr/bin/python3

for i in range(0, 99):
    if (i < 10):
        print("{} = 0x{}".format(i, i))
    else:
        print("{} = {}".format(i, hex(i)))
