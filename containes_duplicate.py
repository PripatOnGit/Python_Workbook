def check_duplicate(nums):
    set_nums = set(nums)

    if len(nums) == len(set_nums):
        return False
    else: return True



#option2:
def check_duplicate(nums):
    set_nums = set()

    for i in nums:
        if i not in set_nums:
            set_nums.add(i)
        else: return True

    return False