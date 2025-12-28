def unset_kth_bitN(N, k):
    mask = ~(1 << k)
    return N & mask


ans = unset_kth_bitN(45, 2)
print(ans)
