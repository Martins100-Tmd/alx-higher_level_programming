#!/usr/bin/python3
"""Defines a BaseGeometry."""


class BaseGeometry:
    """a basegeometry class."""

    def area(self):
        """a public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A value validator

        Args:
            name (str): string
            value (int): integer value
        Errors:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
