# Count digits 1 to N

# TC: O(log(N))
# SC: O(log(N))
# series: 9 * 1 + 9 * 2 * 10^1 + 9 * 3 * 10^2 + ...
# Last number 9*n*pow(10, n-1), where n = number of digits in N.
def count_digits_1_to_n(N):
    n = 1
    i = 1
    res = 0
    while True:
        res += 9*n*i
        i *= 10
        n += 1
        if i*10 >= N:
            print("r: ", res)
            print("s:", n*(N-(i)+1))
            res += n*(N-(i)+1)
            return res
        print(res, i)
# 0 1 1
# 9*1*1 10 2
# 9 + 9*2*10 100 3
#


ans = count_digits_1_to_n(1121)
print(ans)
