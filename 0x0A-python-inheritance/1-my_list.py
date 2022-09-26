#!/usr/bin/python3
"""MyList Inherits from list."""

class MyList(list):
    """prints a sorted list"""

    def print_sorted(self):
        """Prints the sorted list from the main class

        Args:
            self: the instance object
        """
        print(sorted(self))
