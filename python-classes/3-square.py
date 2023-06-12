#!/usr/bin/python3

"""Write class Square that defines a square and the size"""


class Square:
    """ Define a square """

    def __init__(self, size=0):

        """ Instantiation """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        """ Calculet the area"""

        squarearea = self.__size * self.__size
        return squarearea
