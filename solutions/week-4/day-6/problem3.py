# Count digits 1 to N

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


res = count_digits_1_to_n(1121)
print(res)
