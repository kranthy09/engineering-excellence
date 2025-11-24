"""
Given a string S consisting of only opening and closing curly brackets
 '{' and '}', find out the minimum number of operations required
 to convert the string into a balanced expression.

A single operation means changing '{' to '}' or vice-versa.

Return the minimum number of reversals required to balance the
bracket sequence. If balancing is not possible, return -1.
"""


class CountOperations:
    def __init__(self, arr):
        self.arr = list(arr)

    def brute_force(self):
        """
        Find the all possible positions of the arr and flip them
        such that it becomes balanced expression.
        consider all subsets positions of arr and flip them, and check
        whether the arr is balanced.

        TC: O(N^2)
        SC: O(N)
        """
        n = len(self.arr)
        min_val = []

        if n % 2 == 1:
            return -1
        if self.is_balanced(self.arr):
            return 0
        for i in range(1, 2 ** n):
            temps = self.arr.copy()
            ops = 0
            for j in range(n):
                if i & (1 << j):
                    temps[j] = "}" if temps[j] == "{" else "{"
                    ops += 1
            if self.is_balanced(temps):
                min_val.append(ops)
        return min(min_val)

    def expected_approach(self):
        """
        consider the stack, if there an opening push into stack
        and if the next coming element is closing bracket pop the
        the opening bracket so that balanced pattern is removed.
        at last the stack contains the unbalanced brackets, now
        find the operations required for making the string balanced
        with remaining unbalanced bracket.

        TC: O(N)
        SC: O(N)
        """
        n = len(self.arr)
        stack = []
        for i in range(n):
            if self.arr[i] == "{":
                stack.append(self.arr[i])
            else:
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(self.arr[i])
        unmatched = len(stack)
        opening = 0
        closing = 0
        for i in range(unmatched):
            if stack[i] == "{":
                opening += 1
            else:
                closing += 1
        return (opening + 1)//2 + (closing + 1)//2

    def is_balanced(self, temps):
        count = 0
        for i in range(len(temps)):
            if temps[i] == "{":
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0


if __name__ == "__main__":
    chars = "}{{}}{{{"
    res = CountOperations(chars)
    print(res.brute_force())
    print(res.expected_approach())
