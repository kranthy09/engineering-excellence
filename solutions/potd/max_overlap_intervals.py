"""
Max Overlap Intervals (Hard)
@topic: potd
@difficulty: hard
@tags: [PrefixSum, Sorting, Arrays, Hash]

You are given an array of intervals arr[][], where each
interval is represented by two integers [start, end] (inclusive).

Return the maximum number of intervals that overlap at any point in time.

i/o: [[1, 2], [2, 4], [3, 6]]
o/p: 2

Approaches:
1. Brute Force:hashmap for all numbers to count, find max occured
2. Expected: Frequency array representing, boundaries and prefix sum for max.
"""


class Solution:
    def brute_force(self, arr):
        """
        TC: O(n*maxx)
        AS: O(maxx)
        """
        n = len(arr)
        hmap = {}
        for r in range(n):
            # for every number in range, start to end,
            for i in range(arr[r][0], arr[r][1]+1):
                # store counts in hmap
                if hmap.get(i):
                    hmap[i] += 1
                else:
                    hmap[i] = 1
        # Find maximum occurrence
        max_count = max(hmap.values())

        # number with max occurrence
        return max_count

    def overlap_int(self, arr):
        """
        TC: O(n)
        AS: O(maxx), frequency array
        """
        # code here
        n = len(arr)
        maxx = float("-inf")
        for i in range(n):
            maxx = max(maxx, arr[i][1])

        # 1 to maxx are considered
        # 0, maxx+1 are boundaries, so freqmap will be maxx + 2
        freq = [0] * (maxx+2)
        for j in range(n):
            # start of range
            freq[arr[j][0]] += 1

            # next to end range, to cancel out the effect
            freq[arr[j][1]+1] -= 1
        prefix = 0
        res = 0
        for k in range(1, maxx+2):
            # prefix sum, tell about overlaps
            prefix += freq[k]

            # store the max prefix sum
            res = max(res, prefix)

            # update the prefix to get maximum overlap
            if prefix < freq[k]:
                prefix = freq[k]
        return res


if __name__ == "__main__":
    arrs = [
        [[1, 2], [2, 4], [3, 6]],
        [[1, 8], [2, 5], [5, 6], [3, 7]],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.overlap_int(arr))
