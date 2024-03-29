#!/usr/bin/python3

"""
check if the file is exist

read from command line ..
store at a file
"""


from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = load_from_json_file("add_item.json")
if my_list is None:
    my_list = []

i = 1

while i < len(argv):
    my_list.append(str(argv[i]))
    i += 1

save_to_json_file(my_list, "add_item.json")
