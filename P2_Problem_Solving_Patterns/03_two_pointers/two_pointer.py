'''Two Sum (Two Pointer way) - O(n)'''

def two_sum(nums, target):
    left = 0
    right = len(nums)-1

    while(left<right):
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif target < sum:
            right -= 1
        else:
            left += 1
    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))