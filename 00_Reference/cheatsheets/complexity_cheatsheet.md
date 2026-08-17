# Time and Space Complexity Cheat Sheet

## Common Big-O

- O(1): constant time
- O(log n): logarithmic time
- O(n): linear time
- O(n log n): common in efficient sorting
- O(n^2): nested loops
- O(2^n): exponential, usually not ideal for interviews

## Quick examples

- Accessing one item in a list: O(1)
- Search in a list: O(n)
- Dictionary lookup: O(1) average
- Sorting with Python `sorted()`: O(n log n)
- Nested loops: O(n^2)
- Recursive Fibonacci (naive): O(2^n)

## Interview rule

When you see repeated scanning, nested loops, or comparisons across many pairs, think about optimizing to O(n) or O(n log n).
