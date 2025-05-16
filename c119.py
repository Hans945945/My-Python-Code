import math
import sys

for s in sys.stdin:
    n = int(s.rstrip())
    print(sum(int(d) for d in str(math.factorial(n))))
