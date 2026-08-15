'''Given a list of numbers, find the second largest. No sorting.'''



def find_second_largest(arr):
    largest_num = float('-inf')
    second_largest = float('-inf')
    for num in arr:
        if num > largest_num:
            temp = largest_num
            largest_num = num
            second_largest = temp
        elif num < largest_num and num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
            print("no second distinct value exists in this list")
            return(largest_num, None)
    return(largest_num, second_largest)

#arr = [5,5,5,5]
arr = [2,7,4,10,-9,4]
print(find_second_largest(arr))