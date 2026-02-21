"""
Find H Index (Medium)
@topic: potd
@difficulty: medium
@tags: bucketing, sorting, arrays


You are given an array citations[], where each element citations[i]
represents the number of citations received by the ith paper of a
researcher. You have to calculate the researcher’s H-index.
The H-index is defined as the maximum value H, such that the
researcherhas published at least H papers, and all those papers
have citation value greater than or equal to H.

i/o: [5, 1, 2, 4, 1]
o/p: 2


Approaches:
1. Brute Force: For each citation, find max h-index, O(n^2)
2. Expected: Bucketing Technique, store citation counts, O(n)
"""


class Solution:

    def h_index(self, citations):
        """
        H-index can never exceeds the number of papers, 'n'.
        Count how many papers have each citation count and scan
        through find the threshold.

        TC: O(n)
        AS: O(n), maitianing counts(bucket)
        """
        n = len(citations)
        # create array, where i represents citation and its value
        # represents the count of that citation.
        hindexs = [0]*(n+1)

        # handling edge case
        all_zeros = True

        for i in range(n):
            if arr[i] == 0:
                continue
            # minimize for larger papers execeeding h-index constraints
            hindexs[min(arr[i], n)] += 1
            all_zeros = False

        # all zero citiations will be early returned.
        if all_zeros:
            return 0

        # tracks citation counts
        val = 0
        for j in range(n, -1, -1):

            # citation counts from last to first(higher citation to lower),
            val += hindexs[j]
            # j, represents, citations of paper, val represents,
            # val represents, counts of citations till j from last
            # as the indexs are in sorted order, find the number of counts
            # present on the right for an index j.
            if val >= j:
                # need max, so return immediately
                return j
        return 0


if __name__ == "__main__":
    arrs = [
        [3, 0, 5, 0, 3],  # o/p: 3
        [5, 1, 2, 4, 1],  # o/p: 2
        [4, 3, 5, 5, 7, 7, 8, 9, 10, 15, 12],  # o/p: 7
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.h_index(arr))
