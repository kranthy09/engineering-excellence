"""
Longest Span In Bin Arrays (Medium)
@topic: potd
@difficulty: medium
@tags: prefixsum, arrays

Given two binary arrays, a1[] and a2[] of equal length.
Find the length of longest common span (i, j),
where i<= j such that,
a1[i] + a1[i+1] + .... + a1[j] =  a2[i] + a2[i+1] + ... + a2[j].



i/o: a1[] = [0, 1, 0, 0, 0, 0], a2[] = [1, 0, 1, 0, 0, 1]
o/p: 4


Approaches:
1. Brute Force: Naive, Find all substrings, O(n^2)
2. Expected: Difference array prefix sum with hashmap, O(n)
"""


class Solution:

    def equal_sum_span(self, a1, a2):
        """
        difference[k] = a1[k] - a2[k], reduces to
        find maximum difference subarray with sum 0
        TC: O(n)
        AS: O(n), for storing prefix sums in hashmap.
        """
        n = len(a1)
        diff = [-1]*n
        # compute difference array
        for k in range(n):
            diff[k] = a1[k] - a2[k]

        # compute maximum length of subarray with prefix zero
        prefix = 0
        # handle first prefix
        hmap = {0: -1}
        span = 0
        for i in range(n):
            prefix += diff[i]
            # prefix is zero, then subarray sum will be zero
            if prefix == 0:
                # capture max span
                span = max(span, i - hmap[prefix])
            # prefix is already in the subarray, then their difference,
            # will provide subarray sum zero
            if hmap.get(prefix) is not None:
                # capture their span
                span = max(span, i - hmap[prefix])
            else:
                # for new prefix, it can be potential prefix.
                hmap[prefix] = i
        return span


if __name__ == "__main__":
    arrs = [
        [[1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1]]  # 7
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.equal_sum_span(arr[0], arr[1]))
