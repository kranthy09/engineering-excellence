"""
Given an integer of numbers, find contigous subarray with maximum sum
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, arr):
        """
        kadane's algorithm
        """
        maxTillhere = arr[0]
        res = arr[0]
        for i in range(1, len(arr)):
            maxTillhere = max(maxTillhere + arr[i], arr[i])
            res = max(maxTillhere, res)
        return res


if __name__ == "__main__":
    arr = [5, -6, 3, 2, 7, -5, 8]
    ans = Solution()
    print(ans.expected_approach(arr))
