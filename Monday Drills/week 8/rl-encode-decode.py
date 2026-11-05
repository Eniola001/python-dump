# Problem
# Write two functions: rle_encode(text) and rle_decode(encoded). Decoding must reverse encoding perfectly, including counts with more than one digit.

# Examples
# rle_encode("aaabbc")        → "a3b2c1"
# rle_encode("aaaaaaaaaaaab") → "a12b1"
# rle_decode("a12b1")         → "aaaaaaaaaaaab"
# rle_encode("")              → ""

# Constraints
# Input text contains letters only (no digits), so the encoded form is unambiguous.
# Use while loops and index tracking. No itertools, no re.
# rle_decode must read a whole number after each letter (e.g., 12), not just one digit.
# Build the result with string concatenation or a list joined at the end.
# Round-trip check: for every test string s, rle_decode(rle_encode(s)) == s must be True. Print the result of at least four round-trip checks.
# Do not import libraries.

def rle_encode(text):

    # Initialize an empty string to store the encoded result.
    result = ""

    # Initialize the index to track our current position.
    i = 0

    # Continue looping until we reach the end of the input string.
    while i < len(text):

        # Start counting from 1 because the current character
        # already exists once.
        count = 1

        # Check whether the next character exists and is the same
        # as the current character.
        while i + 1 < len(text) and text[i] == text[i + 1]:

            # Increase the count for every consecutive match.
            count += 1

            # Move to the next character.
            i += 1

        # Add the current character and its total count
        # to the encoded result.
        # Convert count to a string because we are concatenating.
        result += text[i] + str(count)

        # Move to the next character after the group we counted.
        i += 1

    # Return the completed encoded string.
    return result

def rle_decode(encoded):

    # Initialize an empty string to store the decoded result.
    result = ""

    # Initialize the index to track our current position.
    i = 0

    # Continue looping until we reach the end of the encoded string.
    while i < len(encoded):

        # Read the character that should be repeated.
        char = encoded[i]

        # Move to the next position to start reading the count.
        i += 1

        # Initialize an empty string to collect all the digits.
        # We use a string because the count might have multiple digits.
        count = ""

        # Continue reading while we are within the string
        # and the current character is a digit.
        while i < len(encoded) and encoded[i].isdigit():

            # Add the current digit to the count string.
            count += encoded[i]

            # Move to the next position.
            i += 1

        # Convert the complete count from a string to an integer.
        count = int(count)

        # Repeat the character according to its count
        # and add it to the decoded result.
        result += char * count

    # Return the reconstructed original string.
    return result