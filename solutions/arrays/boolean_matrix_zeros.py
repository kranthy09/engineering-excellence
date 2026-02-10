"""
A Boolean Matrix Question

Given a boolean matrix mat where each cell contains either 0 or 1,
the task is to modify it such that if a matrix cell matrix[i][j] is 0
then all the cells in its ith row and jth column will become 0.


Input: [[1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],]

Output: [[0, 0, 0],
        [1, 0, 1],
        [0, 0, 0],]


Approaches:
1. Brute Force: find pairs of i, j at zero, to mark their rows, cols to zero
2. Bucketing Technique: Use 0th row and 0th col as buckets
"""

import copy


class Solution:
    def brute_force(self, *args, **kwargs):
        """
        Collect the zeros pairs, i, j and iterate over row, col by
        modifying them to zero.

        TC: O(n*m(n+m))
        AS: O(m*n), to store the pairs
        """
        mat = args[0]
        n = len(mat)  # rows
        m = len(mat[0])  # cols
        row_bucket = [1] * m
        col_bucket = [1] * n
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    row_bucket[j] = 0
                    col_bucket[i] = 0
        for i in range(n):
            for j in range(m):
                if row_bucket[j] or col_bucket[i]:
                    mat[i][j] = 0
        return mat

    def expected_solution(self, *args, **kwargs):
        """
        consider 0th row and cols as buckets to mark zero in corresponding
        (i,j) elements.
        TC: O(n*m)
        AS: O(1)
        """
        mat = args[0]
        n = len(mat)
        m = len(mat[0])
        zeroth_row = False
        zeroth_col = False
        # traverse first row
        for j in range(m):
            if arr[0][j] == 0:
                zeroth_row = True
                break
        for i in range(n):
            if arr[i][0] == 0:
                zeroth_col = True
                break
        # mark the bucket indexes to zero in inner matrix
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[0][j] = 0
                    mat[i][0] = 0
        # iterate over inner matrix
        for i in range(1, n):
            for j in range(1, m):
                if not (mat[i][0] and mat[0][j]):
                    mat[i][j] = 0
        # modify 0th row and 0th col
        if zeroth_row:
            for j in range(m):
                mat[0][j] = 0
        if zeroth_col:
            for i in range(n):
                mat[i][0] = 0
        return mat


if __name__ == "__main__":
    arrs = [
        [
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
        ],
        [
            [0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
        ],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(copy.deepcopy(arr)))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(copy.deepcopy(arr)))
