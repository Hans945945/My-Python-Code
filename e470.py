from math import log
import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    S = 0
    if n > 100:
        S = log(n) + 0.577215
    else:
        for i in range(1,n+1):
            S += 1/i
    r.append(f"{S:.3f}")
sys.stdout.write("\n".join(r)+"\n")
