"""
Given an array of n integers nums, a magic
pattern is a subsequence of three integers
nums[i], nums[j], and nums[k] such that
(i < j < k) and (nums[i] < nums[k] < nums[j]).
Return true if there is a magic pattern
in nums, otherwise, return false.
"""

from typing import List


class FindMagicPattern:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def brute_force(self):
        """
        find all possible values of i, j, k such that it satisfies
        the given pattern
        TC: O(n^3)
        SC: O(1)
        """
        n = len(self.arr)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.arr[i] < self.arr[k] and self.arr[k] < self.arr[j]:
                        return 1
        return 0

    def expected_approach(self):
        """
        construct monotonically increasing stack
        Traverse the arr from right to left
        if there happens more than two pops
        i.e., for any two elements the pse is same
        then their exists the magic pattern
        """
        n = len(self.arr)
        stack = []
        count = 0
        for i in range(n-1, -1, -1):
            while stack and self.arr[i] < self.arr[stack[-1]]:
                stack.pop()
                count += 1
            if count >= 2:
                return 1
            else:
                count = 0
            stack.append(i)
        return 0


if __name__ == "__main__":
    arr = [3, 1, 4, 2]
    res = FindMagicPattern(arr)
    print(res.brute_force())
    print(res.expected_approach())
