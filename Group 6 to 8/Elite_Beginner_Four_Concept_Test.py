##########
# QUEST 1 - Recursion
##########

def total(n): 
  if n == 1: 
    return 1 
  return n + total(n - 1)

### A. Trace it - total(4)
# total(4) = 4 + total(3)
# total(3) = 3 + total(2)
# total(2) = 2 + total(1)
# total(1) = 1
# Therefore, total(4) = 4 + 3 + 2 + 1 = 10

### B. Find the problem - What happens for total(0) and total(-3)?
# For total(0): The function will not terminate because there is no base case for n == 0.
# For total(-3): The function will not terminate because there is no base case for n < 1.

def total_new(n): 
  if n == 0 or n == 1: 
    return n
  if type(n) is not int:
    raise TypeError("Input must be an integer.") # The behaviour I chose for non-integer inputs is to raise a TypeError.
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  return n + total_new(n - 1)

### C. Explain termination
# The base case in the function is when n is 0 or 1. When n reaches 0 or 1, the function returns n, which stops the recursion. If n is negative or not an integer, the function raises an error, preventing infinite recursion.
# The recursive case is when n is greater than 1. In this case, the function calls itself with n - 1, which continues until it reaches the base case.
# Each call must move toward a stopping condition because n is decremented by 1 in each recursive call. This ensures that the function will eventually reach the base case and terminate.
# The failure that occurs if the stopping condition is never reached is an infinite recursion, which would lead to a stack overflow error.

### D. Code it
def countdown_sum(n): 
  if n <= 0: 
    return 0
  if n % 2 == 0:
    n -= 1 
  return n + countdown_sum(n - 2)

print(countdown_sum(5)) # 9
print(countdown_sum(4)) # 4
print(countdown_sum(1)) # 1
print(countdown_sum(0)) # 0


##########
# QUEST 2 - Big O Notation
##########

def has_duplicate_a(items): 
  for i in range(len(items)): 
    for j in range(i + 1, len(items)): 
      if items[i] == items[j]: 
        return True 
  return False 

def has_duplicate_b(items): 
  seen = set() 
  for item in items: 
    if item in seen: 
      return True 
    seen.add(item) 
  return False 

def has_duplicate_c(items): 
  items = sorted(items) 
  for i in range(1, len(items)): 
    if items[i] == items[i - 1]: 
      return True 
  return False

### A. Analyze: For each implementation, state the worst-case or expected time complexity as appropriate, plus auxiliary space complexity. Point to the operations that create that cost.

  # has_duplicate_a (Nested Loops):
  #   - Time Complexity: O(n²) in the worst case, where n is the number of items. This is because for each item, we compare it with every other item.
  #   - Auxiliary Space Complexity: O(1) as no additional data structures are used.

  # has_duplicate_b (Hash Set):
  #   - Time Complexity: O(n) expected time complexity, where n is the number of items. In the best case, each lookup in the set takes constant time.
  #   - Auxiliary Space Complexity: O(n) for storing the elements in the set.

  # has_duplicate_c (Sorting):
  #   - Time Complexity: O(n log n) due to the sorting step. The comparison step is O(n).
  #   - Auxiliary Space Complexity: O(1) if we sort in place, or O(n) if a new list is created for the sorted version.

### B. Predict before running: Compare a list of 10,000 distinct integers with a list whose first two values are equal. Which implementations can return early? Which is likely to do the most work on distinct values? Explain why Big O is not an exact stopwatch.

  # For a list of 10,000 distinct integers: 
  #   - has_duplicate_a: Will check all pairs, resulting in O(n²) time complexity.
  #   - has_duplicate_b: Will iterate through the list once, checking the set for each item. Expected O(n) time complexity.
  #   - has_duplicate_c: Will sort the list (O(n log n)) and then check adjacent elements (O(n)). Overall O(n log n) time complexity.

  # For a list of 10,000 integers with two equal values at the beginning:
  #   - has_duplicate_a: Will check all pairs, but will find the duplicate early in some cases.
  #   - has_duplicate_b: Will find the duplicate immediately after adding the second value to the set.
  #   - has_duplicate_c: Will sort the list and then find the duplicate when comparing adjacent elements.

  # Which functions can return early without processing the entire list?:
  #   - has_duplicate_a can return early if it finds a duplicate during its nested loop checks.
  #   - has_duplicate_b can return early as soon as it finds a duplicate in the set.
  #   - Unlike A and B, Function C must first sort the entire list before it starts checking for duplicates. Although it can return early during the checking loop, it cannot avoid the initial sorting operation.

  # Which function is likely to do the most work on distinct values?:
  #   - has_duplicate_a is likely to do the most work on distinct values because it checks every pair of items, resulting in O(n²) time complexity. In contrast, has_duplicate_b and has_duplicate_c have better time complexities (O(n) and O(n log n), respectively) and will perform fewer operations on distinct values.

  # Why Is Big O Not an Exact Stopwatch?
  #   - Big O notation describes how an algorithm's resource requirements grow as the input size increases, rather than exactly how many seconds it takes to execute. For example, although Function A has O(n²) worst-case time complexity, it can return immediately if the first two elements are equal. In that situation, it may finish faster than Function C, which must sort the list first. This demonstrates that Big O describes growth patterns, not exact execution times.

### C. Correct the misconception - “Implementation B is O(1) because set membership is O(1).” 
  #   - The statement is incorrect because while set membership checks are O(1) on average, the overall time complexity of Implementation B is O(n) in the worst case. This is because we must iterate through all n items in the input list to check for duplicates. Therefore, the time complexity of Implementation B is O(n), not O(1).

### D. Make an engineering choice: Choose an implementation for millions of records. Discuss speed, memory, sorting/input mutation, and what collision-heavy hashing could mean. A strong answer names a trade-off.
  #   - For millions of records, I would choose Implementation B (using a set) for its expected O(n) time complexity and O(n) auxiliary space complexity. This implementation is generally faster than the others because it allows for quick lookups and can return early if a duplicate is found. However, the main trade-off is memory usage. Implementation B requires O(n) additional space because it stores unique records in a set. For millions of records, this could consume substantial memory.


##########
# QUEST 3 — Hashing and Hash Maps
##########