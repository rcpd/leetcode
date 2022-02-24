"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'.
    Read this character in if it is either.
    This determines if the final result is negative or positive respectively.
    Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached.
    The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
    If no digits were read, then the integer is 0.
    Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
        then clamp the integer so that it remains in the range.
    Specifically, integers less than -231 should be clamped to -231,
        and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""


class Solution(object):
    @staticmethod
    def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """

        sign = 1
        int_str = []
        digit = False
        s = s.lstrip()

        # empty string
        if not s:
            return 0

        for i, char in enumerate(s):
            # check sign
            if i == 0 and char in ("-", "+"):
                if char == "-":
                    sign = -1
                    continue
                if char == "+":
                    continue

            # check digit
            if digit:
                # if digit found and non-digit encountered
                if not char.isdigit():
                    break
            else:
                # flag first digit found
                if char.isdigit():
                    digit = True
                else:
                    return 0

            # collect digits
            int_str.append(char)

            # TODO: count with ord(char) - ord(0) faster than list/join/cast
            # TODO: check int before any addition would overflow
            '''
            if num > MAX_NUM // 10 or (num == MAX_NUM // 10 and curr_digit > 7):
                return MAX_NUM if sign == 1 else MIN_NUM
            '''

        # cast digits to int, accounting for sign
        if int_str:
            x = int("".join(int_str)) * sign
        else:
            return 0

        # contrain bounds to signed i32 min/max
        if x < (-2 ** 31):
            return -2 ** 31
        elif x > (2 ** 31 - 1):
            return 2 ** 31 - 1
        else:
            return x


# test code
assert Solution.myAtoi("+1") == 1
assert Solution.myAtoi("-") == 0
assert Solution.myAtoi("") == 0
assert Solution.myAtoi("words and 987") == 0
assert Solution.myAtoi("42") == 42
assert Solution.myAtoi("   -42") == -42
assert Solution.myAtoi("4193 with words") == 4193
assert Solution.myAtoi("-91283472332") == -2147483648
assert Solution.myAtoi("2147483649") == 2147483647







