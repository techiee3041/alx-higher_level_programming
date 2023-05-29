#!/usr/bin/python3
def safe_print_integer(value):
    """function that prints an integer

    args:
        value: integer to be printed

    returns:
        returns true if correctly printed else false
    """
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
