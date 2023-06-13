#!/usr/bin/python3
"""shebang"""


def add_integer(a, b=98):
    """add integer"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer.")
    return int(a) + int(b)
