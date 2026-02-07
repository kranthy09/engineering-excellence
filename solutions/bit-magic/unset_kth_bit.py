"""
# unset kth bit
input: 45, 2
output:45

"""


def unset_kth_bit(N, k):
    # unset involves & as it can flip a bit when 1, unchaged when 0.
    # create mask with 0 at kth bit.
    mask = ~(1 << k)
    return N & mask


if __name__ == "__main__":
    N, k = 45, 2
    ans = unset_kth_bit(N, k)
    print(ans)  # output: 41
