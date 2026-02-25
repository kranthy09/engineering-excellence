"""
Transpose Matrix (Easy)
@topic: matrix
@difficulty: easy
@tags: matrix, arrays

You are given a square matrix of size n x n.
Your task is to find the transpose of the given matrix.
The transpose of a matrix is obtained by converting
all the rows to columns and all the columns to rows.

i/o: [[1, 2], [3, 4]]
o/p: [[1, 3], [2, 4]]


Approaches:
1. Expected: Swapping four elements at a time, O(n^2)
"""


class Solution:
    def transpose(self, mat):
        """
        TC: O(n^2)
        AS: O(1), swapping takes constant amount of time.
        """
        n = len(mat)
        top = 0
        left = 0
        right = n-1
        bottom = n-1

        while top < bottom:
            # left to right
            if top < bottom:
                # swap elements
                for i in range(top, right+1):
                    mat[top][i], mat[i][left] = \
                        mat[i][left], mat[top][i]

            # right to left
            if left < right:
                # swap elements
                for j in range(bottom, left, -1):
                    mat[bottom][j], mat[j][right] = \
                        mat[j][right], mat[bottom][j]
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return mat


if __name__ == "__main__":
    arrs = [
        [[1, 1, 1, 1],
         [2, 2, 2, 2],
         [3, 3, 3, 3],
         [4, 4, 4, 4]],
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.transpose(arr))
    # o/p: [[1, 2, 3, 4],
    #       [1, 2, 3, 4],
    #       [1, 2, 3, 4],
    #       [1, 2, 3, 4]]
