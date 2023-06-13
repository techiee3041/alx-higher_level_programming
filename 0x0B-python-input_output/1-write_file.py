#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    writes text to a file

    Args:
        filename(str, optional): Name of the file to write to.
        text(str, optional): the text to write

    Returns:
        returns the number of charcters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
