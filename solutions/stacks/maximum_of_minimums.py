"""
Max of min for every window size

You are given an array of integers,
find the maximum of minimums of every window size in the array.
where 1 <= window size <= n, and n is the size of the array.

Return the results of an array, where the element at index i represents
the answer for window size i+1.

i/o: [10, 20, 30, 50, 10, 70, 30]
o/p: [70, 30, 20, 10, 10, 10, 10]



"""


class Solution:

    def max_of_minimums_brute_force(self, arr):
        """
        Brute force method to return max of minimums, explicitly calling
        finding for each window size

        TC: O(n^2)
        AS: O(n)
        """
        pass

    def max_of_minimums_pse_nse(self, arr):
        """
        For an element it will be minimum of window size
        to its smaller elements from left and right

        TC:
        AS:
        """
        n = len(arr)
        pse = self.previous_smaller_elements(arr)
        nse = self.next_smaller_elements(arr)
        print("pse", pse)
        print("nse", nse)
        result = [float("-inf")] * n
        for i in range(n):
            window_size = nse[i] - pse[i] - 1
            print("win_size: ", window_size)
            result[window_size - 1] = max(result[window_size-1], arr[i])
        for i in range(n-2, -1, -1):
            result[i] = max(result[i], result[i+1])
        return result

    def previous_smaller_elements(self, arr):
        """
        Returns smaller element recent.

        """
        n = len(arr)
        stack = []
        pse = [0] * n
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            else:
                pse[i] = -1
            stack.append(i)
        return pse

    def next_smaller_elements(self, arr):
        """
        Returns next smaller recent.

        """
        n = len(arr)
        nse = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = n
            stack.append(i)
        return nse


if __name__ == "__main__":
    arr = [10, 20, 30, 50, 10, 70, 30]
    ans = Solution()
    print(ans.max_of_minimums_pse_nse(arr))
