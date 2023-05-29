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
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end="")
            count += 1
        except (ValueError, ValueError):
            pass
    print()
    return (count)
