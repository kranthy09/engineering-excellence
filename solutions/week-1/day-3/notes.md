# Week 1 - Day 3

Date: December 03, 2025
Days since start: 10

## Problem 1

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

## Problem 2

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

## Time Spent

- Problem 1: 1h
- Problem 2: 1h 45m
