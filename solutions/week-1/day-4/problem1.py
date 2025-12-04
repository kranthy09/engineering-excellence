"""
Two Pointers (forward-backward traversal)

Given strings s and t, find the minimum window in s which contains all
characters of t in the same order (subsequence, not substring).
Return the minimum window. If no such window exists, return "".

Example
s = "abcdebdde"
t = "bde"

Output: "bcde"
# Explanation:
# "bcde" is the shortest window containing 'b', 'd', 'e' in order
# Other valid windows: "bdde", "abcdebdde"
"""


def solve(s, t):

    min_len = float("inf")
    min_seq = ""
    i = 0
    while i < len(s):

        j = 0
        curr = i
        while curr < len(s) and j < len(t):
            if s[curr] == t[j]:
                j += 1
            curr += 1
        if j == len(t):
            end = curr-1
            start = end
            j = len(t)-1
            while j >= 0:
                if s[start] == t[j]:
                    j -= 1
                start -= 1
            start += 1
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_seq = s[start:end+1]
            i = start + 1
        else:
            break
    return min_seq


if __name__ == "__main__":
    s = "abcdebdde"
    t = "bde"
    s2 = "timetopractice"
    t2 = "toc"
    res1 = solve(s, t)
    res2 = solve(s2, t2)
    print(res1)
    print(res2)
