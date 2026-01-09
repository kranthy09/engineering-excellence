class Solution:
    def reverseexponentiation(self, n):
        # code here
        # result = 1
        # for i in range(rev):
        #     result *= n
        # return result
        base = n
        exp = 0
        n1 = n
        while n1:
            exp = exp*10 + n1 % 10
            n1 //= 10
        result = 1
        while exp > 0:
            if exp % 2 != 0:
                result *= base
            base = (base * base)
            exp >>= 1
        return result
    