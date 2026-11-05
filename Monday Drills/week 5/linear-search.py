# Problem

# Given a list and a target value, search through the list one item at a time. Print the index where the target first appears, or a message saying it was not found.
# Use this starting list: values = [14, 7, 22, 9, 7, 31].

# Examples
# Target: 22
# Found at index 2
# Target: 18
# Target not found

# Constraints
# Use a loop; do not use the list's index() method.
# Stop searching once the first match is found.
# Do not import libraries.

# What This Tests
# Lists, loops, comparisons, indexing, and control flow.
# Notes / concepts to review: (Remember to write your weakness it if you have one)

values = [14, 7, 22, 9, 7, 31]

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return f"Found at index {i}"
    return "Target not found"

print(search(values, 18))