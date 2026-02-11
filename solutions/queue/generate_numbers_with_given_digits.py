"""
Generate Numbers with Given Digits

Given a number n, print the first n numbers such that all numbers are
generated using the digits 5 and 6 only, in increasing order.

i/o: n = 3
o/p: 5 6 55

i/o: n = 10
o/p: 5 6 55 56 65 66 555 556 565 566
"""

from collections import deque


class Queue:

    def generate_n_numbers_of_5_6_digits(self, n):
        """
        Use a queue to store the 5, 6 digits as strings,
        in order to represent long 'n' digits of number.

        TC:
        AS:
        """
        res = []
        q = deque()  # init deque

        # push 5, 6
        q.append("5")
        q.append("6")

        # for number, formed by adding 5, 6
        for i in range(n):
            curr = q.popleft()
            res.append(curr)
            q.append(curr + "5")
            q.append(curr + "6")
        return res


if __name__ == "__main__":
    n = 10
    q = Queue()
    ans = q.generate_n_numbers_of_5_6_digits(n)
    # ['5', '6', '55', '56', '65', '66', '555', '556', '565', '566']
    print(ans)
