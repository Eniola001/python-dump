# Problem

# Print the first N numbers of the Fibonacci sequence. Calculate the sum of only the even numbers in that sequence.
# Finally, print the sequence in reverse order.

# Examples
# Input: N = 8
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13
# Even Sum: 10 (which is 0 + 2 + 8)
# Reversed: 13, 8, 5, 3, 2, 1, 1, 0

# Constraints
# Generate the sequence using a loop (no recursion).
# Do not store the sequence in an array/list to reverse it.
# Print the reversed sequence using mathematical logic or string-building without [::-1] or .reverse().
# Do not use sum().
# Do not import libraries.

N = int(input("Input: N = "))

a = 0
b = 1
count = 0
even_sum = 0
sequence = ""

while count < N:
    sequence += str(a)

    if count < N - 1:
        sequence += ", "

    if a % 2 == 0:
        even_sum += a

    next_number = a + b
    a = b
    b = next_number

    count += 1

print("Sequence:", sequence)
print("Even Sum:", even_sum)

# Print the sequence in reverse without a list
print("Reversed:", end=" ")

# Find the last number in the sequence
a = 0
b = 1
count = 0

while count < N:
    next_number = a + b
    a = b
    b = next_number
    count += 1

# a is now the last Fibonacci number
# b is the next Fibonacci number
previous = b - a

while count > 0:
    print(a, end="")

    count -= 1

    if count > 0:
        print(", ", end="")

    temp = a
    a = previous
    previous = temp - previous

print()
