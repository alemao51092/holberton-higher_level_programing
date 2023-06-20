#!/usr/bin/python3
"""shebang"""


class MyList(list):
    """print sorted list"""

    def print_sorted(self):
        """sort list"""
        print(sorted(self))
