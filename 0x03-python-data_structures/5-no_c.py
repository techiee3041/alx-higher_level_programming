#!/usr/bin/python3
def no_c(my_string):
    letter = "c"
    new_str = ""

    for i in my_string:
        if i != letter and i != "C":
            new_str += i
    return new_str
