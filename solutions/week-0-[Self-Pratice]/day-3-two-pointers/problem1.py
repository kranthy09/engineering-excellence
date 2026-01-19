"""
Problem 1: Remove Duplicates from Sorted Array II (Medium)


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

Key Challenge: Modify in-place with O(1) space.
"""


# def solve(nums):

#     n = len(nums)
#     i = 0
#     j = 0
#     stretch = 0
#     while i < n - stretch and nums[i] != "_":
#         # print("start: ", i, j)
#         if nums[i] == nums[j]:
#             j += 1
#         else:
#             # nums = nums[:i+2] + nums[j:] + ["_"] * (j-i-2)
#             if j - i == 1:
#                 i += 1
#             elif j - i == 2:
#                 i += 2
#             elif j - i > 2:
#                 for k in range(i, i+(j-i-2)):
#                     nums.remove(nums[k])
#                 for _ in range(j-i-2):
#                     nums.append("_")
#                 i += 2
#             j = i
#     print(nums)
#     # print("end: ", i, j)
#     return i

def solve(nums):
    if len(nums) <= 2:
        return nums
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow-2]:
            nums[slow] = nums[fast]
            slow += 1
    print(nums)
    return slow


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5]
    nums1 = [1, 1, 1, 2, 2, 3]
    nums3 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    for arr in [nums, nums1, nums3]:
        res = solve(arr)
        print(res)
