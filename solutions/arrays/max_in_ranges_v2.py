"""
Maximum occurring integer in given ranges
Given two arrays L[] and R[] of size N where L[i] and R[i]
(0 ? L[i], R[i] < 106)denotes a range of numbers, the task
is to find the maximum occurred integer in all the ranges.
If more than one such integer exists, print the smallest one.

Input: L[] = {1, 4, 3, 1}, R[] = {15, 8, 5, 4}
Output: 4

Input: L[] = {1, 5, 9, 13, 21}, R[] = {15, 8, 12, 20, 30}
Output: 5
Explanation: Numbers having maximum occurrence i.e 2 are
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15. The smallest number among all are 5.

Approaches:
1. Brute Force:


"""


class Solution:

    def max_occured(self, L, R):
        """
        TC: O(n*maxx)
        AS: O(max)
        """
        freq = {}
        # Count occurrences of each number across all ranges
        for left, right in zip(L, R):
            for num in range(left, right + 1):
                freq[num] = freq.get(num, 0) + 1

        # Find maximum occurrence
        max_count = max(freq.values())

        # Return smallest number with max occurrence
        return min(num for num, count in freq.items() if count == max_count)

    def expected_approach(self, L, R):
        """
        TC: O(n*maxx)
        AS: O(maxx)
        """
        result = 0
        maxx = 0
        for i in range(len(R)):
            maxx = max(maxx, R[i])
        freq = [0] * (maxx+2)
        for j in range(len(L)):
            freq[L[j]] += 1
            freq[R[j]+1] -= 1
        result = 0
        prefix = freq[0]
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
            if prefix < freq[i]:
                result = i
            prefix = freq[i]
        return result


if __name__ == "__main__":
    arrs = [
        [[1, 4, 3, 1], [15, 8, 5, 4],]
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.max_occured(arr[0], arr[1]))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_approach(arr[0], arr[1]))
