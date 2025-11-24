"""
You are given an integer array arr of length n
that represents a permutation of the integers
in the range ([0, n - 1]). We split arr into
some number of partitions, and individually
sort each partition. After concatenating them,
the result should equal the sorted array.

Return the largest number of partitions we can make to sort the array.
"""

from typing import List


class MaxPartiotionsSortedArray:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def brute_force(self):
        """
        """
        pass

    def expected_approach(self):
        """
        consider monotonically increasing stack,
        if the incoming element is less than the stack top
        it can make the partition
        """
        n = len(self.arr)
        stack = []
        for i in range(n):
            curr_max = self.arr[i]
            while stack and self.arr[i] < stack[-1]:
                popped = stack.pop()
                curr_max = max(curr_max, popped)
            stack.append(curr_max)
        return len(stack)


if __name__ == "__main__":
    arr = [2, 1, 0, 3, 4]
    res = MaxPartiotionsSortedArray(arr)
    print(res.brute_force())
    print(res.expected_approach())
