"""
Remove Duplicates from sorted array
Given a sorted array A consisting of duplicate elements.
Your task is to remove all distinct elements present in A.
But instead of returning an answer array, you have to rearrange
the given array in-place such that what have been described above.
Hence, return a single integer, the index(1-based) till which
the answer array would reside in the given array A.


i/o: [1, 1, 2]
o/p: 2

i/o: [1, 1, 2, 2, 3, 3, 3]
o/p: 3
"""


class Solution:

    def brute_force(self, arr):
        """
        for each element in the array find its duplicate
        in the remaining arr, is there no duplicate, increase
        unique count.

        TC: O(n^2)
        AS: O(n)
        """
        count = 0
        for i in range(len(arr)):
            occurence = 0
            for j in range(i, len(arr)):
                if arr[i] == arr[j]:
                    occurence += 1
            if occurence == 1:
                count += 1

        return count

    def expected_approach(self, arr):
        """
        TC: O(n)
        SC: O(n)
        """
        # responsible for telling the position of unique element
        unique_pos = 1
        # responsible for fetching unique elements
        current_ele = 1
        hmap = {arr[0]: 1}
        while current_ele < len(arr):
            if hmap.get(arr[current_ele]):
                current_ele += 1
            else:
                arr[unique_pos] = arr[current_ele]
                hmap[arr[current_ele]] = 1
                unique_pos += 1
                current_ele += 1
        return unique_pos


if __name__ == "__main__":
    arrs = [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
            [1, 2, 2, 2, 3, 3, 4, 4, 4, 9, 9, 10],
            [2, 2, 2, 2]
            ]
    ans = Solution()

    print("*****Brute Force*****")
    for arr in arrs:
        print(ans.brute_force(arr))

    print("*****Expected Approach*****")
    for arr in arrs:
        print(ans.expected_approach(arr))
