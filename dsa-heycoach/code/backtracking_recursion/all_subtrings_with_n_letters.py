"""
Generate All Strings with 'A' and 'B'
Same as above but with letters
Example: n=2 → ["AA", "AB", "BA", "BB"]

"""


def solve(n):
    arr = [chr(ele) for ele in range(ord("A"), ord("Z")+1)][:n]
    res = []
    path = []

    def backtrack(i):

        if len(path) == n:
            print(path)
            res.append(path.copy())
            return
        for j in range(n):
            path.append(arr[j])
            backtrack(i)
            path.pop()
    backtrack(0)
    return res


if __name__ == "__main__":
    n = 3
    res = solve(n)
    print(res)
