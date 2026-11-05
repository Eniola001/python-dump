numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))

target = int(input("Enter the target sum: "))

seen = {}

found = False

for i in range(len(numbers)):
    number = numbers[i]
    needed = target - number

    if needed in seen:
        print(f"Numbers: {needed} + {number} = {target}")
        print(f"Indexes: [{seen[needed]}, {i}]")
        found = True
        break

    seen[number] = i

if not found:
    print(f"No pair of numbers adds up to {target}.")
