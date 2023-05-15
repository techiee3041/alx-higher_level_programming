#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        length = 0
        sentence[0] = None
        return (length, sentence[0])
    else:
        length = len(sentence)
        first = sentence[0]
        return (length, first)
