"""A script to demonstrate function parameters.

Example: 
    $ python function_parameters.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"

# def format_greeting(first_name: str, last_name: str) -> str:
#     return f"Hello, {first_name} {last_name}"

# Default Values
# def format_greeting(first_name="world", last_name=""):
#     return f"Hello, {first_name} {last_name}"

def format_greeting(first_name: str, last_name: str, 
                    salutation="Hello", title="Mr.") -> str:
    return f"{salutation}, {title} {first_name} {last_name}"

# Positional Arguments
print(format_greeting("Damien", "Altenburg"))

# Keyword Arguments
print(format_greeting(first_name="Damien", last_name="Altenburg"))
print(format_greeting(last_name="Warkentin", first_name="Deron"))

# Positional Arguments are required
# TypeError
#print(format_greeting(last_name="Altenburg"))

print(format_greeting("Damien", "Altenburg"))
print(format_greeting("Damien", "Altenburg", "Bonjour"))
print(format_greeting("Jane", "Doe", "Bonjour", "Mrs."))
print(format_greeting("Jane", "Doe", title="Dr."))
