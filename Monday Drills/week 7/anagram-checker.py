# Problem
# Check if two strings are anagrams.
# An anagram is a word formed by rearranging another word’s letters, using all original letters exactly once.

# Examples
# Input: "listen", "silent" → Anagram
# Input: "hello", "world" → Not an anagram
# Input: "Dormitory", "dirtyroom" → Anagram

# Constraints
# Treat uppercase and lowercase as the same.
# Do not use sort(), sorted(), or set().
# Build a character-frequency dictionary manually for both strings and compare them.
# Do not import libraries.

string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

frequency1 = {}
frequency2 = {}

for char in string1:
    if char in frequency1:
        frequency1[char] += 1
    else:
        frequency1[char] = 1

for char in string2:
    if char in frequency2:
        frequency2[char] += 1
    else:
        frequency2[char] = 1

if frequency1 == frequency2:
    print(f"{string1}, {string2} → Anagram")
else:
    print(f"{string1}, {string2} → Not an anagram")
