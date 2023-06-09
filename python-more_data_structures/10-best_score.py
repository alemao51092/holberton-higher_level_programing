#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = float('-inf')
    key_max = None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_value:
            max_value = value
            key_max = key
    return key_max
