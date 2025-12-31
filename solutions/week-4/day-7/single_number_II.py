"""
# arr = [1, 1, 1, 4, 5, 5, 5, 6, 7, 8, 6, 7, 6, 8, 7]
# output = 4

"""


def get_single_numberII(arr, k):

    # frequency map of 32 size
    # create frequency map from arr
    print("k: ", k, "repeated numbers")
    fmap = [0] * 32
    for i in range(len(arr)):
        temp = arr[i]
        pos = 0
        while temp:
            if (temp & 1) > 0:
                fmap[pos] += 1
            temp = temp >> 1
            pos += 1
    print(fmap)
    # iterate over map for result
    mul = 1
    result = 0
    for i in range(len(fmap)):
        if fmap[i] % 3:
            result += mul
        mul *= 2
    return result


if __name__ == "__main__":
    arr = [1, 1, 1, 4, 5, 5, 5, 6, 7, 8, 6, 7, 6, 8, 7, 8]
    k = 3
    ans = get_single_numberII(arr, k)
    print(ans)  # 4
