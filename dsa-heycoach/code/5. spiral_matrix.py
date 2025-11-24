"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Inputmatrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(min((rows + 1) // 2, (cols + 1) // 2)):
            self.go_right(matrix, i, i, rows, cols)
            self.go_down(matrix, i, i, rows, cols)
            self.go_left(matrix, i, i, rows, cols)
            self.go_up(matrix, i, i, rows, cols)
        return self.res

    def go_right(self, matrix, i, j, m, n):
        for k in range(j, n - j):
            self.res.append(matrix[i][k])

    def go_down(self, matrix, i, j, m, n):
        for k in range(i + 1, m - i - 1):
            self.res.append(matrix[k][n - j - 1])

    def go_left(self, matrix, i, j, m, n):
        if i < m // 2:
            for k in range(j, n - j):
                self.res.append(matrix[m - 1 - i][n - k - 1])

    def go_up(self, matrix, i, j, m, n):
        if i < n // 2:
            for k in range(i + 1, m - i - 1):
                self.res.append(matrix[m - k - 1][j])
