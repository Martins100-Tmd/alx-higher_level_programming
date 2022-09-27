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
    with open(filename, 'r+', encoding='utf-8') as f:
        f.read()
        len1 = f.tell()
        f.write(text)
        len2 = f.tell()
        len = len1 - len2
        if len < 0:
            return -1 * len
        return len
