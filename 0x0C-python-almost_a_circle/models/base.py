#!/usr/bin/python3
"""Define a Base class"""


class Base:
    """Base class created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class init

        Args:
            id(any): new instance id
        Errors:
            No Error
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
