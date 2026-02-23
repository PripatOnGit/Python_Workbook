#Python program to interchange first and last elements in a list

#1.Using Direct Assignment
lst = [1, 2, 3, 4, 5]
lst[0], lst[-1] = lst[-1], lst[0]

print( lst)

#2.Using Tuple Variable
lst = [12, 35, 9, 56, 24]
pair = lst[-1], lst[0]
lst[0], lst[-1] = pair
print(lst)


#3. Using the * Operator
#This method splits the list into the first element, the middle part, and the last element, then places them back in swapped order.
lst = [12, 35, 9, 56, 24]
a, *mid, b = lst
lst = [b, *mid, a]
print(lst)

#4.Using Slicing
#This method creates a new list by rearranging slices so the last element moves to the front and the first moves to the end.
lst = [12, 35, 9, 56, 24]
lst = lst[-1:] + lst[1:-1] + lst[:1]
print(lst)

#5.Using a Temporary Variable
#This method performs a manual swap using a separate variable to hold the first element.
lst = [12, 35, 9, 56, 24]
tmp = lst[0]
lst[0] = lst[-1]
lst[-1] = tmp
print(lst)