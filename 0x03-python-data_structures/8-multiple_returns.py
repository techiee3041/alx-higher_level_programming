#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return(0, None)
    else:
        length = len(sentence)
        first = sentence[0]
        return length, first
