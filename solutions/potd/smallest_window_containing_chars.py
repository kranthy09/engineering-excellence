"""
Smallest Window Containing Chars (Hard)
@topic: potd
@difficulty: hard
@tags: arrays, slidingwindow

Given two strings s and p. Find the smallest substring in s
consisting of all the characters (including duplicates) of the
string p. Return empty string in case no such substring is present.
If there are multiple such substring of the same length found,
return the one with the least starting index.


i/o: s = "timetopractice", p = "toc"
o/p: "toprac"


Approaches:
1. Expected: Create frequency maps for s and p, slide window.
"""


class Solution:
    def min_window(self, s, p):
        """
        iterate over each character in s, by taking in to window
        comparing with count of in p frequency array. if it can contribute to
        subtring, increment the count of the current window size.
        if the current window size equals to length of p string, then
        try to compress the window to get minimum length by moving
        starting index of the sliding window.
        extract the minimum length and keep track of start index so that
        minimum length subtring is added.

        TC: O(n + m), every character in s and p are visited atmost twice
        AS: O(1), even though we are creating frqeuncy array the auxiliary
        is constant because the arrays are of contant 256 size length
        containing all characters ascii values from 0 to 255.
        """

        ns = len(s)
        np = len(p)

        count_s = [0] * 256
        count_p = [0] * 256

        for ch in p:
            count_p[ord(ch)] += 1

        start = 0
        start_idx = -1
        min_len = float("inf")
        count = 0

        for j in range(ns):
            # expand window
            count_s[ord(s[j])] += 1

            # calculate window size by comparing its counts in
            # frequency map of p string.
            if count_p[ord(s[j])] != 0 and \
                    count_s[ord(s[j])] <= count_p[ord(s[j])]:
                count += 1

            # when the current subarray between start to j has
            # same length of p string
            if count == np:
                # try to minimize the window
                while count_s[ord(s[start])] > count_p[ord(s[start])] or \
                        count_p[ord(s[start])] == 0:

                    if count_s[ord(s[start])] > count_p[ord(s[start])]:
                        count_s[ord(s[start])] -= 1
                    start += 1
                # update window size
                length = j - start + 1
                if min_len > length:
                    min_len = length
                    start_idx = start

        if start_idx == -1:
            return ""

        return s[start_idx: start_idx + min_len]


if __name__ == "__main__":
    arrs = [
        ["timetopractice", "toc"],
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.min_window(arr[0], arr[1]))
        # toprac
