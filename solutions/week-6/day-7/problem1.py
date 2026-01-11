"""
getDistinct in array
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, arr):
        """
        TC:
        SC:
        """
        n = len(arr)
        i = 0
        j = 0
        while i < n:
            arr[j] = arr[i]
            j += 1
            i += 1
            while i < n and (arr[i] == arr[i-1]):
                i += 1
        return j


if __name__ == "__main__":
    arr = []
    ans = Solution()
    print(ans.expected_approach(arr))
