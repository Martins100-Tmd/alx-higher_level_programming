#!/usr/bin/python3
"""define a attr returning function."""


def lookup(obj):
    """Make a function that returns all attributes and methods of an object
    Args:
        obj (any): object which attribute to print
    Returns: return the attributes and method of obj
    """
    return dir(obj)
