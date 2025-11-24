# Mastering Binary Search with Real-World Examples

Binary Search is one of the most fundamental algorithms in computer science, often appearing in coding interviews and competitive programming. Beyond the classic "find an element in a sorted array," binary search can solve a variety of complex problems efficiently.

In this blog, we'll go beyond basics with **two practical applications**:

1. **Finding the smallest number strictly greater than a given number K in a sorted array**
2. **Finding the peak element in an array**

---

## 🚀 What is Binary Search?

Binary search is an efficient algorithm to find an element in a **sorted** array with a time complexity of **O(log n)**. It repeatedly divides the search space in half until the target is found (or not found).

### Alogirithm

To find an element in an array we have to define the search space where the target is located.

1. Search Space: Part of the array where the element is found
2. Update the search space by comparing the mid element with the target element
3. Size of the new search space will be approx. half of the previous search space

```python
# An array of size n, with a 'target' element to be found
l=0, r=n-1 # initial search space (complete array)
while l<=r:
 mid = l + (r-l)//2
 if arr[mid] == target:
  return mid
 elif arr[mid] > target:
  move the search space to left
 else:
  move the search space to right
```

Initially define the search space with 'l', 'r', and 'mid' for comparing with the target.

---

**Note**: mid is updated with `mid = l + (r-l)/2)` instead with `mid = (l+r)/2`. Hence the l, r can be integers of maximum value 2^31-1. `l+r` will execeed 2^31. An overflow condition occurs when the result of an arithmetic operation exceeds the maximum value that a given data type can represent, leading to an incorrect or unexpected result.

---

Middle element of the array is compared with the target in each iteration.
There can three cases following:

1. Mid element is the target
2. Mid element is greater than the target
3. Mid element is less than the target

**Case 1:** `arr[mid] == target`
Return the index of the middle element, as the target is found.

**Case 2:** `arr[mid] > target`
Mid element is greater than the target. As the array is sorted,the left part of the array can be ignored . so the search space will be moved to right by updating `l, r`.

- `l` becomes `mid+1` and `r` remains same.

**Case 3:** `arr[mid] < target`
Mid element is less than the target. As the array is sorted, the right part of the array can be ignored. so the search space will be moved to left by updating `l, r`.

- `r` becomes `mid-1` and `l` remains same.

### :nut_and_bolt: Full Code ~python

```python
arr = [1, 2, 5, 7, 9 , 11, 24, 28]
target = 11
l = 0,
r = len(arr) - 1
def binary_search(arr):
 while l <= r:
  mid = l + (r - l)//2
  if arr[mid] == target:
   return mid
  elif arr[mid] > target:
   r = mid - 1
  else:
   l = mid + 1
 return -1 # no target found

print(binary_search(arr, target))
# index of target: 5
```

### Time Complexity:

Time complexity is nothing but the number of computations made by the algorithm. On each iteration the search space will be reduced to half such that search space will become 1.

```
| Computations | Seach space(n) |
| ------------ | -------------- |
|      1       |         n      |
|      2       |         n/2    |
|      3       |         n/4    |
|      4       |         n/8    |
       .                  .
       .                  .
       .                  .
       k                  1
```

Assume after `k` iterations, `n` becomes 1,

such that,
$`1 = n/2^k`$

apply $`log`$ on both sides,

$`log n = log 2^k`$

which results in,

$`k = log n`$

Hence the time complexity to find one element using binary search will be **O(log n)**

---

## 📌 Problem 1: Find the Smallest Number Strictly Greater than K

### Problem

Given a **sorted array**, find the smallest number that is **strictly greater** than a given number `K`. If no such number exists, return `-1`.

### Example

```text
Input: nums = [2, 4, 6, 8, 10], K = 6
Output: 8
```

## 📌 Problem 2: Find the peak element

### Problem

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

### Example

```text
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

## 📌 Problem 3: Find the minimum in rotated sorted array

### Problem

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

### Example

```text
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

## 📌 Problem 4: Sqrt(x)

### Problem

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

### Example

```text
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## 📌 Problem 5: Count occurencers

### Problem

Given a sorted array, count the number of occurences of an element.

### Example

```text
Input: arr = [2, 3, 4, 4, 5, 5, 5, 5, 6], target = 5
Output: 4
Explanation: Target element 5 occurs 4 times in the array
```

## 📌 Performing binary search on unsorted array


There is a case where you have to search for an element inside an unsorted array. Now binary search cannot able to perform directly. So we have to preprocess the array and perform binary search. This involves two steps,
1. Preprocess: Sort the array
2. Perform binary search

- In 1st step, Time complexity to sort an array will be O(nlogn)
- 2nd step the time complexity will be O(logn)
- total TC: O(nlogn + logn).

But there is already an efficient solution which can be achieved in O(n) time complexity is linear search (Brute force)

Time complexity for linear search will be less than that of by preprocess and apply binary search. In this scenario choosing linear search over binary search makes it easy to find one element.

Suppose, there are 'k' queries to perform on unsorted array to search for a number in each query, then the brute force (linear search) time complexity will be O(k*n) and by preprocess, perform binary search the time complexity will be O(nlogn + klogn)

- Hence O(k*n) > O(nlogn + klogn)

So here preprocessing the array and performing binary search makes it easy to find queries of elements.