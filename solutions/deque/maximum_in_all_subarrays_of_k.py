"""
Maximum in all subarrays of size k

You are given an array and a number k, you need to find the maximum
for each and every contiguous subarray of size k.

i/o: arr = [1,3,-1,-3,5,3,6,7], k = 3
o/p : [3,3,5,5,6,7]
Explanation:
1. Subarray with max 3 is [1 3 -1]
2. Subarray with max 3 is [3 -1 -3]
3. Subarray with max 5 is [-1 -3 5]
4. Subarray with max 5 is [-3 5 3]
5. Subarray with max 6 is [5 3 6]
6. Subarray with max 7 is [3 6 7]

Approaches:
1. Brute Force: find each subarray of k and find max, O(n*k)
2. Optimized using Deque: O(n)

"""

from collections import deque


class Solution:

    def brute_force(self, arr, k):
        """
        For each subarray of size k, find the maximum element.

        TC: O(n*k)
        AS: O(1)
        """
        pass

    def deque_approach(self, arr, k):
        """
        Take a deque of size k and maintain the maximum.

        TC: O(n)
        AS: O(k)
        """
        n = len(arr)
        if n == 0 or k == 0:
            return []
        if k > n:
            return [max(arr)]
        q = deque()
        res = []
        # construct for the first k elements
        for i in range(k):
            # smaller elements on the left of current elemet are not useful
            # so remove them from the deque
            while q and arr[q[-1]] <= arr[i]:
                q.pop()
            q.append(i)
        # process through the rest of the elements
        for i in range(k, n):
            # front element of deque is largest element of the previous window
            res.append(arr[q[0]])
            # remove previous window larger elements which
            # are out of this window
            while q and q[0] <= i - k:
                q.popleft()
            # while processing next elements, remove smaller elements
            while q and arr[q[-1]] <= arr[i]:
                q.pop()
            q.append(i)
        # for the last window
        res.append(arr[q[0]])
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.deque_approach(arr, k))
