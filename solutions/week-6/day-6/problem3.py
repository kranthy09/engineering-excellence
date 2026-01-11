"""
maxInNranges
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, L, R):
        """
        """
        result = 0
        maxx = 0
        for i in range(len(R)):
            maxx = max(maxx, R[i])
        freq = [0] * (maxx+2)
        for j in range(len(L)):
            freq[L[j]] += 1
            freq[R[j]+1] -= 1
        for k in range(1, len(freq)):
            freq[k] = freq[k-1] + freq[k]
            if freq[i] > freq[result]:
                result = i
        return i


if __name__ == "__main__":
    L = [1, 4, 3, 1]
    R = [15, 8, 5, 4]
    ans = Solution()
    print(ans.expected_approach(L, R))
