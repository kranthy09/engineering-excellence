"""
Sudoku Solver (Hard)
@topic: recursion
@difficulty: hard
@tags: recursion, backtracking, puzzles

Sudoku solver.
Given an partially filled sudoku puzzle, complete the board with
suitable numbers, such that, same numbers shouldn't present
in row, col and 3 X 3 matrix its present in.

i/o:
o/p:


Approaches:
1. Expected: Recursion.
"""


def is_safe(i, j, arr, num):
    """
    Checks whether the cell can be assigned
    """

    # check in the row
    for k in range(9):
        if arr[i][k] == num:
            return False

    # check in the column
    for k in range(9):
        if arr[k][j] == num:
            return False

    # check in 3 X 3 matrix
    row_start = i - i % 3  # stating position of 3 X 3
    col_start = j - j % 3  # ending position of 3 X 3
    for r in range(3):
        for c in range(3):
            if arr[row_start + r][col_start + c] == num:
                return False
    return True


def sudoku_solver_util(i, j, arr):
    """
    Util for assigning values to cell and backtract
    for incorrect values.
    """
    # base case
    if i == 8 and j == 9:
        return True

    # column reaches end, move to next row.
    if j == 9:
        i += 1
        j = 0

    # number is already present, move to fill next cell
    if arr[i][j] != 0:
        return sudoku_solver_util(i, j+1, arr)

    for num in range(1, 10):

        # number should be meet condition of puzzle
        if is_safe(i, j, arr, num):
            # fill the number
            arr[i][j] = num
            # check the number can form puzzle
            if (sudoku_solver_util(i, j+1, arr)):
                return True
            # backtrack for the numbers doesnot satisfy the puzzle.
            arr[i][j] = 0
    return False


def sudoku_sovler(arr):
    """
    Solves partially filled sudoku
    """
    # array is directly modified, no need for shared variables.
    sudoku_solver_util(0, 0, arr)

    return arr


if __name__ == "__main__":
    arr = [[3, 0, 6, 5, 7, 8, 4, 0, 0],
           [5, 2, 0, 0, 0, 0, 0, 0, 0],
           [0, 8, 7, 0, 0, 0, 0, 3, 1],
           [0, 0, 3, 0, 1, 0, 0, 8, 0],
           [9, 0, 0, 8, 6, 3, 0, 0, 5],
           [0, 5, 0, 0, 9, 0, 6, 0, 0],
           [1, 3, 0, 0, 0, 0, 2, 5, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 4],
           [0, 0, 5, 2, 8, 6, 3, 0, 0],]
    ans = sudoku_sovler(arr)
    print(ans)
