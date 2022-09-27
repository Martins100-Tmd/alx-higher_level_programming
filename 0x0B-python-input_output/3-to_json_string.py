#!/usr/bin/python3
"""JSON representation of obj"""


import json



def to_json_string(my_obj):
    """
    Args:
        obj(any): object to be stringified
    Errors:
        No error
    """
    return json.dumps(my_obj)
