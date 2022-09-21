#!/usr/bin/python3
"""Define a text breaker function."""


def text_indentation(text):
    """text_indentation function init.

    Args:
        text(string): text to be broken down by delimeters
    Raises:
        TypeError: if string is not a string type
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
