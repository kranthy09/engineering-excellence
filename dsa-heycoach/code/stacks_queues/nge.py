"""
Given an array of integers, determine the next greater element (NGE),
for every element in the array maintaing the order of appearance

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and
 for 4, since it doesn't exist, it is -1.

Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there
is no larger elements hence it is -1, for 0 it is 1 ,
for 1 it is 3 and then for 3 there is no larger element on right and hence -1.
"""


class NextGreaterElement:
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        TC: O(n^2)
        SC: O(n)
        """
        n = len(arr)
        result = [-1] * n
        for i in range(len(self.arr)):
            for j in range(i+1, len(self.arr)):
                if self.arr[i] < self.arr[j]:
                    result[i] = self.arr[j]
                    break
        return result

    def expected_approach(self):
        """
        consider monotonically decreasing stack
        because at a point, the current element is smaller than top
        element, that cannot be a NGE, if the current element is greater the
        top that means, it can become NGE to all the elements that are smaller
        to the current element

        TC: O(n)
        SC: O(n)
        """
        res = [-1] * len(self.arr)
        stack = []
        for i in range(len(self.arr)):

            while stack and arr[stack[-1]] <= arr[i]:
                inx = stack.pop()
                res[inx] = arr[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    arr = [6, 8, 0, 1, 3]
    res = NextGreaterElement(arr)
    print(res.brute_force())
    print(res.expected_approach())
