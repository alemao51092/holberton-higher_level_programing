#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    romanInt = 0
    rs = roman_string
    if type(rs) is not str or rs is None:
        return 0
    for x in range(len(rs)):
        for k, v in d.items():
            if k == rs[x]:
                if x < len(rs) - 1 and v < d.get(rs[x + 1]):
                    romanInt -= v
                else:
                    romanInt += v
    return romanInt
