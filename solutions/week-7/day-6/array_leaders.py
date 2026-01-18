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
    def leaders(self, arr):
        # code here
        n = len(arr)
        i = n-1
        mx = arr[i]
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
    print(ans.leaders(arr))
