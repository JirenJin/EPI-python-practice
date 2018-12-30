from test_framework import generic_test


def parity(x, n=64):
    while n > 1:
        right = x & (2 ** (n//2) - 1)
        left = x >> (n // 2)
        return parity(left, n//2) ^ parity(right, n//2)
    return x


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
