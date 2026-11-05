# Problem
# Given an integer N, determine if it is a prime number.
# Then, print the sum of all prime numbers from 2 up to N.

# Examples
# Input: N = 10
# 10 is not prime.
# Primes up to 10: [2, 3, 5, 7]
# Sum of primes: 17

# Input: N = 7
# 7 is prime.
# Primes up to 7: [2, 3, 5, 7]
# Sum of primes: 17

# Constraints
# You may not use range() to iterate from 2 to N directly for the primality check. You must use a while loop.
# To check if a number is prime, stop checking divisors at its square root (use i * i <= num without importing math).
# Do not use sum().
# Do not import libraries.
# Do not hardcode the answer.

N = int(input("N = "))

if N == 2:
    print(f'{N} is prime')
    print('Primes up to {N}: [{N}]')
    print('Sum of primes: {N}')
else:
    i = 2
    is_prime = True

    while i * i <= N:
        if N % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"{N} is prime.")
    else:
        print(f"{N} is not prime.")

n = 2
primes = []
prime_sum = 0

while n <= N:
    i = 2
    is_prime = True

    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        primes.append(n)
        prime_sum += n

    n += 1

print(f'Primes up to {N}: {primes}')
print("Sum of primes:", prime_sum)
