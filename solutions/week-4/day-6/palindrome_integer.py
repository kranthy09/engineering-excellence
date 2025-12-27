# 121
# True

# 457
# False

def is_palindrome_integer(N):
    digits = 0
    temp = N
    while temp:
        temp //= 10
        digits += 1
    print(digits)
    i = 0
    j = digits-1
    temp = N
    while i < j:
        right = (temp//10**i) % 10
        left = (temp//10**j) % 10
        print("l, r", left, right)
        if left != right:
            return False
        i += 1
        j -= 1
    return True


ans = is_palindrome_integer(155621)
print(ans)

# reverse half approach
# 12344321
# number = n%10
#  ````````````````````````


def reversed_half(N):
    rev_num = 0
    while N > rev_num:
        rev_num = rev_num * 10 + N % 10
        N //= 10
    return N == rev_num or N == rev_num//10


ans2 = reversed_half(345563)
print(ans2)

# String Method


def string_method(N):
    if N < 0:
        return False
    s = str(N)
    return s == s[::-1]


ans3 = string_method(776677)
print(ans3)
