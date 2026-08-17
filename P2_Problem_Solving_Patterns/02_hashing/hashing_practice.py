# Hashing / dictionary practice.

# 1. Count frequencies in a string
text = "banana"
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print("Frequency map:", frequency)

# 2. Count numbers in a list
numbers = [1, 2, 2, 3, 3, 3, 4]
count = {}
for num in numbers:
    count[num] = count.get(num, 0) + 1
print("Number count:", count)

# 3. Check duplicates
items = [1, 2, 3, 2, 4]
seen = set()
has_duplicate = False
for item in items:
    if item in seen:
        has_duplicate = True
        break
    seen.add(item)
print("Has duplicate:", has_duplicate)

# 4. Most frequent element
from collections import Counter
nums = [3, 3, 5, 5, 5, 8]
print("Most frequent:", Counter(nums).most_common(1)[0][0])

# 5. First non-repeating character
sample = "aabccdeef"
for ch in sample:
    if sample.count(ch) == 1:
        print("First non-repeating:", ch)
        break

# 6. Two-sum using hash map
arr = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        print("Pair found:", (seen[complement], i))
        break
    seen[num] = i
