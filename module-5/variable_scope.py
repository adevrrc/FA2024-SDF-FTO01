"""A script to demonstrate variable scope.

Example: 
    $ python variable_scope.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"

name = "Damien"

decimal_number = 0
binary_number = ""

def to_binary(decimal_number: int) -> str:
    binary_number = ""

    # Global scope
    print(name)

    while decimal_number > 0:
        # The binary digit is the remainder of dividing by 2
        binary_digit = decimal_number % 2

        # Update the number to the the quotient
        decimal_number = int(decimal_number / 2)

        # Add the digit to the beginning of the string
        binary_number = str(binary_digit) + binary_number

    return binary_number

print(to_binary(147))

# Global scope
print(name)

print(decimal_number)
print(binary_number)
