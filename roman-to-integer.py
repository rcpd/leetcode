"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""


class Solution(object):
    @staticmethod
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        num_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numerals = list(s)  # string into list TODO: faster to iterate directly and not pop
        num = 0
        i = 0

        while numerals:
            # subtraction edge cases
            if numerals[0] in "IXC" and len(numerals) > 1:
                if numerals[0] == "I":
                    if numerals[1] in "VX":
                        num -= 1
                        numerals.pop(0)

                elif numerals[0] == "X":
                    if numerals[1] in "CL":
                        num -= 10
                        numerals.pop(0)

                elif numerals[0] == "C":
                    if numerals[1] in "DM":
                        num -= 100
                        numerals.pop(0)

            # the rest
            num += num_dict[numerals[0]]
            numerals.pop(0)
            i += 1

        return num


# test code
assert Solution.romanToInt("III") == 3
assert Solution.romanToInt("LVIII") == 58
assert Solution.romanToInt("MCMXCIV") == 1994







