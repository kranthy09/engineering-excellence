"""
Check if array is sorted and rotated

Given an array arr[] of positive and distinct integers,
determine if it is sorted (either in increasing or decreasing order)
and then rotated at least once in the counter-clockwise direction.
Note: A sorted array (in increasing or decreasing order) is not
considered a sorted and rotated array

i/o: arr[] = [3, 4, 1, 2]
o/p: True

i/o: arr[] = [1, 2, 3]
o/p: False

Approaches:
1. Brute Force: Check for rotated sorted arrays - O(n)
2. Inversions: Calculate inversions - O(n)

"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """
        For every rotated sorted array, by comparing arr[0]
        and arr[-1] will help whether it is increasing
        or decreasing already sorted or rotated sorted.

        Catch all possible values for true rotated sorted array
        either in inc or dec order.
        TC: O(n)
        AS: O(1)
        """
        arr = args[0]
        n = len(arr)
        inc_sorted = False
        not_dec = False
        if n < 2:
            return False
        if n == 2:
            return True
        if arr[0] >= arr[-1]:
            for i in range(1, n):
                if arr[i] == arr[i-1]:
                    continue
                if arr[i-1] < arr[i]:
                    inc_sorted = True
                else:
                    not_dec = True
            if not_dec:
                return inc_sorted
            else:
                return not_dec
        dec_sorted = False
        not_inc = False
        if arr[0] <= arr[-1]:
            for i in range(1, n):
                if arr[i] == arr[i-1]:
                    continue
                if arr[i-1] > arr[i]:
                    dec_sorted = True
                else:
                    not_inc = True
            if not_inc:
                return dec_sorted
            else:
                return not_inc

    def expected_solution(self, *args, **kwargs):
        """
        For a rotated sorted array there must be only 1
        inversion such that current element is greater than
        next element(for non-decreasing array) and same for
        non-increasing array.

        TC: O(n)
        AS: O(1)
        """
        arr = args[0]
        n = len(arr)
        non_dec = True
        for i in range(n):
            if arr[0] > arr[-1]:
                non_dec = True
            else:
                non_dec = False
        if non_dec:
            inc_inversions = 0
            # non-decreasing
            for i in range(n):
                if arr[i] > arr[(i+1) % n]:
                    inc_inversions += 1
            if inc_inversions == 1:
                return True
            else:
                return False
        else:
            # non-increasing
            dec_inversions = 0
            for i in range(n):
                if arr[i] < arr[(i+1) % n]:
                    dec_inversions += 1
            if dec_inversions == 1:
                return True
            else:
                return False


if __name__ == "__main__":
    arrs = [
        [3, 4, 1, 2,],
        [1, 2, 3],
        [2, 1, 4, 3],
        [3, 3, 3, 3],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))
