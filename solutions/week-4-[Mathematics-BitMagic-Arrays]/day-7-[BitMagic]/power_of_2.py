def check_power_of_2(N):
    if N <= 0:
        return False
    return N & (N-1) == 0


ans = check_power_of_2(64)
print(ans)
