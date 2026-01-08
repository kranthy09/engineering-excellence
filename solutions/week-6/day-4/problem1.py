def binomial_optimized(n, r):
    if r > n or r < 0:
        return 0
    r = min(r, n - r)  # Use symmetry: C(n,r) = C(n,n-r)

    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
        print(f"i={i}: result = {result}")  # Debug trace
    return result


print(binomial_optimized(98, 87))
