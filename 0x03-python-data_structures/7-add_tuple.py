#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result=list()
    for i in range(len(tuple_a)):
        sum=tuple_a[i] + tuple_b[i]
        result.append(sum)
    T_result=tuple(result)
    return T_result
