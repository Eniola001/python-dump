# Problem
# Given a list and a target value, find every index where the target appears.
# Print all matching indices, the total count of matches, and the index of the first and last occurrence.
# If the target does not appear, print a not-found message.

# Examples
# Starting list: values = [14, 7, 22, 9, 7, 31, 7, 5]
# Target: 7 → Found at indices: [1, 4, 6] | Count: 3 | First: 1 | Last: 6
# Target: 22 → Found at indices: [2] | Count: 1 | First: 2 | Last: 2
# Target: 18 → Target not found

values = [14, 7, 22, 9, 7, 31, 7, 5]

print(f"Starting list: values = {values}")
target = int(input("Target: "))

indices = []
for i in range(len(values)):
    if values[i] == target:
        indices.append(i)

if not indices:
    print(f"Target: {target} → Target not found")
else:
    count = len(indices)
    first = indices[0]
    last = indices[len(indices) - 1]
    print(f"Target: {target} → Found at indices: {indices} | Count: {count} | First: {first} | Last: {last}")