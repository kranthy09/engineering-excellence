"""
3Sum Closest

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
nums = [-1, 2, 1, -4]
target = 1
Output: 2
Explanation:
The sum that is closest to the target is 2:
(-1 + 2 + 1 = 2)

Example 2:
nums = [0, 0, 0]
target = 1
Output: 0
Explanation:
The only possible sum is 0 (0 + 0 + 0 = 0)
"""


def solve(nums, target):
    """
    TC: O(n^2)
    SC: O(1) or O(log n) # extra memomry for sorting needs.
    """
    nums.sort()
    n = len(nums)
    closest_sum = float("inf")
    for i in range(n-2):
        l = i+1  # noqa
        r = n-1
        while l <= r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if abs(curr_sum-target) < abs(closest_sum-target):
                closest_sum = curr_sum
            if curr_sum == target:
                return target
            if curr_sum > target:
                r -= 1
            else:
                l += 1
    return closest_sum


if __name__ == "__main__":
    nums = [-1, 2, 4, 1]
    target = 2
    res = solve(nums, target)
    print(res)
