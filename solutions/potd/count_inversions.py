"""
Count Inversions (Medium)
@topic: potd
@difficulty: medium
@tags: Divide

i/o:
o/p:


Approaches:
1. Brute Force:
2. Expected:
"""


class Solution:
    def inversion_count(self, arr):
        # Code Here

        # brute force
        # for each element find
        # number of next smaller elements
        n = len(arr)
        res = self.count_inv(arr, 0, n-1)

        return res

    def count_inv(self, arr, l, r):  # noqa(linter comment)
        """
        Recursive function to calculate inversions
        for each arr from l to r
        """
        # base case
        if l >= r:
            return 0

        # obtain mid subarray
        m = l + (r-l)//2

        inversion_cnt = 0
        # count the inversions required for left half
        inversion_cnt += self.count_inv(arr, l, m)

        # count the inversions required for right half
        inversion_cnt += self.count_inv(arr, m+1, r)

        # count the inversions when merging left and right halves
        inversion_cnt += self.count_merge_inv(arr, l, m, r)

        return inversion_cnt

    def count_merge_inv(self, arr, l, m, r):  # noqa(linter comment)
        """
        given sorted arrays from l: m and m+1: r
        merge and count the inversions while sorting.
        """
        # create the actual arrays for comparison
        left = arr[l: m+1]
        right = arr[m+1: r+1]

        # inititalize count and size of left and
        # right arrays
        res = 0
        n1 = len(left)
        n2 = len(right)

        # initialize pointers
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:

            # left smaller elements have no inversions,
            # donot count them her
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                # right larger elements will have inversions
                # invert and count the inversions
                arr[k] = right[j]
                res += (len(left)-i)
                j += 1
            k += 1

        # merge remaining elements
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

        return res


if __name__ == "__main__":
    arrs = [
        [2, 4, 1, 3, 5],  # 3
        [10, 10, 10]  # 0

    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.inversion_count(arr))
