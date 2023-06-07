#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        squarerow = []
        for num in row:
            squarenum = num ** 2
            squarerow.append(squarenum)
        newmatrix.append(squarerow)
    return newmatrix
