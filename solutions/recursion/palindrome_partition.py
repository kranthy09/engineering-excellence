"""
Palindrome Partition (Hard)
@topic: recursion
@difficulty: hard
@tags: recursion, backtracking

Given a string s, find all possible ways to partition
it such that every substring in the partition is a palindrome.


i/o: "geeks"
o/p: [[g, e, e, k, s], [g, ee, k, s]]


Approaches:
1. Expected: Recursion + bactracking
"""


class Solution:

    def palindrome_partition(self, s):
        """
        At an instant a substring is palindrome, add curr substring to
        result and open a gate next to it, send remaining substring to
        recursion for finding out other palindrome partitions.

        TC: O(n*2^n), checking palindrome and each palindrome, has two branches
        AS: O(n), recursive call stack.
        """
        curr = []
        res = []
        self.palindrome_partition_util(0, s, curr, res)

        return res

    def palindrome_partition_util(self, i, s, curr, res):
        """
        Util for paritioning string, such that all substrings
        are palindrome.
        """
        # base case
        if i == len(s):
            res.append(",".join(curr))
            return

        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                curr.append(s[i:j+1])
                self.palindrome_partition_util(j+1, s, curr, res)
                curr.pop()

    def is_palindrome(self, string, i, j):
        """
        Returns True for palindrome string.
        """
        while (i < j):
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    strings = [
        "abcba", "geeks"
    ]
    ans = Solution()
    for s in strings:
        print(ans.palindrome_partition(s))
