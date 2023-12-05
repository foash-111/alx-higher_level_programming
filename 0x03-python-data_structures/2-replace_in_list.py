#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    else:
        count = 0
        for i in my_list:
            if (count == idx):
                my_list[count] = element
                return (my_list)
            count = count + 1
