#!/usr/bin/python3
"Task 8"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "A rectangle that is subclass of basegeometry"

    def __init__(self, width, height):
        "Instantiation"
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
