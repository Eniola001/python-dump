# Problem
# Given a list of numbers, find all the numbers that appear more than once. Print each duplicate only once, in the order it first appears as a duplicate.

# Examples
# Input: [1, 2, 3, 2, 4, 5, 1] → [1, 2]
# Input: [4, 4, 4, 4] → [4]
# Input: [1, 2, 3, 4] → [] (no duplicates)
# Input: [10, 20, 10, 30, 20] → [10, 20]


numbers = [1, 2, 3, 2, 4, 5, 1]

duplicates = []
seen = []

for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print(duplicates)
