"""
Rotate Matrix 90 (Easy)
@topic: matrix
@difficulty: easy
@tags:

i/o:
o/p:


Approaches:
1. Expected: Reverse rows and swap the lower triangle with upper triangle.
"""

# TODO: Rotate 90 degrees clock-wise


class Solution:

    def expected_solution(self, mat):
        """

        TC:
        AS:
        """
        n = len(mat)
        # step 1 -  reverse the rows
        # step 2 - swap the lower triangle with upper triangle
        return n


if __name__ == "__main__":
    arrs = [
        [],
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.expected_solution(arr))
