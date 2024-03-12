"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        # search and yield index(es)
        mid = len(nums) // 2

        if nums[mid] == target:
            min_index = max_index = mid

        low = Solution.recurse(nums, target, 0, mid, "min", -1, -1)
        high = Solution.recurse(nums, target, mid+1, len(nums)-1, "max", -1, -1)
        return [low, high]

    @staticmethod
    def recurse(nums, target, low, high, min_in, max_in, search):
        mid = (high-low) // 2
        print(mid)
        if high-low >= 1:
            min_in = Solution.recurse(nums, target, 0, mid, min_in, max_in, search)
            max_in = Solution.recurse(nums, target, mid+1, len(nums)-1, min_in, max_in, search)
        else:
            if nums[mid] == target:
                if search == "min":
                    return min(mid, min_in)
                else:
                    return max(mid, max_in)
            else:
                if search == "min":
                    return max(-1, min_in)
                else:
                    return max(-1, max_in)


# test code
assert Solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
assert Solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
assert Solution.searchRange(nums=[], target=0) == [-1, -1]

