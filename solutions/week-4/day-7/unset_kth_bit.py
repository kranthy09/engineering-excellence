"""
# unset kth bit
input: 45, 2
output:45

"""


def unset_kth_bit(N, k):
    mask = ~(1 << k)
    return N & mask


ans = unset_kth_bit(41, 2)
print(ans)
