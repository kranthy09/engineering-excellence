"""
A ramp in an integer array nums is a pair ((i, j))
for which (i < j) and (nums[i] <= nums[j]).
The breadth of such a ramp is (j - i). Given an
integer array nums, return the maximum breadth of a ramp in nums.
If there is no ramp in nums, return 0.
"""

from typing import List


class PossibleMaxBreadthRamp:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def brute_force(self):
        """
        find all the possible values that can form
        ramp and calculate the breadth.
        TC: O(n^2)
        SC: O(1)
        """
        n = len(self.arr)
        max_breath = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if self.arr[i] <= self.arr[j]:
                    max_breath = max(max_breath, j-i)
        return max_breath

    def expected_approach(self):
        """
        Construct monotonically decreasing stack
        which keeps track of smaller elements
        then traverse the array from right to left
        such that use stack for finding out the ramp breadth
        """
        n = len(self.arr)
        stack = []
        for i in range(n):
            if not stack or self.arr[i] < self.arr[stack[-1]]:
                stack.append(i)
        max_breadth = 0
        for i in range(n-1, -1, -1):
            while stack and self.arr[stack[-1]] <= self.arr[i]:
                max_breadth = max(max_breadth, i - stack.pop())
        return max_breadth


if __name__ == "__main__":
    arr = [6, 0, 8, 2, 1, 4]
    res = PossibleMaxBreadthRamp(arr)
    print(res.brute_force())
    print(res.expected_approach())
