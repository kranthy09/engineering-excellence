"""
Given an array of integers, determine the previous greater element (PGE),
for every element in the array maintaing the order of appearance

Input: arr[] = [1, 3, 2, 4]
Output: [-1, -1, 3, -1]
Explanation: The previous larger element to 1 is -1 since it doesn't exist,
3 is -1, 2 is 3 and for 4 it is -1.
"""


class PreviousGreaterElement:
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        TC: O(n^2)
        SC: O(n)
        """
        res = [-1] * len(self.arr)
        for i in range(len(self.arr)):
            for j in range(i-1, -1, -1):
                if self.arr[i] < self.arr[j]:
                    res[i] = self.arr[j]
                    break
        return res

    def expected_approach(self):
        """
        Take monotonically decreasing stack, because at a point the
        current incoming number is smaller than the stack, every element
        in the stack is smaller, no greater element can be emitted. If the
        the current number is greater, then it can be pge to the smaller
        elements

        TC: O(n)
        SC: O(n)
        """
        n = len(self.arr)
        res = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                inx = stack.pop()
                res[inx] = arr[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    arr = [6, 8, 0, 1, 3]
    res = PreviousGreaterElement(arr)
    print(res.brute_force())
    print(res.expected_approach())
