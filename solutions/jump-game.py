"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
from typing import List


class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        # edge case: start on zero jump
        if not nums[0]:
            if len(nums) > 1:
                return False
            else:
                return True

        target = len(nums)-1
        stack = [0]

        while stack:
            # retrieve next possible index
            index = stack.pop()
            jump = nums[index]

            # try to satisfy jump
            if jump >= target-index:
                return True

            # else queue possible jumps
            for i in range(index+1, index+jump+1):
                stack.append(i)

        return False


# test code
assert Solution.canJump([2, 3, 1, 1, 4])
assert not Solution.canJump([3, 2, 1, 0, 4])
assert Solution.canJump([0])
assert not Solution.canJump([0, 1])
assert Solution.canJump([1, 1, 1, 0])

