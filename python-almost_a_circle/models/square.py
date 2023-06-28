#!/usr/bin/python3
"""shebang"""
from models.rectangle import Rectangle


class Square(Rectangle):
    "sub class Square"

    def __init__(self, size, x=0, y=0, id=None):
        "instantation"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "String representation of the square"
        return (
            f"[Square] ({self.id}) {self.x}/{self.y}"
            f" - {self.width}"
        )

    @property
    def size(self):
        "return width"
        return self.width

    @size.setter
    def size(self, value):
        "Setter of the size"
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value
