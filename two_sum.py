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
    return None

nums = [2, 7, 11, 15]
target = 9
print(f"Target value at indices: {two_sum(nums, target)}")
