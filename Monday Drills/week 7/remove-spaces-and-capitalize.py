# Problem
# Given a sentence, capitalize the first letter of every word, then create a second version with all spaces removed.

# Examples
# Input: "hello world from python"
# Capitalized: "Hello World From Python"
# No Spaces: "HelloWorldFromPython"

# Constraints
# Do not use .replace() to remove spaces.
# Do not use .title() or .capitalize().
# Use loops and conditionals.
# Use ASCII logic to capitalize the first letter (check if the character is between 'a' and 'z', and convert it by subtracting 32 from its ASCII value using ord() and chr()).
# Do not import libraries.

sentence = input("Enter a sentence: ")

capitalized = ""
no_spaces = ""
new_word = True

for char in sentence:
    if char == " ":
        capitalized += char
        new_word = True
    else:
        if new_word and 'a' <= char <= 'z':
            char = chr(ord(char) - 32)

        capitalized += char
        no_spaces += char
        new_word = False

print("Capitalized:", capitalized)
print("No Spaces:", no_spaces)
