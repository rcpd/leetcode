"""
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.
"""


class Solution:
    @staticmethod
    def removeKdigits(num, k):
        """
        Solution: pop the largest numbers from the front while building new number in a stack O(n)
        """
        stack = []

        for number in num:
            # compare number to last stack member(s)
            while k and stack and stack[-1] > number:
                # while previously seen numbers are larger delete up to k times
                k -= 1
                stack.pop()

            # every number is stacked
            stack.append(number)

        # if members still in stack (i.e. largest were least significant)
        if k > 0:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"


# test code
if __name__ == '__main__':
    assert Solution.removeKdigits(num="1432219", k=3) == "1219"
    assert Solution.removeKdigits(num="10200", k=1) == "200"
    assert Solution.removeKdigits(num="10", k=2) == "0"


