"""
Unique subsets

Given an array of duplicate elements, find the
unqiue subsets.

i/o:[1, 2, 2]
o/p: [{}, {1}, {2}, {1, 2}, {1, 2, 2}]

Approaches:
1. Brute Force
2. Recursion + backtracking
"""


def get_unique_subsets(arr):
    """

    """
    curr = []
    res = []
    arr.sort()
    print(arr)
    get_unique_subsets_util(0, arr, curr, res)
    return res


def get_unique_subsets_util(i, arr, curr, res):
    """
    take an element and find the subsets,
    skip an element and find the subsets.

    TC: O(2^n)
    AS: O(n)
    """
    # print(curr, i)
    # base case
    if i == len(arr):
        import copy
        curr2 = copy.deepcopy(curr)
        res.append(curr2)
        return

    j = i + 1
    # find repeated elements window length
    while j < len(arr) and arr[i] == arr[j]:
        j += 1
    freq = j - i
    for count in range(freq+1):
        # take repeated elements one at a time
        for k in range(count):
            curr.append(arr[i])
        # send them to recursion, with other elements
        get_unique_subsets_util(j, arr, curr, res)
        # backtrack, cleanup the elements.
        for k in range(count):
            curr.pop()


if __name__ == "__main__":
    arr = [1, 2, 2]
    ans = get_unique_subsets(arr)
    print(ans)
