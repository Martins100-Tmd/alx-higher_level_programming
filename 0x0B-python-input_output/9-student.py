#!/usr/bin/python3
"""Define a student class"""


class Student:
    """Student class created"""

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Instance of student will be initialised"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return __dict__ of the new class instance"""
        return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
