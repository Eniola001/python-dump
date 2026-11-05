# Problem
# Given a sorted list of integers and a target, return the index of the first (leftmost) occurrence of the target, or -1 if it is not present. Also return how many comparisons your search made.

# Examples
# nums = [1, 3, 3, 3, 5, 8], target = 3  → (1, comparisons)
# nums = [1, 3, 5, 8],       target = 4  → (-1, comparisons)
# nums = [],                 target = 7  → (-1, 0)

# Constraints
# Use a while loop with low and high pointers. No recursion in the main version.
# No .index(), no in, no .count().
# Must find the leftmost match when duplicates exist. Finding any match is not enough.
# The function binary_search(nums, target) -> tuple[int, int] must be pure: no printing inside.
# Do not import libraries.

nums = list(map(int, input("Enter a sorted list of integers separated by spaces: ").split()))
target = int(input("target = "))

def binary_search(nums, target):

    # Initialize the pointers.
    # low represents the first index of the list.
    # high represents the last index of the list.
    low = 0
    high = len(nums) - 1

    # Store the index of the target when we find it.
    # Start with -1 because we haven't found the target yet.
    index = -1

    # Keep track of how many comparisons we make
    # while searching for the target.
    comparisons = 0

    # Continue searching as long as there are elements
    # within our current search range.
    while low <= high:

        # Calculate the middle index of the current search range.
        # The // operator performs integer division.
        mid = (low + high) // 2

        # Count the comparison between the middle element
        # and the target.
        comparisons += 1

        # Check if the middle element is equal to the target.
        if nums[mid] == target:

            # We found the target, so save its current index.
            index = mid

            # Don't return yet!
            # Move high to the left of mid because we want
            # to check whether the target appears earlier.
            high = mid - 1

        # If the middle element is smaller than the target,
        # the target can only be in the right half because
        # the list is sorted.
        elif nums[mid] < target:
            # Move the low pointer to the right of mid.
            low = mid + 1

        # If the middle element is greater than the target,
        # the target can only be in the left half.
        else:
            # Move the high pointer to the left of mid.
            high = mid - 1

    # Once the loop finishes, return:
    # 1. The leftmost index where the target was found (-1 if absent).
    # 2. The total number of comparisons made.
    return (index, comparisons)

print(binary_search(nums, target))
