def fizzbuzz(n):
    output = []
    if n == 0:
        return []
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            output.append(str(i))
        elif i % 3 == 0 and i % 5 != 0:
            output.append("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            output.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
    return output 

