class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def give_raise(self, amount):
        if amount>0:
            self.salary += amount
        else: 
            print("Raise amount must be positive")
        return self.salary    

    def get_info(self):
        return f"{self.name} belongs to dept {self.dept} has salary {self.salary}"


    def apply_tax(self, tax_rate):
        self.salary = self.salary * (1 - tax_rate)
        return self.salary
        

emp1 = Employee('Alex','AI',240000)
emp2 = Employee('Sam','Computer',50000)

emp1.give_raise(500)
emp1.get_info()
emp1.apply_tax(0.25)

emp2.give_raise(500)
emp2.get_info()
emp2.apply_tax(0.25)