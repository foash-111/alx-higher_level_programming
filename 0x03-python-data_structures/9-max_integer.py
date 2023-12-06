#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        temp = my_list[0]
        for i in my_list:
            if (int(i) >= temp):
                temp = int(i)
        return (temp)
    else:
        return None
