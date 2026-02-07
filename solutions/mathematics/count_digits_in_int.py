# 234
# 3

# 45573
# 5

def count_digits(N):
    count = 0
    while N:
        N //= 10
        count += 1
    return count


ans = count_digits(234)
print(ans)
