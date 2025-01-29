import math
import sys
for s in sys.stdin:
    n,m = map(int, s.split())
    print(math.factorial(n) // (math.factorial(m)*math.factorial(n-m)))
