#!/usr/bin/python3
def print_last_digit(number):
    temp = int(repr(number)[-1])
    print("{}".format(temp), end='')
    return temp
