# Complexity practice.

# This file is mainly conceptual, but here are examples to reason about.

# O(n)
print("Linear loop:")
for i in range(1, 11):
    print(i)

# O(n^2)
print("Nested loop:")
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)

# O(1) dictionary lookup
details = {"name": "Priya", "age": 24}
print("Dictionary lookup:", details["name"])

# O(n) count of characters
text = "python"
count = 0
for ch in text:
    count += 1
print("Character count:", count)

# O(log n) example: binary search logic
# This is conceptual; here is a simple integer comparison approach.
arr = [1, 3, 5, 7, 9, 11]
start, end = 0, len(arr) - 1
target = 7
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
        print("Found at index:", mid)
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
