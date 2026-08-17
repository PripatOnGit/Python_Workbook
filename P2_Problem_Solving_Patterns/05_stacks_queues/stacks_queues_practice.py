# Stacks and queues practice.

# 1. Stack example
stack = []
stack.append(10)
stack.append(20)
print("Stack pop:", stack.pop())

# 2. Queue example
from collections import deque
queue = deque(["A", "B", "C"])
queue.append("D")
print("Queue dequeue:", queue.popleft())

# 3. Valid parentheses

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

print("Balanced:", is_valid_parentheses("{[()]}"))

# 4. Reverse a string using stack
text = "python"
stack = list(text)
reversed_text = ""
while stack:
    reversed_text += stack.pop()
print("Reversed string:", reversed_text)
