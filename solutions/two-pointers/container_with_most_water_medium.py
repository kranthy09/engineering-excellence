"""
Problem 1: Container With Most Water (Medium)
You're given an array height where height[i] represents the height of a
vertical line at position i. Find two lines that together with the
x-axis form a container that holds the most water.
Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 (height 8) and index 8 (height 7)
form container with area = 7 * (8-1) = 49
Constraints:

2 ≤ height.length ≤ 10^5
0 ≤ height[i] ≤ 10^4
"""


def solve(height):
    left = 0
    right = len(height)-1
    area = float("-inf")
    while left < right:
        print(left, right)
        area = max(area, min(height[left], height[right])*(right-left))
        print(area)
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
    return area


if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = solve(heights)
    print(res)
