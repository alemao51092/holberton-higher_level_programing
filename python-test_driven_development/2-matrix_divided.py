#!/usr/bin/python3
"""shebang"""


def matrix_divided(matrix, div):
    """divide matrix"""
    frl = len(matrix[0])
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != frl:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div is None:
        raise TypeError("missing 1 required positional argument: 'div'")
    dm = []
    for row in matrix:
        dr = [round(e / div, 2) for e in row]
        dm.append(dr)
    return dm
