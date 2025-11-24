"""
Given a string s, return all possible strings,
formed by toggling the case of each alphabetical character.

Digits remain fixed.
"""


def solve(s):
    res = []
    path = []

    def backtrack(i):
        if i == len(s):
            print(res)
            res.append(path)
            return
        for j in range(len(s)):
            alphabet = s[j]
            if s[j] in range(ord('A'), ord('Z')):
                alphabet = s[j].lower()
            else:
                alphabet = s[j].upper()

            path.append(alphabet)
            backtrack(j+1)
            path.pop()
    backtrack(0)
    return res


if __name__ == "__main__":
    s = "a1zb"
    res = solve(s)
    print(res)
