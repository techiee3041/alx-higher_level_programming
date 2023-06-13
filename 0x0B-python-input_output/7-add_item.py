#!/usr/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Get the command-line arguments, excluding the script name itself
arguments = sys.argv[1:]

# Load existing items from the file if it exists, or create an empty list
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Add the command-line arguments to the list
items.extend(arguments)

# Save the updated list to the file
save_to_json_file(items, "add_item.json")
