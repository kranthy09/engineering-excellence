# Special Palindrome

def is_alpha_numeric(ch):
    return (ch >= 'a' and ch <= 'z') or \
        (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9')


def is_same(ch1, ch2):
    return ch1 == ch2 or (abs(ord(ch1) - ord(ch2)) == ord('a') - ord('A'))


def is_special_palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if not is_alpha_numeric(s[i]):
            i += 1
        elif not is_alpha_numeric(s[j]):
            j -= 1
        else:
            if is_same(s[i], s[j]):
                i += 1
                j -= 1
            else:
                return False
    return True


s = "A man:nama"
res = is_special_palindrome(s)
print(res)
