#!/usr/bin/python3
"""shebang"""
from models.base import Base


class Rectangle(Base):
    """ sub class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if width <= 0:
            raise ValueError("width must be > 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        "return width"
        return self.__width

    @width.setter
    def width(self, value):
        "Setter of the width"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "return height"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter of the height"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "return x"
        return self.__x

    @x.setter
    def x(self, value):
        "Setter of the x"
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        "return y"
        return self.__y

    @y.setter
    def y(self, value):
        "Setter of the y"
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        "Returns the rectangle area"
        return (self.__height * self.__width)
