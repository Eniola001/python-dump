from_base = int(input("Enter the base of the number: "))
value = input("Enter the value: ")
to_base = int(input("Enter the base you want to convert to: "))

# Convert the value to decimal first
decimal_value = int(value, from_base)

# Convert decimal to the target base
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if decimal_value == 0:
    result = "0"
else:
    result = ""

    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value = decimal_value // to_base

print("Result:", result, "(Base", to_base, ")")
