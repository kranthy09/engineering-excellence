"""
Given an array, generate all k length combinations
"""


def solve(arr, k):
    res = []
    path = []

    def backtrack(i):
        if len(path) == k:
            res.append(path.copy())
            return
        if len(path) + len(arr) - i < k:
            return
        for j in range(i, len(arr)):
            path.append(arr[j])
            backtrack(j+1)
            path.pop()
    backtrack(0)
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 3
    print(solve(arr, k))
