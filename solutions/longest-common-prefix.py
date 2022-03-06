"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


class Solution:
    @staticmethod
    def longestCommonPrefix(strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]

        return shortest


# test code
assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert Solution.longestCommonPrefix(["flower", "flower", "flower", "flower"]) == "flower"




