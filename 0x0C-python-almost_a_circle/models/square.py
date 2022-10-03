#!/usr/bin/python3
"""Define a square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square init."""

    def __init__(self, size, x=0, y=0, id=None):
        """New instance of Square.

        Args:
            size(int): size of square
            x(int): x
            y(int): y
            id(int): id of the new class instance
        """
        super()__init(id, x, y, size, size)

    @property
    def size(self):
        """return the size attr."""
        return self.size

    @size.setter
    def size(self):
        """set size"""
        self.width = size
        self.height = size
