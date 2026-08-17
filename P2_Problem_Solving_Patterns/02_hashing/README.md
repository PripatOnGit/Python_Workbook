# Hashing

Hashing is used to store and access data efficiently using key-value mappings.

## Core ideas

- A dictionary maps a key to a value
- Hashing helps with fast lookup, counting, and grouping
- Common interview tasks involve frequency counting and duplicate detection

## Practice problems

1. Count frequencies of characters in a string
2. Count frequencies of numbers in a list
3. Check if an array contains duplicates
4. Find the most frequent element in a list
5. Group words by length
6. Find the first non-repeating character in a string
7. Check if two strings are anagrams using a dictionary
8. Find pairs that sum to a target
9. Build a dictionary of student scores
10. Count repeated words in a sentence

## Typical patterns

- Use a dictionary as a frequency map
- Use the key as the value to track
- Use set membership for quick existence checks

## Example

```python
freq = {}
for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

## Interview tip

If the problem demands quick lookup or counting, hashing is often the natural solution.
