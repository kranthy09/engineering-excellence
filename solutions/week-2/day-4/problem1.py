"""
Longest Duplicate Substring

Given a string s, consider all duplicated substrings: contiguous
substrings of s that occur 2 or more times. The occurrences may overlap.
Return any duplicated substring that has the longest possible length.
If s does not have a duplicated substring, return "".

Example 1:
pythons = "banana"
Output: "ana"
Explanation:
"ana" appears twice: "b[ana]na" and "ban[ana]"

Example 2:
pythons = "abcd"
Output: ""
Explanation:
No substring appears more than once

Example 3:
pythons = "aaaaa"
Output: "aaaa"
Explanation:
"aaaa" appears twice: "[aaaa]a" and "a[aaaa]"
(Note: "aaaaa" appears only once, so it's not the answer)

Example 4:
pythons = "aabcaabc"
Output: "aabc"
Explanation:
"aabc" appears twice: "[aabc]aabc" and "aabc[aabc]"

Constraints:
2 <= s.length <= 3 * 10^4
s consists of lowercase English letters
Return any valid answer (if multiple exist)
"""
