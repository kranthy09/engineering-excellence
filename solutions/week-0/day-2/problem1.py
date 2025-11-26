"""
Problem 2: Trapping Rain Water (Hard)
Given an elevation map array where the width of each bar is 1,
compute how much water can be trapped after raining.
Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Visual representation:
       █
   █   ██ █
 █ ██ ███████
 [0,1,0,2,1,0,1,3,2,1,2,1]
Water fills the valleys between peaks.
Constraints:

n == height.length
1 ≤ n ≤ 2 * 10^4
0 ≤ height[i] ≤ 10^5
"""


def solve(height):
    n = len(height)
    amount = 0
    print("i | h[i] | il | ir | amount")
    for i in range(n):
        il = nge_left(i, height)
        ir = nge_right(i, height)
        if il > -1 and ir < n:
            amount += (min(height[il], height[ir]) - height[i])
        print(i, height[i], il, ir, amount, sep=" |   ")
    return amount


def nge_left(k, height):

    temp = height[k]
    flag = False
    for i in range(k, -1, -1):
        if height[temp] < height[i]:
            temp = i
            flag = True
    if flag:
        return temp
    else:
        return -1


def nge_right(k, height):
    temp = height[k]
    flag = False
    for i in range(k, len(height)):
        if height[temp] < height[i]:
            temp = i
            flag = True
    if flag:
        return temp
    else:
        return len(height)


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = solve(height)
    print(res)
