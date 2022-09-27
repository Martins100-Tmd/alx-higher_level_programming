#!/usr/bin/python3
"""file to python Object"""

import json

from types import SimpleNamespace


def load_from_json_file(filename):
    """
    module converts a json file to a python object

    Args:
        filename(file): file to be converted

    Error:
        No error
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        f_read = f.read()
        x = json.loads(f_read, object_hook=lambda d: SimpleNamespace(**d))
        return x
