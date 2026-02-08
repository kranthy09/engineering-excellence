"""
Check paranthesis in correct order.


i/o: "(){}[]"
o/p: True

i/o: "([)]"
o/p: False

Approaches:
1. Brute Force:
"""


class Solution:

    def is_match(self, op, cl):

        return op == "(" and cl == ")" or \
            op == "[" and cl == "]" or \
            op == "{" and cl == "}"

    def check_paranthesis_(self, string):
        """
        Checks the string contains have equal closing
        and opening paranthesis.

        TC:
        AS:
        """
        n = len(string)
        stack = []
        for i in range(n):
            if string[i] in "({[":
                stack.append(string[i])
            else:
                if (len(stack) == 0) or \
                        not self.is_match(stack[-1], string[i]):
                    return False
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    arrs = [
        "(){}[]",
        "([)]",
        "({[]})",
    ]
    ans = Solution()

    for arr in arrs:
        print(ans.check_paranthesis_(arr))
