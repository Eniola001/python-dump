# Problem
# Given a list of integers (positive and negative), find the contiguous slice with the largest sum. Return the sum and the start and end indices.

# Examples
# [-2, 1, -3, 4, -1, 2, 1, -5, 4] → sum 6, indices (3, 6)   # [4, -1, 2, 1]
# [5]                              → sum 5, indices (0, 0)
# [-3, -1, -2]                     → sum -1, indices (1, 1)

# Constraints
# Write two functions:
# max_subarray_brute(nums): checks every possible slice (nested loops are allowed here).
# max_subarray_fast(nums): a single pass with no nested loops.
# Both must return identical answers on every test.
# No max(), min(), sum(), or slicing to compute sums.
# All-negative lists must return the single largest element, not 0.
# Do not import libraries.

# Hint
# At each position, ask: is it better to extend the running sum, or to start fresh here?

def max_subarray_brute(nums):

    # Handle an empty list.
    if not nums:
        raise ValueError("Input list cannot be empty.")

    # Initialize the maximum sum using the first element.
    # This ensures all-negative lists are handled correctly.
    best_sum = nums[0]

    # Store the starting and ending indexes of the best subarray.
    best_start = 0
    best_end = 0

    # Outer loop: Choose where the subarray starts.
    for i in range(len(nums)):

        # Reset the running sum whenever we start a new subarray.
        current_sum = 0

        # Inner loop: Extend the subarray from index i onwards.
        for j in range(i, len(nums)):

            # Add the current element to the running sum.
            current_sum += nums[j]

            # Check whether this subarray has a larger sum
            # than the best one we've found so far.
            if current_sum > best_sum:

                # Update the maximum sum.
                best_sum = current_sum

                # Remember the starting and ending indexes.
                best_start = i
                best_end = j

    # Return the maximum sum and its corresponding indexes.
    return best_sum, best_start, best_end

def max_subarray_fast(nums):

    # Handle an empty list.
    if not nums:
        raise ValueError("Input list cannot be empty.")

    # Initialize the current running sum with the first element.
    current_sum = nums[0]

    # Initialize the maximum sum found so far.
    # Starting with nums[0] ensures all-negative lists work correctly.
    best_sum = nums[0]

    # Track where the current subarray starts.
    current_start = 0

    # Track the starting and ending indexes of the best subarray.
    best_start = 0
    best_end = 0

    # Start from index 1 because index 0 was used for initialization.
    for i in range(1, len(nums)):

        # Decide whether to extend the existing subarray
        # or start a completely new subarray at index i.
        if nums[i] > current_sum + nums[i]:

            # Starting fresh gives us a larger sum.
            current_sum = nums[i]

            # Update the starting index of the current subarray.
            current_start = i

        else:

            # Extending the existing subarray is better.
            current_sum += nums[i]

        # Check whether the current subarray has the largest sum
        # we've encountered so far.
        if current_sum > best_sum:

            # Update the maximum sum.
            best_sum = current_sum

            # Save the starting and ending indexes.
            best_start = current_start
            best_end = i

    # Return the maximum sum and its indexes.
    return best_sum, best_start, best_end


print(max_subarray_fast([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
