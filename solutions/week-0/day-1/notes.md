# Week 0 - Day 1 (Total: Day 1)

## Problems

1: Container With Most Water (Medium)
You're given an array height where height[i] represents the height of a vertical line at position i. Find two lines that together with the x-axis form a container that holds the most water.
Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 (height 8) and index 8 (height 7) form container with area = 7 \* (8-1) = 49
Constraints:

2 ≤ height.length ≤ 10^5
0 ≤ height[i] ≤ 10^4

## Pattern:

There are two lines which form containers, we have to find the pairs of
lines forming maximum water contain.
Two pointer Pattern

## Key Learnings

Thinking/Approach towards two pointers:

1. Why start at opposite sides?
   Maximum width guarenteed
   Covers all lines
   As you move inward, width decreases
   You need to compensate by finding taller lines.
2. Which pointer to move?
   we move the smaller line, since the height of container by both lines
   will be min of thier heights.
3. When to stop?
   if left is greater than right.

-

## Time Spent

- Problem 1: 1h 30m
- Problem 2:
