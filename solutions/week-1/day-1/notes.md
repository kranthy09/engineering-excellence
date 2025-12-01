# Week 1 - Day 1

Date: December 01, 2025
Days since start: 8

## Problem

1. 4Sum (Medium), Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

## Pattern:

two pointers pattern

## Notes:

Brute force approach can be of four for loops checking all quadruple that sum up to target.
Time complexity with be TC: O(n^4)

Expected approach:
Sort the array can provide an approach that can be solved using two pointer technique.
convert this approach into two sum problem with the help of freezing the two numbers. so that the required sum will be checked across two elements in the other elements of array. We can freeze two elements with two for loops and send the required sum in to the remaining sorted array to find the other two elements in O(n). Total time complexity with O(n^3).

The main problem exists to avoid the duplicates, so before sending the element in to checking the target sum process, we check each element(i) with its prevoius element(i-1) with necessary index conditions to avoid index errors. if they are equal we can avoid that as duplicate which is already included in previous loop iteration so skip it and move forward, this way each iteration can achieve unique quadruples, that sum up to target.

## Key Learnings

From all possible pairs of 4 elements, optimization can only be done with sorting, the ability to conclude why we have to sort the array provides an extensive behaviour of solving problems.

## Time Spent

- Problem 1:
- Problem 2:
