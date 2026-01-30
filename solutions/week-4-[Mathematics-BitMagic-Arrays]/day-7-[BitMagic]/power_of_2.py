
"""
Python code to find the most significant set bit in 'n'.
"""
import math


def check_power_of_2(N):
    if N <= 0:
        return False
    return N & (N-1) == 0


def find_msb_value(n):
    """
    TC: O(1)
    AS: O(1)
    """
    return 1 << int(math.log2(n))


if __name__ == "__main__":
    n = 8
    ans = find_msb_value(n)
    print(ans)
    ans = check_power_of_2(64)
    print(ans)
