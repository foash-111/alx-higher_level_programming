#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # new_tuple = ()
    # count = 0
    # for i in range(0, 2):
    #     if (tuple_a is None):
    #         tuple_a = 0
    #     if (tuple_b is None):
    #             tuple_b = 0
    #     new_tuple[count] = tuple_a[count] + tuple_b[count]

    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    new_tuple = (a[0] + b[0], a[1] + b[1])
    return (new_tuple)
