# Week 0 - Day 2 (Total: Day 2)

## Problems

1.: Trapping Rain Water (Hard)
Given an elevation map array where the width of each bar is 1,
compute how much water can be trapped after raining.
Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Visual representation:
█
█ ██ █
█ ██ ███████
[0,1,0,2,1,0,1,3,2,1,2,1]
Water fills the valleys between peaks.
Constraints:

n == height.length
1 ≤ n ≤ 2 \* 10^4
0 ≤ height[i] ≤ 10^5 2.

## Pattern:

1. TWo pointers

## Key Learnings

1. Here for each element the pointers moving apart/outward by increasing the width
2. So there can be two pointers solve by moving inward or outward.
3. Visualizing this helps to identify the pattern to find the solution in inward pointers moving
   or outwards pointer moving.

-

## Time Spent

- Problem 1: 2 hrs
- Problem 2:
