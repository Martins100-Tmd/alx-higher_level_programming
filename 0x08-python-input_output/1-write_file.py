#!/usr/bin/python3
"""Writes a text to a file"""


def write_file(filename="", text=""):
    """
    Args:
        filename(file): File to be written to
        text(string): text to write to file
    Error: No errors
    """
    with open(filename, 'w+', encoding='utf-8') as f:
        f_write = f.write(text)
        return f.tell()
