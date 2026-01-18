"""
Array Leaders
You are given an array arr of positive integers.
Your task is to find all the leaders in the array.
An element is considered a leader if it is greater than
or equal to all elements to its right. The rightmost
element is always a leader.

i/o: arr = [16, 17, 4, 3, 5, 2]
o/p: [17, 5, 2]

Approaches:
1.
"""


class Solution:

    def brute_force(self, arr):
        """
        At i, check if the arr[i] is largest
        from its right by traversing array from
        i to n-1 and store it in auxilary array

        TC:
        AS:
        """
        arr = arr.copy()
        n = len(arr)
        res = []
        for i in range(n-1):
            leader = True
            for j in range(i+1, n-1):
                if arr[i] < arr[j]:
                    leader = False
                    break
            if leader:
                res.append(arr[i])
        res.append(arr[-1])  # last element is always a leader
        return res

    def leaders(self, arr):
        """
        Using Two pointers, watch from end of the array,
        see leaders and swap with next leaders position.

        TC: O(n)
        AS: O(1)
        """
        n = len(arr)
        i = n-1
        for j in range(n-2, -1, -1):
            if arr[j] < arr[i]:
                continue
            else:
                i -= 1
                arr[i] = arr[j]
        return arr[i:]


if __name__ == "__main__":
    arr = [10, 4, 2, 4, 1]
    ans = Solution()
    print(ans.brute_force(arr))
    print(ans.leaders(arr))
