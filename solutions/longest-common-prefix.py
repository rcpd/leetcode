"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


class Solution(object):
    @staticmethod
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        '''
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        '''

        prefix_dict = {}
        for string in strs:
            for i, char in enumerate(string):
                prefix = string[:i+1]
                if prefix in prefix_dict:
                    prefix_dict[prefix] += 1
                else:
                    prefix_dict[prefix] = 1

        pre_len = 0
        pre_str = ""
        for prefix in prefix_dict:
            if prefix_dict[prefix] == len(strs):
                pre_len = len(prefix)
                pre_str = prefix

        print(prefix_dict)
        print(pre_len, pre_str)
        return pre_str


# test code
assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert Solution.longestCommonPrefix(["flower", "flower", "flower", "flower"]) == "flower"




