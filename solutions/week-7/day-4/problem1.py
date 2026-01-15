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
        """
        maximum j-i can be obtained with samller value on the left
        greater value on the right. Compute two axuilary arr with
        min values till i from left, and max value till i from right

        then return first Rmax[0](index) - Lmin[0](index) for Lmin <= Rmin.
        TC:
        AS:
        """
        arr = args[0]
        n = len(arr)
        Lmin = [[0, 0]] * n
        Rmax = [[0, 0]] * n
        temp = float("+inf")
        for i in range(1, n):
            if temp > arr[i]:
                Lmin[i][0] = i
                Lmin[i][1] = arr[i]
            else:
                Lmin[i][0] = i
                Lmin[i][1] = temp
        temp = float("-inf")
        for i in range(n, -1, -1):
            if temp < arr[i]:
                Rmax[i][0] = i
                Rmax[i][1] = arr[i]
            else:
                Rmax[i][0] = i
                Rmax[i][1] = temp
        print(Lmin)
        print(Rmax)
        mx = float("-inf")
        for i in range(n):
            if Lmin[i] <= Rmax[i]:
                j_i = Rmax[i][0] - Lmin[i][0]
                mx = max(mx, j_i)
        return mx


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
