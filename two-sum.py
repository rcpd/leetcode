"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Solution: cache the index of all seen members O(n), calculate the diff from the target
        """
        num_dict = {}

        # search for the diff
        for i, num in enumerate(nums):
            # calc the diff
            diff = target - num

            # if calc in diff return indexes as list
            if diff in num_dict:
                return [num_dict[diff], i]

            else:
                # store the index of a seen number
                num_dict[num] = i


print(Solution.twoSum([2, 7, 11, 15], 9))
print(Solution.twoSum([3, 2, 4], 6))
print(Solution.twoSum([3, 3], 6))
