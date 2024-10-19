"""A script to demonstrate function standards and raising exceptions.

Example: 
    $ python function_standards.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, salutation="Hello", title="Mr.") -> str:
    first_name = first_name.strip()

    if first_name != "":
        first_name += " "

    return f"{salutation}, {title} {first_name}{last_name}"

def to_binary(decimal_number: int) -> str:
    binary_number = ""

    while decimal_number > 0:
        # The binary digit is the remainder of dividing by 2
        binary_digit = decimal_number % 2

        # Update the number to the the quotient
        decimal_number = int(decimal_number / 2)

        # Add the digit to the beginning of the string
        binary_number = str(binary_digit) + binary_number

    return binary_number
