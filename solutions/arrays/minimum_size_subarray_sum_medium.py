"""
Minimum Size Subarray Sum (Medium)

Given an array of positive integers nums and a positive integer target,
 return the minimal length of a subarray whose sum is greater than or
 equal to target. If there is no such subarray, return 0 instead.
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal
length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

1 ≤ target ≤ 10^9
1 ≤ nums.length ≤ 10^5
1 ≤ nums[i] ≤ 10^4

Follow-up: If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log n).
"""


def solve(nums, target):
    """
    compute elements sum in each iteration and
    check with target, shrink using left and right pointers
    to obtain minimum window length

    TC: O(n)
    AS: O(1)
    """
    n = len(nums)
    ele_sum = 0
    left = 0
    right = 0
    min_len = float("inf")
    for right in range(n):
        ele_sum += nums[right]
        while ele_sum >= target:
            min_len = min(min_len, right - left + 1)
            ele_sum -= nums[left]
            left += 1
    return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    nums2 = [1, 4, 4]
    target2 = 4
    res = solve(nums, target)
    print(res)
