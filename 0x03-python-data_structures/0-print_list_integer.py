#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        if my_list is None:
            return
        for i in my_list:
            print("{}".format(i))
