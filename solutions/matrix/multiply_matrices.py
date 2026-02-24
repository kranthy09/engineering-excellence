"""
Multiply Matrices (Easy)
@topic: matrix
@difficulty: easy
@tags: matrix, builtin

Given two matrices mat1[][] and mat2[][] of size (4x4).
Find whether the resultant res[][] matrix is equal
to the multiplication of both the matrices.


i/o: mat1[[1, 2, 3, 4], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
     mat2[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
o/p: [[1, 2, 3, 4], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


Approaches:
1. Expected: Direct multiplication, O(n^2)
"""


class Solution:

    def multiply_matrices(self, mat1, mat2):
        """
        TC: O(n^2)
        AS: O(1)
        """
        mat = []
        for i in range(4):
            mat.append([])
            for j in range(4):
                val = 0
                for k in range(4):
                    val += mat1[i][k] * mat2[k][j]
                mat[i].append(val)
        return mat


if __name__ == "__main__":
    mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]]
    mat2 = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]]
    ans = Solution()
    print(ans.multiply_matrices(mat1, mat2))
    # [[4, 6, 6, 4], [12, 14, 14, 12], [20, 22, 22, 20], [4, 6, 6, 4]]
