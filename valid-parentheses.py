"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution(object):
    @staticmethod
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        s = list(s)

        while s:
            # TODO: sort?
            if s[0] in "([{":
                stack.append(s.pop(0))
            else:
                if stack:
                    # TODO: dict?
                    if s[0] == ")" and stack and stack[-1] == "(":
                        stack.pop()
                        s.pop(0)
                    elif s[0] == "]" and stack and stack[-1] == "[":
                        stack.pop()
                        s.pop(0)
                    elif s[0] == "}" and stack and stack[-1] == "{":
                        stack.pop()
                        s.pop(0)
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
