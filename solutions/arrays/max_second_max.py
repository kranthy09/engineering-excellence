"""

Max and Second Max

Given an array arr[] of positive integers which may have duplicates.
The task is to find the maximum and second maximum from the array,
and both of them should be different from each other, and If no
second maximum exists, then the second maximum will be -1.

i/o: arr[] = 9 8 7 9 99 8 7 6 7 3 73 48 9 74 84 39 84
o/p = 99, 84

Approaches:
1. Expected: find max and 2nd max in one pass
"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        return None

    def expected_solution(self, *args, **kwargs):
        """
        Compute max and second max which is not equal to first
        max.
        TC: O(n)
        AS: O(1)
        """
        arr = args[0]
        n = len(arr)
        mx1 = -1
        mx2 = -1
        for i in range(n):
            if mx1 < arr[i]:
                mx1 = arr[i]
        # print(mx1)
        for i in range(n):
            if mx2 < arr[i] and arr[i] < mx1:
                mx2 = arr[i]
        # print(mx2)
        if mx1 == mx2:
            return mx1, -1
        return mx1, mx2


if __name__ == "__main__":
    arrs = [
        [9, 8, 7, 9, 99, 8, 7, 6, 7, 3, 73, 48, 9]
    ]
    ans = Solution()

    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))
