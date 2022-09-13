#!/usr/bin/python3
"""Define a square class."""


class Square:
    """Square class initialised."""

    def __init__(self, size=0):
        """Class initialised.

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        return (self.size)

    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): value of the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
