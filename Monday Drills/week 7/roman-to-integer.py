# Problem
# Given a string representing a Roman numeral, convert it to an integer.
# Symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.
# If a smaller numeral appears before a larger one, subtract it (e.g., IV = 4, IX = 9); otherwise, add it.

# Examples
# Input: "III" → 3
# Input: "LVIII" → 58 (L = 50, V = 5, III = 3)
# Input: "MCMXCIV" → 1994 (M = 1000, CM = 900, XC = 90, IV = 4)

# Constraints
# Store Roman numeral mappings in a dictionary.
# Use a while loop to traverse the string.
# Do not import libraries.
# Do not hardcode the answers.

def roman_to_integer(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total += roman[s[i + 1]] - roman[s[i]]
            i += 2
        else:
            total += roman[s[i]]
            i += 1

    return total

roman_numeral = input("Enter a number in roman numerals: ").upper()
print(f"Input: '{roman_numeral}' → {roman_to_integer(roman_numeral)}")

# Examples
# print(roman_to_integer("III"))      # 3
# print(roman_to_integer("LVIII"))    # 58
# print(roman_to_integer("MCMXCIV"))  # 1994
