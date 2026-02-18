"""
Missing Elements In Range (Medium)
@topic: potd
@difficulty: medium
@tags: Hash

Given an array arr[] of distinct integers and a range [low, high],
find all the numbers within the range that are not present in the
array. return the missing numbers in sorted order.

i/o: [10, 12, 11, 15], low = 10, high = 15
o/p: [13, 14]


Approaches:
1. Expected: create Hashmap to store existence of array numbers.
"""


class Solution:
    def missing_range(self, arr, low, high):
        """
        TC: O(n+(high-low)+1)
        AS: O(n)
        """
        # code here
        n = len(arr)
        res = []
        # consider hashmap for larger n, other approach can build
        # freq array which takes more than 500mb of auxiliary space
        # for an 10^5 input size.
        hmap = dict()
        for i in range(n):
            # mark the presence of elements
            hmap[arr[i]] = 1
        for num in range(low, high+1):
            # .get method returns None, for no key with num
            if not hmap.get(num):
                res.append(num)
        return res


if __name__ == "__main__":
    arrs = [
        [[1, 4, 11, 51, 15], 50, 55],  # [50, 52, 53, 54, 55]
        # [46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60]
        [[1, 14, 31, 51, 45], 45, 60],

    ]
    ans = Solution()
    for arr in arrs:
        print(ans.missing_range(arr[0], arr[1], arr[2]))
        print("*"*10)
