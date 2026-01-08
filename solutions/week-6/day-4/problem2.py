from math import gcd


class Solution:
    def nCr(self, n, r):
        # code here
        # n, r, n-r
        # if n < r return 0;
        if n < r:
            return 0

        # if r < n - r
        # n-r+1, n-r+2, ..., n
        # 1, 2, 3, 4,... r
        # n!/r!(n-r)!
        # 1, ..., r, r+1, ... n
        # r!, 1, 2,..., n-r
        # r+1*r+2*...*n/1*2*3*...*n-r
        # r > n -r
        # r+1, r+2,..., n
        # 1, 2, 3, .., n-r
        r = min(r, n-r)
        nume = 1
        deno = 1
        for i in range(r):
            nume *= (n-i)
            deno *= (i+1)
            g = gcd(nume, deno)
            nume //= g
            deno //= g
        return nume//deno
