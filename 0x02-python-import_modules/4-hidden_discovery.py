#!/usr/bin/python3
if __name__ == "__main__":
    """prints all names that are defined in hidden_4 module"""
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print(f"{i}")
