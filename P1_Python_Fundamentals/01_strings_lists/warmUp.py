# Find Max Value from List
def find_max(numbers):
    temp = numbers[0]
    for num in range(len(numbers)):
        if numbers[num] >= temp:
            temp = numbers[num]
    return temp


# Find Min Value from List
def find_min(numbers):      
    temp = numbers[0]
    for num in range(len(numbers)):
        if numbers[num] <= temp:
            temp = numbers[num]
    return temp

#Modify it into find_max_and_its_index(numbers) — return both the max value AND its position in the list
def find_max_and_its_index(numbers):
    max_value = numbers[0]
    max_index = 0
    for index in range(len(numbers)):
        if numbers[index] > max_value:
            max_value = numbers[index]
            max_index = index
    return max_value, max_index


#Given a list of numbers, count how many of them are even — without using any built-in filter/count functions.
#Example: [3, 7, 2, 9, 4, 6] 

def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

#Write get_even_numbers(numbers) that returns a list of all even numbers (not just the count).
def get_even_numbers(numbers):
    l = []
    count = 0
    for num in numbers:
        if num % 2 == 0:
            l.append(num)
    return l

#count_frequency(items)
def count_frequency(numbers):
    dict = {}
    for num in numbers:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    return dict

#freqency counting
def count_vowels(word):
    vowels = ['a','e','i','o','u']
    counter  = 0
    for char in word:
        if char in vowels:
            counter += 1
    return counter
print(count_vowels('education'))