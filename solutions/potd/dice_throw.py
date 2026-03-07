"""
Dice Throw (Medium)
@topic: potd
@difficulty: medium
@tags: arrays, dynamicprogramming

Given n dice each with m faces. Find the number of ways
to get sum x which is the summation of values on each face
when all the dice are thrown.


i/o: m = 6, n = 3, x = 12
o/p: 25


Approaches:
1. Expected:
"""


class Solution:

    def no_of_ways(self, m, n, x):
        """

        TC: O(n*m)
        AS: O(x)
        """

        # at index i, value represents
        # number of ways to get a sum of 'j' using i dice
        dp = [0] * (x + 1)

        # there is only one way to get a sum of 0.
        # (using no dice)
        dp[0] = 1
        for i in range(1, n+1):

            for j in range(x, 0, -1):
                dp[j] = 0

                for k in range(1, m+1):
                    if j - k >= 0:
                        # place where we do deep with dynamic
                        # checks with help previous checks
                        dp[j] += dp[j-k]
            dp[0] = 0

        return dp[x]


if __name__ == "__main__":
    arrs = [
        [],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))
