#!/usr/bin/python3
"""shebang"""


def matrix_divided(matrix, div):
    typ = TypeError
    zerr = ZeroDivisionError
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise typ("div must be a number")
    if div == 0:
        raise zerr("division by zero")

    first_row_length = len(matrix[0])
    div_matrix = []
    for row in matrix:
        if len(row) != first_row_length:
            raise typ("Each row of the matrix must have the same size")
        if any(not isinstance(item, (int, float)) for item in row):
            raise typ(err)

        div_row = [round(element / div, 2) for element in row]
        div_matrix.append(div_row)

    return div_matrix
