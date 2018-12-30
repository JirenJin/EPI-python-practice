from test_framework import generic_test


def reverse(x):
    res = 0
    xx = abs(x)
    while xx:
        res = res * 10 + xx % 10
        xx //= 10
    return res if x > 0 else -res
    #return int(str(x).reverse()) * (1 if x >= 0 else -1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
