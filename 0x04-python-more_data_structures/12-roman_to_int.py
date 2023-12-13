#!/usr/bin/python3

# I	V	X	L	C	D	M
# 1	5	10	50	100	500	1000

def roman_to_int(roman_string):
    sum = 0
    temp = 0
    # The isinstance() function in Python is used to
    # check if an object or variable
    # is an instance of a particular class or type.

    # If roman_string is a string, isinstance(roman_string, str)
    # will return True. If roman_string is not a string
    # (for example, if it's an integer, a list, or None),
    # isinstance(roman_string, str) will return False.
    if isinstance(roman_string, str):
        # 246 = CC + XL + VI = CCXLVI.
        # 789 = DCC + LXXX + IX = DCCLXXXIX.
        for i in roman_string:
            if i == "I":
                i = 1
            elif i == "V":
                i = 5
            elif i == "X":
                i = 10
            elif i == "L":
                i = 50
            elif i == "C":
                i = 100
            elif i == "D":
                i = 500
            elif i == "M":
                i = 1000
            else:
                return 0
            sum += i
            if (i > temp):
                sum -= (temp * 2)
            temp = i
        return sum
    else:
        return 0
