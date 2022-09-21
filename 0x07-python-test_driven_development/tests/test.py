#!/usr/bin/python3

add_integer = __import__('0-add_integer').add_integer
import random

n = random.randint(0, 1000)
print(n)
print(add_integer(100, n))
