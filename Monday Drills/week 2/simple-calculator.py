print("#### SIMPLE CALCULATOR #####")
num1 = int(input("Enter the first operand: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = int(input("Enter the second operand: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    elif num2 != 0:
        print(num1 / num2)
else:
    print("Invalid operator")
