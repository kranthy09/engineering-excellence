# TC: O(sqrt(n))
# SC: O(1)
def is_prime(N):
    i = 2
    while i*i < N:
        if N % i == 0:
            return False
        i += 1
    return True


ans = is_prime(2)
print(ans)
