import sys
import math
r = []
for s in sys.stdin:
    n,m = map(int, s.split())
    if n == 0 and m == 0:
        break
    c = math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
    r.append(f"{n} things taken {m} at a time is {c} exactly.")
sys.stdout.write("\n".join(r)+"\n")
