#!/usr/bin/python3

"""MyList Inherits from list."""

class MyList(list):
    """prints a sorted list"""

    def print_sorted(self):
        print(sorted(self))
