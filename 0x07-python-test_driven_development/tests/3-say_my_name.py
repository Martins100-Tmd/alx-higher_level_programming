#!/usr/bin/python3
"""Define a function that prints."""


def say_my_name(first_name, last_name=""):
    """say_my_name initialized.

    Args:
        first_name(string): first name to be printed
        last_name(string): second name to be printed

    Raises:
        TypeError: if first_name and last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    return "My name is {} {}".format(first_name, last_name)
