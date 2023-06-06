#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    maxnum = 0
    for i in my_list:
        if i > maxnum or maxnum is None:
            maxnum = i
    return maxnum
