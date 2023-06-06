#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for number in my_list:
        if number % 2 == 0:
            newlist += [True]
        else:
            newlist += [False]
    return newlist
