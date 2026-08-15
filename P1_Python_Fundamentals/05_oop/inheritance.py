'''
CLASS Manager INHERITS Employee:
    INIT(name, dept, salary, team_size):
        CALL parent init with super().__init__(name, dept, salary)
        SET self.team_size = team-size

    hold_meeting():
        RETURN f"{self.name} holds meeting with {self.team_size} people"

    get_info():                    ← override
        RETURN parent get_info + team_size info

CLASS Intern INHERITS Employee:
    INIT(name, dept, salary, duration):
        CALL parent init with ???
        SET self.duration = duration

    convert_to_fulltime():
        IF duration >= 6:
            RETURN f"Converted to full time.'
        ELSE:
            duration = 6 - {self.duration}
            RETURN f"{self.name} needs {self.duration} more months"

    apply_tax():                   ← override
        flat 10% regardless of tax_rate
        RETURN net_salay
'''
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

class Manager(Employee):
    def __init__(self,name, dept, salary, team_size):
        super().__init__(name,dept,salary)
        self.team_size = team_size

    def hold_meetings(self):
        return f"{self.name} holds meeting with {self.team_size} people"

    def get_info(self):
        return f"{self.name} belongs to dept {self.dept} has salary {self.salary} and has {self.team_size} people in team."

class Intern(Employee):
    def __init__(self,name, dept, salary, duration):
        super().__init__(name,dept,salary)
        self.duration = duration

    def convert_to_fulltime(self):
        if self.duration >= 6:
            return f"Converted to full time."
        else:
            rem = 6 - self.duration
            return f"{self.name} needs {rem} more months"

    def get_info(self):
        return f"{self.name} belongs to dept {self.dept} has salary {self.salary}."

    def apply_tax(self, tax_rate):
        self.salary = self.salary * 0.9  # ignore tax_rate, always 10%
        return self.salary

m1 = Manager('Nick', 'Test', 40000, 10)
print(m1.get_info())
print(m1.apply_tax(0.2))
print(m1.give_raise(50000))
print(m1.hold_meetings())


i1 = Intern('Sam', 'Cloud', 50000, 4)
print(i1.get_info())
print(i1.convert_to_fulltime())
print(i1.apply_tax(0.2))