"""
Product of Array Except Self
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, arr):
        """
        """
        prefixProd = [0] * len(arr)
        suffixProd = [0] * len(arr)
        ans = [0] * len(arr)
        prefixProd[0] = 1
        for i in range(1, len(arr)):
            prefixProd[i] = prefixProd[i-1] * arr[i-1]


if __name__ == "__main__":
    pass
