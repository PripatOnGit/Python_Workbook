# Function practice for logic building.

# 1. Add two numbers

def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

# 2. Check even number

def is_even(num):
    return num % 2 == 0

print(is_even(6))

# 3. Largest of two numbers

def max_of_two(a, b):
    if a > b:
        return a
    return b

print(max_of_two(10, 20))

# 4. Factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

# 5. Reverse a string

def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_string("python"))

# 6. Count vowels

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Learning Python"))

# 7. Prime check

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(17))
