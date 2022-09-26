#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        super().__width = width
        super().integer_validator("height", height)
        self.__height = height

    def Area(self):
        """Defines an Area function"""
        return int(self.width * self.height)

    def __str__(self):
        """Returns a formatted result"""
        string = "[" + self.__class__.__name__ + "]"
        string += str(self.width) + "/" + str(self.height)
        return string
