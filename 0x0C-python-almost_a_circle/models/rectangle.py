#!/usr/bin/python3
"""Class Rectangle"""
from base import Base


class Rectangle(Base):
    """
    Defining the Rectangle class
    Inherits from:
        Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle class init

        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): x
            y(int): y
            id(int): id of new instance
        Error:
            TypeError: If either height or width is not a number]
            ValueError: If either width or height is less than equals to zero
            TypeError: If either x or y is not a number
            ValueError: If either x or y is less than zero
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returning private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returning private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returning private attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returning private attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area returns the area of the rectangle"""

        return (self.width) * (self.height)

    def display(self):
        """Display the rectangle in symbolic form"""

        if self.width == 0 or self.height == 0:
            print("")
            return;

        for i in range(self.height):
            str = ''
            for i in range(self.x):
                str += " "
            for i in range(self.width):
                str += "#"
            print(str)

    def __str__(self):
        """overriding inbuilt __str__method to print a formatted string"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Assign each elements in the args list to the insatcne attribute

        Args:
            args(tuple): unknown number of elements
        """
        return;
