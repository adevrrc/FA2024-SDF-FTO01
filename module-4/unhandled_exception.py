"""
Description: Demonstrates what happens when exceptions are not handled.
Author: Damien Altenburg
Date: 2023-10-1
Usage: python unhandled_exceptions.py
"""

from random import randint

quiz_grades = [67.8, 78.9, 89.0, 43.5]

hockey_teams = {
    "winnipeg": "jets",
    "calgary": "flames",
    "edmonton": "oilers",
    "ottawa": "senators",
    "vancouver": "canucks",
    "montreal": "canadians"
}

# ValueError Example
# grade = int("damien")

# TypeError Example
# grade = int(None)

# NameError Example
# print(number_of_items)

# IndexError Example
# print(quiz_grades[999])

# KeyError Example
# print(hockey_teams["chicago"])

# FileNotFoundError Example
# with open("data.txt") as file:
#     data = file.read()

# ZeroDivisionError Example
# result = 9 / 0

# AssertionError Example
# We will see this in a future module.

# AttributeError Example
# We will see this in a future module.

# NOTE: The code below does not execute when an exception is raised in an 
# earlier part of the code.
decimal_number: int = randint(1, 100)

working_number: int = decimal_number
binary_number: int = ""

while working_number > 0:
    # The binary digit is the remainder of dividing by 2
    binary_digit = working_number % 2

    # Update the number to the the quotient
    working_number = int(working_number / 2)

    # Add the digit to the beginning of the string
    binary_number = str(binary_digit) + binary_number

print(f"Decimal {decimal_number} -> Binary {binary_number}")
