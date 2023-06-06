#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence == None:
        fchar = None
    fchar = sentence[0] if lenght > 0 else None
    return lenght, fchar
