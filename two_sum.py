'''Two Sum:
Given a list of integers and a target number, return the indices of the two numbers that add up to the target. Assume exactly one solution exists.

Psuedocode:


'''

def two_sum(ls, target):
    index_dict = {}
    for index, num in enumerate(ls):
        rem = target - num 
        if rem in index_dict:
            return [index_dict[rem], index]
        else:
            index_dict[num]=index
            print(index_dict[num])
    return None

nums = [3, 7, 3, 15]
target = 6
print(f"Target value at indices: {two_sum(nums, target)}")
