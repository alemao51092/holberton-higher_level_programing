#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    numtotal = 0
    for num in my_set:
        numtotal += num
    return numtotal
