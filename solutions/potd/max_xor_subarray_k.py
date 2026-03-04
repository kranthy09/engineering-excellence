"""
Max Xor Subarray K (Medium)
@topic: potd
@difficulty: medium
@tags: arrays, prefix

Given an array of integers arr[]  and a number k.
Return the maximum xor of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

i/o: [2, 5, 8, 1, 1, 3], k = 3
o/p: 15


Approaches:
1. Expected: Slide window size of k, compute prefix xors.
"""


class Solution:
    def maximum_xor_k(self, arr, k):
        """
        compute the prefix xors of elements, when the window size
        exceeds, shirnk the window by removing windows first element
        so at and index i, of length k-size window then first element
        would be at i-k.(utilizing a^a=0) property.
        TC: O(n), window is slided forward and every element is visited
        at most twice.
        AS: O(1)
        """

        n = len(arr)

        curr_xor = 0
        # compute xor for first k-size window
        for i in range(0, k):
            curr_xor ^= arr[i]

        # result
        max_xor = curr_xor

        # now slide window to array last
        for j in range(k, n):

            # incoming next element into window
            curr_xor ^= arr[j]

            # shrink the window size
            curr_xor ^= arr[j-k]

            # capture the maximum
            max_xor = max(max_xor, curr_xor)
        return max_xor


if __name__ == "__main__":
    arrs = [
        [[2, 5, 8, 1, 1, 3], 3],  # 15
        [[1, 2, 4, 5, 6], 2],  # 6
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.maximum_xor_k(arr[0], arr[1]))
