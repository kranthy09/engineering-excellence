"""
Nth Fibonacci (Easy)
@topic: recursion
@difficulty: easy
@tags: recursion, mathematics

You are given a number n. You need to find the nth Fibonacci number.

i/o: 5
o/p: 5


Approaches:
1. Expected: Recursion
"""


class Solution:

    def nth_fibonacci(self, n):
        """
        # Fibonacci series:
        # 1, 1, 2, 3, 5, 8, 13, ...
        # f(n) = f(n-2) + f(n-1)
        # n0 = 1, n1 = 1

        TC: O(2^n)
        AS: O(n), recursive call stack
        """

        # base case
        if n == 1:
            return 1
        if n == 2:
            return 1
        # asking recursion for nth number, do sum of n-1, n-2
        return self.nth_fibonacci(n-1) + self.nth_fibonacci(n-2)


if __name__ == "__main__":
    nums = [
        3,  # 2
        5,  # 5
        8,  # 21
    ]
    ans = Solution()
    for num in nums:
        print(ans.nth_fibonacci(num))
