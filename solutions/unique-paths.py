"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot
can take to reach the bottom-right corner.
"""
from functools import cache

class Solution:
    @staticmethod
    def uniquePaths(m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n: return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)


# test code
assert Solution.uniquePaths(3,7) == 28
assert Solution.uniquePaths(3,2) == 3

