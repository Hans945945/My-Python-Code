import sys
import math
r = []
for s in sys.stdin.readlines():
    D,V = map(int, s.split())
    if D == 0 and V == 0:
        break
    r.append(f"{pow(D**3 - 6*V/math.pi,1/3):.3f}")
sys.stdout.write("\n".join(r)+"\n")
