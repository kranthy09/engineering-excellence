"""
Generalizing the of k-sum as extension for problem-1
using recursion
"""


def ksum(nums, target, k):
    nums.sort()
    res = []
    if len(nums) < k:
        return res
    if k == 2:
        return twosum(nums, target)

    for i in range(len(nums) - k + 1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        new_target = target - nums[i]
        result = ksum(nums[i+1:], new_target, k-1)
        for sub in result:
            res.append([nums[i]]+sub)
    return res


def twosum(nums, target):
    l = 0  # noqa
    r = len(nums)-1
    res = []
    while l < r:
        if nums[l] + nums[r] == target:
            res.append([nums[l], nums[r]])
        if nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return res


if __name__ == "__main__":
    nums = [-2, -1, -1, 0, 0, 1, 2]
    target = 0
    k = 4
    ans = ksum(nums, target, k)
    print(ans)
