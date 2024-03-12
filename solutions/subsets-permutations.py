"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    """
    This pattern generally solves similar "backtracking" problems as well (i.e. permutations)
    """
    @staticmethod
    def subsets(nums):
        res = []
        Solution.dfs(nums, [], res)
        print(res)
        return res

    @staticmethod
    def dfs(nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            Solution.dfs(nums[i+1:], path+[nums[i]], res)


# test code
assert Solution.subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
assert Solution.subsets([0]) == [[], [0]]
