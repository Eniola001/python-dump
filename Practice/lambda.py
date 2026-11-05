# Exercise 1: Write a lambda function that calculates the cube of a number.
cube = lambda x: x * x * x
# print(cube(3))

# Exercise 2: Write a lambda function that returns the smaller of two numbers.
smaller = lambda x, y: x if x < y else y
# print(smaller(5,6))

# Exercise 3: Use map() and lambda to add 10 to every number in this list:
numbers = [0,1,2,3,4,5,6,7,8,9]
add_ten = list(map(lambda x: x + 10, numbers))
# print(add_ten)

# Exercise 4: Use filter() and lambda to select numbers greater than 5.
over_five = list(filter(lambda x: x > 5, numbers))
# print(over_five)

# Exercise 5: Sort these tuples by age, from youngest to oldest.
people = [
    ("Alice", 25),
    ("Bob", 19),
    ("Charlie", 30),
    ("David", 22)
]
result = sorted(people, key=lambda people: people[1])
# print(result)