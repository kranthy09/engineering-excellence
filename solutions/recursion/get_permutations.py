"""
Get Permutations (Easy)
@topic: recursion_2
@difficulty: easy
@tags: recursion, backtracking

Given an array of numbers, generate all
permutations

i/o: [1, 2, 3]
o/p:[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]


Approaches:
1. Expected: Recursion
"""


def get_permutations_from(arr):
    """
    Client for permutaions recursive utility
    """
    res = []
    get_permutations_util(0, arr, res)

    return res


def get_permutations_util(i, arr, res):
    """
    at an instant, permutations of i, is
    swap(i, i) -> keep the element at i, send remaining
    elements recursively to find out thier permutations

    Do the same step for n numbers in the array as it can swap from i to n

    TC:
    AS:
    """
    # base case
    if i == len(arr):
        res.append(arr[:])  # copy of arr
        return

    for j in range(i, len(arr)):
        # swap and send remaining numbers to compute permutations.
        arr[i], arr[j] = arr[j], arr[i]
        get_permutations_util(i+1, arr, res)

        # backtrack, clean up for next nodes
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr = [1, 2, 3]
    ans = get_permutations_from(arr)
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    print(ans)
