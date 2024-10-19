"""
Write a program that generates five random integers between 60 and 100 and 
calculates the smallest of the five numbers.

Input
- 5 random numbers between 60 and 100

Processing
- generate random numbers
- find the smallest value

Output
- random numbers
- the smallest random number
"""

from random import randint

NUMBER_OF_RANDOM_NUMBERS = 5
LOWER_RANGE = 60
UPPER_RANGE = 100

random_numbers = []

for count in range(NUMBER_OF_RANDOM_NUMBERS):
    random_number = randint(LOWER_RANGE, UPPER_RANGE)
    random_numbers.append(random_number)

print(random_numbers)

smallest_number = random_numbers[0]

# Determine which is the smallest number
for index in range(1, NUMBER_OF_RANDOM_NUMBERS):
    if random_numbers[index] < smallest_number:
        smallest_number = random_numbers[index]

print(f"The smallest number is {smallest_number}.")
