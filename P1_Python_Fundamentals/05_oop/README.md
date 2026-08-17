# Object-Oriented Programming Basics

This topic introduces classes and objects, which help organize code into reusable building blocks.

## Core idea

A class is a blueprint, and an object is an instance of that class.

## Common concepts

- class
- object
- attribute
- method
- constructor (`__init__`)
- inheritance

## Practice problems

1. Create a `Student` class with name and grade
2. Add a method to display the student info
3. Create a `Car` class with brand and speed
4. Add a method to accelerate the car
5. Create a `BankAccount` class with balance and deposit/withdraw methods
6. Create a subclass `Developer` from a `Person` class
7. Add an `__init__` constructor to a class
8. Use inheritance to share common attributes

## Example

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, self.grade)
```

## Interview tip

Keep OOP simple: understand objects, attributes, methods, and inheritance before worrying about advanced design patterns.

Classes and Objects are best for complex, structured applications where you need to combine data with behaviors (methods), enforce data protection, and reuse code through inheritance. They prevent runtime key errors and provide autocompletion and static type checking.

Dictionaries (dict) are best for simple, lightweight key-value lookups, dynamic data, or quick script utility where you only need raw data storage without custom logic or methods attached.