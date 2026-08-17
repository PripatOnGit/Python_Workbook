# Practice file for conditionals.
# Write the logic first, then code it.

# 1. Even or odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Voting eligibility
age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 3. Largest of three numbers
a, b, c = 10, 25, 18
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number:", largest)

# 4. Grade system
marks = 82
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"
print("Grade:", grade)

# 5. Positive / negative / zero
value = -5
if value > 0:
    print("Positive")
elif value < 0:
    print("Negative")
else:
    print("Zero")

# 6. Leap year
year = 2024
if year % 400 == 0:
    is_leap = True
elif year % 4 == 0 and year % 100 != 0:
    is_leap = True
else:
    is_leap = False
print(year, "is leap year:", is_leap)
