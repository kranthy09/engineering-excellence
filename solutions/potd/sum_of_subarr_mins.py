"""
Sum Of Subarr Mins (Medium)
@topic: potd
@difficulty: medium
@tags: arrays

Given an array arr[] of positive integers,
find the total sum of the minimum elements of
every possible subarrays.

Note: It is guaranteed that the total sum will
fit within a 32-bit unsigned integer.

i/o: arr[] = [10, 20]
o/p: 40


Approaches:
1. Expected: find nge, pge for each element.
"""


class Solution:

    def sum_sub_mins(self):
        """
        TC: O(n)
        AS: O(n), to maintain the nge and pge subarrays
        """
        n = len(arr)

        s1 = []
        s2 = []
        left = [0]*n
        right = [0]*n

        for i in range(n):

            while s1 and arr[s1[-1]] > arr[i]:
                s1.pop()
            if s1:
                left[i] = (i - s1[-1])
            else:
                left[i] = (i+1)
            s1.append(i)

        for i in range(n-1, -1, -1):

            while s2 and arr[s2[-1]] >= arr[i]:
                s2.pop()

            if s2:
                right[i] = (s2[-1] - i)
            else:
                right[i] = (n-i)
            s2.append(i)

        total_sum = 0
        for i in range(n):
            total_sum += arr[i] * left[i] * right[i]

        return total_sum


if __name__ == "__main__":
    arrs = [
        [1, 2, 3, 4],
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.sum_sub_mins(arr))
