"""
Given a 2D grid of characters and a word,
determine if the word exists in the grid.

You may move:

up, down, left, right

A cell cannot be reused in the same word.

Return True if the word can be formed, else False.

board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

word = "ABCCED"
"""


def solve(arr, word):
    path = []
    moved = [[0]*len(arr[0])]*len(arr)

    def backtrack(i, j, k):
        if k == len(word):
            print(path)
            if word == "".join(path):
                return word
        print(path)
        print(i, j, k)
        if j+1 <= len(arr[0]) and j-1 >= -1 and \
                i+1 <= len(arr) and i-1 >= -1:
            print("go right")
            path.append(arr[i][j])
            moved[i][j] = 1
            backtrack(i, j+1, k+1)  # go right
            path.pop()
            moved[i][j] = 0
            k -= 1

            print("go down")
            path.append(arr[i][j])
            moved[i][j] = 1
            backtrack(i+1, j, k+1)  # go down
            path.pop()
            moved[i][j] = 0
            k -= 1

            print("go left")
            path.append(arr[i][j])
            moved[i][j] = 1
            backtrack(i, j-1, k+1)  # go left
            path.pop()
            moved[i][j] = 0
            k -= 1

            print("go up")
            path.append(arr[i][j])
            moved[i][j] = 1
            backtrack(i-1, j, k+1)  # go up
            path.pop()
            moved[i][j] = 0
            k -= 1

    res = backtrack(0, 0, 0)
    if not res:
        return False
    return res


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    word = "ABCCED"
    ans = solve(board, word)
    print(ans)
