#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that divides two integers and prints result
    args:
        a - integer to divide
        b - diviser
    returns:
        returns the value divided otherwise None
    """
    result = 0
    try:
        result = a/b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
