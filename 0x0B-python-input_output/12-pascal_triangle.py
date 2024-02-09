#!/usr/bin/python3
"""pascal_triangle problem"""


def pascal_triangle(n):
    """
    >>> pascal_triangle(0)
    []
    >>> pascal_triangle(-1)
    []
    >>> pascal_triangle(5)
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    [1,5,5,5,5,1]
    [1,6,7,8,7,6,1]
    """
    my_list = []
    if n <= 0:
        return my_list
    else:
        if n == 1:
            return [1]
        temp = [1, 1]
        for i in range(1, n + 1):
            row_list = [1]
            for j in range(1, i):
                if j == i - 1:
                    row_list.append(1)
                else:
                    row_list.append(temp[j] + temp[j - 1])

            temp = row_list.copy()
            my_list.append(row_list)
        return (my_list)
