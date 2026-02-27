"""
Square Submatrix Sum X (Hard)
@topic: potd
@difficulty: hard
@tags: matrix, prefix
@starred: true

Given a matrix mat[][] of size n × m and an integer x,
find the number of square submatrices whose sum of elements is equal to x.

i/o: [[2, 4, 7, 8, 10],
      [3, 1, 1, 1, 1],
      [9, 11, 1, 2, 1],
      [12, -17, 1, 1, 1]] , x = 10

o/p: 3


Approaches:
1. Expected: Compute prefix sums of matrix and find the submatrix sum with x.
"""


class Solution:

    def count_squares(self, mat, x):
        """
        TC:
        AS:
        """

        n = len(mat)
        m = len(mat[0])

        prefix = [[0]*m for _ in range(n)]
        prefix[0][0] = mat[0][0]
        for i in range(1, n):
            prefix[i][0] = prefix[i-1][0] + mat[i][0]

        for j in range(1, m):
            prefix[0][j] = prefix[0][j-1] + mat[0][j]

        for i in range(1, n):
            for j in range(1, m):
                prefix[i][j] = mat[i][j] + prefix[i-1][j] + \
                    prefix[i][j-1] - prefix[i-1][j-1]
        # square matrix of length k
        sq = min(n, m)
        cnt = 0
        for k in range(1, sq+1):
            result = 0
            for r in range(k-1, n):
                for c in range(k-1, m):
                    result = prefix[r][c]
                    if r - k >= 0:
                        result -= prefix[r-k][c]

                    if c - k >= 0:
                        result -= prefix[r][c-k]
                    if r - k >= 0 and c - k >= 0:
                        result += prefix[r-k][c-k]
                    if result == x:
                        cnt += 1
        return cnt


if __name__ == "__main__":
    arrs = [
        [[[2, 4, 7, 8, 10],
          [3, 1, 1, 1, 1],
          [9, 11, 1, 2, 1],
          [12, -17, 1, 1, 1]], 10]
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.count_squares(arr[0], arr[1]))
