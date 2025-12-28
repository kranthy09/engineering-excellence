# All primes from 2 to n
# BF: TC: O(n^3/2), SC: O(1)

# seive method
def sieve(N):
    is_primes = [True] * (N+1)
    i = 2
    while i*i <= N:
        if is_primes[i]:
            j = i
            while j*j <= N:
                is_primes[j] = False
                j += i
        i += 1
    return is_primes


ans = sieve(20)
print(ans)
