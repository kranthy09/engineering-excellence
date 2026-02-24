"""
Spirally Traversing Matrix (Medium)
@topic: matrix
@difficulty: medium
@tags: matrix, puzzles

You are given a rectangular matrix mat of size n x m, and your
task is to return an array while traversing the matrix in spiral form.


i/o: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

o/p: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


Approaches:
1. Expected: Identify repeated work and do for every step.
"""


class Solution:
    def spirally_traverse(self, mat):
        """
        TC: O(n*m)
        AS: O(1), resultant array is output space.
        """
        n = len(mat)
        m = len(mat[0])

        top = 0
        right = m-1
        left = 0
        bottom = n-1

        res = []
        while len(res) < n*m:
            # left to right
            for k in range(left, right+1):
                res.append(mat[top][k])

            # top to bottom
            for i in range(top+1, bottom):
                res.append(mat[i][right])

            # right to left
            if bottom > top:
                for k in range(right, left-1, -1):
                    res.append(mat[bottom][k])

            # bottom to top
            if right > left:
                for i in range(bottom-1, top, -1):
                    res.append(mat[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return res


if __name__ == "__main__":
    mats = [
        [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],

        [[32, 44, 27, 23], [54, 28, 50, 62]]
    ]
    ans = Solution()
    for mat in mats:
        print(ans.spirally_traverse(mat))
    # [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
    # [32, 44, 27, 23, 62, 50, 28, 54]
