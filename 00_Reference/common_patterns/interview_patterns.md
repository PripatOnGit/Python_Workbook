# Interview Problem Patterns

## 1. Frequency counting

Use when the problem asks for:
- counts
- duplicates
- repeated characters
- most frequent item

Pattern:
```python
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

## 2. Two pointers

Use when:
- array is sorted
- you need to compare endpoints
- you want to avoid nested loops

Pattern:
```python
left, right = 0, len(arr) - 1
while left < right:
    # compare or move pointers
    left += 1
    right -= 1
```

## 3. Sliding window

Use when:
- you need a subarray or substring
- the window grows and shrinks

Pattern:
```python
left = 0
for right in range(len(arr)):
    # expand window
    while condition_is_false:
        left += 1
```

## 4. Recursion

Use when the problem naturally breaks into smaller subproblems.

Pattern:
```python
def solve(n):
    if base_case:
        return result
    return solve(smaller_problem)
```

## 5. Stack

Use for:
- parentheses checking
- reverse order
- nesting validation

Pattern:
```python
stack = []
stack.append(value)
value = stack.pop()
```

## 6. Queue

Use for:
- order processing
- breadth-first traversal
- task scheduling

Pattern:
```python
from collections import deque
queue = deque()
queue.append(value)
value = queue.popleft()
```

## 7. Brute force first

Before optimizing, always ask:
- What is the simplest correct version?
- Can I write it clearly?
- Then can I improve it?

## 8. Explain-before-code

In interviews, say:
- What the problem is asking
- What the brute-force idea is
- What the pattern is
- Why this is efficient enough
