#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    check = a_dictionary.keys();
    if key in check:
        a_dictionary[key] = value
    else:
        a_dictionary.update({key:value})
    return a_dictionary
