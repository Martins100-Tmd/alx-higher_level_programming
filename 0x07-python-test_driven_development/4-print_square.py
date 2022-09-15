#!/usr/bin/python3
"""Define a square printing function."""


def print_square(size):
    """print_square initialised.

    Args:
        size(int): size of square
    Raises:
        TypeError: If size is not integer
        ValueError: if size is less than 0
        TypeError: If size is float and less than 0 
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print("")
