#!/usr/bin/python3

"""function that appends"""


def append_write(filename="", text=""):
    """
    Append text to a file.

    Args:
        filename (str, optional): The name of the file.
        text (str, optional): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
