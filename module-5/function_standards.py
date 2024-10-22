"""A script to demonstrate function standards and raising exceptions.

Example: 
    $ python function_standards.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, 
                    salutation="Hello", title="Mr.") -> str:
    """Returns a formatted greeting using the specified person's name.
    
    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        salutation (str): The salutation part of the greeting. 
        The default is "Hello".
        title (str): The person's title. The default is "Mr.".
        
    Returns:
        str: A formatted greeting using the specified person's name.
    """
    first_name = first_name.strip()

    if first_name != "":
        first_name += " "

    return f"{salutation}, {title} {first_name}{last_name}"

def to_binary(decimal_number: int) -> str:
    """Returns the binary equivalent for the specified decimal number.

    Args:
        decimal_number (int): The decimal number to convert to a
        binary number.

    Returns:
        str: The binary equivalent for the specified decimal number.
    """
    if not isinstance(decimal_number, int):
        raise TypeError("The decimal number must be int.")

    binary_number = ""

    while decimal_number > 0:
        # The binary digit is the remainder of dividing by 2
        binary_digit = decimal_number % 2

        # Update the number to the the quotient
        decimal_number = int(decimal_number / 2)

        # Add the digit to the beginning of the string
        binary_number = str(binary_digit) + binary_number

    return binary_number

print(to_binary(127))
