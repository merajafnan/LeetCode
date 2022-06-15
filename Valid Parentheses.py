# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Input: s = "()[]{}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'}':'{',')':'(',']':'['}

        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
        # return True if not stack else False

