# OOP practice.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

s1 = Student("Priya", "A")
s1.show()

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} speed is now {self.speed}")

car = Car("Tesla", 100)
car.accelerate(30)

class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"Hi, I am {self.name}")

class Developer(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def intro(self):
        print(f"Hi, I am {self.name} and I work with {self.language}")

p = Developer("Asha", "Python")
p.intro()
