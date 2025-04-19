from math import pi
import sys
r = []
for s in sys.stdin.readlines()[1:]:
    n = int(s)
    red = (n/5)**2*pi
    green = n*(n*3/5)-red
    r.append(f"{red:.2f} {green:.2f}")
sys.stdout.write("\n".join(r)+"\n")
