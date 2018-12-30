from test_framework import generic_test


def reverse_bits(x, cache={}):
    x0 = x & 0xFFFF
    x1 = x >> 16 & 0xFFFF
    x2 = x >> 32 & 0xFFFF
    x3 = x >> 48 
    def reverse_16(x):
        if x in cache:
            return cache[x]
        xx = x
        for i in range(8):
            if x >> i & 1 != x >> (15 - i) & 1:
                x ^= 1 << i | 1 << (15 - i)
        cache[xx] = x
        return x
    x0 = reverse_16(x0)    
    x1 = reverse_16(x1)    
    x2 = reverse_16(x2)    
    x3 = reverse_16(x3)    
    return (x0 << 48) + (x1 << 32) + (x2 << 16) + x3


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
