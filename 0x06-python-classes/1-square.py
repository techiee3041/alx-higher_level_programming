#!/usr/bin/python3
"""Class Square that defines a squire"""


class Square:
    """A class attribute with private size"""

    def __init__(self, size):
        """Initializing a class


        Args:
            size(int): size of the square
        """
        self.__size = size
