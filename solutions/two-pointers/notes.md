<!-- Source: week-0-[Self-Pratice]/day-1-two-pointers -->

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


---

<!-- Source: week-0-[Self-Pratice]/day-2-two-pointers -->

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
2. So there can be two pointers, solve by moving inward or outward.
3. Visualizing this helps to identify the pattern to find the solution in inward pointers moving
   or outwards pointer moving.

-

## Time Spent

- Problem 1: 2 hrs
- Problem 2:


---

<!-- Source: week-0-[Self-Pratice]/day-3-two-pointers -->

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


---

<!-- Source: week-0-[Self-Pratice]/day-4-two-pointers -->

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


---

<!-- Source: week-0-[Self-Pratice]/day-5-two-pointers -->

# Week 0 - Day 5

Date: November 29, 2025
Days since start: 5

## Problems

1.Longest Substring Without Repeating Characters (Medium)

2.

## Pattern:

Substring should be tracked with left and right (two pointers)
the right pointer waits for left to remove characters that doesnot
meet unique condition.

-> take the right pointer char
-> append the char
-> if the char is already in hashset, move left until it exludes char in hashset

## Key Learnings

The ability to give a pointer to stop for removing duplicates
that points to left which is the start of the next substring

## Time Spent

- Problem 1: 1h 30m
- Problem 2:


---

<!-- Source: week-1-[Self-Pratice]/day-1-two-pointers -->

# Week 1 - Day 1

Date: December 01, 2025
Days since start: 8

## Problem

1. 4Sum (Medium), Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: they sum up to given target.

## Pattern:

two pointers pattern

## Notes:

Brute force approach can be of four for loops checking all quadruple that sum up to target.
Time complexity with be TC: O(n^4)

Expected approach:
Sort the array, it can provide an approach that can be solved using two pointer technique.
convert this approach into two sum problem with the help of freezing the two numbers. so that the required sum will be checked across two elements in the other elements of array. We can freeze two elements with two for loops and send the required sum in to the remaining sorted array to find the other two elements in O(n). Total time complexity with O(n^3).

The main problem exists to avoid the duplicates, so before sending the element in to checking the target sum process, we check each element(i) with its prevoius element(i-1) with necessary index conditions to avoid index errors. if they are equal we can avoid that as duplicate which is already included in previous loop iteration so skip it and move forward, this way each iteration can achieve unique quadruples, that sum up to target.

## Key Learnings

From all possible pairs of 4 elements, optimization can only be done with sorting, the ability to conclude why we have to sort the array provides an extensive behaviour of solving problems.

## Problem

1. kSum Given an array nums of n integers, return an array of all the unique k-elements of groups [nums[a], nums[b], nums[c], nums[d]...., nums[k]] such that: they sum up to given target.

## Pattern:

two pointers pattern, so we solve the problem with help of recursion so that each k-sum can be deduced to two sum and append the results

## Notes:

Brute force approach can be of four for loops checking all k-groups that sum up to target.
Time complexity with be TC: O(n^k)

Expected approach:
Sort the array, it can provide an approach that can be solved using two pointer technique.

the ksum problem is broken in to fix one element and k-1sum, fix another elements of k-1sum into k-2sum, fix another element of k-2sum into k-3sum, which can stopped at fixing k-2 elements of k-2sum into 2 sum. so we solve that last deduced 2sum and append the result to call stack function. This way ksum can be solved with help of recursion.

## Key Learnings

Explore more complexities in the given problem, like 2sum, 3sum, what if i get ksum?, should question ourself after complete solving the problem.

## Time Spent

- Problem 1: 1h
- Problem 2: 1h


---

<!-- Source: week-1-[Self-Pratice]/day-4-two-pointers -->

# Week 1 - Day 4

Date: December 04, 2025
Days since start: 11

## Problem 1

Two Pointers (forward-backward traversal)

Given strings s and t, find the minimum window in s which contains all
characters of t in the same order (subsequence, not substring).
Return the minimum window. If no such window exists, return "".

## Pattern:

#### Ask questions:

#### Visualization:

**Two pointers** forward and backward pass

## Key Learnings

- Apply backward pass after find the solution region

## Time Spent

- Problem 1: 2h
- Problem 2:


---

<!-- Source: week-2-[Self-Pratice]/day-5 -->

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
