print("##### SECOND-LARGEST #####")

numbers = list(map(int, input("Enter a list of numbers: ").split()))
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

highest = unique_numbers[0]

for i in range(len(unique_numbers)):
    if unique_numbers[i] > highest:
        highest = unique_numbers[i]

unique_numbers.remove(highest)

if len(unique_numbers) > 0:
    second_highest = unique_numbers[0]
    for i in range(len(unique_numbers)):
        if unique_numbers[i] > second_highest:
            second_highest = unique_numbers[i]
    print(f"The second highest is {second_highest}")

if len(unique_numbers) < 1:
    print("There is no second highest number in this list")
