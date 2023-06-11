#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    errorList = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
            newList.append(div)
        except ZeroDivisionError:
            errorList.append("division by 0")
            newList.append(0)
        except TypeError:
            errorList.append("wrong type")
            newList.append(0)
        except IndexError:
            errorList.append("out of range")
            newList.append(0)
        finally:
            pass
    for e in errorList:
        print(e)
    return newList            
