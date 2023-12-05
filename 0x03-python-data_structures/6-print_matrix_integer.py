#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (matrix is not None):
        for i in matrix:
            count = 0
            for j in i:
                if count == 0:
                    print("{:d}".format(j), end="")
                else:
                    print(" {:d}".format(j), end="")
                count += 1
            print("")
