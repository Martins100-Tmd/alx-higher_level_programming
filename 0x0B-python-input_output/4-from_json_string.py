#!/usr/bin/python3
"""Function changes an object from json to string"""


import json


def from_json_string(my_str):
    """
    Args:
        my_str(string): string to be parsed
    Error:
        No error
    """
    return json.loads(my_str)
