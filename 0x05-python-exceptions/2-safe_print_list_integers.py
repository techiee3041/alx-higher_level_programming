#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints X elements of a list

    Args:
        my_list: printed list
        x: number of lements to print

    Returns:
        returns the real number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return (count)
