#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    for i in sentence:
        count = count + 1;
    firstChar = sentence[0]
    return (count,firstChar)
