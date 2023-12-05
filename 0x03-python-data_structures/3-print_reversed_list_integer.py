#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # if (my_list == None):// erorr in pycode style
    # was wrong in pystyle code because 'is' and '==' aren't the same
    # It's important to note that == checks for equality in value,
    # while is checks for equality in identity
    # (i.e., both variables point to the exact same object). For example:
    # list1 = [1, 2, 3]
    # list2 = [1, 2, 3]
    # print(list1 == list2)  # Outputs: True
    # print(list1 is list2)  # Outputs: False

    if (my_list is None):
        return None
    count = -1
    for i in my_list:
        print("{:d}".format(my_list[count]))
        count -= 1
