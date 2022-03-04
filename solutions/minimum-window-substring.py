"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string ""

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    @staticmethod
    def minWindow(s, t):
        size = len(t)-1
        max_size = len(s)
        start = 0
        res = ""

        def extend_window(start, size):
            found = {}
            s_slice = s[start:start+size]
            for i, t_char in enumerate(t):
                for j, s_char in enumerate(s_slice):
                    # record position if found and not previously used (duplicates)
                    if t_char == s_char:
                        if i in found and found[i] >= j:
                            continue
                        else:
                            found[i] = j
                            break

            if len(found) != len(t):
                print("%s not found in %s (expanding search)" % (t, s_slice))
                start += 1
                if start >= max_size-size+1:
                    print("max size reached")
                    return ""
                else:
                    return extend_window(start, size)
            else:
                print("%s found in %s (returning)" % (t, s_slice))
                return s_slice

        while not res and size <= max_size:
            size += 1
            res = extend_window(start, size)

        return res


# test code
print("result: %s" % Solution.minWindow("ADOBECODEBANC", "ABC"))
