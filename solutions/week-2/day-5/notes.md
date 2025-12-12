# Week 2 - Day 5

Date: December 12, 2025
Days since start: 19

## Problems

1. 3Sum Closest

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

### Ask Questions:

1. Are the intergers should be contigous?

- No, the three integers can be any.

2. What do you mean by closed to target?

- There can be nC3 of 3 integers be formed from the list in that abs(target - 3sum) should be minimum

### Visualization:

Lets try the brute force method for it, we have to find all 3 integers groups and find the min abs(target-3sum)
so here if we observe, for i=0 to n-1, for j=0 to n-1, for k=0 to n-1, finding sum of two pointers can be sufficient so that in third iteration we can change to target - nums[k] and change it becomes to sum.

So if we can sort the array, we can skip integers that cannot contribute to min difference to target - 3sum.

## Pattern:

### sorting + two pointers(converge)

So, construct current sum from the three integers at i = 0 to n-3, l = i+1 and r=n-1
then find the distance between the target, current sum and closest sum , target and update with next values if lesser absolute difference found than abs(closest sum-target)
ie., we are trying to find the closest sum, which is nearer to target.
Now, to move pointers, if curr_sum is greater than target, move larger integer pointer inward to adjust the curr_sum and move smaller integer pointer forward to adjust smaller curr sum to target.

## Key Learnings

- Ability to understand the closest distance in terms of abosulte difference and when comparing the values we have to include the all the 3 integers to condition with target for moving which pointer.

## Time Spent

- Problem 1: 1h 30min
