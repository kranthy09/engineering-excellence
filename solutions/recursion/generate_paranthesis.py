"""
Generate Paranthesis (Hard)
@topic: recursion
@difficulty: hard
@tags: recursion, backtracking

Given a number n, print all combinations of balanced parentheses of length n.


i/o: 4
o/p: [ "( ( ) )", "( )( )"]

Approaches:
1. Expected: Recursion.
"""


class Solution:
    def get_all_valid_paranthesis(self, n):
        """
        T(n) = 2*T(n-1) + c
        TC: n*2^n
        AS: O(n), recursive call stack
        """
        curr = []
        res = []
        self.get_all_valid_paranthesis_util(n, 0, res, curr)

        return res

    def get_all_valid_paranthesis_util(self, n, op, res, curr):
        """
        Recursively generate valid paranthesis of size n
        """
        # base case
        if len(curr) == n:
            res.append("".join(curr))
            return

        if op < n//2:
            curr.append("(")
            self.get_all_valid_paranthesis_util(n, op+1, res, curr)
            curr.pop()
        cl = len(curr) - op
        if cl < op:
            curr.append(")")
            self.get_all_valid_paranthesis_util(n, op, res, curr)
            curr.pop()


if __name__ == "__main__":
    nums = [
        2,  # ['()']
        3,  # []
        4,  # ['()']
    ]
    ans = Solution()
    for num in nums:
        print(ans.get_all_valid_paranthesis(num))
