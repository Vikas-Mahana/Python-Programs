"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(self, s: str) -> bool:
    # Dictionary to store matching brackets
    brackets = {')': '(', '}': '{', ']': '['}

    # Stack to keep track of opening brackets
    stack = []

    # Iterate through each character in the string
    for char in s:
        # If it's a closing bracket
        if char in brackets:
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != brackets[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()
        else:
            # Push opening bracket onto stack
            stack.append(char)

    # Return True if stack is empty, False otherwise
    return len(stack) == 0
