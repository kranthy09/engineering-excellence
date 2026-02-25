"""
Rotate Matrix 90 (Easy)
@topic: matrix
@difficulty: easy
@tags:

Given a square matrix mat[][] of size n x n.
The task is to rotate it by 90 degrees in an
anti-clockwise direction without using any extra space.


i/o:   [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

o/p:   [[2, 5, 8],
        [1, 4, 7],
        [0, 3, 6]]


Approaches:
1. Expected_1: Reverse rows and swap the lower triangle with upper triangle.
2. Expected_2: Actually rotate by swapping the elements.
"""

# TODO: Rotate 90 degrees clock-wise


class Solution:

    def rotate_matrix_expected_2(self, mat):
        """
        TC: O(n^2)
        AS: O(1)
        """
        n = len(mat)
        top = 0
        left = 0
        right = n - 1
        bottom = n - 1
        while top < bottom:
            # left to right
            for k in range(left, right):
                # swap four elements
                (
                    mat[top][k],
                    mat[n - k - 1][left],
                    mat[bottom][n - k - 1],
                    mat[k][right],
                ) = (
                    mat[k][right],
                    mat[top][k],
                    mat[n - k - 1][left],
                    mat[bottom][n - k - 1],
                )
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return mat


if __name__ == "__main__":
    arrs = [
        [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]],
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.rotate_matrix_expected_2(arr))
    # o/p : [[2, 5, 8],
    #        [1, 4, 7],
    #        [0, 3, 6]]
