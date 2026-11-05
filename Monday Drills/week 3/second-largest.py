numbers = list(map(int, input("Enter a list of numbers: ").split()))

largest = None
second_largest = None

for number in numbers:
    if number == largest or number == second_largest:
        continue

    if largest is None or number > largest:
        second_largest = largest
        largest = number
    elif second_largest is None or number > second_largest:
        second_largest = number

if second_largest is None:
    print("There is no second-largest unique number.")
else:
    print(f"The second highest is {second_largest}")
