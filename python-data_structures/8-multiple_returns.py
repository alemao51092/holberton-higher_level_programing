#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if len(sentence) > 0:
        latupla = (lenght, sentence[0])
    else:
        latupla = (lenght, None)
    return latupla
