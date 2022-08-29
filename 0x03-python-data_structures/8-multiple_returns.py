#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    if sentence:
        for i in sentence:
            count = count + 1
    else:
        return None
    firstChar = sentence[0]
    return (count, firstChar)
