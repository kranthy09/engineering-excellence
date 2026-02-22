"""
Count Subarrays Given Xor (Medium)
@topic: potd
@difficulty: medium
@tags: arrays, prefix, map, bitmagic

Given an array of integers arr[] and a number k,
count the number of subarrays having XOR of their elements as k.

i/o: [4, 2, 2, 6, 4], k = 6
o/p: 4


Approaches:
1. Brute Force: O(n^2), find all subarrays
2. Expected: Prefix xors with hashmap., O(n)
"""


class Solution:

    def subarray_xor(self, arr, k):
        """
        TC: O(n)
        AS: O(n), storing prefixes in hashmap.
        """
        hmap = {0: 1}
        count = 0
        prefix = 0
        for num in arr:
            prefix ^= num
            needed = prefix ^ k
            count += hmap.get(needed, 0)
            hmap[prefix] = hmap.get(prefix, 0) + 1
        return count


if __name__ == "__main__":
    arrs = [
        [[4, 2, 2, 6, 4], 6],  # 4
        [[4, 9, 7, 3, 6, 5, 8, 12, 22], 8],  # 2
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.subarray_xor(arr[0], arr[1]))
