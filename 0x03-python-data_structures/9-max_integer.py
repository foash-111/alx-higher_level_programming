#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        temp = int(i)
        for i in my_list:
            if (int(i) >= temp):
                temp = int(i)
        return (temp)
    else:
        return None
