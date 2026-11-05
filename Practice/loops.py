#### FOR LOOP ####
##number = int(input("Enter a number I should count to from 1: "))
##for i in range(1, number + 1):
##    print(i)
##
##sentence = input("Enter a sentence and I'll output every third word: ")
##words = sentence.split()
##
##for i in range(2, len(words), 3):
##    print(words[i])

number = int(input("Enter a number to get the multiplication table(s): "))

for i in range(1, number + 1):
    print(f"#### {i} TIMESTABLE ####")
    for j in range(1, 13):
        print(f"{i} x {j} = {i*j}")

#### WHILE LOOP ####
secret_number = 7
print("Hint: The secret number is between 0 and 9")
print("""Instruction: Enter whole numbers only (no alphabets, symbols, etc)
You have only 5 attempts""")
attempts = 0

while attempts < 5:
    guess = int(input("Guess the secret number - "))
    attempts += 1
    if guess == secret_number:
        print(f"Guess #{attempts} - Correct!")
        break
    elif guess > secret_number:
        print(f"Guess #{attempts} - Too high!")
    elif guess < secret_number:
        print(f"Guess #{attempts} - Too low!")

if attempts == 5 and guess != secret_number:
    print("Out of attempts :(")
        
