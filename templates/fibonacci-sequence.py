"""
Generate a Fibonacci Sequence
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
O(2^n), O(n) time complexity if cached
"""
from functools import cache


class Template:
    @staticmethod
    @cache
    def nth_fibonacci_recursive(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Template.nth_fibonacci_recursive(n - 1) + Template.nth_fibonacci_recursive(n - 2)

    @staticmethod
    def nth_fibonacci_iterative(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


# test code
assert Template.nth_fibonacci_recursive(4) == 3
assert Template.nth_fibonacci_iterative(4) == 3
