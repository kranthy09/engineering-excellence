"""
Move All 0s End (Easy)
@topic: potd
@difficulty: easy
@tags: arrays

You are given an array arr[] of non-negative integers.
You have to move all the zeros in the array to the right end
while maintaining the relative order of the non-zero elements.
The operation must be performed in place, meaning you should not
use extra space for another array.

i/o: [1, 2, 0, 4, 3, 0, 5, 0]
o/p: [1, 2, 4, 3, 5, 0, 0, 0]


Approaches:
1. Expected: Maintain the non-zero position with point and swap, O(n)
"""


class Solution:

    def push_zeros_to_end(self, arr):
        """

        TC: O(n)
        AS: O(1)
        """
        n = len(arr)

        # track non-zero element pos
        j = 0

        for i in range(n):

            if arr[i] != 0:
                # swap the current element with
                # next 0 at index 'j'
                arr[j], arr[i] = arr[i], arr[j]

                # increment j for non-zero element
                j += 1


if __name__ == "__main__":
    arrs = [
        [1, 2, 0, 4, 3, 0, 5, 0],  # [1, 2, 0, 4, 3, 0, 5, 0]
        [40, 20, 30]  # [40, 20, 30]
    ]
    ans = Solution()
    for arr in arrs:
        ans.push_zeros_to_end(arr)
        print(arr)
