# Problem
# Convert an integer from 1 to 3999 into a Roman numeral. This is the reverse of Roman to Integer.

# Examples
# 3    → "III"
# 58   → "LVIII"
# 1994 → "MCMXCIV"
# 3999 → "MMMCMXCIX"

# Constraints
# Use a greedy approach with an ordered list of (value, symbol) pairs that includes the subtractive forms (900 → CM, 400 → CD, 90 → XC, 40 → XL, 9 → IX, 4 → IV).
# Use a while loop. Do not hardcode answers.
# Return "" or raise a clear error message for numbers outside 1–3999 (your choice, but be consistent and say which).
# Do not import libraries.

number = int(input("Enter an integer you want to convert to roman numerals = "))
def int_to_roman(number):

    # Check whether the number is within the valid range.
    # Roman numerals in this challenge support numbers from 1 to 3999.
    if number < 1 or number > 3999:
        raise ValueError("Number must be between 1 and 3999.")

    # Create an ordered list of Roman numeral values and symbols.
    # The list must be arranged from largest to smallest.
    # Include subtractive combinations such as 900 (CM), 400 (CD),
    # 90 (XC), 40 (XL), 9 (IX), and 4 (IV).
    roman_values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    # Initialize an empty string to store the Roman numeral result.
    result = ""

    # Go through each value-symbol pair, starting with the largest.
    for value, symbol in roman_values:
        # Keep using the current Roman numeral as long as
        # its value is less than or equal to the remaining number.
        while number >= value:
            # Add the current Roman numeral symbol to the result.
            result += symbol
            # Subtract its numerical value from the remaining number.
            number -= value
    # Return the completed Roman numeral.
    return result

print(int_to_roman(number))