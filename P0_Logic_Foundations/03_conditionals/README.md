# Conditionals

This topic teaches you how to make decisions in code.

## Core idea

Conditionals let your program choose different actions based on a condition.

- `if` executes when a condition is true
- `else` executes when the condition is false
- `elif` handles multiple possible conditions

## Why it matters

Most real-world logic is based on decisions:
- is the user old enough?
- is the number even or odd?
- should the program allow login?
- is the grade pass/fail?

## Practice problems

1. Check if a number is even or odd
2. Check if a person is eligible to vote
3. Find the largest of three numbers
4. Grade a student based on marks
5. Check if a year is a leap year
6. Decide if a password is valid
7. Check if a number is positive, negative, or zero
8. Check if a string is empty
9. Determine if an item is in stock
10. Simulate a simple login system

## Approach

For each question:
1. Write the condition clearly
2. Identify the possible outcomes
3. Draft the decision tree
4. Then translate it into Python

## Example pattern

```python
age = 18
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

## Questions to ask while solving

- What exact condition decides the path?
- Are there more than two outcomes?
- What happens when the condition is false?
- What is the simplest way to express the logic?
