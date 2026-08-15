'''A teacher has a list of students and their scores. Write a program that:

Calculates each student's grade (A/B/C/D/F)
Prints each student's name and grade
At the end prints how many students passed (D and above)
python
students = [
    ("Alice", 92),
    ("Bob", 45),
    ("Carol", 73),
    ("Dan", 58),
    ("Eve", 81)
]
Rules:
A: 90+
B: 75–89
C: 60–74
D: 50–59
F: below 50'''

def grades(students):
    passed_students = []
    for student, marks in students:
        if marks >= 90:
            print(f"{student}'s grade is 'A'")
            passed_students.append(student)
        elif marks >= 75:
            print(f"{student}'s grade is 'B'")
            passed_students.append(student)
        elif marks >= 60:
            print(f"{student}'s grade is 'C'")
            passed_students.append(student)
        elif marks >= 50:
            print(f"{student}'s grade is 'D'")
            passed_students.append(student)
        else:
            print(f"{student}'s grade is 'F'")
    return passed_students

students = [
    ("Alice", 92),
    ("Bob", 45),
    ("Carol", 73),
    ("Dan", 58),
    ("Eve", 81)
]
print(grades(students))

#students = [("Test", 60)]
#print(grades(students))