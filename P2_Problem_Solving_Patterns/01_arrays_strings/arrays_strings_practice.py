# Arrays and strings practice.

# 1. Largest number in array
numbers = [5, 12, 9, 21, 3]
print("Largest number:", max(numbers))

# 2. Sum of array elements
print("Sum:", sum(numbers))

# 3. Check palindrome string
word = "racecar"
print("Palindrome:", word == word[::-1])

# 4. Count vowels
sentence = "python interview practice"
vowels = "aeiou"
count = sum(1 for ch in sentence.lower() if ch in vowels)
print("Vowel count:", count)

# 5. Remove duplicate characters
text = "programming"
unique_chars = "".join(sorted(set(text)))
print("Unique characters:", unique_chars)

# 6. Most frequent element
arr = [1, 2, 2, 3, 3, 3, 4]
from collections import Counter
freq = Counter(arr)
print("Most frequent:", freq.most_common(1)[0][0])

# 7. Check anagram
s1 = "listen"
s2 = "silent"
print("Anagram:", sorted(s1) == sorted(s2))

# 8. Longest substring without repeating characters
sample = "abcabcbb"
seen = {}
start = 0
best = 0
for i, ch in enumerate(sample):
    if ch in seen and seen[ch] >= start:
        start = seen[ch] + 1
    seen[ch] = i
    best = max(best, i - start + 1)
print("Longest substring length:", best)
