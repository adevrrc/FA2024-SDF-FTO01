"""A script to demonstrate the basics of functions.

Example: 
    $ python functions_basics.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"

# Not defined error
#print_greeting("Elvis", "Presley")

# def print_greeting() -> None:
#     print("Hello World")

def print_greeting(first_name: str, last_name: str) -> None:
    print(f"Hello, {first_name} {last_name}")

print_greeting()

print_greeting("Damien", "Altenburg")

# Must satisfy parameter list
# TypeError
#print_greeting("Damien")
