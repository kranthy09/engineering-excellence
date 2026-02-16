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

## Problem 3

1. Boats to Save People (Medium)
   You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
   Return the minimum number of boats to carry every given person.

## Pattern:

#### Ask Questions:

- do we have order in the array?
  : No, but ordering might help
- if the max weight of persons is greater than limit?
  : solution not found case.

#### Visualization:

- At any time we have two choices, take one person or take both persons, and which person is take from both. if we can send the lightest person with heavier can help to maintain the least boats used. so sorting the data can help us to identify which person can pick.

**Two pointers Pattern** , at start and end positions moves inwards to select one or two persons and greater weights pointer moving inward, such that current lighter person is again checked with next larger person.

at an instance of allocating the persons to boats, at start, end indices,

```python
if nums[start] + nums[end] <= limit:
    boats_count += 1
    start += 1
    end -= 1
else:
    boats_count += 1
    end -= 1
```

## Key Learnings

- Identification of pattern and solution in visualization step.
- Order in array elements can help find the pairs efficiently.
- Used "which choices to make" thinking from recursion solving techniques.

## Problem 4

Find K Closest Elements (Medium)

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

## Pattern:

#### Ask Questions:

- do we have order in the array?
  : yes, increasing order
- what is k?
  : length of number array to return
- what is x?
  : k-elements that are closer to x.

#### Visualization:

- Subtract 'x' from each element of given array, then we can observe a pattern, such that either, the trend in the elements is strictly increasing or decreasing - increasing nature
- For strictly increasing nature, the x lies in outside the range of the elements so can return arr[:k] if x is smaller than first value or arr[-k:] if x is larger than last value
- For increasing - decreasing nature, we have to find the window size of k such that they are closer to x

**Two pointers Pattern** , at start and end positions moves inwards and stop by reaching atmost window size k, to calculate the distance between the elements., abs(arr[start]-x) and abs(arr[end]-x) in which more distance pointer will be moved inwards to find the closer k values to x

```python
if x < arr[0]:
        return arr[:k]
    if arr[-1] < x:
        return arr[-k:]
    left = 0
    right = len(arr)-1
    while right - left + 1 > k:
        if abs(arr[left] - x) <= abs(arr[right]-x):
            right -= 1
        else:
            left += 1
    return arr[left:right+1]
```

## Key Learnings

- Identification of pattern with two pointers to calculate the local minimum in the region.
- deducing to max window size of pattern of length k is the constraint, i.e., left and right cannot shrink less k size.

**Notes**

When there is a search in the problem, we have can have linear search, binary search, and hashmap as common methods to solve the problem. Smallest positive number can be solved in those three ways and fourth way is bucketing technique, every time we search for the smallest missing positive number.

### problem 5. Smallest positive missing number.

You are given an array of []N integers including zero, The task is to find the smallest missing positive number in the array.

### problem 6. Boolean matrix Question.

Given a boolean matrix mat where each cell contains either 0 or 1,
the task is to modify it such that if a matrix cell matrix[i][j] is 0
then all the cells in its ith row and jth column will become 0.

### problem 7. kadane's

Given an integer of numbers, find contigous subarray with maximum sum.

### problem 8. Maximum Index

Given an array arr of positive integers. You have to return the
maximum of j - i such that arr[i] < arr[j] and i < j.

### problem 9. Check if array is sorted and rotated

Given an array arr[] of positive and distinct integers, determine if it is sorted (either in increasing or decreasing order) and then rotated at least once in the counter-clockwise direction.
Note: A sorted array (in increasing or decreasing order) is not considered a sorted and rotated array

## Key Learnings

- For Rotated sorted array, by counting inversions can tell it is actual rotated sorted array
  For non decreasing array, it is rotated by clock or counterclock wise direction, the larger elements will come front, such that there exists a pivot at which current element is greater than next element
  For non increasing array, there will be one inversion at the pivot.

**Short Notes**:
Recursion:
Convert non tail recursive to tail recursive if there is scope.

Key Learnings:

- Tail recursion, non-tail recursion
