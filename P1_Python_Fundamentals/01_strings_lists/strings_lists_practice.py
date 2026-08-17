# Strings and lists practice.

# 1. Reverse a string
text = "python"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# 2. Check palindrome
word = "racecar"
print("Palindrome:", word == word[::-1])

# 3. Count vowels
sentence = "hello world"
vowels = "aeiou"
count = sum(1 for ch in sentence.lower() if ch in vowels)
print("Vowel count:", count)

# 4. Remove spaces
text_with_spaces = "python practice session"
clean_text = text_with_spaces.replace(" ", "")
print("No spaces:", clean_text)

# 5. Find most frequent character
sample = "banana"
char_count = {}
for ch in sample:
    char_count[ch] = char_count.get(ch, 0) + 1
most_common = max(char_count, key=char_count.get)
print("Most common character:", most_common)

# 6. Reverse a list
numbers = [1, 2, 3, 4, 5]
print("Reversed list:", numbers[::-1])

# 7. Find second largest
nums = [10, 20, 30, 40]
# If list is sorted
print("Second largest:", sorted(nums)[-2])
# If list is Unsorted
# Initialise large, second_large to float(-inf)-> loop through list-->  compare numbers --> if both numbers are same then return secon_large number as 'None' and print msg for such case.



# 8. Remove duplicates
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print("Unique items:", unique_items)



## Pallindrom checking with Two Pointers appraches
## 1.skips alphanum 2.Skips 1. Basic Palindrome (All Characters)
# keep alphabets and numbers --> a.alphanum()
# Keep alphabets --> a.alpha()

'''1. Basic Palindrome (All Characters)

Checks if the exact string reads the same forward and backward.'''
#Checks if the exact string reads the same forward and backward.
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False  # Mismatch found
        l, r = l + 1, r - 1  # Move left inward, right inward
    return True  # All characters matched
'''l, r = 0, len(s) - 1 --> Sets l at index 0 and r at the final character's index.

while l < r -->Continues checking as long as the pointers haven't met in the center.

if s[l] != s[r] --> Compares current characters; returns False immediately if they differ.

l, r = l + 1, r - 1 -->Shifts l one step right and r one step left for the next check.'''


'''2. Alphabet-Only Palindrome (Ignore Non-Letters & Case)

Ignores spaces, numbers, and symbols while treating uppercase and lowercase letters as identical.'''
def is_alpha_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalpha():
            l += 1  # Skip non-letters from the left
        while l < r and not s[r].isalpha():
            r -= 1  # Skip non-letters from the right
        if s[l].lower() != s[r].lower():
            return False  # Compare letters in lowercase
        l, r = l + 1, r - 1
    return True

'''while l < r and not s[l].isalpha()  ->Advances l to skip spaces, numbers, and symbols until it lands on a letter.

while l < r and not s[r].isalpha()  -->Reverses r to skip non-alphabetic characters from the end.

s[l].lower() != s[r].lower() -->Converts both letters to lowercase so 'A' matches 'a'.'''