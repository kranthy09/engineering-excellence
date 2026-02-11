"""
Single Number II
Given an array of integers, every element appears
three times except for one. Find that single one.

i/o: arr = [1, 1, 1, 4, 5, 5, 5, 6, 7, 8, 6, 7, 6, 8, 7]
o/p: 4

i/o: arr = [2, 2, 3, 2]
o/p: 3

Approach:
1. Create a frequency map of size 32 (for 32-bit integers).
2. For each number in the array, update the frequency map based on
   the bits set in the number.
3. After processing all numbers, iterate over the frequency map and
   construct the result by checking which bits have a frequency that
   is not a multiple of 3.

Time Complexity: O(n) where n is the number of elements in the array.
Space Complexity: O(1) since the frequency map size is fixed (32 bits).
"""


def get_single_numberII(arr, k):
    """
    arr: List[int] - input array
    k: int - number of times other elements are repeated (3 in this case)
    return: int - the single number that appears once
    """

    # frequency map of 32 size
    # create frequency map from arr
    fmap = [0] * 32
    for i in range(len(arr)):
        temp = arr[i]
        pos = 0
        while temp:
            # check if last bit is set
            if (temp & 1) > 0:
                # if set, update frequency map
                fmap[pos] += 1
            # right shift temp to check next bit
            temp = temp >> 1
            pos += 1

    # iterate over map for result
    mul = 1
    result = 0
    for i in range(len(fmap)):
        # if frequency is not multiple of 3, then set the bit in result
        if fmap[i] % k != 0:
            result += mul
        # update mul for next bit
        mul = mul << 1
    return result


if __name__ == "__main__":
    arr = [1, 1, 1, 4, 5, 5, 5, 6, 7, 8, 6, 7, 6, 8, 7, 8]
    k = 3
    ans = get_single_numberII(arr, k)
    print(ans)  # 4, single number in the array
