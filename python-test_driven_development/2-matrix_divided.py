#!/usr/bin/python3
"""shebang"""


def matrix_divided(matrix, div):
    """divide matrix"""
    firstrowlenght = len(matrix[0])
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != firstrowlenght:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divmatrix = []
    for row in matrix:
        divrow = [round(element / div, 2) for element in row]
        divmatrix.append(divrow)
    return divmatrix
