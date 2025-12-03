"""
Find K Closest Elements (Medium)
Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array.
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

1 ≤ k ≤ arr.length
1 ≤ arr.length ≤ 10^4
arr is sorted in ascending order
-10^4 ≤ arr[i], x ≤ 10^4

"""


# def solve(arr, k, x):
#     if x < arr[0]:
#         return arr[:k]
#     if arr[-1] < x:
#         return arr[-k:]
#     left = 0
#     right = len(arr)-1
#     while left <= right:
#         if abs(arr[left] - x) <= abs(arr[right]-x):
#             right -= 1
#         else:
#             left += 1
#     if k > left:
#         return arr[:k]
#     return arr[k:left] + arr[left:2*k-left]


def solve(arr, k, x):
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


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    res = solve(nums, k, x)
    print(res)
