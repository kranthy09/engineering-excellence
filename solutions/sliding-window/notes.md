

## Problems

1. Substring with Concatenation of All Words

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

## Pattern:

Two pointer with sliding window and hashmap

## Key Learnings

From 0 to word_len, a substring can be formed from its successive paths such that they are formed with all words in words list. Key identification is to its enough to check with these starting values so that automatically all substrings are captured.

construct each word from left and right pointers, with help of moving them forward, on each word in words freq, add the word to current window, if the current window appears too many times, shirnk the window forward with left by removing it from current window freq and words used.

Words used is equal to word_len then substring is valid, append the left pointer to result, move the window to next word. Here the window shouldn't completely reset to start, just eliminate the left word, move left pointer forward, so it can maintain the strings that again we have to calculate.

If there is no constructed word present in the words freq, now reset to defaults to process for next.

resetting is different from move left word of word_len, in the second case we already have got the answer just want to check whether next word can form valid substring, in first the word entirely not present in words freq so we skip it and reset as fresh.
