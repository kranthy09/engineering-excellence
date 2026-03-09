"""
Largest Number In One Swap (Easy)
@topic: potd
@difficulty: easy
@tags: strings, greedy

Given a string s, return the lexicographically
largest string that can be obtained by swapping
at most one pair of characters in s.


i/o: s = "768"
o/p: "867"


Approaches:
1. Expected: swap left most smallest, with right most largest
"""


class Solution:
    def largest_swap(self, s):
        """
        TC: O(n)
        AS:O(1)
        """
        arr = list(s)

        n = len(s)

        maxx = '0'
        left = -1
        right = -1
        maxx_i = -1

        for i in range(n-1, -1, -1):

            if arr[i] > maxx:
                maxx = arr[i]
                maxx_i = i
            elif arr[i] < maxx:
                left = i
                right = maxx_i
        if left == -1:
            return s

        arr[left], arr[right] = arr[right], arr[left]

        return "".join(arr)


if __name__ == "__main__":
    arrs = [
        "768",  # 867
    ]
    ans = Solution()
    for s in arrs:
        print(ans.largest_swap(s))
