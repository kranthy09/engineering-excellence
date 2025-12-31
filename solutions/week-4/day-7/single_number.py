def get_single_number(arr):
    result = 0
    for i in range(len(arr)):
        result ^= arr[i]
    return result


ans = get_single_number([1, 2, 1, 5, 5])
print(ans)
