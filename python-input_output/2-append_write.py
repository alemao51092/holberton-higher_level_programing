#!/usr/bin/python3
"""shebang"""


def append_write(filename="", text=""):
    """append a str at the end of a file"""
    with open(filename, mode="a", encoding="utf-8") as a:
        a.write(text)
    return len(text)
