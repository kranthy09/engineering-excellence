"""
Given an array arr[] of integers,
find the Next Smaller Element (NSE) for each element in the array.

Input: arr[] = [4, 8, 5, 2, 25]
Output: [2, 5, 2, -1, -1]
Explanation:
The first element smaller than 4 having index > 0 is 2.
The first element smaller than 8 having index > 1 is 5.
The first element smaller than 5 having index > 2 is 2.
There are no elements smaller than 2 having index > 3.
There are no elements smaller than 25 having index > 4.
"""


class NextSmallerElement:
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        TC: O(n^2)
        SC: O(n)
        """
        n = len(self.arr)
        res = [-1] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    res[i] = arr[j]
                    break
        return res

    def expected_approach(self):
        """
        consider monotonically increasing stack,
        at a point the current element is smaller than the top element
        of the stack, then the current element can be next smaller ele
        to the corresponding elements in the stack.
        TC:
        SC:
        """
        n = len(self.arr)
        res = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                inx = stack.pop()
                res[inx] = arr[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    arr = [13, 7, 6, 12]
    res = NextSmallerElement(arr)
    print(res.brute_force())
    print(res.expected_approach())
