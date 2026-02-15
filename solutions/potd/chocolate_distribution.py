"""
Chocolate Distribution (Easy)
@topic: potd
@difficulty: easy
@tags:

i/o:
o/p:


Approaches:
1. Brute Force:
2. Expected:
"""


class Solution:
    def brute_force(self):
        """

        TC:
        AS:
        """
        pass

    def find_min_diff(self, arr, M):
        """


        TC:O(nlogn)
        Sorting takes n*logn, sliding window takes n, asymptotically,
        nlogn.
        AS: O(1)
        """
        n = len(arr)
        arr.sort()
        min_diff = float("+inf")

        # min diff for each window of size M
        for i in range(n-M+1):
            min_diff = min(min_diff, arr[i+M-1] - arr[i])

        return min_diff


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
