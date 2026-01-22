"""
Stock buy and sell
Given an array arr[] denoting the cost of stock on each day,
the task is to find the maximum total profit if we can buy
and sell the stocks any number of times.

Note: We can only sell a stock which we have bought earlier
and we cannot hold multiple stocks on any day.

i/o: arr[] = [100, 180, 260, 310, 40, 535, 695]
o/p: 865

i/o:
o/p:

Approaches:
1. Brute Force:

"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """
        Generate all possible pairs of buy, sell and
        return max from it.


        TC:
        AS:
        """
        arr = args[0]
        result = 0
        answer = []
        return self.buy_sell_recur(0, arr, result, answer)

    def buy_sell_recur(self, i, arr, result, answer):
        # base case
        if i > len(arr)-2:
            answer.append(result)
            return result

        print(result, answer, i)
        # include
        if arr[i] > arr[i+1]:
            result += (arr[i+1]-arr[i]) + \
                self.buy_sell_recur(i+1, arr, result, answer)
        # exclude
            result -= (arr[i+1] - arr[i])
        else:
            result += self.buy_sell_recur(i+1, arr, result, answer)

    def expected_solution(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass


if __name__ == "__main__":
    arrs = [
        [100, 180, 260, 310, 40, 535, 695],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))
