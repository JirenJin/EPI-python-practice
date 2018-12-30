from test_framework import generic_test


def power(x, y):
    if y < 0:
        return 1 / power(x, -y)
    if y == 0:
        return 1
    if y == 1:
        return x
    d, m = divmod(y, 2)
    half = power(x, d)
    return half * half * (x if m else 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
