import sys
import math

for s in sys.stdin.readlines():
    n,m = map(int, s.split())
    if m == 0:
        digit = 1
    elif n == 0:
        digit = 1
    else:
        digit = int(m * math.log10(n)) + 1
    print(int(math.log10(digit)) + 1 if digit > 0 else 1)
