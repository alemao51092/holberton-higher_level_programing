#!/usr/bin/python3

"""Write class Square that defines a square and the size"""


class Square:
    """ Define a square """

    def __init__(self, size=0, position=(0, 0)):

        """ Instantiation """
        self.__size = size
        self.__position = position

        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[0])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[1])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

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

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
