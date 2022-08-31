#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    val = list()
    for i, j in a_dictionary.items():
        val.append(j)
    if value in val:
        res = dict()
        for k, v in a_dictionary.items():
            if v != value:
                res.update({k: v})
        return res
    else:
        return a_dictionary
