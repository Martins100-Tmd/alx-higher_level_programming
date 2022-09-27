#!/usr/bin/python3
"""File reader function"""


def read_file(filename=""):
    """
    A function that reads a file

    Args:
        filename (file): File to be read
    Error:
        No error to be handled
    """
    with open(filename, 'r', encoding='utf-8') as f:
        f_read = f.read()
        print(f_read)
