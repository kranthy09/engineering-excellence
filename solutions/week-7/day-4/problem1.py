"""
Maximum Index

Given an array arr of positive integers.
You have to return the maximum of j - i such that arr[i] < arr[j] and i < j.


i/o: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
o/p:6

i/o:
o/p:

Approaches:
1. Brute Force: Find all pairs of i, j and return max of j-i
2. 
"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """
        Generate all pairs of i, j and compute j-i such that,
        arr[i] <= arr[j] for i <= j

        TC:
        AS:
        """
        arr = args[0]
        n = len(arr)
        maxx = float("-inf")
        for i in range(n):
            for j in range(i, n):
                if arr[i] <= arr[j]:
                    maxx = max(maxx, j-i)
        return maxx

    def expected_solution(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    arrs = [
        [34, 8, 10, 3, 2, 80, 30, 33, 1],
    ]
    ans = Solution()

    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Brute Force******")
    for arr in arrs:
        print(ans.expected_solution(arr))
