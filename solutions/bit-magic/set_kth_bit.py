
# TC: O(1)
# AS: O(1)
def set_kth_bitN(N, k):
    mask = 1 << k
    return N | mask


ans = set_kth_bitN(47, 1)
print(ans)
