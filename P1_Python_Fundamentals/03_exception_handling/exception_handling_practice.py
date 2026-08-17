# Exception handling practice.

# 1. Division by zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Invalid integer conversion
try:
    number = int("abc")
except ValueError:
    print("Invalid integer value")

# 3. List index error
numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError:
    print("Index is out of range")

# 4. File not found
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# 5. Clean finally block
try:
    value = int("42")
except ValueError:
    print("Bad input")
else:
    print("Conversion succeeded")
finally:
    print("This always runs")
