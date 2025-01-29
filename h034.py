import sys
from itertools import zip_longest
n = int(sys.stdin.readline())
print(''.join(c for group in zip_longest(*sys.stdin, fillvalue='') for c in group if c.isalpha()))
