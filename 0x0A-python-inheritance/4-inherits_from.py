#!/usr/bin/python3
"""Define a sub-class checking function."""


def inherits_from(obj, a_class):
    """Function return True if obj is an instance of a subclass

    Args:
        obj (any): object to be checked
        a_class: a class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
