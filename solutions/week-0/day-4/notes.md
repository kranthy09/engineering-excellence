# Week 0 - Day 4

Date: November 28, 2025
Days since start: 4

## Problems

1.Sort Colors (Medium)

Given an array nums with n objects colored red,
white, or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white, and blue.We will use
the integers 0, 1, and 2 to represent red, white, and blue, respectively.
You must solve this without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 ≤ n ≤ 300
nums[i] is either 0, 1, or 2
Follow-up: Can you solve it in one pass with O(1) space?

2.

## Pattern:

We need to sort the given array, so there should be pointers involved to sort
and the solution should be in in-place, so we have to consider pointers to make
in-place possible

## Key Learnings

Making a partition that helps to divide the elements to the boundaries of the partition,
as there are three kinds of colors or numbers (0, 1, 2) we can make two pointers in the index
such that the boundary elements can be swapped with current incoming element.

so we have to consider three pointer one for low, one for high, one for current incoming element.
if the curr element is 0,
where should 0 belongs in place of low, so swap with low and move low, current forward.
if the curr element is 1,
where should 1 belongs in place of current only, move curr forward.
if the curr element is 2,
where should 2 belongs in place of hight, swap with high and move high inward.
here we donot move current forward, as we have to examine the swapped element, it can be 0, or 1

Time Complexity: O(n)
Space complexity: O(1)

## Time Spent

- Problem 1: 1hr 30mins
- Problem 2:
