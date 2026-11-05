# Problem
# Implement bubble sort that sorts a list in place and returns the number of comparisons and swaps it performed.

# Examples
# [5, 1, 4, 2, 8] → sorted [1, 2, 4, 5, 8], with counts
# [1, 2, 3, 4, 5] → already sorted: your optimized version should stop after ONE pass
# []              → [] with 0 comparisons and 0 swaps

# Constraints
# No sort(), sorted(), min(), max().
# Implement the early-exit optimization: if a full pass makes no swaps, stop immediately.
# Each pass should check one fewer pair than the last (the largest items have already settled at the end).
# Show with comparison counts that your function makes fewer comparisons on an already-sorted list than on a reverse-sorted list of the same size.
# Do not import libraries.

def bubble_sort(nums):

    # Initialize the comparison counter.
    comparisons = 0

    # Initialize the swap counter.
    swaps = 0

    # Get the length of the list.
    n = len(nums)

    # Outer loop controls how many passes we make.
    # We need at most n - 1 passes to sort the list.
    for i in range(n - 1):

        # Assume no swaps will be needed during this pass.
        swapped = False

        # Inner loop compares neighbouring elements.
        # Subtract i because the largest elements have
        # already settled at the end of the list.
        for j in range(n - 1 - i):

            # Count every comparison between neighbouring elements.
            comparisons += 1

            # Check whether the current element is greater
            # than the next element.
            if nums[j] > nums[j + 1]:

                # Swap the elements if they are in the wrong order.
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

                # Increase the swap counter.
                swaps += 1

                # Record that a swap happened during this pass.
                swapped = True

        # If no swaps occurred during the entire pass,
        # the list is already sorted.
        # Stop early to avoid unnecessary comparisons.
        if not swapped:
            break

    # Return the sorted list and the operation counts.
    return f'{nums}, {comparisons} comparisons, {swaps} swaps'

print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([1, 2, 4, 5, 8]))
