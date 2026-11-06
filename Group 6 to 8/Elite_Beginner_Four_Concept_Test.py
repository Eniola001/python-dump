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

def hash_key(key): 
  return sum(ord(char) for char in key) % 7 

### A. Calculate: Manually calculate the slot index for 'cat', 'act', 'dog', and 'god'. Show the character code sum and remainder for each.
  # cat = ord('c') + ord('a') + ord('t') = 99 + 97 + 116 = 312; 312 % 7 = 4
  # act = ord('a') + ord('c') + ord('t') = 97 + 99 + 116 = 312; 312 % 7 = 4
  # dog = ord('d') + ord('o') + ord('g') = 100 + 111 + 103 = 314; 314 % 7 = 6
  # god = ord('g') + ord('o') + ord('d') = 103 + 111 + 100 = 314; 314 % 7 = 6

### B. Reason about collisions: Identify any collisions. Explain why different strings can map to the same index and why a matching index does not prove two keys are equal.
  # Collisions:
  # 'cat' and 'act' both map to index 4.
  # 'dog' and 'god' both map to index 6.

  # Different strings can map to the same index due to the modulo operation, which can result in the same remainder for different sums.

  # A matching index does not prove two keys are equal because multiple different strings can have the same hash value, leading to a collision. e.g., 'cat' and 'act' have the same hash value but are different strings.

### C. Implement: Build a seven-slot hash map using separate chaining. Implement put(key, value), get(key), and delete(key). put must update an existing key rather than duplicate it; get must return None for a missing key; delete must remove only the requested key.

# Create seven empty slots
hash_map = [[] for _ in range(7)]

# Add or update a key-value pair
def put(key, value):
  slot = hash_map[hash_key(key)]

  for pair in slot:
    if pair[0] == key:
      pair[1] = value
      return

  slot.append([key, value])

# Retrieve the value associated with a key
def get(key):
  slot = hash_map[hash_key(key)]

  for pair in slot:
    if pair[0] == key:
        return pair[1]

  return None

# Delete only the requested key
def delete(key):
    slot = hash_map[hash_key(key)]

    for i, pair in enumerate(slot):
      if pair[0] == key:
        slot.pop(i)
        return

# Testing the hash map
put("cat", 14)
put("act", 16)
put("dog", 20)

print(get("cat"))  # 14
print(get("act"))  # 16

put("cat", 50)
print(get("cat"))  # 50 (updated)

delete("cat")
print(get("cat"))  # None (deleted)
print(get("act"))  # 16 (still exists)

print(hash_map)


### D. Analyze:  Explain expected time complexity under reasonable hashing assumptions and worst case complexity if all keys land in one bucket. Explain how a larger table may help without guaranteeing O(1)or every operation.

  # Under reasonable hashing assumptions, where keys are uniformly distributed across the hash table, the expected time complexity for `put`, `get`, and `delete` operations is O(1). This is because each operation involves computing the hash value and accessing the corresponding slot, which should take constant time on average.

  # However, in the worst-case scenario where all keys land in one bucket (due to poor hash function or many collisions), the time complexity for these operations can degrade to O(n), where n is the number of keys in that bucket. In this case, we would have to iterate through all the key-value pairs in that single bucket to find, update, or delete a key.

  # A larger table can help reduce the likelihood of collisions by providing more slots for keys to be distributed across. This can improve the average-case performance of the hash map but it also requires more memory and does not guarantee collision-free hashing. The performance will depend on the quality of the hash function and the distribution of keys.


##########
# QUEST 4 — Decorators
##########

def announce(func):
  print("Decorator is running")
  def wrapper(*args, **kwargs):
      print("Before function")
      result = func(*args, **kwargs)
      print("After function")
      return result
  return wrapper

@announce
def multiply(a, b):
  print("Multiplying")
  return a * b

print("Program started")
answer = multiply(3, 4)
print("Answer:", answer)

### A. Predict the output: Write every printed line in exact order before running the program. Explain why the decorator's first print happens before “Program started.”

  # Expected output:
  # Decorator is running
  # Program started
  # Before function
  # Multiplying
  # After function
  # Answer: 12

  # The decorator's first print happens before “Program started” because the `@announce` decorator is applied to the `multiply` function at definition time. When the Python interpreter encounters the `@announce` decorator, it immediately calls the `announce` function with `multiply` as an argument, and the print statement inside `announce` executes right away.

### B. Explain the parts: What does @announce do? What is wrapper? Why are *args and **kwargs useful? Why does returning result matter?

  # The @announce tells Python to pass the multiply function into the announce decorator.

  # The wrapper is an inner function defined inside the decorator. Its job is to wrap additional behavior around the original function.

  # *args and **kwargs are useful because they allow the wrapper function to accept any number of positional and keyword arguments, making it flexible enough without needing to know the exact parameters of the function being decorated.

  # Returning `result` from the `wrapper` function is important because it allows the modified function to return the same value as the original function. If we didn't return `result`, the caller of the decorated function would not receive the expected output, which could lead to unexpected behavior in the program.

### C. Repair a bug: If wrapper calls func(*args, **kwargs) but does not return its result, answer becomes None. Explain why and correct the wrapper.

  # If the wrapper calls func(*args, **kwargs) but does not return its result, the decorated function will return None because the wrapper function itself does not have a return statement. In Python, if a function does not explicitly return a value, it implicitly returns None.

  # To correct the wrapper, we need to ensure that it returns the result of the original function call. The corrected wrapper should look like this:
    # def wrapper(*args, **kwargs):
    #     print("Before function")
    #     result = func(*args, **kwargs)
    #     print("After function")
    #     return result  # Ensure the result is returned to the caller

###. D. Implement: Write count_calls, a decorator that tracks how many times a decorated function is called. The count must persist, the original result must be returned, and positional arguments must work. Demonstrate three calls and show the final count

def count_calls(func):
    count = 0  # Initialize a counter

    def wrapper(*args, **kwargs):
        nonlocal count  # Use nonlocal to modify the count variable
        count += 1  # Increment the count each time the function is called
        result = func(*args, **kwargs)  # Call the original function
        return result  # Return the result of the original function

    def get_count():  
        return count  # Return the current count
    wrapper.get_count = get_count  # Attach the get_count function to the wrapper
    return wrapper

@count_calls
def multiply(a, b):
    return a * b

# Demonstrate three calls
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(6, 7))

# Display the final count
print("Total function calls:", multiply.get_count())