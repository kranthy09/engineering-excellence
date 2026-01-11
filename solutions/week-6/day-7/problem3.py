"""
Subarrays with Equal Os and 1s
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, arr):
        """
        TC:
        SC:
        """
        ps = 0
        hmap = {ps: 1}
        freq = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                ps += 1
            else:
                ps -= 1
            if hmap.get(ps):
                freq += hmap[ps]
                hmap[ps] += 1
            hmap[ps] = 1
        return freq


if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 0, 1, 1]
    ans = Solution()
    print(ans.expected_approach(arr))
