# Exception Handling

This topic is about writing code that fails gracefully instead of crashing unexpectedly.

## Core idea

Exceptions occur when the program hits an unexpected condition.

Examples:
- division by zero
- invalid input type
- file not found
- index out of range

## Common keywords

- `try`: code that may fail
- `except`: what to do if it fails
- `else`: code to run if no exception occurs
- `finally`: code that always runs

## Practice problems

1. Handle division by zero
2. Catch invalid integer input
3. Handle file not found errors
4. Validate a list index before access
5. Catch a `ValueError` from conversion
6. Handle empty input gracefully
7. Use `finally` to print cleanup messages
8. Create a custom message for invalid age

## Example

```python
try:
    value = int("abc")
except ValueError:
    print("That is not a valid integer")
```

## Interview tip

Good exception handling is about making the program safe and understandable, not hiding the real bug.
