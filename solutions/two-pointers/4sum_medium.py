"""
4Sum (Medium)

Given an array nums of n integers, return an array of
all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

1 ≤ nums.length ≤ 200
-10^9 ≤ nums[i] ≤ 10^9
-10^9 ≤ target ≤ 10^9
"""


def solve(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j + 1  # noqa
            r = len(nums)-1
            required_sum = target - nums[i] - nums[j]
            while l < r:
                if nums[l] + nums[r] == required_sum:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                if nums[l] + nums[r] < required_sum:
                    l += 1
                else:
                    r -= 1
    return res


if __name__ == "__main__":
    nums = [1, 0, -1, -1, 0, -2, 2]
    target = 0
    res = solve(nums, target)
    print(res)
