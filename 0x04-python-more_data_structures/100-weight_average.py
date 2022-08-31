#!/usr/bin/python3
def weight_average(my_list=[]):
    mult = 0
    sum = 0
    for i in my_list:
        mult = mult + (i[0] * i[1])
        sum = sum + (i[1])
    return mult/sum
