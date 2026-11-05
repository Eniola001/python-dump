# Problem

# Determine whether a string contains balanced parentheses. Every opening parenthesis '(' must have a matching closing parenthesis ')' in the correct order.
# You only need to handle round parentheses; ignore other character types.

# Examples
# Input: (a+b) * (c-d)
# Output: Balanced
# Input: (a+b))
# Output: Not balanced
# Input: ((a+b)
# Output: Not balanced

# Constraints
# Use a loop and a counter.
# Do not import libraries.
# If the counter ever becomes negative, the string is not balanced. At the end, the counter must be zero.

# What This Tests
# Strings, loops, counters, conditionals, and algorithmic reasoning.

text = input("Input: ")

def parentheses_check(text):
    brackets = 0
    for char in text:
        if char == "(":
            brackets += 1
        elif char == ")" and brackets > 0:
            brackets -= 1
    if brackets == 0:
        print("Output: Balanced")
    else:
        print("Output: Not Balanced")

parentheses_check(text)