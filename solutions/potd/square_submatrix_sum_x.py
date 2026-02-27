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
        TC: O(n*m*min(n,m))
        AS: O(n*m), maitaining prefixsums
        """
        n = len(mat)
        m = len(mat[0])

        # init prefixsum matrix with 0s
        prefix = [[0]*m for _ in range(n)]
        # assign first value
        prefix[0][0] = mat[0][0]

        # prefix of first row
        for i in range(1, n):
            prefix[i][0] = prefix[i-1][0] + mat[i][0]

        # prefix of first column
        for j in range(1, m):
            prefix[0][j] = prefix[0][j-1] + mat[0][j]

        # prefix for remaining elements
        for i in range(1, n):
            for j in range(1, m):
                prefix[i][j] = mat[i][j] + prefix[i-1][j] + \
                    prefix[i][j-1] - prefix[i-1][j-1]
        # maximum length of square submatrix
        sq = min(n, m)
        cnt = 0
        # for each side length of k
        for k in range(1, sq+1):
            result = 0
            # find the all square matrices of k length and thier
            # prefix sums to find the k-length square submatrix sum is X
            for r in range(k-1, n):
                for c in range(k-1, m):

                    # assign the result, to sum of matrix for all elements
                    # ending at (r,c)
                    result = prefix[r][c]

                    # top overlapping region sum
                    if r - k >= 0:
                        result -= prefix[r-k][c]
                    # remove left overlapping region sum
                    if c - k >= 0:
                        result -= prefix[r][c-k]
                    # add the prefix sum of at i-k, j-k
                    # because two times its removed from overlapping regoins
                    if r - k >= 0 and c - k >= 0:
                        result += prefix[r-k][c-k]

                    # check the square submatrix sum holds condition
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
