numbers = []

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

largest = numbers[0]
smallest = numbers[0]
total = 0

even = 0
odd = 0
positive = 0
negative = 0
zero = 0

for number in numbers:
    # Sum
    total += number

    # Largest and smallest
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    # Even and odd
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    # Positive, negative, and zero
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

average = total / 10

print("\n--- Number Analysis ---")
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
