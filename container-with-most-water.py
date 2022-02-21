"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
"""


class Solution(object):
    @staticmethod
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        # left/right index
        i = 0
        j = len(height) - 1
        area = 0

        while i != j:
            width = j-i
            area = max(area, (width * min(height[i], height[j])))

            # creep in from left/right until exhausted maintaining highest
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area


# test code
assert Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution.maxArea([1, 1]) == 1
