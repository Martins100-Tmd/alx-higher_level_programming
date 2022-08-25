#!/usr/bin/python3

from calculator_1.py import add, sub, mul, div

if __name__ == "__main_":
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
