# Recursion practice.

# 1. Countdown

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# 2. Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial 5:", factorial(5))

# 3. Sum 1 to n

def sum_upto(n):
    if n == 0:
        return 0
    return n + sum_upto(n - 1)

print("Sum upto 5:", sum_upto(5))

# 4. Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci 6:", fibonacci(6))
