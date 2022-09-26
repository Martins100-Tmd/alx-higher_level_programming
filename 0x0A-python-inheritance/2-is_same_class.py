#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """check for the instance of an object

    Args:
        obj (any): The object to be checked
        a_class (type): the type obj is compared to
    Returns: returns True if obj is an exact instance of a_class
    and return False if not.
    """
    return type(obj) is a_class;
