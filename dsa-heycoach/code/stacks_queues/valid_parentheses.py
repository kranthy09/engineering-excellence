"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
"""


class ValidParentheses:

    def __init__(self, s):
        self.s = s

    def brute_force(self):
        """
        find the valid parentheses pattern in the string
        and replace the patter with empty string
        if by reaching last the original string becomes empty
        then it contains valid parentheses.
        TC: O(n^2)
        SC: O(n)
        """
        while True:
            new_s = []
            changed = False
            i = 0

            while i < len(self.s):
                if i + 1 < len(self.s):
                    pair = self.s[i] + self.s[i+1]
                    if pair == "()" or pair == "[]" or pair == "{}":
                        i += 2
                        changed = True
                        continue
                new_s.append(self.s[i])
                i += 1
            self.s = "".join(new_s)
            print(self.s)
            if not changed:
                break
        return len(self.s) == 0

    def expected_approach(self):
        """
        consider the stack, hmap(of closed parentheses as keys
        and open as values) and push the opening brackets to
        the stack and if the incoming parentheses is closed
        check with top element in the stack with hmap, if there
        is valid parentheses, pop from the stack.
        at the end stack should be empty if the string has
        valid parentheses.
        TC: O(n)
        SC: O(n)
        """
        stack = []
        hmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in range(len(self.s)):
            if self.s[i] == "(" or self.s[i] == "{" or self.s[i] == "[":
                stack.append(self.s[i])
            else:
                if stack and hmap[self.s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = "([{}])"
    res = ValidParentheses(s)
    print(res.brute_force())
    print(res.expected_approach())
