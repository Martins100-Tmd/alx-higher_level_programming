#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    L1 = list(set_1)
    L2 = list(set_2)
    for i in L1:
        L2.append(i)
    L2.sort()
    res = set(L2)
    return res
