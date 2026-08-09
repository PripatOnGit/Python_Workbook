'''Sliding Window - Variable window size'''


def longest_string(s):
    max_len = 0
    left = 0
    seen = set()

    for right in range(0,len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right-left+1) 
    print(seen)
    return max_len

s = 'abcabcbb'
print(longest_string(s))