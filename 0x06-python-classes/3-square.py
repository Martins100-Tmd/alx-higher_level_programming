#!/usr/bin/python3
"""Define a square class."""


class Square:
    """Square class defined."""

    def __init__(self, size=0):
        """Initialise Square class.

        Args:
            size (int): size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)
