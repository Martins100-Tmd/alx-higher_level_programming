#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    if sentence:
        for i in sentence:
            count = count + 1
        First = sentence[0]
    else:
        First = None
    return (count, First)
