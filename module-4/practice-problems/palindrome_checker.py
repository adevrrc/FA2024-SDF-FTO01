"""
Write a program that takes a sentence as an input and checks whether that 
sentence is a palindrome. A palindrome is a word, phrase, or sentence that is 
symmetrical; that is, it is spelled the same forward and backward. Examples are 
"otto," "mom," and "Able was I ere I saw Elba." Your program should be case 
insensitive; that is, "Otto" should also be counted as a palindrome.

Inputs

- sentence

Processing

- sentence is a palindrome if the characters are the same forward and backwards

Outputs

- Whether or not the sentence is a palindrome

TODO:
- Evaluate sentence ignoring spaces and punctuation
"""

sentence = input("Enter a sentence: ")

#sentence = "racecar"
#sentence = "tacocat"

# original: tacocat
#     copy: tacocat
#           1111111

# original: taco cat
#     copy: tac ocat
#           1110
#           01234567

sentence_copy = sentence[::-1]

characters_are_equal = True
index = 0

while characters_are_equal and index < len(sentence):
    characters_are_equal = sentence[index] == sentence_copy[index]

    index += 1

print(f"The sentence \"{sentence}\""
      f" is{" not" if not characters_are_equal else ""}"
      " a palindrome.")
