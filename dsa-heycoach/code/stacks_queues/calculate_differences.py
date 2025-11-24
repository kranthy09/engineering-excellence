"""
Given an integer array arr of length n, for each element
in the array, find the nearest smaller element on both
the left and right sides. If a nearest smaller element
does not exist on either side, consider it as 0.
The task is to determine the maximum absolute difference
between the nearest smaller elements on the left and right
for every element in the array.
"""


class CalculateMaxDifference:

    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        for each element in the array, iterate over the
        array to find the next first smaller element and store
        in a right array in the index of the element.
        same for the previous first smaller element, store in left array.
        """
        n = len(self.arr)
        left = [0] * n
        right = [0] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if self.arr[i] > self.arr[j]:
                    right[i] = self.arr[j]
                    break
        for i in range(n-1, 0, -1):
            for j in range(i-1, -1, -1):
                if self.arr[i] > self.arr[j]:
                    left[i] = self.arr[j]
                    break
        max_diff = float("-inf")
        for i in range(n):
            max_diff = max(max_diff, abs(right[i] - left[i]))
        return max_diff

    def expected_approach(self):
        """
        For each element in the array, find the nse and pse
        consider monotinically increasing stack, such that at a
        particular point the incoming element is less than the
        top element of the stack then element can be nse to the
        elements present in the stack.
        """
        n = len(self.arr)
        stack = []
        right = [0] * n
        left = [0] * n
        for i in range(n):
            while stack and self.arr[stack[-1]] > self.arr[i]:
                inx = stack.pop()
                right[inx] = self.arr[i]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and self.arr[stack[-1]] > self.arr[i]:
                inx = stack.pop()
                left[inx] = self.arr[i]
            stack.append(i)
        max_diff = float("-inf")
        for i in range(n):
            max_diff = max(max_diff, abs(right[i] - left[i]))
        return max_diff


if __name__ == "__main__":
    chars = [2, 4, 8, 7, 7, 9, 3]
    res = CalculateMaxDifference(chars)
    print(res.brute_force())
    print(res.expected_approach())
