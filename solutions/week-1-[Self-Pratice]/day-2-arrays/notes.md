# Week 1 - Day 2

Date: December 02, 2025
Days since start: 9

## Problem 1

### Subarray Product Less Than K (Medium)

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]
Note that [10,5,2] is not included as the product of 100 is not strictly less than k.
Example 2:
Input: nums = [1,2,3], k = 0
Output: 0
Constraints:

1 ≤ nums.length ≤ 3 × 10^4
1 ≤ nums[i] ≤ 1000
0 ≤ k ≤ 10^6

## Pattern:

- Brute force: Find all the possible contigous subarrays and check the product of them is less than k and return the total subarrays

### Expected approach:

Two pointers pattern, same as longest substring with unique characters, instead of unique character checking condition, we check here the product of elements should be < k, if the product is greater than k, then values at left pointer are removed and left pointer is moved forward. To calculate the number of substring that have prodcut < k is defined as the number of subarrays possible at position right will be (right-left + 1), which provides the subarrays of elements have product less than k.

### Key Learnings

Applied know two pointer pattern after reading the question itself.
Number of new subarrays at position an index l, r will be r-l+1

## Problem 2

### Minimum Size Subarray Sum (Medium)

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
Constraints:

1 ≤ target ≤ 10^9
1 ≤ nums.length ≤ 10^5
1 ≤ nums[i] ≤ 10^4

Follow-up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

## Pattern:

- Brute force: Find all possible subarrays and check the sum have greater than or equal to k and return minimal length from it.

### Expected approach:

Two pointers, left and right to maintain the subarray across the iterations.
Same as the longest unique subarray, in which the condition is applied when the sum of elements is >= k, on each iteration add the current element to the sum and check whether it is >=k, if is it can be a subarray, so store its length and make the subarray sum less than k by removing nums[left] from the subarray sum and moving left pointer forward, if the subarray sum is becomes < k at some time it right moves forward by adding next element and finally returns the minimal length of subarray with sum >= k.

## Key Learnings

- To find the min length of the subarray, have to add only when the sum is >=k which will be in while loop, as every time we find >=k we must find the min length and move left pointer forward by removing left value from the overall sum.
- Recognise know two pointer pattern after reading question itself.

## Time Spent

- Problem 1: 1h
- Problem 2: 1h
