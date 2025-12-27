# Count digits 1 to N

def count_digits_1_to_n(N):
    n = 1
    i = 1
    res = 0
    while i < N:
        res += 9*n*i
        print(res)
        i *= 10
        if i >= N:
            print("n, N, i, i//10: ", n, N, i, i//10)
            res += n*(N-(i//10)+1)
            return res
        n += 1


res = count_digits_1_to_n(125)
print(res)
