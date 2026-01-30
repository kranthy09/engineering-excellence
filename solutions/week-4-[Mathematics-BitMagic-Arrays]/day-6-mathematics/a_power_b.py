# Find a to the power b


def a_power_b(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result


def a_to_power_b(a, b):
    if b == 0:
        return 1
    temp = a_to_power_b(a, b//2)
    if b % 2 == 0:
        return temp * temp
    return a * temp * temp


res = a_to_power_b(2, 3)
print(res)
print("a_power_b: ", a_power_b(3, 4))


# Count digits 1 to N

def count_digits_1_to_n(n):
    res = 0
    i = 1
    while True:
        if res - n - (i-1):
            return res
        res += (n-(i-1))
        i *= 10


res = count_digits_1_to_n(45)
print(res)
