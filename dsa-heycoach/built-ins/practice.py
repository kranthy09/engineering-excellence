class Solution:
    def solve(self, s: str):
        # Write your code here
        s = list(sorted(s))
        n = len(s)
        indices = list(range(n))
        cycles = list(range(n, 0, -1))
        print(indices)
        print(cycles)
        first_perm = "".join([s[i] for i in indices])
        yield first_perm


k = Solution()
res = k.solve("abc")
print(res)