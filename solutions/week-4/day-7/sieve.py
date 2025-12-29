# All primes from 2 to n
# TC: O(n^3/2), SC: O(1)

# seive method
def sieve(N):
    is_primes = [True] * (N+1)
    i = 2
    while i*i <= N:
        if is_primes[i]:
            # j = i + i
            # assign i*i,
            # as the smaller multiples are already marked by samller primes.
            j = i * i
            while j <= N:
                is_primes[j] = False
                j += i
        i += 1
    return is_primes


ans = sieve(20)

for i in range(2, len(ans)):
    print(ans[i], i)
