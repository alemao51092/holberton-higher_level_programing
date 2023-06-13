#!/usr/bin/python3
"""shebang"""


def matrix_divided(matrix, div):
    """divide matrix"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    divmatrix = []
    firstrowlenght = len(matrix[0])
    for row in matrix:
        if len(row) != firstrowlenght:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div is None:
        raise TypeError("missing 1 required positional argument: 'div'")
    for row in matrix:
        divrow = [round(element / div, 2) for element in row]
        divmatrix.append(divrow)
    return divmatrix
