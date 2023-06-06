#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    maxnum = None
    for i in my_list:
        if maxnum is None or maxnum < i:
            maxnum = i
    return maxnum
