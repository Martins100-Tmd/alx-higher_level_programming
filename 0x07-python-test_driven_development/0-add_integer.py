#!/usr/bin/python3
"""Define a additon function."""


def add_integer(a, b=98):
    """Initialized addition function.

    All floats are typecasted to an integer

    Params:
        a (int or float)
        b (int or float)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int (b)
