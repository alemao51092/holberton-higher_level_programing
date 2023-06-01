#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    index = len(argv) - 1
    if index > 1:
        print("{} arguments:".format(index))
    elif index == 1:
        print("{} argument:".format(index))
    elif index == 0:
        print("{} arguments.".format(index))
    for index in range(1, len(argv)):
        print("{0}: {1}".format(index, argv[index]))
