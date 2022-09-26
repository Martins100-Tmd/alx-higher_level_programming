#!/usr/bin/python3
"""MyList Inherits from list."""


class MyList(list):
    """prints a sorted list"""

    def print_sorted(self):
        """prints the sorted list of the main class."""

        print(sorted(self))
