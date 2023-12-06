#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        count = 0
        for i in my_list:
            if (i == search):
                new_list.append(replace)
            else:
                new_list.append(i)
            count += 1
        return new_list
