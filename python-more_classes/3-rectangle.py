#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """ A rectangle with a width and height. """

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Calculet the area"""
        rectanarea = self.__width * self.__height
        return rectanarea

    def perimeter(self):
        """ Calculate Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeterrectang = (self.__width + self.__height) * 2
        return perimeterrectang

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        rectangulo = ""
        for k in range(self.__height):
            for j in range(self.__width):
                rectangulo += "#"
            if k < self.__height - 1:
                rectangulo += "\n"
        return rectangulo
