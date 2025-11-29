"""
Problem 1: Longest Substring Without Repeating Characters (Medium)
Given a string s, find the length of the longest substring
without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
Constraints:

0 ≤ s.length ≤ 5 × 10^4
s consists of English letters, digits, symbols and spaces

"""


# def solve(s):
#     i = 0
#     j = 0
#     substring = ""
#     hash = {}
#     res = [""]
#     while i < len(s) and j < len(s):
#         print("s: i, j", i, j)
#         if hash.get(s[j]) is None:
#             hash[s[j]] = 1
#             substring += s[j]
#             j += 1
#             print(substring)
#             print()
#         else:
#             if len(res[-1]) < len(substring):
#                 res.append(substring)
#             i = j
#             print("i,j", i, j)
#             substring = ""
#             hash = {}

#     return len(res[-1])


def solve(s):
    left = 0
    char_set = set()
    max_length = float("-inf")
    for right in range(len(s)):

        # remove char util left pointer excludes the duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # append each char
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    s = "pwwkew"
    res = solve(s)
    print(res)
