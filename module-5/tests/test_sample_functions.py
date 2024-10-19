"""Defines the TestSampleFunctions class to demonstrate unit testing.

Test Cases

format_greeting()

1. first_name not a string - TypeError (first_name must be a str.)
2. last_name not a string - TypeError (last_name must be a str.)
3. last_name blank string - ValueError (last_name must contain 
non-whitespace characters.)
4. salutation not a string - TypeError (salutation must be a str.)
5. salutation blank string - ValueError (salutation must contain 
non-whitespace characters.)
6. title not a string - TypeError (title must be a str.)
7. title blank string - ValueError (title must contain non-whitespace 
characters.)
8. first_name blank string - returns formatted without a first name
9. first_name not blank - returns formatted with a first name

get_whole_number()

1. prompt not a string - TypeError (prompt must be a str.)
2. console input not a whole number - exception (Input was not a whole 
number.)
3. console input is a whole number - returns whole number

Examples: 
    $ python -m unittest tests/test_sample_functions.py
    $ clear; python -m unittest tests/test_sample_functions.py
"""

__version__ = "0.11.2024"
__author__ = "Damien Altenburg"
