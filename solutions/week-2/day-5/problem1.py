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

Example 3:
nums = [1, 1, 1, 0]
target = -100
Output: 2
Explanation:
The closest sum is 2 (1 + 1 + 0 = 2)

Example 4:
nums = [-100, -98, -2, -1]
target = -101
Output: -101
Explanation:
The closest sum is -101 (-100 + -98 + -2 = -200... wait!)
Actually: -100 + -2 + -1 = -103 (distance 2)
Or: -100 + -98 + -1 = -199 (distance 98)
Best: -100 + -2 + 1... wait, there's no 1

Actually with [-100, -98, -2, -1]:
-100 + -98 + -2 = -200 (distance 99)
-100 + -98 + -1 = -199 (distance 98)
-100 + -2 + -1 = -103 (distance 2) ✓
-98 + -2 + -1 = -101 (distance 0) ✓✓✓
Output: -101

Constraints
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4

"""

"""
Psuedo code:

psuedo code:


```
n = len(nums)
nums.sort()
min_distance = float("inf")
for i in range(n):
l = i+1
r = n-1
distance = float("inf")
while l < r:
if abs(target - nums[l] - nums[r] - nums[i]) <= distance:
distance = target - nums[l] - nums[r] - nums[i]
min_distance_sum = nums[l] + nums[r] + nums[i]
if target - nums[i] < nums[l] + nums[r]:
r -= 1
else:
l += 1

return min_distance_sum

```
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
