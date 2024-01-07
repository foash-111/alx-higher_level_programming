#!/usr/bin/python3
"""
matrix division

return new matrix
"""


def matrix_divided(matrix, div):
    """
    matrix division for each element
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    row = []
    temp = len(matrix[0])

    for each_list in matrix:
        if len(each_list) != temp:
            raise TypeError("Each row of the matrix must have the same size")
        for each_element in each_list:
            if not isinstance(each_element, (int, float)):
                raise TypeError(" matrix must be a matrix (list of lists)\
                                 of integers/floats")

            result = each_element / div
            row.append(round(result, 2))
        new_list.append(row[:])
        row = []

    return new_list
