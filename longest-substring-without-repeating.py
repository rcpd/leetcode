"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution(object):
    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int

        Solution: Record first/last index of non-repeating chars
        """
        encountered = {}
        substring = []
        max_len = start = count = 0

        for i, char in enumerate(s):
            # unencountered chars go straight onto substring
            if char not in encountered:
                substring.append(char)  # debug string method

            elif char in encountered:
                # start new substring on next char
                if start <= encountered[char]:
                    start = encountered[char] + 1
                    
                    # warning: this is useful for debug but too slow (and unnecessary) for solution
                    substring = list(s[start:i+1])  # debug string method

                # previous char was already excluded
                else:
                    substring.append(char)  # debug string method

            # test if max increased
            max_len = max(max_len, i - start + 1)

            # cache index of encountered char
            encountered[char] = i

            # debug
            print(max_len, start, substring, encountered)

        return max_len


# test code
if __name__ == '__main__':
    assert Solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution.lengthOfLongestSubstring("bbbbb") == 1
    assert Solution.lengthOfLongestSubstring("pwwkew") == 3
    assert Solution.lengthOfLongestSubstring("dvdf") == 3
    assert Solution.lengthOfLongestSubstring("tmmzuxt") == 5
