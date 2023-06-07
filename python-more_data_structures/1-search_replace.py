#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = list(my_list)
    for idx in range(len(my_list)):
        if newlist[idx] == search:
            newlist[idx] = replace
    return newlist
