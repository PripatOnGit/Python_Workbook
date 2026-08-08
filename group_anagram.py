'''
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
check Group Anagram
'''
from collections import defaultdict
def group_anagram(words):
    words_dict = defaultdict(list)

    for w in words:
        words_dict[tuple(sorted(w))].append(w)

    return list(words_dict.values())
    

words = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(words))