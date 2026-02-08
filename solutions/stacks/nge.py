"""
Next Greater Element (NGE):

Given an array of integers, find the next greater element
for each element in the array. The next greater element for
an element x is the first greater element on the right side
of x in the array. If there is no greater element for x,
then the next greater element is -1.

i/o: [4, 5, 2, 10]
o/p: [5, 10, 10, -1]

i/o: [3, 7, 1, 7, 8]
o/p: [7, 8, 7, 8, -1]

Approaches:
1. Brute Force:
2. Stack:

"""


class Solution:

    def next_greater_element_brute_force(self, arr):
        """
        For each element iterate over next elements to find the
        greater.

        TC:
        AS:
        """
        n = len(arr)
        nge = []
        for i in range(n):
            ele = arr[i]
            for j in range(i+1, n):
                if ele < arr[j]:
                    ele = arr[j]
                    break
            if ele != arr[i]:
                nge.append(ele)
            else:
                nge.append(-1)
        return nge

    def nge_stack(self, arr):
        """
        Store the next greater element in a stack.

        TC:
        AS:
        """
        n = len(arr)
        nge = []
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            if stack:
                nge.append(stack[-1])
            else:
                nge.append(-1)
            stack.append(arr[i])
        return nge[::-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ans = Solution()
    print(ans.next_greater_element_brute_force(arr))
    print(ans.next_greater_element_brute_force(
        [2, 3, 1, 2, 3, 5, 3, 2, 1, 1, 2, 4, 5, 3, 2, 1, 2]))
    print(ans.nge_stack(arr))
    print(ans.nge_stack([2, 3, 1, 2, 3, 5, 3, 2, 1, 1, 2, 4, 5, 3, 2, 1, 2]))
