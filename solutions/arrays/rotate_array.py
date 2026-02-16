"""
Array Leaders

Given an array arr[]. Rotate the array to
the left (counter-clockwise direction) by
d steps, where d is a positive integer.

i/o: arr[] = [1, 2, 3, 4, 5], d = 2
o/p: [3, 4, 5, 1, 2]

"""


class Solution:

    def brute_force(self, arr, d):
        """
        Rotate each element by shifting remaining elements,
        forward

        TC: O(n^2)
        AS: O(1)
        """
        arr = arr.copy()
        n = len(arr)
        for i in range(d):
            temp = arr[0]
            for j in range(n-1):
                arr[j] = arr[j+1]
            arr[n-1] = temp
        return arr

    def rotateArr(self, arr, d):
        """
        Reverse d elements and reverse n-d elements and
        reverse whole array

        TC: O(n)
        AS: O(1)
        """
        arr = arr.copy()

        n = len(arr)
        d = d % n
        for i in range(d//2):
            arr[i], arr[d-1-i] = arr[d-1-i], arr[i]
        for j in range((n-d)//2):
            arr[d+j], arr[n-1-j] = arr[n-1-j], arr[d+j]
        for k in range(n//2):
            arr[k], arr[n-1-k] = arr[n-1-k], arr[k]

        return arr


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    d = 3
    ans = Solution()
    print(ans.brute_force(arr, d))
    print(ans.rotateArr(arr, d))
