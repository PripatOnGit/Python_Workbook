'''
FUNCTION valid_parentheses(s):
    INITIALISE stack = []
    INITIALISE mapping = {')':'(', ']':'[', '}':'{'}

    FOR each char in s:
        IF char is opening bracket:
            stack.append(char)       ← push ✓

        ELSE:  ← it's a closing bracket
            IF stack is empty OR stack[-1] != mapping[char]:
                RETURN False         ← mismatch or empty

            stack.pop()             ← pop the matched opening bracket

    RETURN stack is empty            ← True if all matched, False if leftovers
'''

def valid_parenthesis(s):
    brackets = []
    mapping = {')':'(', ']':'[', '}':'{'}

    for char in s:
        if char not in mapping:
            brackets.append(char)
        elif len(brackets) == 0 or brackets[-1] != mapping[char]:
            return False
        else:
            brackets.pop()
    return (len(brackets)==0)

print(valid_parenthesis('{[]}()))'))
print(valid_parenthesis('()[]{}'))   # → True
print(valid_parenthesis('(]'))       # → False
print(valid_parenthesis('(((' ))     # → False — unmatched openers