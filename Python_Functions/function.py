#Write a function sum_all(*args) that returns the sum of any number of numbers.
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,5))

#Write a function print_details(**kwargs) that prints each key and value on a separate line.
#Example: print_details(name="Priyanka", role="DE")

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_details(name="Priyanka", role='DE')

#Write a function get_name_age() that returns two values: your name and age. Unpack them into variables
def get_name_age(name, age):
    return name, age

name, age = get_name_age("Priyanka", 33)
print(name, age)

#Lambda Functions
#Use a lambda with map() to double all numbers in a list [1,2,3,4].

l = [1,2,3,4]
print(list(map(lambda x:x*2, l)))
