"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
"""


class Solution:
    def reverse(self, x):
        # abs to remove sign, reverse the string
        x_list = str(abs(x))[::-1]

        # check the sign
        sign = -1
        if x > 0:
            sign = 1

        # str > int
        x = int("".join(x_list)) * sign

        # constrain bounds to signed i32 min/max
        if (x < (-2 ** 31)) or (x > ((2 ** 31) - 1)):
            return 0
        else:
            return x


# test code
sol = Solution()
assert sol.reverse(123) == 321
assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21

