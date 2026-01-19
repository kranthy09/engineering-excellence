"""
Smallest positive missing number

You are given an array of []N integers including zero, The task is to find
the smallest missing positive number in the array.

i/o:
N = 5, arr = [1, 2, 3, 4, 5]
o/p:
6

What can be the brute force solution?
Positive numbers are 1,2,3,...,N
There can be 1 missing from the array, 2, and 3.. so on..
So search the number starting from 1 and end when we find the number.
so iterating over the n numbers leading to O(n) and for each number starting
from 1, we have to search in arr of size n, leads to O(n^2) and auxillary
space O(1).

Problems come across searching can be solved using three ways, namely,
linear search, like above, binary search and hash map approach

Consider binary search approach, to find the smallest missing number, if we
can sort the array and search from 1 till we get the number. Here sorting takes
O(nlogn), and searching through n elements requires n * log(n) as binary search
takes, log(n) operations to search, leads to O(nlogn), and auxillary space
O(1).

Is there any better way to do it?, yes, with hashmap.
Hashmap's set and get are O(1), constant operations, we can construct a hashmap
n length and search for the number starting from 1. So the time complexity
will be O(n), and auxillary space of O(n) for maintaing hashmap.

Instead of hashmap, construct isPresent array of size n, where we store
the elements present in the array to find the missing number.
Any element present in the array must have the array length equal to
its number. For example, for the element 100, the array size should be 99, such
that 100 will be smallest missing number, i.e., the element in the array is
greater than n, cannot contribute to the result, smallest positive number.
Similarly, negative numbers and 0.


Algorithm:
1. Initially, mark all values with False in isPresent array.
2. For each element in the array mark the arr[i]-1 index of isPresent array
to True.
3. At the end, isPresent array contains the True or False values, where
the index+1 is present in the array.
4. For each boolean in isPresent array and if there no element present in the
original array then, isPresent array index's value would be False.
5. return first False's index+1, which will be the smallest missing
positive number.
The time complexity will be O(n) and auxillary space of O(n) for constructing
isPresent array.

Instead of creating extra space, for storing the contributions, we can use
the array which is of same length n.

Bucketing Technique(Expected Appraoch):
Lets First assume there are all positive numbers in the array, later we can
get through negatives and zero.

Algorithm:
1. for each element in the array, there can be three cases.
2. two cases are element > len(arr), element <= 0 can be ignored as they
cannot contribute to the smallest missing number.
3. if the element < len(arr), then make bucket index value negative of value.
4. for an element at x, the bucket index will be x-1
5. At the end, the iterate over the array, the first positive element's index+1
will be the smallest missing postive number.

But Intially we have assumed, elements in the array are positive, what if some
of them are negative?.
Initially iterate over the array and replace negative numbers with positive
value greater than len(arr), such that it doesnot contribute towards solution.

So, time complexity will be O(n), and Auxillary space of O(1).

"""


class Solution:
    def brute_force(self, arr):
        """
        TC: O(N^2)
        AS: O(N)
        """

        num = 1
        for i in range(len(arr)):
            if num not in arr:
                return num
            num += 1
        return num

    def expected_solution(self, arr):
        """
        Bucketing Technique
        TC: O(N)
        AS: O(1)
        """
        n = len(arr)
        for i in range(n):
            if arr[i] < 0:
                arr[i] = n+1
        bucket_index = 0
        for i in range(n):
            bucket_index = abs(arr[i])-1
            if bucket_index < n and arr[bucket_index] > 0:
                arr[bucket_index] *= -1

        for i in range(n):
            if arr[i] > 0:
                return i + 1
        return len(arr) + 1

    def hash_map_solution(self, arr):
        """
        TC: O(n)
        AS: O(n)
        """
        hmap = dict()
        for ele in arr:
            hmap[ele] = True
        for i in range(len(arr)):
            if not hmap.get(i+1):
                return i + 1
        return len(arr) + 1

    def binary_search_solutin(self, arr):
        """
        TC: O(nlogn)
        AS: O(1)
        """
        arr.sort()
        num = 1
        while num < len(arr)+1:
            left = 0
            right = len(arr)-1
            found = False
            while left <= right:
                mid = (left + right)//2
                if arr[mid] == num:
                    found = True
                    break
                if arr[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            if not found:
                return num
            num += 1
        return num

    def linear_search_sorting(self, arr):
        """
        TC:
        AS:
        """
        arr.sort()
        for i in range(len(arr)):
            if arr[i] != i+1:
                return i + 1
        return len(arr) + 1


if __name__ == "__main__":
    arrs = [[5, 2, 3, 4, 1],
            [-1, -10, 3, 5, 2, 6],
            ]
    solve = Solution()
    print("*****BruteForce solution*****")
    for arr in arrs:
        print(solve.brute_force(arr.copy()))
    print("*****Expected approach*****")
    for arr in arrs:
        print(solve.expected_solution(arr.copy()))
    print("*****Hash Map solution*****")
    for arr in arrs:
        print(solve.hash_map_solution(arr.copy()))
    print("*****Sorting + Binary Search*****")
    for arr in arrs:
        print(solve.binary_search_solutin(arr.copy()))
    print("*****Sorting + Linear Search*****")
    for arr in arrs:
        print(solve.linear_search_sorting(arr.copy()))
