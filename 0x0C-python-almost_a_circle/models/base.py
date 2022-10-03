#!/usr/bin/python3
"""Define a Base class"""

import json


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

    def to_json_string(list_dictionaries):
        """return JSON string"""
        if list_dictionaries == None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)
