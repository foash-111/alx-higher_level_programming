#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            counter += 1
        except (IndexError, TypeError, ValueError):
            print()
            return counter
    print()
    return counter
