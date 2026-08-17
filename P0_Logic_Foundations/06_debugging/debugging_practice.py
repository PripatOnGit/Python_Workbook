# Debugging practice.
# Look at the logic, find the issue, and fix it.

# Example 1: off-by-one bug
# Expected: print 1 to 5
# Actual: may print 1 to 4 depending on the loop
print("Example 1")
for i in range(1, 6):
    print(i)

# Example 2: wrong condition bug
# Intended: print only even numbers
print("Example 2")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Example 3: variable tracking bug
# Intended: count vowels in text
print("Example 3")
text = "python"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Vowel count:", count)

# Example 4: wrong total accumulation
print("Example 4")
values = [2, 4, 6, 8]
total = 0
for value in values:
    total += value
print("Total:", total)

# Example 5: debugging a function
print("Example 5")
def is_even(num):
    return num % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))

# Exercise: find why this code is wrong
# It should print the largest value in the list.
print("Exercise")
nums = [4, 8, 2, 15, 7]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest value:", largest)
