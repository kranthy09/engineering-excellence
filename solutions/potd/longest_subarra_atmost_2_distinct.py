"""
Longest Subarra Atmost 2 Distinct (Medium)
@topic: potd
@difficulty: medium
@tags: sliding, window, hashmap

Given an array arr[] consisting of positive integers,
your task is to find the length of the longest subarray
that contains at most two distinct integers.


i/o: [2, 1, 2, 2, 2, 3]
      0  1  2  3  4  5
o/p: 5, from index 0 to 4


Approaches:
1. Expected: sliding window, with hashmap as window size.
"""


class Solution:

    def total_elements(self, arr):
        """
        Create a hashmap and maintain it as window of size 2,
        shirnk the window by moving forward pointer if the
        length of window is greater than 2(atmost two distinct elements)

        TC: O(n)
        AS: O(1)
        """
        n = len(arr)

        res = float("-inf")

        # hashmap with max window (elements) size two
        hmap = {}

        # left start
        i = 0
        # right start
        j = 0
        while j < n:
            # increment the count of j, by expanding the window.
            if hmap.get(arr[j]):
                hmap[arr[j]] += 1
            else:
                hmap[arr[j]] = 1

            # for window size larger than 2, shrink by removing elements
            # from the hashmap.
            while len(hmap) > 2:
                hmap[arr[i]] -= 1
                # if the element count is zero, remove the elements from
                # previous window.
                if hmap.get(arr[i]) == 0:
                    del hmap[arr[i]]
                # shrink by incrementing count of start pointer.
                i += 1
            # atmost two distinct elements capture their window sizes.
            res = max(res, j - i + 1)
            j += 1

        return res


if __name__ == "__main__":
    arrs = [
        [3, 1, 2, 2, 2, 2],  # 5
        [6, 7, 2, 4, 4, 4, 9, 9, 9]  # 6
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.total_elements(arr))
