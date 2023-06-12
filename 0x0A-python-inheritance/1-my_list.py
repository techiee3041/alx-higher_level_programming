#!/usr/bin/python3
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def __init__(self):
        """initializes the object"""

        super().__init__()

    def print_sorted(self):
        """
        Prints the list in ascending order.

        This method sorts the list in ascending order
        using the built-in sorted function,
        and then prints the sorted list to the console.

        """
        print(sorted(self))
