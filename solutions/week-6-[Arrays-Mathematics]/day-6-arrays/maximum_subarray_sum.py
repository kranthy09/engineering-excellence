"""
Given an integer of numbers, find contigous subarray with maximum sum
"""


class Solution:

    def brute_force(self, arr):
        """
        Generate all possible subarrays

        TC: O(n^2))
        AS: O(1)
        """
        n = len(arr)
        res = float("-inf")
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                res = max(res, curr_sum)
        return res

    def expected_approach(self, arr):
        """
        kadane's algorithm, single pass
        TC: (n)
        AS: O(1)
        """
        maxTillhere = arr[0]
        res = arr[0]
        for i in range(1, len(arr)):
            maxTillhere = max(maxTillhere + arr[i], arr[i])
            res = max(maxTillhere, res)
        return res

    def prefix_sum_approach(self, arr):
        """
        construct prefix sum array
        TC: O(n)
        AS: O(n)
        """
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(n):
            prefix[i] = prefix[i-1] + arr[i]
        min_subsum = 0
        res = float("-inf")
        for i in range(n):
            res = max(res, prefix[i] - min_subsum)
            min_subsum = min(min_subsum, prefix[i])
        return res


if __name__ == "__main__":
    arr = [5, -6, 3, 2, 7, -5, 8]
    ans = Solution()
    print(ans.brute_force(arr))
    print(ans.expected_approach(arr))
    print(ans.prefix_sum_approach(arr))
