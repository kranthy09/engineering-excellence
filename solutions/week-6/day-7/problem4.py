"""
Number of Subarrays sum with equals to target
Given an array arr[] of postive and negative integers,
the objective is to find the number of subarrays having
a sum exactly equal to a given number k.

i/p: arr[] = [10, 2, -2, -20, 10], k = -10
o/p: 3

Approaches:
1. Brute Force:

"""


class Solution:

    def brute_force(self, arr, k):
        """
        Generate all subarrays and compute its sum
        TC: O(n*3)
        AS: O(1)
        """
        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(n, i, -1):
                subarr = sum(arr[i:j])
                if subarr == k:
                    count += 1
        return count

    def expected_approach(self, arr, k):
        """
        find prefix sum reduced from target in hashmap,
        to form a subarray sum equals to target.

        TC:
        SC:
        """
        n = len(arr)
        prefix = 0
        count = 0
        seen = {}
        for i in range(n):
            prefix += arr[i]
            if prefix == k:
                count += 1
            if seen.get(prefix-k):
                count += seen[prefix-k]
                seen[prefix-k] += 1
            else:
                seen[prefix] = 1
        return count


if __name__ == "__main__":
    arrs = [
        [[9, 4, 20, 3, 10, 5], 33],
        [[1, 3, 5], 2],
        [10, 2, -2, -20, 10],
    ]
    ans = Solution()
    print("*****Brute Force*****")
    for arr in arrs:
        print("**************")
        print(ans.brute_force(arr[0], arr[1]))
    print("*****Expected Approach*****")
    for arr in arrs:
        print(ans.expected_approach(arr[0], arr[1]))
