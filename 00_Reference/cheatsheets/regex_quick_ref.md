# Regex Quick Reference

## Common patterns

- `\d` = digit
- `\w` = word character
- `\s` = whitespace
- `.` = any character except newline
- `*` = zero or more
- `+` = one or more
- `?` = zero or one
- `[]` = character class
- `|` = OR
- `^` = start of string
- `$` = end of string

## Common examples

```python
import re

text = "abc123"
print(re.search(r"\d+", text))
print(re.findall(r"[A-Za-z]+", text))
```

## Use cases

- validate email or phone patterns
- find numbers in text
- remove extra whitespace
- check for patterns in logs or CSV data

## Interview reminder

Regex is useful for messy data, but keep it readable and test a few examples before relying on it.
