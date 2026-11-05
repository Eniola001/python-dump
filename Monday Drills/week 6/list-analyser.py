# Find smallest, largest, total, average
# Find the index of smallest and largest
# Find how many numbers are above average

# Example
# Input list: [12, 5, 27, 8, 14, 27, 3]
# Smallest: 3 (at index 6)
# Largest: 27 (at index 2)
# Total: 96
# Average: 13.71
# Numbers above average: 3

numbers = [12, 5, 27, 8, 14, 27, 3]

smallest, largest, total = numbers[0], numbers[0], 0

for i in range(len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
        smallest_index = i
    if numbers[i] > largest:
        largest = numbers[i]
        largest_index = i
    total += numbers[i]

average = total / len(numbers)
above_average = 0

for number in numbers:
    if number > average:
        above_average += 1

print(f"Smallest: {smallest} (at index {smallest_index})")
print(f"Largest: {largest} (at index {largest_index})")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Numbers above average: {above_average}")