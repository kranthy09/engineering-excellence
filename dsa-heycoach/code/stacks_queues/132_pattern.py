"""
Given an array of n integers nums, a 132 pattern is a
subsequence of three integers nums[i], nums[j], and
nums[k] such that (i < j < k) and (nums[i] < nums[k] < nums[j]).

Return true if there is a 132 pattern in nums, otherwise, return false.

Sample Input 1:
4
1 2 3 4

Sample Output 1:
false
"""


class Find132Pattern:

    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        list out the possible indexes that satisfy the condition
        TC: O(n)
        SC: O(n)
        """
        n = len(self.arr)
        for i in range(n-2):
            if arr[i] < arr[i+2] < arr[i+1]:
                return True
        return False

    def expected_approach(self):
        """
        Consider monotonically increasing stack. at a point of time
        if the incoming element is less than the top element of the stack
        pop the larger elements, if the count of poped elements is
        greater than or equal to 2, than there exists a 132 pattern
        TC: O(n)
        SC: O(n)
        """
        stack = []
        count = 0
        n = len(self.arr)
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
                count += 1
                if count >= 2:
                    return True
            stack.append(i)
            count = 0
        return False


if __name__ == "__main__":
    arr = [3, 1, 4, 2]
    res = Find132Pattern(arr)
    print(res.brute_force())
    print(res.expected_approach())
