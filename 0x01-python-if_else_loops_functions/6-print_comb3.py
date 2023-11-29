#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if (i == 8 and j == 9):
            print("{}{}".format(i, j))
            break
        if (i == j or j < i):
            continue
        else:
            print("{}{}".format(i, j), end=", ")
