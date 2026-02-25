"""
Longest Subarr Majority K (Medium)
@topic: potd
@difficulty: medium
@tags: prefix, arrays

Given an array arr[] and an integer k, the task
is to find the length of longest subarray in which
the count of elements greater than k is more than
the count of elements less than or equal to k.

i/o: [1, 2, 3, 4, 1], k = 2
o/p: 2
The subarray [2, 3, 4] or [3, 4, 1] satisfy the given condition,
and there is no subarray of length 4 or 5 which will
hold the given condition, so the answer is 3.

Approaches:
1. Brute Force: Find all subarrays and count > k, <= k, O(n^3)
2. Expected: Store prefixsums by converting to 1, -1, O(n)
"""


class Solution:
    def longest_subarray(self, arr, k):
        """
        TC: O(n)
        AS: O(n)
        """
        n = len(arr)
        # prefix storage
        hmap = {0: -1}
        # init prefix
        prefix = 0
        # output space
        res = 0
        for i in range(n):
            # convert to 1, for greater elements
            if arr[i] > k:
                prefix += 1
            else:
                # convert to -1, for smaller elements
                prefix -= 1
            # condition for subarray
            if prefix > 0:
                # capture longest
                res = max(res, i+1)
            else:
                # prefix-1 can be potential, to satisfy condition with k
                if prefix - 1 in hmap:
                    # capture longest subarray length
                    res = max(res, i - hmap[prefix-1])
            # for new prefix, store in hmap
            if prefix not in hmap:
                hmap[prefix] = i
        return res


if __name__ == "__main__":
    arrs = [
        [[1, 2, 3, 4, 1], 2]  # 3
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.longest_subarray(arr[0], arr[1]))
