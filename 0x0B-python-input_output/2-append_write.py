#!/usr/bin/python3
"""Defines a file-appending eith function."""


def append_write(filename="", text=""):
    """Appends a str to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The str to append to the file.
    Returns:

        The num of charx appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
