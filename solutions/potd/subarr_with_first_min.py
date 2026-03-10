"""
Subarr With First Min (Medium)
@topic: potd
@difficulty: medium
@tags: arrays

You are given an integer array arr[ ]. Your task is to count
the number of subarrays where the first element is the minimum
element of that subarray.

Note: A subarray is valid if its first element is not greater
than any other element in that subarray.

i/o: arr[] = [1, 3, 5, 2]
o/p: 8


Approaches:
1. Expected: using stack and find nse for each element.
"""


class Solution:

    def count_subarrays(self, arr):
        """
        TC: O(n)
        AS: O(n), for maintaining a stack
        """

        n = len(arr)

        # construct a monotonic stack
        s = []
        ans = 0
        for i in range(n-1, -1, -1):

            while s and arr[s[-1]] >= arr[i]:
                s.pop()

            if len(s) == 0:
                last = n
            else:
                last = s[-1]

            ans += (last - i)
            s.append(i)
        return ans


if __name__ == "__main__":
    arrs = [
        [1, 3, 5, 8, 2],  # 12
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.count_subarrays(arr))
