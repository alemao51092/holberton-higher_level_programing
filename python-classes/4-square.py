#!/usr/bin/python3

"""Write class Square that defines a square and the size"""


class Square:
    """ Define a square """

    def __init__(self, size=0):

        """ Instantiation """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """ Calculet the area"""

        squarearea = self.__size * self.__size
        return squarearea
