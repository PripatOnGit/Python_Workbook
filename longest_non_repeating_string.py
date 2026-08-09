'''Sliding Window - Variable window size'''


def longest_string(s):
    max_len = 0
    left = 0
    seen = set()

    for right in range(0,len(s)):
        if s[right] in seen:
            seen.remove(s[right])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right-left+1) 
    return max_len, seen

s = 'abcabcbb'
print(longest_string(s))