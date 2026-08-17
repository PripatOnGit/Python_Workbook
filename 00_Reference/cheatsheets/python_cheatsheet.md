# Python Quick Cheat Sheet

## Core syntax

- Variables: `name = "Priya"`
- Print: `print("Hello")`
- Input: `value = input("Enter value: ")`
- Conditionals:
  ```python
  if x > 0:
      print("Positive")
  elif x == 0:
      print("Zero")
  else:
      print("Negative")
  ```
- Loops:
  ```python
  for i in range(5):
      print(i)

  while count < 5:
      print(count)
      count += 1
  ```

## Common built-ins

- `len(obj)`
- `sum(list)`
- `max(list)`
- `min(list)`
- `sorted(list)`
- `enumerate(list)`
- `range(start, stop, step)`
- `list(set(...))`

## String methods

- `strip()`
- `split()`
- `join()`
- `replace()`
- `lower()`
- `upper()`
- `startswith()`
- `endswith()`

## List methods

- `append()`
- `extend()`
- `insert()`
- `pop()`
- `remove()`
- `sort()`
- `reverse()`
- `index()`
- `count()`

## Dictionary methods

- `get(key, default)`
- `keys()`
- `values()`
- `items()`
- `update()`
- `setdefault()`

## Set methods

- `add()`
- `remove()`
- `discard()`
- `union()`
- `intersection()`
- `difference()`

## Exception handling

```python
try:
    value = int("abc")
except ValueError:
    print("Invalid integer")
else:
    print("Valid integer")
finally:
    print("Always executes")
```

## File I/O

```python
with open("file.txt", "r") as f:
    content = f.read()

with open("file.txt", "w") as f:
    f.write("hello")
```

## Function pattern

```python
def add(a, b):
    return a + b
```

## Quick interview checklist

- Understand the problem
- Write brute-force logic
- Identify the pattern
- Optimize if needed
- Explain time and space complexity
- Test edge cases
