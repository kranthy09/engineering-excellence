"""
Power Of Numbers (Medium)
@topic: recursion
@difficulty: medium
@tags: Recursion, BinaryExponentiation

Given a number n, find the value of n raised to the power of its own reverse.
Note: The result will always fit into a 32-bit signed integer.

i/o: n = 2
o/p: 4


Approaches:
1. Recursion: Binary Exponentiation
"""


class Solution:

    def reverse_power_of_number(self, n):
        """
        Returns power of number's reverse to the base number.
        Obtains the reverse of number, and recursively computes
        power with the help of sqauring the base and dividing
        the exponentiation half, and handling odd and even powers.

        TC: O(log n) for reverse,  log(reverse) for binary exponentiation,
        Overall O(log n)
        AS: O(log reverse), recursive call stack
        """
        rev = self._obtain_rev_num(n)

        return self._bin_exp(n, rev)

    def _obtain_rev_num(self, x):
        """
        Given a number abc, returns its reverse cba
        """
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        return rev

    def _bin_exp(self, n, x):
        """
        for an even exponent, n^x = (n^2)^(x//2)
        for odd, n^x = n*(n)^(x-1)
        compute multiplication recursively.
        """
        # base case
        if x == 0:
            return 1
        if x == 1:
            return n

        if x % 2:
            # for odd, construct it as even by removing one power,
            # ie., include it as multiplier
            return n * self._bin_exp(n, x-1)
        else:
            # compute current square and process to recursion
            # to find out for next half
            return self._bin_exp(n*n, x//2)


if __name__ == "__main__":
    arr = [
        5, 7
    ]
    ans = Solution()
    for num in arr:
        print(ans.reverse_power_of_number(num))  # 3125 823543
