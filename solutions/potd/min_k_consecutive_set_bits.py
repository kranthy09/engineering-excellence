"""
Min K Consecutive Set Bits (Hard)
@topic: potd
@difficulty: hard
@tags: greedy

You are given a binary array arr[] (containing only 0's
and 1's) and an integer k. In one operation, you can select
a contiguous subarray of length k and flip all its bits (i.e.,
change every 0 to 1 and every 1 to 0).

Your task is to find the minimum number of such operations
required to make the entire array consist of only 1's. If
it is not possible, return -1.


i/o: [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], k = 2
o/p: 4

Approaches:
1. Expected: Greedy
"""


class Solution:
    def k_bit_flips(self, arr, k):
        """
        TC: O(n)
        AS: O(n), for maintainig diff array
        """
        n = len(arr)

        flips = 0
        active = 0
        diff = [0] * (n+1)

        for i in range(n):
            active += diff[i]
            effective = arr[i] ^ (active % 2)

            if effective == 0:

                if i + k > n:
                    return -1

                flips += 1
                active += 1

                diff[i + k] -= 1
        return flips


if __name__ == "__main__":
    arrs = [
        [[1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], 2],  # 4
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.k_bit_flips(arr[0], arr[1]))
