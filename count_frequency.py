'''FUNCTION first_unique(s):
    PASS 1:
        COUNT frequency using Counter

    PASS 2:
        FOR each index, char in enumerate(s):
            IF freq[char] == 1:
                RETURN index

    RETURN -1
'''

#Problem: First occurance of non repeating characters in string.
from collections import defaultdict
def count_frequency(s):
    count = defaultdict(int)

    for char in s:
        count[char] += 1

    for index, char in enumerate(s):
        if count[char] == 1:
            return (index,char)
    return -1

s = "loveleetcode"
print(count_frequency(s))