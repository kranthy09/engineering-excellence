"""
Search In Sorted Matrix (Medium)
@topic: matrix
@difficulty: medium
@tags: matrix, binarysearch

Given a strictly sorted 2D matrix mat[][] of size n x m
and a number x. Find whether the number x is present in
the matrix or not.

Note: In a strictly sorted matrix, each row is sorted
in strictly increasing order, and the first element of
the ith row (i!=0) is greater than the last element of
the (i-1)th row.

i/o: [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
o/p: True


Approaches:
1. Expected: Consider top right element to start search, O(log(n*m))
"""


class Solution:
    def search_in_sorted(self, mat, x):
        """
        TC: O(log(n*m))
        AS: O(1)
        """
        n = len(mat)
        m = len(mat[0])

        # first row index
        i = 0
        # last column index
        j = m-1

        while i < n and j >= 0:
            # element is target
            if mat[i][j] == x:
                return True
            # first element in the last row is greater than target,
            # no other element will be target as the column is in
            # increasing sorted order.
            if mat[i][j] > x:
                j -= 1
            else:
                # else the row cannot have element lesser than current i,j
                # discard row to search in next row.
                i += 1
        return False


if __name__ == "__main__":
    arrs = [
        [[[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], 42],
        # o/p: False
        [[[87, 96, 99], [101, 103, 111]], 101],
        # o/p: True
    ]
    ans = Solution()

    for arr in arrs:
        print(ans.search_in_sorted(arr[0], arr[1]))
