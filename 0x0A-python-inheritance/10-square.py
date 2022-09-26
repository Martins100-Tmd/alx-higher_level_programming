#!/usr/bin/python3
"""Defines a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square rectangle"""
    def __init__(self, size):
        """Create own size prop"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        super().area(self.__width, self.__height)
