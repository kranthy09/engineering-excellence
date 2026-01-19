"""
Minimum Window Subsequence (forward-backward traversal)

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


def solve(s: str, t: str) -> str:
    """
    Docstring for solve

    :param s: string
    :param t: string

    Time complexity:
    Space Complexity:
    """
    min_len = float("inf")
    min_start = 0
    s_idx = 0

    while s_idx < len(s):

        curr = s_idx
        t_idx = 0
        # Forward pass

        while t_idx < len(t) and curr < len(s):

            if s[curr] == t[t_idx]:
                t_idx += 1
            curr += 1

        # no sequence found
        if t_idx < len(t):
            break
        end = curr-1
        start = end
        t_idx = len(t)-1

        # Backward pass
        while t_idx >= 0:
            if s[start] == t[t_idx]:
                t_idx -= 1
            start -= 1
        start += 1
        window_len = end - start + 1
        if window_len < min_len:
            min_len = window_len
            min_start = start
        s_idx = start + 1
    return "" if min_len == float("inf") else s[min_start:min_start+min_len]


if __name__ == "__main__":
    s = "abcdebdde"
    t = "bde"
    s2 = "timetopractice"
    t2 = "toc"
    res1 = solve(s, t)
    res2 = solve(s2, t2)
    print(res1)
    print(res2)
