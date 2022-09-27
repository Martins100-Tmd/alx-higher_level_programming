#!/usr/bin/python3
"""writes a json file to a .txt file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj(any): data type to be added
        filename(file): file to be appended to
    Error:
        No error
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
