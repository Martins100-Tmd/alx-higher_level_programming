#!/usr/bin/python3
"""Define a square class."""

class Square:
    """Square class defined."""

    def __init__(self, size=0):
        """Class initialised.

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
