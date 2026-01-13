"""
Subarray sum 0

Given an array of positive and negative numbers,
the task is to find if there is a subarray (of size at least one) with 0 sum.

i/p: {4, 2, -3, 1, 6}
o/p: true

Approaches:
1. Brute Force: Check all subarrays - O(n^2).
2. Prefix Sum + Hashmap(Expected): Track prefix sum, see in hashmap: O(n) time.
3. Prefix Sum + Hashset: Similar, Cleaner than approach 2.
4. Sliding window variant: check each subarray sum dynamically, O(n^2) time.
5. Cummulative Check: build prefix array, check subarray sum, O(n^2) time.
"""


class Solution:

    def brute_force(self, arr):
        """
        Find all subarrays and compute their sum,
        return subarray with zero sum

        TC: O(n^3)
        AS: O(1)
        """
        n = len(arr)
        for i in range(n):
            for j in range(n, i, -1):
                subarr_sum = sum(arr[i:j])
                if subarr_sum == 0:
                    return True
        return False

    def expected_approach(self, arr):
        """
        compute prefixes, and add to hashmap, if there is already
        prefxi present, then there will be subarray contribute sum zero.

        TC: O(n)
        SC: O(n)
        """
        n = len(arr)
        prefix = 0
        # to ensure prefix of zero in array is handled
        # assign zero is already present
        hmap = {0: True}
        for i in range(n):
            prefix += arr[i]
            if hmap.get(prefix):
                return True
            hmap[prefix] = True
        return False

    def prefix_sum_set(self, arr):
        """
        track seen prefix sum.
        TC: O(n)
        AS: O(n)
        """
        n = len(arr)
        prefix = 0
        hashset = {0}  # zero for prefix == 0
        for i in range(n):
            prefix += arr[i]
            if prefix in hashset:
                return True
            hashset.add(prefix)
        return False

    def sliding_window_variant(slef, arr):
        """
        for each starting position, accumate the sum until
        it reaches zero, equivalent to bruteforce with O(n^2) time

        TC: O(n^2)
        SC: O(1)
        """
        n = len(arr)
        for start in range(n):
            curr_sum = 0
            for end in range(start, n):
                curr_sum += arr[end]
                if curr_sum == 0:
                    return True
        return False

    def cummulative_check(self, arr):
        """
        construct prefix array and check the sum present

        TC: O(n^2)
        AS: O(n)
        """
        n = len(arr)
        prefixes = [0]
        subarr_sum = 0
        for i in range(n):
            subarr_sum += arr[i]
            if subarr_sum in prefixes:
                return True
            prefixes.append(subarr_sum)
        return False


if __name__ == "__main__":
    arrs = [
        [4, 2, -3, 1, 6],
        [0, 2, 3, -3,],
        [1, 2, 3, 4, 5, 6]
    ]
    ans = Solution()

    print("*****Brute Force*****")
    for arr in arrs:
        print(ans.brute_force(arr))

    print("*****Expected Approach*****")
    for arr in arrs:
        print(ans.expected_approach(arr))
    print("*****Sliding Window Variant*****")
    for arr in arrs:
        print(ans.sliding_window_variant(arr))
    print("*****Cummulative Check*****")
    for arr in arrs:
        print(ans.cummulative_check(arr))
