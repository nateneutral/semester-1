"""
Utility functions for Worksheet 1.2.
"""
import sys

def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    nonNum = 0
    numbers = []
    line = input("Enter some numbers, separated by spaces: ")

    for item in line.split():
        if not((item.replace(".","")).isnumeric()):
            nonNum = nonNum +1
        else:
            numbers.append(float(item))
           
    if nonNum == len(line.split()):
        sys.exit("Error: no numbers provided")
    print(numbers)
    return numbers

