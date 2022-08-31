#!/usr/bin/python3
def best_score(a_dictionary):
    arr = list()
    store = dict()
    for k, v in a_dictionary.items():
        arr.append(v)
        store.update({v:k})
    arr.sort()
    return store[arr[-1]]
