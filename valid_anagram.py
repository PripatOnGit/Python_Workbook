'''Valid Anagram
Given two strings, return True if one is an anagram of the other, False otherwise. An anagram uses the same characters the same number of times in any order.
Input:  s = "anagram", t = "nagaram"  → True
Input:  s = "rat",     t = "car"      → False
Input:  s = "cat",     t = "cats"     → False

Pseudocode:
FUNCTION is_anagram(s, t):
    IF len(s) != len(t):
        RETURN ???

    INITIALISE empty dict

    FOR each char in s:
        ADD char to dict with frequency

    FOR each char in t:
        IF char not in dict:
            RETURN ???
        ???  ← what do you do to the count?
        IF count reaches ???:
            REMOVE from dict

    RETURN dict is empty
'''
'''
def valid_anagram(s,t):
    if len(s) == len(t):
        s_dict={}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else: s_dict[i] += 1

        for i in t:
            if i not in s_dict:
                return False
            else: s_dict[i] -= 1
            if s_dict[i] == 0:
                s_dict.pop(i)
        return True
    return False
'''

from collections import Counter
def valid_anagram(s,t):
    return Counter(s) == Counter(t)

check_anagram = valid_anagram('cat','rat')
print(check_anagram)