# Week 0 - Day 3

Date: November 27, 2025
Days since start: 3

## Problems

1.Remove Duplicates from Sorted Array II (Medium)

Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element
appears at most twice. The relative order should be kept the same.
Return k after placing the final result in the first k slots of nums.
Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements
of nums being 1, 1, 2, 2 and 3 respectively.
Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Constraints:

1 ≤ nums.length ≤ 3 × 10^4
-10^4 ≤ nums[i] ≤ 10^4
nums is sorted in non-decreasing order

Key Challenge: Modify in-place with O(1) space. 2.

## Pattern:

1.As there is order in data, it can be binary search or two points. 2. No element to find or search here it can be two pointers.

## Key Learnings

1. Pointers move according to a particular condition such that they transform the logic in to solution.
2. Two pointers, namely one is slow and other fast. slow pointer has its own condition to move but slowly, and fast pointer has its own condition to move but fastly

## Time Spent

- Problem 1: 2hrs
- Problem 2:
