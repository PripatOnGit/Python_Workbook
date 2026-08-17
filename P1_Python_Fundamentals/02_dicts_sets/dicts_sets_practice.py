# Dictionaries and sets practice.

# 1. Count character frequency
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("Character frequency:", freq)

# 2. Student dictionary
student = {
    "name": "Priya",
    "age": 24,
    "course": "Python"
}
print(student)

# 3. Common keys
a = {"a": 1, "b": 2, "c": 3}
b = {"b": 5, "d": 6}
print("Common keys:", set(a.keys()) & set(b.keys()))

# 4. Remove duplicates using set
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print("Unique items:", unique_items)

# 5. Membership check
numbers = {10, 20, 30}
print("20 in set:", 20 in numbers)

# 6. Frequency of entries
marks = [90, 80, 90, 70, 80]
count = {}
for value in marks:
    count[value] = count.get(value, 0) + 1
print("Marks frequency:", count)

# 7. Group words by first letter
words = ["apple", "ant", "banana", "blue"]
by_letter = {}
for word in words:
    first = word[0]
    by_letter.setdefault(first, []).append(word)
print("Grouped by first letter:", by_letter)

'''This code categorizes a list of strings into a dictionary based on their starting letter, creating key-value pairs where each key is a first letter and its value is a list of words starting with that letter.
How the original code works
first = word[0]: Extracts the first character of the current word.
by_letter.setdefault(first, []): Checks if first is already a key in by_letter. If it isn't, it initializes that key with an empty list [] and returns it. If it already exists, it simply returns the existing list.
.append(word): Adds the current word to the list retrieved or created by setdefault().'''

#Alternative Approaches
#1. Using collections.defaultdict (Cleanest & Most Pythonic)
#Instead of manually handling missing keys inside the loop, defaultdict automatically initializes a new list whenever a non-existent key is accessed.
from collections import defaultdict

words = ["apple", "ant", "banana", "blue"]
by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)

print(dict(by_letter))
# Output: {'a': ['apple', 'ant'], 'b': ['banana', 'blue']}

#2. Using Standard if/else Checking (Explicit Logic)
#This approach manually verifies if the key exists before attempting to append to it. It is slightly more verbose but straightforward.
words = ["apple", "ant", "banana", "blue"]
by_letter = {}

for word in words:
    first = word[0]
    if first not in by_letter:
        by_letter[first] = []
    by_letter[first].append(word)
#3. Using itertools.groupby (Functional Approach)
#If your word list is already sorted (or you sort it first), groupby can group adjacent items sharing the same key function.

from itertools import groupby

words = ["apple", "ant", "banana", "blue"]
# Ensure words are sorted by their first letter first
words_sorted = sorted(words, key=lambda w: w[0])

by_letter = {key: list(group) for key, group in groupby(words_sorted, key=lambda w: w[0])}


# 8. Common elements between lists
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
print("Common elements:", set(list_a) & set(list_b))
