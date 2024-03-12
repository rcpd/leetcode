"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
from collections import deque


class Solution:
    @staticmethod
    def isValid(s):
        stack = []
        q = deque(s)

        while q:
            if q[0] in "([{":
                stack.append(q.popleft())
            else:
                if stack:
                    if q[0] == ")" and stack and stack[-1] == "(":
                        stack.pop()
                        q.popleft()
                    elif q[0] == "]" and stack and stack[-1] == "[":
                        stack.pop()
                        q.popleft()
                    elif q[0] == "}" and stack and stack[-1] == "{":
                        stack.pop()
                        q.popleft()
                    else:
                        return False
                else:
                    return False

        if stack:
            return False
        else:
            return True


# test code
assert Solution.isValid("()")
assert Solution.isValid("()[]{}")
assert not Solution.isValid("([")
assert not Solution.isValid("(){}}{")
