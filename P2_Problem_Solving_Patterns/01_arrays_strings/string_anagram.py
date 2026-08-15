'''
Anagram in String

Given strings s and p, find all start indices of p's anagrams in s.

Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]

# "cba" at index 0 is anagram of "abc" ✓
# "bac" at index 6 is anagram of "abc" ✓
'''
from collections import Counter
def check_anagrams_string(s,p):
    result = []
    p_count = Counter(p)
    window_size = len(p)

    for i in range(len(s)-window_size+1):
        window = s[i: window_size+i]
        if Counter(window) == p_count:
            result.append(i)
    return result

s = 'cbaebabacd'
p = 'abc'
print(check_anagrams_string(s,p))

