import sys
import math
r = []
for s in sys.stdin.readlines():
    d,l = map(int, s.split())
    r.append(f"{math.acos(0) * (l / 2.0) * ((l + d) * (l - d))**0.5:.3f}")
sys.stdout.write("\n".join(r)+"\n")
