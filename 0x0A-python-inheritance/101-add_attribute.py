#!/usr/bin/python3
"""Classes"""


def add_attribute(obj, att, value):
    """Add_attribute function

    Args:
        att(any): attribute to check for
        value(str): value to be added if possible
    Error:
        TypeError: if the operation is not possible
    """
    if not hasattr(att, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
