#!/usr/bin/python3


"""a json representation of object-to-text file function"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, "w" encoding="utf-8") as f:
        f.dump(my_obj, f)
