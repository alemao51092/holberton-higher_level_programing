#!/usr/bin/python3
"""shebang"""


def write_file(filename="", text=""):
    """write a string in a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
