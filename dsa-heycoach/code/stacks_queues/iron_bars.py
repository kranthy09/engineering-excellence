"""
You are a blacksmith at Iron&Steel Sons. You are presented
with a large piece of iron sheet by a client who says it's
waste material from the construction of his house.
The sheet is in a weird shape because it has been created
by welding together a number of rectangular iron sheets side
by side of width 1cm but of variable height.
The client wants you to cut out the greatest rectangle-shaped
iron sheet from the given shape.

You are given an array representing the height of each
 iron sheet which was welded into the larger iron sheet.
   Remember each of these sheets had a width of 1cm.
   Your task is to return the area of the largest rectangular
   iron sheet that can be cut out from this.
"""


class MaxAreaIronBars:
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        find all the possible iron bars, that will make up to the
        area with the minimum height of the bar and width its spans.

        TC: O(n^3)
        SC: O(n)
        """
        n = len(self.arr)
        max_area = float("-inf")
        for i in range(n-1):
            for j in range(i+1, n):
                min_height = min(arr[i:j+1])
                area = min_height * (j - i + 1)
                max_area = max(area, max_area)
        return max_area

    def expected_approach(self):
        """
        for each iron bar, it can span till the height of bar that is
        less than current height of current iron bar from left and right.
        for every element in the arr find the next smaller element(height)
        and previous smaller element(height), the width it spans will become
        the maximum area.
        So consider monotonically increasing stack and for each iron bar,
        find the left index for smaller element and right index
        for smaller element.
        """
        n = len(self.arr)
        stack = []
        left = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        right = [n] * n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        max_area = float("-inf")
        for i in range(n):
            width = right[i] - left[i] - 1
            area = width * arr[i]
            max_area = max(area, max_area)
        return max_area


if __name__ == "__main__":
    arr = [2, 1, 5, 6, 2, 3]
    res = MaxAreaIronBars(arr)
    print(res.brute_force())
    print(res.expected_approach())
