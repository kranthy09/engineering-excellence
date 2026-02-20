"""
Form The Largest Number (Medium)
@topic: potd
@difficulty: medium
@tags: Arrays, Sorting

Given an array of integers arr[] representing non-negative integers,
arrange them so that after concatenating all of them in order, it results
in the largest possible number. Since the result may be very large,
return it as a string.

i/o: [3, 30, 34, 5, 9]
o/p: 9534330


Approaches:
1. Expected: sort the array and compare strings of numbers.
"""

from functools import cmp_to_key


class Solution:

    def find_largest_inbuilt_sort(self, arr):
        """
        Define comparing numbers, from normal comparison to custom
        comparison, where strings of numbers are considered for comparing.

        "3" + "30" = "330" and "30" + "3" = "303"
        then, "330" > "303", => "30" comes first in descending order. even
        its value is greater than number "3".

        TC: O(nlogn), for sorting
        AS: O(n), auxiliary array to store strings of numbers.
        """

        # create array of strings of numbers
        arr_str = [str(ele) for ele in arr]

        # custom comparator method to compare strings
        def compare(a, b):
            # larger value returns -1 => a, b are sorted in descending order
            if a + b > b + a:
                return -1
            # else, value returns, 1 => a, b are sorted in ascending order
            elif a + b < b + a:
                return 1
            # else if , value returns 0, => equal numbers
            else:
                return 0
        # tell the inbuilt to sort with custom compare function.
        arr_str.sort(key=cmp_to_key(compare))

        # if all the numbers are 0, we should return 0.
        # else return by joining the array string.
        return "0" if arr_str[0] == "0" else "".join(arr_str)


if __name__ == "__main__":
    arrs = [
        [54, 546, 548, 60],  # o/p: 6054854654
        [3, 4, 6, 5, 9],  # o/p: 96543
        [0, 0, 0, 0, 0, 0]  # o//p: 0
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.find_largest_inbuilt_sort(arr))
