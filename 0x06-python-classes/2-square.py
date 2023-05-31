#!/usr/bin/python3
"""Square class definition"""


class Square:
    """class defining a square"""
    def __init__(self, size=0):
        """Initializes the class


        Args:
            size(int): size of the square
        """
        self.__size = size
        if type(size) == int:
            pass
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            pass
        else:
            raise ValueError("size must be >= 0")
