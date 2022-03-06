"""
Generate a Fibonacci Sequence
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
O(2^n), O(n) time complexity if cached
"""
import timeit
from functools import cache


class Template:
    @staticmethod
    def nth_fibonacci_iterative(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    @staticmethod
    def nth_fibonacci_recursive(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Template.nth_fibonacci_recursive(n - 1) + Template.nth_fibonacci_recursive(n - 2)

    @staticmethod
    @cache
    def nth_fibonacci_recursive_cached(n):
        """
        @cache significantly reduces time/space complexity for recursive functions by hashing the function call
        with its arguments so previously computed results can be returned in O(1) time, collapsing the complexity
        into something closer to O(n).
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Template.nth_fibonacci_recursive(n - 1) + Template.nth_fibonacci_recursive(n - 2)


# test code
assert Template.nth_fibonacci_iterative(4) == 3
assert Template.nth_fibonacci_recursive(4) == 3
assert Template.nth_fibonacci_recursive_cached(4) == 3

print(timeit.timeit("Template.nth_fibonacci_iterative(5)", globals=globals()))
print(timeit.timeit("Template.nth_fibonacci_recursive(5)", globals=globals()))
print(timeit.timeit("Template.nth_fibonacci_recursive_cached(5)", globals=globals()))

