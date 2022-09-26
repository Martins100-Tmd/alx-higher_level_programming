#!/usr/bin/python3
"""MyList Inherits from list."""


class MyList(list):
    """Defines MyList class a subclass to list class."""

    def print_sorted(self):
        """Prints the sorted list from the main class

        Args:
            self: the instance object
        """
        print(sorted(self))
