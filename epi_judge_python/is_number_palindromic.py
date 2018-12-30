from test_framework import generic_test


def is_palindrome_number(x):
    # s = str(x)
    # for i in range(len(s) // 2):
    #     if s[i] != s[-1-i]:
    #         return False
    # return True
    if x < 0:
        return False
    if x == 0:
        return True
    import math
    n = math.floor(math.log10(x)) + 1
    for i in range(n // 2):
        head = x // 10**(n-1-2*i)
        tail = x % 10
        x %= 10**(n-1-2*i)
        x //= 10
        if head != tail:
            return False
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
