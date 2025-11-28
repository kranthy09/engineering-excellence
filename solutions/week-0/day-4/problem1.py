"""
Problem 1: Sort Colors (Medium)

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
"""


def solve(nums):
    low = 0
    curr = 0
    high = len(nums)-1
    while curr <= high:
        if nums[curr] == 0:
            nums[low], nums[curr] = nums[curr], nums[low]
            low += 1
            curr += 1
        elif nums[curr] == 1:
            curr += 1
        elif nums[curr] == 2:
            nums[high], nums[curr] = nums[curr], nums[high]
            high -= 1
        print(nums)
    return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    res = solve(nums)
    print(res)
