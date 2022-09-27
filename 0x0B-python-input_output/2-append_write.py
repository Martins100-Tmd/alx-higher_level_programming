#!/usr/bin/python3
"""Count append text"""


def append_write(filename="", text=""):
    """
    Args:
        filename(file): file to be add to
        text(string): string to add to filename

    Error:
        No errors
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
