numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))

target = int(input("Enter the target sum: "))

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Numbers: {numbers[i]} + {numbers[j]} = {target}")
            print(f"Indexes: [{i}, {j}]")
            found = True

if not found:
    print(f"No pair of numbers adds up to {target}.")
