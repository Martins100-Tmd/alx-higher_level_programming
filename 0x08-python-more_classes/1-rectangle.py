#!/usr/bin/python3
"""Define a rectangle class."""


class Rectangle:
    """Rectangle class initialized.


    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

    Errors:
        TypeError: 
                1. If width is not an integer
                2. If height is not an integer
        ValueError:
                1. If width is less than 0
                2. If height is less than 0
    """
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the set value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the set value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
