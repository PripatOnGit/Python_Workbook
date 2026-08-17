# Recursion

Recursion is when a function calls itself to solve a smaller version of the same problem.

## Core idea

Every recursive solution needs:
- a base case: when to stop
- a recursive step: reduce the problem toward the base case

## Practice problems

1. Print numbers from n to 1
2. Calculate factorial recursively
3. Calculate Fibonacci recursively
4. Reverse a string recursively
5. Count down from a value
6. Sum numbers from 1 to n
7. Find the nth Fibonacci number
8. Check whether a string is a palindrome recursively

## Example

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
```

## Interview tip

A recursive solution is elegant when the problem naturally breaks into smaller subproblems, but it can be less memory-efficient than iterative solutions.
