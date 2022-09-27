#!/usr/bin/python3
"""return dictionary description of an obj"""


def class_to_json(obj):
    """
    Args:
        obj(any): object
    Error:
        No error
    """
    return obj.__dict__
