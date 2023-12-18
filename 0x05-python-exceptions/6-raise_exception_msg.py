#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(" erorrrr")
    except NameError:
        print(message)
