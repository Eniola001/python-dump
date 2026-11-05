# Problem

# Given a list of numbers, find the smallest number, largest number, total, and average without using built-in shortcuts for these calculations.
# Use this starting list: numbers = [12, 5, 27, 8, 14].

# Examples
# Input list: [12, 5, 27, 8, 14]
# Smallest: 5
# Largest: 27
# Total: 66
# Average: 13.2

# Constraints
# Use loops and variables to calculate the results.
# Do not use min(), max(), or sum().
# You may use len() to calculate the average.
# Assume the list contains at least one number.

# What This Tests
# Lists, iteration, accumulators, comparisons, and arithmetic.
# Notes / concepts to review: (Remember to write your weakness it if you have one)

numbers = [12, 5, 27, 8, 14]

def analyze(nums):
    smallest, largest, total = nums[0], nums[0], 0

    for num in nums:
        total += num
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    average = total/len(nums)

    print("Smallest:", smallest)
    print("Largest:", largest)
    print("Total:", total)
    print("Average:", average)

analyze(numbers)