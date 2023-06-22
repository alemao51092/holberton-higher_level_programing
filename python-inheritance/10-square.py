#!/usr/bin/python3
"""shebang"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a sub class square of the base class rectangle"""

    def __init__(self, size):
        """square"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """return area"""
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle], {self.__size}/{self.__size}"
