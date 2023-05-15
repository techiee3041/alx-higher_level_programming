#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []

    for i in my_list:
        new.append(False if i % 2 else True)
    return new
