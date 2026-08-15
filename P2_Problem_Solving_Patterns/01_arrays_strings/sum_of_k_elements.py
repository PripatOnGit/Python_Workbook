'''Sliding Window Problem -- fixed Window'''

def calc_max_sum(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

nums = [2,  1,  5,  1,  3,  2]
k = 3

print(calc_max_sum(nums,k))

'''
from collections import Counter
print(Counter("hello"))

from collections import defaultdict
d = defaultdict(list)
d['alice'].append('Math')
d['alice'].append('Science')
d['bob'].append('Physics')
print(d)'''