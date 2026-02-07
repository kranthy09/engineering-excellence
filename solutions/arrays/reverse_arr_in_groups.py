"""
Reverse array in groups
Given an array arr[] of positive integers.
Reverse every sub-array group of size k.
Note: If at any instance, k is greater or
equal to the array size, then reverse the entire array.

i/o: arr[] = [1, 2, 3, 4, 5], k = 3
o/p:  3, 2, 1, 5, 4]

i/o:
o/p:

Approaches:
1. Brute Force: find k-size subarrays and swap to reverse - O(n)
2.

"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        arr = args[0]
        k = args[1]
        n = len(arr)
        if n % k:
            sub = (n//k) + 1
        else:
            sub = n//k
        print(sub)
        for i in range(sub):
            a = i*k
            b = a + k - 1
            if b >= n:
                b = n-1
            while a <= b:
                arr[a], arr[b] = arr[b], arr[a]
                a += 1
                b -= 1
        return arr

    def expected_solution(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass


if __name__ == "__main__":
    arrs = [
        [[1, 2, 3, 4, 5], 3],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(*arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(*arr))
