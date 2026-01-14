"""
Subarrays with equal 1s and 0s

Given an array arr[] containing 0s and 1s.
Count the number of subarrays having equal number of 0s and 1s.


i/o:: arr[] = [1, 0, 0, 1, 0, 1, 1]
o/p: 8

Approaches:
1. Brute Force: find all subarrays and check 1s and 0s: O(n^3)
2. Prefix + hashmap: assume 0 as -1 and with prefix count subarrays: O(n)


Python fundamentals:
 A statement like zero_count evaluates to a value but doesn't need to be used.
 This is intentional design — it's useful in interactive shells
 where you might type a variable name to inspect its value.
"""


class Solution:

    def is_equal_1s0s(self, subarr):
        """
        returns True for equal 1s and 0s in arr,
        works for only arrays with 1, 0.
        """
        one_count = 0
        zero_count = 0
        for ele in subarr:
            if ele:
                one_count += 1
            else:
                zero_count += 1
        return zero_count == one_count

    def brute_force(self, arr):
        """
        Generate all subarrays and compute equal 1s and 0s

        TC:
        AS:
        """
        n = len(arr)
        result = 0
        for i in range(n):
            for j in range(n, i, -1):
                subarr = arr[i:j]
                if self.is_equal_1s0s(subarr):
                    result += 1
        return result

    def expected_approach(self, arr):
        """
        replace 0s with -1 such that sum of subarray with
        equal 1s and 0s contribute to zero.
        Track prefix sums in hashmap and find the subarrays
        possible.

        TC: O(n)
        SC: O(n)
        """
        n = len(arr)
        # convert 0 to -1
        prefix = 0
        seen = {prefix: 1}
        count = 0
        for i in range(n):
            prefix += (-1 if arr[i] == 0 else arr[i])
            if seen.get(prefix):
                count += seen[prefix]
                seen[prefix] += 1
            else:
                seen[prefix] = 1
        return count


if __name__ == "__main__":
    arrs = [
        [1, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
    ]
    ans = Solution()
    print("*****Brute Force*****")
    for arr in arrs:
        print("**************")
        print(ans.brute_force(arr))
    print("*****Expected Approach*****")
    for arr in arrs:
        print(ans.expected_approach(arr))
