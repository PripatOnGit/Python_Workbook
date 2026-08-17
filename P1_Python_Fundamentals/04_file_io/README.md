# File I/O

This topic focuses on reading from and writing to files.

## Common file types

- `.txt`
- `.csv`
- `.json`

## Core operations

- open a file
- read content
- write content
- append content
- close file properly

## Practice problems

1. Read a text file and print its contents
2. Write a sentence to a new file
3. Append a line to an existing file
4. Read a CSV file and print each row
5. Read JSON data from a file
6. Write JSON data to a file
7. Handle missing file errors
8. Count how many lines are in a file

## Example

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

## Interview tip

Use `with open(...)` because it closes the file automatically and makes the code cleaner and safer.
