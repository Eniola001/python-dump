# Problem
# Given a positive integer, convert it to its binary representation.

# Examples
# Input: 10 → Output: 1010
# Input: 25 → Output: 11001
# Input: 1 → Output: 1

# Constraints
# Do not use the built-in bin() function.
# Do not use string formatting like f"{num:b}".
# Use the mathematical method: repeatedly divide by 2 and track the remainders.
# Build the final binary string manually using string concatenation.
# Do not import libraries.

decimal_value = int(input('Input: '))
result = ''

decimal = decimal_value
while decimal > 0:
    remainder = decimal % 2
    result = str(remainder) + result
    decimal = decimal // 2

print(f'Input: {decimal_value} → Output: {result}')