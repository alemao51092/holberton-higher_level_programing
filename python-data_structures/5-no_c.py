#!/usr/bin/env python3
def no_c(my_string):
    res_my_string = ""
    for a in my_string:
        if a == "c" or a == "C":
            continue
        else:
            res_my_string += a
    return (res_my_string)
