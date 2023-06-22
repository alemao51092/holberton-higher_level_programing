#!/usr/bin/python3
"""shebang"""


def read_file(filename=""):
    """read a file"""
    with open(filename, encoding="utf-8") as fileRO:
        text = fileRO.read()
        print(text, end="")
