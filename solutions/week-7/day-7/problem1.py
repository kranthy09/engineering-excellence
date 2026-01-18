"""
Rearrange Array Alternately
Given an array of positive integers.
Your task is to rearrange the array elements alternatively
i.e. first element should be the max value, the second
should be the min value, the third should be the second
max, the fourth should be the second min, and so on.
Note: Modify the original array itself. Do it without
using any extra space. You do not have to return anything.

i/o: arr[] = [1, 2, 3, 4, 5, 6]
o/p: [6, 1, 5, 2, 4, 3]

i/o:
o/p:

Approaches:
1. Brute Force: Reverse each subarray from i to n-1, O(n^2)
2.

"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """
        Final output requires alternative max and mins
        if we see output, 6 1 5 2 4 3
        that implies, 6 can be obtained from by one time reverse
        of whole array 6 5 4 3 2 1, next 1 can be obtained in
        2nd pos by reversing 5 4 3 2 1, the array becomes
        6 1 2 3 4 5, now reverse 2 to 4, becomes 6 1 2 5 3 4,
        3 to 4, finally becomes, alternatives of max and mins
        6 1 5 2 4 3

        TC: O(n^2)
        AS:O(1)
        """
        n = len(arr)
        for x in range(n):
            for i in range((n-x)//2):
                arr[i+x], arr[n-1-i] = arr[n-1-i], arr[i+x]
        return arr

    def expected_solution(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass


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
