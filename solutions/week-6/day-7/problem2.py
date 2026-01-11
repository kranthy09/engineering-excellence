"""
Subarray sum 0
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, arr):
        """
        TC:
        SC:
        """
        presum = 0
        visited = {0: True}
        for i in range(len(arr)):
            presum += arr[i]
            if visited.get(presum):
                return True
            visited[presum] = True
        return False


if __name__ == "__main__":
    arr = [4, 2, -3, 1, 6]
    ans = Solution()
    print(ans.expected_approach(arr))
