#!/usr/bin/python3
"""shebang"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "A rectangle that is subclass of basegeometry"

    def __init__(self, width, height):
        "Instantiation"
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """calculet area"""
        return self.__height * self.__width
        

    def __str__(self):
        """str method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
