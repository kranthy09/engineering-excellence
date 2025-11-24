"""
Given an array arr[],
find the Previous Smaller Element (PSE) for every element in the array.

Input: arr[] = [1, 6, 2]
Output: [-1, 1, 1]
Explanation: For the first element 1,
there is no element to its left, so the result is -1.
For 6, the previous smaller element is 1.
For 2, the previous smaller element is also 1,
since it is the closest smaller number when looking left.
"""


class PreviousSmallerElement:
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        TC: O(n^2)
        SC: O(n)
        """
        n = len(self.arr)
        res = [-1] * n
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if arr[i] > arr[j]:
                    res[i] = arr[j]
                    break
        return res

    def expected_approach(self):
        """
        consider monotonically increasing stack,
        at a point of time the current element is smaller than the
        top element in stack, then all the elements that are greater
        in stack will have smaller number as current element
        TC: O(n)
        SC: O(n)
        """
        n = len(self.arr)
        stack = []
        res = [-1] * n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                inx = stack.pop()
                res[inx] = arr[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    arr = [1, 13, 7, 6, 12]
    res = PreviousSmallerElement(arr)
    print(res.brute_force())
    print(res.expected_approach())
