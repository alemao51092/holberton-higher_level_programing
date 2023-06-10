#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element in range(x):
            print("{}".format(my_list[element]), end='')
            count += 1
    except Exception:
        pass
    finally:
        print()
    return element
