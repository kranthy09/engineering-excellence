"""
Trapping Rain Water (Hard)
@topic: potd
@difficulty: hard
@tags: arrays, stack, nextgreaterelement

Given an array arr[] with non-negative integers representing
the height of blocks. If the width of each block is 1, compute
how much water can be trapped between the blocks during the rainy season.

i/o: [3, 0, 1, 0, 4, 0 2]
o/p: 10


Approaches:
1. Expected: compute next greater poles to calculate trapped water. O(n)
"""


class Solution:

    def max_water(self, arr):
        """
        Precompute next greater elements in an array and find out
        each pole can store water on top of it by knowing its water level
        from next greater poles from left and right indexes.

        TC: O(n)
        AS: O(n), for maintaing nge indexes
        """
        n = len(arr)

        water = 0
        # compute next greater element left of element
        nge_l = self.nge_left(arr)

        # compute next greater element right of element
        nge_r = self.nge_right(arr)
        for i in range(n):
            il = nge_l[i]
            ir = nge_r[i]
            if il != -1 and ir != n:
                water += (min(arr[il], arr[ir]) - arr[i])
        return water

    def nge_left(self, arr):

        n = len(arr)
        nge_l = [-1] * n

        # stack data structure, maintains greater element at the top.
        s = []
        for i in range(n):

            # compare the next coming element to the current greater element at
            # the top of stack
            while s and arr[s[-1]] < arr[i]:
                # if there are lesser elements coming from left
                # remove from the stack.
                s.pop()
            # current top will be nge
            if s:
                nge_l[i] = s[-1]
            else:
                # if there are no elements in stack,
                # current element arr[i] is greater than previous elements
                nge_l[i] = -1
            # push only greater elements than at top in the stack,
            # so that greater elements overall till index i is maintained.
            if s:
                if arr[s[-1]] < arr[i]:
                    s.append(i)
            else:
                s.append(i)
        return nge_l

    def nge_right(self, arr):

        n = len(arr)

        nge_r = [n]*n
        s = []

        # as we need next greater to the right, we must come from end.
        for i in range(n-1, -1, -1):

            # compare the next coming element to the current greater element at
            # the top of stack
            while s and arr[s[-1]] < arr[i]:
                # if lesser elements are present in the stack remove them
                # to maintain greater elements at top of stack.
                s.pop()
            # stack is not empty, there is greater element to the right
            # capture its index.
            if s:
                nge_r[i] = s[-1]
            else:
                # stack is empty, current element is greater then
                # all elements to its right
                nge_r[i] = n
            # push elements that are greater than the top element of stack,
            # so that greater elements are considered as greater in all
            # elements in right side if the element.
            if s:
                if arr[s[-1]] < arr[i]:
                    s.append(i)
            else:
                s.append(i)

        return nge_r


if __name__ == "__main__":
    arrs = [
        [3, 0, 1, 0, 4, 0, 2],  # 10
        [3, 0, 2, 0, 4],  # 7
        [1, 2, 3, 4]  # 0
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.max_water(arr))
