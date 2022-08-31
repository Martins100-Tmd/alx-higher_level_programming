#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    Unl = set(my_list)
    new_list = list(Unl)
    for i in new_list:
        sum = sum + i
    return sum
