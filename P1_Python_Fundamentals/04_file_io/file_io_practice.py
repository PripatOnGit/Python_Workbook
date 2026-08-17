# File I/O practice.

# 1. Read a text file
with open("sample.txt", "w") as f:
    f.write("Hello, Python!\nThis is file IO practice.\n")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# 2. Append to a file
with open("sample.txt", "a") as f:
    f.write("Appended line\n")

# 3. Read lines from a file
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# 4. JSON write and read
import json

data = {"name": "Priya", "skills": ["Python", "SQL"]}
with open("sample.json", "w") as f:
    json.dump(data, f)

with open("sample.json", "r") as f:
    loaded = json.load(f)
    print("JSON data:", loaded)
