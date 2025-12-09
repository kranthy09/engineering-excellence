"""
You are given a string s and an array of strings words. All strings in words
are of the same length.Return the starting indices of all substrings in s that
are a concatenation of each word in words exactly once, in any order, and
without any intervening characters.

Example 1:
s = "barfoothefoobarman"
words = ["foo", "bar"]
Output: [0, 9]

Explanation:
# Index 0: "barfoo" = "bar" + "foo" ✓
# Index 9: "foobar" = "foo" + "bar" ✓

Example 2:
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
Output: []

Explanation:
# No valid concatenation exists
# We need: "word" twice, "good" once, "best" once
# But s doesn't contain this exact combination

Example 3:
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
Output: [6, 9, 12]

Explanation:
# Index 6: "foobarthe" = "foo" + "bar" + "the" ✓
# Index 9: "barthefoo" = "bar" + "the" + "foo" ✓
# Index 12: "thefoobar" = "the" + "foo" + "bar" ✓

Constraints

1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters
All strings in words are the same length
"""


def solve(s, words):
    """
    Docstring for solve

    :param s: Description
    :param words: Description

    TC: O(m*n)
    SC: O(n)
    """
    fmap = {}
    for word in words:
        if fmap.get(word) is None:
            fmap[word] = 0
        fmap[word] += 1
    lenw = len(words) * len(words[0])
    lens = len(s)
    span = len(words[0])
    s_idx = 0
    res = []
    ans = []
    while s_idx < lens - lenw + 1:
        subs = []
        fmapcp = fmap.copy()
        for i in range(len(words)):
            subs.append(s[s_idx+i*span:s_idx+(i+1)*span])
        for sub in subs:
            if fmapcp.get(sub) is None:
                break
            else:
                fmapcp[sub] -= 1
                if fmapcp[sub] == 0:
                    del fmapcp[sub]
        if not fmapcp:
            ans.append(s_idx)
            res.append(subs)

        s_idx += 1
    return ans


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["bar", "foo"]
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    res1 = solve(s, words)
    res2 = solve(s2, words2)
    res3 = solve(s3, words3)
    print(res1)
    print(res2)
    print(res3)
