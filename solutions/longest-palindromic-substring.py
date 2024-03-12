"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution(object):
    @staticmethod
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str

        Solution: starting at left/right expand outwards to find the biggest palindrome using two interleaved
            search patterns to cover odd or even numbered palindromes.
        Edge cases: single char
        """
        res = ""
        for i in range(len(s)):
            odd = Solution.palindromeAt(s, i, i)  # 1, 3, 5, ...
            even = Solution.palindromeAt(s, i, i + 1)  # 2, 4, 6, ...
            res = max(res, odd, even, key=len)
        return res

    @staticmethod
    def palindromeAt(s, left, right):
        """
        :type s: str
        :type left: int
        :type right: int
        :rtype: str
        """
        # while in bounds and matching
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # exclude the last -/+ 1 (which is now out of bounds or mismatch)
        return s[left+1:right]


# test code
if __name__ == "__main__":
    assert Solution.longestPalindrome("babaddtattarrattatddetartrateedredividerb") == "ddtattarrattatdd"
    assert Solution.longestPalindrome("aacabdkacaa") == "aca"
    assert Solution.longestPalindrome("aaaa") == "aaaa"
    assert Solution.longestPalindrome("a") == "a"
    assert Solution.longestPalindrome("ac") == "a"
    assert Solution.longestPalindrome("bb") == "bb"
    assert Solution.longestPalindrome("babab") == "babab"
    assert Solution.longestPalindrome("baab") == "baab"
    assert Solution.longestPalindrome("babad") in ("bab", "aba")
    assert Solution.longestPalindrome("cbbd") == "bb"


