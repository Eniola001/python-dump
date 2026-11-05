# Calculating the sum of a list recursively
def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        return 0

    return numbers.pop() + recursive_sum(numbers)

#print(recursive_sum([1, 2, 3, 4])) # 10
#print(recursive_sum([5, 10]))      # 15
#print(recursive_sum([]))           # 0

# Reversing a string recursively
def reverse_string(text):
    if len(text) == 0:
        return ""

    return text[-1] + reverse_string(text[:-1])

print(reverse_string("Banzai"))

# factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def function(n):
    if n==4:
        return n
    else:
        return 2*function(n+1)
        
print(function(2))
