"""
Substring with Concatenation of All Words

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

from collections import Counter


def solve(s, words):
    """
    TC: O(m*n)
    SC: O(n)
    """
    word_len = len(words[0])
    words_count = len(words)
    words_freq = Counter(words)
    res = []
    for offset in range(word_len):
        left = offset
        curr_freq = Counter()
        words_used = 0
        for right in range(offset, len(s) - word_len + 1, word_len):
            # construct the word
            word = s[right: right+word_len]
            # add word to current window
            if word in words_freq:  # O(1)
                curr_freq[word] += 1
                words_used += 1
                while curr_freq[word] > words_freq[word]:
                    left_word = s[left:left+word_len]
                    curr_freq[left_word] -= 1
                    words_used -= 1
                    left += word_len
                if words_count == words_used:
                    res.append(left)
                    # silde window by one word
                    left_word = s[left:left+word_len]
                    left += word_len
                    curr_freq[word] -= 1
                    words_used -= 1
            else:
                # restore window
                curr_freq.clear()
                words_used = 0
                left = right + word_len
        return res


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["bar", "foo"]
    res = solve(s, words)
    print(res)
