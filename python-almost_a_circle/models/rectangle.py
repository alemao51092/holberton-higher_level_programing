#!/usr/bin/python3
"""shebang"""
from models.base import Base


class Rectangle(Base):
    """ sub class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

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
        self.__width = value

    @property
    def height(self):
        "return height"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter of the height"
        self.__height = value

    @property
    def x(self):
        "return x"
        return self.__x

    @x.setter
    def x(self, value):
        "Setter of the x"
        self.__x = value

    @property
    def y(self):
        "return y"
        return self.__y

    @y.setter
    def y(self, value):
        "Setter of the y"
        self.__y = value
