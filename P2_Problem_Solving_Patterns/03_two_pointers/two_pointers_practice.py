# Two pointers practice.

# 1. Check if a string is a palindrome
text = "racecar"
left, right = 0, len(text) - 1
is_palindrome = True
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print("Palindrome:", is_palindrome)

# 2. Pair sum target
arr = [1, 2, 3, 4, 6]
target = 6
left, right = 0, len(arr) - 1
found = False
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        found = True
        print("Pair found:", (arr[left], arr[right]))
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
if not found:
    print("No pair found")

# 3. Move zeroes to end
nums = [0, 1, 0, 3, 12]
write_index = 0
for num in nums:
    if num != 0:
        nums[write_index] = num
        write_index += 1
while write_index < len(nums):
    nums[write_index] = 0
    write_index += 1
print("After moving zeroes:", nums)
