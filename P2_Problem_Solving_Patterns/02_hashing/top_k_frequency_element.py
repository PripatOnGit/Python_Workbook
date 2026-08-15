from collections import defaultdict,Counter

def top_k(nums, k):
    freq_dict = Counter(nums)
    sorted_freq_dict = sorted(freq_dict, key=lambda x: freq_dict[x], reverse=True)
    #print(sorted_freq_dict)
    return sorted_freq_dict[:k]
    
nums = [1,1,1,2,2,3]
k = 2
print(top_k(nums, k))