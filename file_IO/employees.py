import json

employees = {
    "employees": [
        {"name": "Alice", "department": "Engineering", 
         "salary": 95000, "active": True},
        {"name": "Bob", "department": "Marketing",    
         "salary": 72000, "active": False},
        {"name": "Carol", "department": "Engineering", 
         "salary": 88000, "active": True}
    ]
}

with open('employees.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("File created successfully")

with open('employees.json') as f:
    data = json.load(f)

print(type(data))           # what type is data?
print(type(data['employees']))    # what type is this?
print(data['employees'][0])       # what does this give you?
print(type(data['employees'][0]['active']))  # True or true?