"""
Queens (Hard)
@topic: recursion
@difficulty: hard
@tags: recursion, backtracking, puzzles

N-Queens Problem
The n-queens puzzle is the problem of placing n queens on a (nx n)
chessboard such that no two queens can attack each other. Note that
two queens attack each other if they are placed on the same row,
the same column, or the same diagonal.
Given an integer n, find all distinct solutions to the n-queens puzzle.

You can return your answer in any order but each solution should
represent a distinct board configuration of the queen placements,
where the solutions are represented as permutations of [1, 2, 3,..., n].
In this representation, the number in the ith position denotes the
column in which the queen is placed in the ith row.
For eg. below figure represents a chessboard [2, 4, 1, 3].


i/o: n = 4
o/p: [[2, 4, 1, 3], [3, 1, 4, 2]


Approaches:
1. Expected: Recursion + Backtracking
"""


class Solution:

    def n_queens(self, n):
        """
        TC:
        AS:
        """
        pass


if __name__ == "__main__":
    arrs = [
        4, 8, 3, 9
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.n_queens(arr))
