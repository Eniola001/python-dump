name, age, gender = input("Enter your details (in the format: 'Name - Age - Gender', e.g. 'John - 25 - Male')): ").split(' - ')
message = f"Hi there {name}! You are {age} and you are {gender}"
print(message)
