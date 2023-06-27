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
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")
