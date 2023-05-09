#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if abs(i) % 3 == 0:
            print("Fizz", end=" ")
        elif abs(i) % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
