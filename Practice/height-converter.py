print("##### HEIGHT CONVERTER #####")

cm_height = float(input("Enter your height in centimeters: "))
cm_to_inches = round(cm_height / 2.54)
feet = int(cm_to_inches // 12)
remainder_inches = round(cm_to_inches % 12)

# covering edge case
if remainder_inches == 12:
    feet += 1
    remainder_inches = 0

print(f"You are {feet}'{remainder_inches}\"")
