#!/usr/bin/python3
"""file to python Object"""

import json


def load_from_json_file(filename):
    """
    module converts a json file to a python object

    Args:
        filename(file): file to be converted

    Error:
        No error
    """
    with open(filename) as f:
        return json.load(f)
