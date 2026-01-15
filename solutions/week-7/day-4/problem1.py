"""
Maximum Index

Given an array arr of positive integers.
You have to return the maximum of j - i such that arr[i] < arr[j] and i < j.


i/o: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
o/p:6

i/o:
o/p:

Approaches:
1. Brute Force: Find all pairs of i, j and return max of j-i O(n^2)
2. Precalculate Lmin + Rmax: O(n)
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

        in the Left array, starting at 0, count the number of times,
        it satifies with the condition Lmin[i] <= Rmax[j] such that,
        the j can stretch up to the condition fails.

        L - minimum till i,
        R - maximum till n-1 to i
        A minimum number in L, can form a pair with an element in R,
        on <= condition, so j is moved where it can go, and can go maximum
        of its condition to its value j-i.
        For each iteration, j is increased, till the condition is satisfied,
        later i is increased and j is continues from the previous index place
        not from the start, such that L is min of elements which is decreasing
        so, previous elements in R, will satisfy the condition and now for the
        current ele from L, will move j forward till the condition is satified.
        The movement of i, j pointers is crucial as it playes between sorted
        arrays with a condition to satify.
        Both pointers are moved forward. Key take way is distance is calculated
        by moving pointers.
        TC: O(n)
        AS: O(n)
        """
        arr = args[0]
        n = len(arr)
        Lmin = [0] * n
        Rmax = [0] * n

        temp = float("+inf")
        for i in range(n):
            if temp > arr[i]:
                Lmin[i] = arr[i]
                temp = arr[i]
            else:
                Lmin[i] = temp
        temp = float("-inf")
        for i in range(n-1, -1, -1):
            if temp < arr[i]:
                Rmax[i] = arr[i]
                temp = arr[i]
            else:
                Rmax[i] = temp
        i = 0
        j = 0
        mx = 0
        while i < n and j < n:
            if Lmin[i] <= Rmax[j]:
                mx = max(mx, j-i)
                j += 1
            else:
                i += 1
        return mx


if __name__ == "__main__":
    arrs = [
        [34, 8, 10, 3, 2, 80, 30, 33, 1],
        [2, 3, 2, 5, 23, 54, 12, 7, 8, 1],
        [9, 4, 8, 16, 19, 2]
    ]
    ans = Solution()

    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))
