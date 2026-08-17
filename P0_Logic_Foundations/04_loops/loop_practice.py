# Loop practice exercises for logic building.
# Solve each problem by writing the logic first before coding.

# 1. Print numbers from 1 to 10
# Example solution:
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Find sum of numbers from 1 to 10
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i
print("Sum from 1 to 10:", sum_numbers)

# 4. Count vowels in a string
text = "python logic practice"
vowel_count = 0
for ch in text:
    if ch in "aeiou":
        vowel_count += 1
print("Vowel count:", vowel_count)

# 5. Find the largest number in a list
numbers = [12, 45, 7, 89, 23, 52]
largest = numbers[0]
for num in numbers[1:]:
    if num > largest:
        largest = num
print("Largest number:", largest)

# 6. Print multiplication table for 5
print("Multiplication table for 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 7. Print a simple triangle pattern
print("Pattern:")
for i in range(1, 6):
    print("*" * i)

# 8. Check if a given number is prime
number = 17
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
print(f"{number} is prime:", is_prime)
